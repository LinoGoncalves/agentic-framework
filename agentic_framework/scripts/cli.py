#!/usr/bin/env python3
"""
Agentic SDLC Command Line Interface

Simple CLI wrapper for managing the agentic SDLC workflows.
"""

import sys
import json
from pathlib import Path
from typing import Optional

# Add the scripts directory to Python path
sys.path.append(str(Path(__file__).parent))

from agent_integration import AgenticSDLC

class AgenticSDLCCLI:
    """Command line interface for Agentic SDLC."""
    
    def __init__(self):
        self.sdlc = AgenticSDLC()
    
    def list_agents(self) -> None:
        """List all available agents."""
        print("🤖 Available AI Agents:")
        print("=" * 50)
        
        agents = self.sdlc.agent_registry.list_agents()
        for agent_name in sorted(agents):
            agent = self.sdlc.agent_registry.get_agent(agent_name)
            print(f"📋 {agent_name}")
            print(f"   Role: {agent.role}")
            if agent.capabilities:
                print(f"   Capabilities: {', '.join(agent.capabilities[:3])}{'...' if len(agent.capabilities) > 3 else ''}")
            print()
    
    def create_project(self, project_brief_path: str) -> None:
        """Create a new project from project brief."""
        try:
            project = self.sdlc.initialize_project(project_brief_path)
            print(f"✅ Project Created Successfully!")
            print(f"   Name: {project.name}")
            print(f"   ID: {project.id}")
            print(f"   Type: {project.type}")
            print(f"   Workflow: {project.workflow}")
            
            if project.team:
                print(f"   Team Members:")
                for role, member in project.team.items():
                    print(f"     - {role}: {member}")
                    
        except Exception as e:
            print(f"❌ Error creating project: {e}")
    
    def start_workflow(self, project_id: str) -> None:
        """Start workflow for a project."""
        try:
            tasks = self.sdlc.start_project_workflow(project_id)
            print(f"🚀 Workflow Started Successfully!")
            print(f"   Created {len(tasks)} tasks")
            print()
            
            print("📋 Task Summary:")
            print("-" * 60)
            for i, task in enumerate(tasks, 1):
                print(f"{i:2d}. {task.title}")
                print(f"    Agent: {task.agent}")
                print(f"    Reviewer: {task.human_reviewer or 'Not assigned'}")
                print(f"    Status: {task.status}")
                print()
                
        except Exception as e:
            print(f"❌ Error starting workflow: {e}")
    
    def show_status(self, project_id: str) -> None:
        """Show project status."""
        try:
            status = self.sdlc.get_project_status(project_id)
            
            print(f"📊 Project Status: {status['project_name']}")
            print("=" * 60)
            print(f"Progress: {status['progress']:.1f}% complete")
            print(f"Total Tasks: {status['total_tasks']}")
            print(f"✅ Completed: {status['completed_tasks']}")
            print(f"🔄 Active: {status['active_tasks']}")
            print(f"⏳ Pending Review: {status['pending_reviews']}")
            
            # Show detailed task breakdown
            project_tasks = [
                task for task in self.sdlc.workflow_engine.active_tasks.values()
                if task.id.startswith(project_id)
            ]
            
            if project_tasks:
                print()
                print("📋 Task Details:")
                print("-" * 60)
                for task in project_tasks:
                    status_emoji = {
                        "assigned": "📌",
                        "in_progress": "🔄", 
                        "draft_ready": "⏳",
                        "under_review": "👀",
                        "completed": "✅",
                        "revision_requested": "🔄"
                    }.get(task.status, "❓")
                    
                    print(f"{status_emoji} {task.title}")
                    print(f"   Agent: {task.agent}")
                    print(f"   Status: {task.status}")
                    if task.human_reviewer:
                        print(f"   Reviewer: {task.human_reviewer}")
                    print()
                    
        except Exception as e:
            print(f"❌ Error getting project status: {e}")
    
    def execute_task(self, task_id: str) -> None:
        """Execute a specific task."""
        try:
            prompt = self.sdlc.execute_task(task_id)
            print(f"🤖 Task Execution Started")
            print(f"Task ID: {task_id}")
            print()
            print("Generated Agent Prompt:")
            print("=" * 80)
            print(prompt)
            print("=" * 80)
            print()
            print("ℹ️  In a production system, this prompt would be sent to the AI agent.")
            print("   The agent would then work on the task and produce deliverables.")
            
        except Exception as e:
            print(f"❌ Error executing task: {e}")
    
    def interactive_mode(self) -> None:
        """Run in interactive mode."""
        print("🚀 Agentic SDLC Interactive Mode")
        print("=" * 50)
        print("Commands:")
        print("  list-agents - Show available agents")
        print("  create-project <path> - Create new project")
        print("  start-workflow <project-id> - Start project workflow")
        print("  status <project-id> - Show project status")
        print("  execute-task <task-id> - Execute a specific task")
        print("  help - Show this help")
        print("  exit - Exit interactive mode")
        print()
        
        while True:
            try:
                command = input("agentic-sdlc> ").strip()
                
                if not command:
                    continue
                    
                parts = command.split()
                cmd = parts[0].lower()
                
                if cmd == "exit":
                    print("👋 Goodbye!")
                    break
                elif cmd == "help":
                    print("Available commands: list-agents, create-project, start-workflow, status, execute-task, help, exit")
                elif cmd == "list-agents":
                    self.list_agents()
                elif cmd == "create-project":
                    if len(parts) < 2:
                        print("❌ Usage: create-project <path-to-project-brief>")
                    else:
                        self.create_project(parts[1])
                elif cmd == "start-workflow":
                    if len(parts) < 2:
                        print("❌ Usage: start-workflow <project-id>")
                    else:
                        self.start_workflow(parts[1])
                elif cmd == "status":
                    if len(parts) < 2:
                        print("❌ Usage: status <project-id>")
                    else:
                        self.show_status(parts[1])
                elif cmd == "execute-task":
                    if len(parts) < 2:
                        print("❌ Usage: execute-task <task-id>")
                    else:
                        self.execute_task(parts[1])
                else:
                    print(f"❌ Unknown command: {cmd}")
                    print("   Type 'help' for available commands")
                    
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except EOFError:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")

def main():
    """Main CLI entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Agentic SDLC Management System",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # List agents command
    subparsers.add_parser("list-agents", help="List all available AI agents")
    
    # Create project command
    create_parser = subparsers.add_parser("create-project", help="Create a new project")
    create_parser.add_argument("project_brief", help="Path to project brief file")
    
    # Start workflow command  
    start_parser = subparsers.add_parser("start-workflow", help="Start workflow for a project")
    start_parser.add_argument("project_id", help="Project ID")
    
    # Status command
    status_parser = subparsers.add_parser("status", help="Show project status")
    status_parser.add_argument("project_id", help="Project ID")
    
    # Execute task command
    execute_parser = subparsers.add_parser("execute-task", help="Execute a specific task")
    execute_parser.add_argument("task_id", help="Task ID")
    
    # Interactive mode command
    subparsers.add_parser("interactive", help="Run in interactive mode")
    
    args = parser.parse_args()
    
    cli = AgenticSDLCCLI()
    
    if not args.command:
        # No command provided, show help and enter interactive mode
        parser.print_help()
        print()
        print("Starting interactive mode...")
        cli.interactive_mode()
        return
    
    if args.command == "list-agents":
        cli.list_agents()
    elif args.command == "create-project":
        cli.create_project(args.project_brief)
    elif args.command == "start-workflow":
        cli.start_workflow(args.project_id)
    elif args.command == "status":
        cli.show_status(args.project_id)
    elif args.command == "execute-task":
        cli.execute_task(args.task_id)
    elif args.command == "interactive":
        cli.interactive_mode()

if __name__ == "__main__":
    main()