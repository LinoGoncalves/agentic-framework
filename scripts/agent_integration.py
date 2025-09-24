#!/usr/bin/env python3
"""
Agent Integration and Communication Scripts

This module provides utilities for loading agent personas, managing communication
between agents, and orchestrating the agentic SDLC workflow.
"""

import json
import yaml
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class AgentPersona:
    """Represents an AI agent persona loaded from markdown file."""
    name: str
    role: str
    file_path: Path
    content: str
    capabilities: List[str] = field(default_factory=list)
    dependencies: List[str] = field(default_factory=list)
    standards_references: List[str] = field(default_factory=list)

@dataclass
class Task:
    """Represents a task assigned to an agent."""
    id: str
    title: str
    description: str
    agent: str
    human_reviewer: str
    status: str = "assigned"
    deliverables: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.utcnow)
    due_date: Optional[datetime] = None
    dependencies: List[str] = field(default_factory=list)

@dataclass
class Project:
    """Represents a project in the agentic SDLC."""
    id: str
    name: str
    type: str
    workflow: str
    brief_path: Path
    status: str = "initiated"
    current_phase: str = ""
    team: Dict[str, str] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.utcnow)

class AgentRegistry:
    """Registry for managing AI agent personas."""
    
    def __init__(self, agents_directory: Path = Path("./sub-agents")):
        self.agents_directory = agents_directory
        self.agents: Dict[str, AgentPersona] = {}
        self._load_all_agents()
    
    def _load_all_agents(self) -> None:
        """Load all agent personas from the agents directory."""
        if not self.agents_directory.exists():
            logger.error(f"Agents directory not found: {self.agents_directory}")
            return
        
        for agent_file in self.agents_directory.glob("*-agent.md"):
            try:
                agent = self._load_agent_from_file(agent_file)
                self.agents[agent.name] = agent
                logger.info(f"Loaded agent: {agent.name}")
            except Exception as e:
                logger.error(f"Failed to load agent from {agent_file}: {e}")
    
    def _load_agent_from_file(self, file_path: Path) -> AgentPersona:
        """Load an agent persona from a markdown file."""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract agent name from filename
        agent_name = file_path.stem  # removes .md extension
        
        # Parse agent role from content (look for "# Persona:" line)
        role = "Unknown"
        for line in content.split('\n'):
            if line.startswith("# Persona:"):
                role = line.replace("# Persona:", "").strip()
                break
        
        # Extract capabilities, dependencies, and standards references
        capabilities = self._extract_capabilities(content)
        dependencies = self._extract_dependencies(content)
        standards_refs = self._extract_standards_references(content)
        
        return AgentPersona(
            name=agent_name,
            role=role,
            file_path=file_path,
            content=content,
            capabilities=capabilities,
            dependencies=dependencies,
            standards_references=standards_refs
        )
    
    def _extract_capabilities(self, content: str) -> List[str]:
        """Extract capabilities from agent content."""
        capabilities = []
        in_functions_section = False
        
        for line in content.split('\n'):
            if "## Core Functions" in line or "## Tasks" in line:
                in_functions_section = True
                continue
            elif line.startswith("## ") and in_functions_section:
                break
            elif in_functions_section and line.strip().startswith(('1.', '2.', '3.', '4.', '-')):
                # Extract capability description
                capability = line.strip().lstrip('1234567890.- ').split(':')[0]
                if capability:
                    capabilities.append(capability)
        
        return capabilities
    
    def _extract_dependencies(self, content: str) -> List[str]:
        """Extract dependencies from agent content."""
        dependencies = []
        
        # Look for references to other agents
        for line in content.split('\n'):
            if 'agent' in line.lower() and any(keyword in line.lower() for keyword in ['engage', 'collaborate', 'work with']):
                # Extract agent names from the line
                words = line.split()
                for word in words:
                    if word.endswith('-agent'):
                        dependencies.append(word.strip('`'))
        
        return list(set(dependencies))  # Remove duplicates
    
    def _extract_standards_references(self, content: str) -> List[str]:
        """Extract standards file references from agent content."""
        standards = []
        
        for line in content.split('\n'):
            if 'development-standards' in line or './development-standards/' in line:
                # Extract file references
                import re
                matches = re.findall(r'`\./development-standards/([^`]+)`', line)
                standards.extend(matches)
        
        return list(set(standards))  # Remove duplicates
    
    def get_agent(self, agent_name: str) -> Optional[AgentPersona]:
        """Get an agent persona by name."""
        return self.agents.get(agent_name)
    
    def list_agents(self) -> List[str]:
        """List all available agent names."""
        return list(self.agents.keys())
    
    def get_agents_by_capability(self, capability: str) -> List[AgentPersona]:
        """Find agents that have a specific capability."""
        matching_agents = []
        for agent in self.agents.values():
            if any(capability.lower() in cap.lower() for cap in agent.capabilities):
                matching_agents.append(agent)
        return matching_agents

class WorkflowEngine:
    """Engine for managing and executing agentic SDLC workflows."""
    
    def __init__(self, agent_registry: AgentRegistry):
        self.agent_registry = agent_registry
        self.projects: Dict[str, Project] = {}
        self.active_tasks: Dict[str, Task] = {}
        self.state_file = Path("./workflow_state.json")
        self._load_state()
    
    def _load_state(self) -> None:
        """Load workflow state from file."""
        if self.state_file.exists():
            try:
                with open(self.state_file, 'r') as f:
                    data = json.load(f)
                    # TODO: Deserialize projects and tasks
                    logger.info("Loaded workflow state")
            except Exception as e:
                logger.error(f"Failed to load workflow state: {e}")
    
    def _save_state(self) -> None:
        """Save workflow state to file."""
        try:
            # TODO: Serialize projects and tasks
            data = {
                "projects": {},  # Serialized projects
                "tasks": {},     # Serialized tasks
                "last_updated": datetime.utcnow().isoformat()
            }
            with open(self.state_file, 'w') as f:
                json.dump(data, f, indent=2)
            logger.info("Saved workflow state")
        except Exception as e:
            logger.error(f"Failed to save workflow state: {e}")
    
    def create_project(self, project_brief_path: Path) -> Project:
        """Create a new project from a project brief."""
        if not project_brief_path.exists():
            raise FileNotFoundError(f"Project brief not found: {project_brief_path}")
        
        # Parse project brief to extract metadata
        project_data = self._parse_project_brief(project_brief_path)
        
        project = Project(
            id=self._generate_project_id(),
            name=project_data.get("name", "Unnamed Project"),
            type=project_data.get("type", "unknown"),
            workflow=self._determine_workflow(project_data.get("type", "")),
            brief_path=project_brief_path,
            team=project_data.get("team", {})
        )
        
        self.projects[project.id] = project
        self._save_state()
        
        logger.info(f"Created project: {project.name} (ID: {project.id})")
        return project
    
    def _parse_project_brief(self, brief_path: Path) -> Dict[str, Any]:
        """Parse project brief to extract metadata."""
        # This is a simplified parser - in practice you'd want more robust parsing
        with open(brief_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract basic information
        project_data = {}
        
        # Look for project name
        for line in content.split('\n'):
            if line.startswith('# ') and 'Project' in line:
                project_data['name'] = line.replace('#', '').strip()
                break
        
        # Determine project type from checkboxes
        if '[x]' in content or '[X]' in content:
            if 'FastAPI' in content:
                project_data['type'] = 'api'
            elif 'Streamlit' in content:
                project_data['type'] = 'dashboard'
            elif 'Django' in content or 'Flask' in content:
                project_data['type'] = 'web_app'
        
        return project_data
    
    def _determine_workflow(self, project_type: str) -> str:
        """Determine which workflow to use based on project type."""
        data_science_types = ['dashboard', 'ml_model', 'data_pipeline', 'analytics']
        
        if any(ds_type in project_type.lower() for ds_type in data_science_types):
            return "data_science"
        else:
            return "software_systems"
    
    def _generate_project_id(self) -> str:
        """Generate a unique project ID."""
        import uuid
        return f"proj_{uuid.uuid4().hex[:8]}"
    
    def start_workflow(self, project_id: str) -> List[Task]:
        """Start the appropriate workflow for a project."""
        project = self.projects.get(project_id)
        if not project:
            raise ValueError(f"Project not found: {project_id}")
        
        if project.workflow == "software_systems":
            return self._start_software_workflow(project)
        elif project.workflow == "data_science":
            return self._start_data_science_workflow(project)
        else:
            raise ValueError(f"Unknown workflow: {project.workflow}")
    
    def _start_software_workflow(self, project: Project) -> List[Task]:
        """Start the software/systems development workflow."""
        workflow_phases = [
            {
                "phase": "definition_design",
                "tasks": [
                    {"agent": "product-owner-agent", "task": "Draft and prioritize epic"},
                    {"agent": "business-analyst-agent", "task": "Create user stories and acceptance criteria"},
                    {"agent": "solutions-architect-agent", "task": "Design system architecture"},
                    {"agent": "security-expert-agent", "task": "Create threat model"}
                ]
            },
            {
                "phase": "build_qa", 
                "tasks": [
                    {"agent": "software-developer-agent", "task": "Implement core functionality"},
                    {"agent": "QA-engineer-agent", "task": "Create test plans"},
                    {"agent": "test-automation-expert-agent", "task": "Automate test cases"}
                ]
            },
            {
                "phase": "delivery_operations",
                "tasks": [
                    {"agent": "devops-engineer-agent", "task": "Setup CI/CD pipeline"},
                    {"agent": "product-owner-agent", "task": "Final acceptance review"}
                ]
            }
        ]
        
        return self._create_tasks_from_workflow(project, workflow_phases)
    
    def _start_data_science_workflow(self, project: Project) -> List[Task]:
        """Start the data science/ML workflow."""
        workflow_phases = [
            {
                "phase": "problem_framing",
                "tasks": [
                    {"agent": "product-owner-agent", "task": "Define business problem and metrics"},
                    {"agent": "business-analyst-agent", "task": "Document success criteria"}
                ]
            },
            {
                "phase": "data_engineering",
                "tasks": [
                    {"agent": "data-engineer-agent", "task": "Build data pipelines"}
                ]
            },
            {
                "phase": "analysis_experimentation",
                "tasks": [
                    {"agent": "data-scientist-agent", "task": "Exploratory data analysis and modeling"}
                ]
            },
            {
                "phase": "operationalization",
                "tasks": [
                    {"agent": "ML-engineer-agent", "task": "Productionize models"}
                ]
            }
        ]
        
        return self._create_tasks_from_workflow(project, workflow_phases)
    
    def _create_tasks_from_workflow(self, project: Project, workflow_phases: List[Dict]) -> List[Task]:
        """Create tasks from workflow definition."""
        tasks = []
        task_counter = 1
        
        for phase in workflow_phases:
            for task_def in phase["tasks"]:
                task = Task(
                    id=f"{project.id}_task_{task_counter:03d}",
                    title=task_def["task"],
                    description=f"{task_def['task']} for project {project.name}",
                    agent=task_def["agent"],
                    human_reviewer=project.team.get(task_def["agent"].replace("-agent", ""), "")
                )
                
                tasks.append(task)
                self.active_tasks[task.id] = task
                task_counter += 1
        
        self._save_state()
        return tasks
    
    def assign_task(self, task_id: str) -> str:
        """Assign a task to an agent and generate the agent prompt."""
        task = self.active_tasks.get(task_id)
        if not task:
            raise ValueError(f"Task not found: {task_id}")
        
        agent = self.agent_registry.get_agent(task.agent)
        if not agent:
            raise ValueError(f"Agent not found: {task.agent}")
        
        # Update task status
        task.status = "in_progress"
        self._save_state()
        
        # Generate agent prompt
        prompt = self._generate_agent_prompt(agent, task)
        
        logger.info(f"Assigned task {task_id} to agent {task.agent}")
        return prompt
    
    def _generate_agent_prompt(self, agent: AgentPersona, task: Task) -> str:
        """Generate a prompt for the agent to work on the task."""
        project = None
        for p in self.projects.values():
            if task.id.startswith(p.id):
                project = p
                break
        
        prompt = f"""
# Agent Assignment: {agent.role}

## Agent Persona
{agent.content}

## Task Assignment
**Task ID**: {task.id}
**Title**: {task.title}
**Description**: {task.description}
**Due Date**: {task.due_date or 'Not specified'}
**Human Reviewer**: {task.human_reviewer}

## Project Context
**Project**: {project.name if project else 'Unknown'}
**Project Type**: {project.type if project else 'Unknown'}
**Current Phase**: {project.current_phase if project else 'Unknown'}

## Standards to Follow
You must adhere to all standards referenced in your persona, including:
{chr(10).join(f"- ./development-standards/{ref}" for ref in agent.standards_references)}

## Expected Deliverables
{chr(10).join(f"- {deliverable}" for deliverable in task.deliverables)}

## Instructions
1. Review the project brief and relevant standards
2. Complete the assigned task according to your persona guidelines
3. Create all specified deliverables
4. When complete, mark the task as "draft_ready" and notify the human reviewer
5. Be prepared to incorporate feedback and make revisions as needed

## Handoff Protocol
When you complete this task:
1. Update the task status to "draft_ready"
2. Create a handoff document listing all deliverables
3. Notify {task.human_reviewer} for review
4. Wait for approval before proceeding to the next task

Begin working on this task now.
"""
        
        return prompt

class CommunicationHub:
    """Hub for managing communication between agents and humans."""
    
    def __init__(self, workflow_engine: WorkflowEngine):
        self.workflow_engine = workflow_engine
        self.message_log: List[Dict] = []
        self.notifications: List[Dict] = []
    
    def send_message(self, from_agent: str, to_agent: str, message: str, context: Dict = None) -> None:
        """Send a message between agents."""
        message_record = {
            "id": self._generate_message_id(),
            "timestamp": datetime.utcnow().isoformat(),
            "from": from_agent,
            "to": to_agent,
            "message": message,
            "context": context or {},
            "type": "agent_communication"
        }
        
        self.message_log.append(message_record)
        logger.info(f"Message sent from {from_agent} to {to_agent}")
    
    def notify_human(self, human_email: str, subject: str, message: str, urgency: str = "normal") -> None:
        """Send notification to a human team member."""
        notification = {
            "id": self._generate_message_id(),
            "timestamp": datetime.utcnow().isoformat(),
            "recipient": human_email,
            "subject": subject,
            "message": message,
            "urgency": urgency,
            "status": "pending",
            "type": "human_notification"
        }
        
        self.notifications.append(notification)
        
        # In a real implementation, this would send an actual email/Slack message
        logger.info(f"Notification queued for {human_email}: {subject}")
    
    def _generate_message_id(self) -> str:
        """Generate a unique message ID."""
        import uuid
        return f"msg_{uuid.uuid4().hex[:8]}"
    
    def get_conversation_history(self, agent_name: str, limit: int = 50) -> List[Dict]:
        """Get conversation history for an agent."""
        agent_messages = [
            msg for msg in self.message_log
            if msg["from"] == agent_name or msg["to"] == agent_name
        ]
        
        return sorted(agent_messages, key=lambda x: x["timestamp"], reverse=True)[:limit]

# Main orchestrator class
class AgenticSDLC:
    """Main orchestrator for the Agentic SDLC system."""
    
    def __init__(self, agents_dir: Path = Path("./sub-agents")):
        self.agent_registry = AgentRegistry(agents_dir)
        self.workflow_engine = WorkflowEngine(self.agent_registry)
        self.communication_hub = CommunicationHub(self.workflow_engine)
    
    def initialize_project(self, project_brief_path: str) -> Project:
        """Initialize a new project from a project brief."""
        brief_path = Path(project_brief_path)
        project = self.workflow_engine.create_project(brief_path)
        
        # Send initial notifications
        self.communication_hub.notify_human(
            project.team.get("product_owner", ""),
            f"Project Initialized: {project.name}",
            f"Your project {project.name} has been initialized and is ready to begin.",
            urgency="normal"
        )
        
        return project
    
    def start_project_workflow(self, project_id: str) -> List[Task]:
        """Start the workflow for a project."""
        tasks = self.workflow_engine.start_workflow(project_id)
        
        # Notify team members about task assignments
        for task in tasks:
            if task.human_reviewer:
                self.communication_hub.notify_human(
                    task.human_reviewer,
                    f"Task Assigned: {task.title}",
                    f"A new task has been assigned to the {task.agent} agent and will require your review.",
                    urgency="normal"
                )
        
        return tasks
    
    def execute_task(self, task_id: str) -> str:
        """Execute a specific task."""
        prompt = self.workflow_engine.assign_task(task_id)
        
        # In a real implementation, this would interface with the actual AI model
        # For now, we return the prompt that would be sent to the AI
        return prompt
    
    def get_project_status(self, project_id: str) -> Dict:
        """Get the current status of a project."""
        project = self.workflow_engine.projects.get(project_id)
        if not project:
            raise ValueError(f"Project not found: {project_id}")
        
        # Get all tasks for this project
        project_tasks = [
            task for task in self.workflow_engine.active_tasks.values()
            if task.id.startswith(project.id)
        ]
        
        # Calculate progress
        completed_tasks = len([t for t in project_tasks if t.status == "completed"])
        total_tasks = len(project_tasks)
        progress = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0
        
        return {
            "project_id": project.id,
            "project_name": project.name,
            "status": project.status,
            "progress": progress,
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "active_tasks": len([t for t in project_tasks if t.status == "in_progress"]),
            "pending_reviews": len([t for t in project_tasks if t.status == "draft_ready"])
        }

# CLI interface for testing
def main():
    """Main CLI interface for testing the agentic SDLC system."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Agentic SDLC Management System")
    parser.add_argument("command", choices=["list-agents", "create-project", "start-workflow", "status"])
    parser.add_argument("--project-brief", help="Path to project brief file")
    parser.add_argument("--project-id", help="Project ID for operations")
    
    args = parser.parse_args()
    
    # Initialize the system
    sdlc = AgenticSDLC()
    
    if args.command == "list-agents":
        agents = sdlc.agent_registry.list_agents()
        print("Available Agents:")
        for agent in agents:
            agent_obj = sdlc.agent_registry.get_agent(agent)
            print(f"  - {agent}: {agent_obj.role}")
    
    elif args.command == "create-project":
        if not args.project_brief:
            print("Error: --project-brief required for create-project")
            return
        
        project = sdlc.initialize_project(args.project_brief)
        print(f"Created project: {project.name} (ID: {project.id})")
    
    elif args.command == "start-workflow":
        if not args.project_id:
            print("Error: --project-id required for start-workflow")
            return
        
        tasks = sdlc.start_project_workflow(args.project_id)
        print(f"Started workflow with {len(tasks)} tasks")
        for task in tasks:
            print(f"  - {task.id}: {task.title} (Agent: {task.agent})")
    
    elif args.command == "status":
        if not args.project_id:
            print("Error: --project-id required for status")
            return
        
        status = sdlc.get_project_status(args.project_id)
        print(f"Project Status: {status['project_name']}")
        print(f"  Progress: {status['progress']:.1f}%")
        print(f"  Total Tasks: {status['total_tasks']}")
        print(f"  Completed: {status['completed_tasks']}")
        print(f"  Active: {status['active_tasks']}")
        print(f"  Pending Review: {status['pending_reviews']}")

if __name__ == "__main__":
    main()