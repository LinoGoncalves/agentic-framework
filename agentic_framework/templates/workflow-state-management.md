# Workflow State Management

## Overview

This document defines the state management system for tracking project progress through the agentic SDLC workflows. It provides a standardized way to monitor phase completion, manage handoffs between agents, and ensure quality gates are met.

## Workflow States

### Project-Level States

- **INITIATED**: Project brief approved, master agent activated
- **IN_PROGRESS**: Active development across multiple phases
- **BLOCKED**: Waiting for external dependency or approval
- **ON_HOLD**: Temporarily paused (resource constraints, scope changes)
- **COMPLETED**: All phases finished, project delivered
- **CANCELLED**: Project terminated before completion

### Phase-Level States

- **NOT_STARTED**: Phase has not begun
- **IN_PROGRESS**: Phase is actively being worked on
- **REVIEW_PENDING**: Phase deliverables awaiting human review
- **REVIEW_FAILED**: Human reviewer rejected deliverables (requires rework)
- **COMPLETED**: Phase deliverables approved and accepted
- **SKIPPED**: Phase not applicable for this project type

### Agent Task States

- **ASSIGNED**: Task assigned to AI agent
- **IN_PROGRESS**: AI agent actively working on task
- **DRAFT_READY**: AI deliverable ready for human review
- **UNDER_REVIEW**: Human counterpart reviewing AI deliverable
- **REVISION_REQUESTED**: Human requested changes to AI deliverable
- **APPROVED**: Human approved AI deliverable
- **COMPLETED**: Task fully finished and handed off

## State Tracking Schema

### Project State Document

```json
{
  "project": {
    "id": "proj_001",
    "name": "Customer Analytics Dashboard",
    "type": "data_dashboard",
    "status": "IN_PROGRESS",
    "workflow": "data_science",
    "created_at": "2025-09-24T10:00:00Z",
    "updated_at": "2025-09-24T15:30:00Z",
    "estimated_completion": "2025-11-15",
    "current_phase": "analysis_experimentation",
    "team": {
      "product_owner": "john.doe@company.com",
      "lead_developer": "jane.smith@company.com",
      "data_scientist": "alex.johnson@company.com"
    }
  },
  "phases": [
    {
      "name": "problem_framing",
      "status": "COMPLETED",
      "start_date": "2025-09-24T10:00:00Z",
      "completion_date": "2025-09-26T16:00:00Z",
      "agents_involved": ["product-owner-agent", "business-analyst-agent"],
      "deliverables": ["problem_statement.md", "success_metrics.md"],
      "quality_gate_passed": true
    },
    {
      "name": "data_engineering",
      "status": "COMPLETED", 
      "start_date": "2025-09-27T09:00:00Z",
      "completion_date": "2025-10-02T17:00:00Z",
      "agents_involved": ["data-engineer-agent"],
      "deliverables": ["data_pipeline.py", "data_quality_report.md"],
      "quality_gate_passed": true
    },
    {
      "name": "analysis_experimentation",
      "status": "IN_PROGRESS",
      "start_date": "2025-10-03T09:00:00Z",
      "completion_date": null,
      "agents_involved": ["data-scientist-agent"],
      "deliverables": ["eda_notebook.ipynb", "baseline_models.py"],
      "quality_gate_passed": null,
      "current_tasks": [
        {
          "task_id": "task_003_1",
          "description": "Exploratory Data Analysis",
          "agent": "data-scientist-agent",
          "human_reviewer": "alex.johnson@company.com",
          "status": "DRAFT_READY",
          "deliverable": "eda_notebook.ipynb",
          "created_at": "2025-10-03T09:00:00Z",
          "due_date": "2025-10-05T17:00:00Z"
        }
      ]
    }
  ],
  "blockers": [],
  "risks": [
    {
      "id": "risk_001",
      "description": "Data quality issues in source system",
      "impact": "medium",
      "likelihood": "low", 
      "mitigation": "Implement data validation checks",
      "owner": "data-engineer-agent"
    }
  ]
}
```

### Agent Task Document

```json
{
  "task": {
    "id": "task_003_1",
    "project_id": "proj_001", 
    "phase": "analysis_experimentation",
    "title": "Exploratory Data Analysis",
    "description": "Perform comprehensive EDA on customer transaction data",
    "agent": "data-scientist-agent",
    "human_reviewer": "alex.johnson@company.com",
    "status": "DRAFT_READY",
    "priority": "high",
    "created_at": "2025-10-03T09:00:00Z",
    "due_date": "2025-10-05T17:00:00Z",
    "estimated_hours": 16,
    "actual_hours": 14
  },
  "deliverables": [
    {
      "name": "eda_notebook.ipynb",
      "type": "jupyter_notebook",
      "path": "./analysis/eda_notebook.ipynb",
      "status": "ready_for_review",
      "ai_confidence": 0.85,
      "checksum": "abc123def456"
    }
  ],
  "dependencies": [
    {
      "task_id": "task_002_1",
      "description": "Data pipeline must be completed",
      "status": "completed"
    }
  ],
  "reviews": [
    {
      "reviewer": "alex.johnson@company.com",
      "review_date": null,
      "status": "pending",
      "feedback": null,
      "approved": null
    }
  ],
  "conversation_log": [
    {
      "timestamp": "2025-10-03T09:00:00Z",
      "actor": "master-agent",
      "action": "task_assigned",
      "message": "Task assigned to data-scientist-agent"
    },
    {
      "timestamp": "2025-10-03T14:30:00Z",
      "actor": "data-scientist-agent", 
      "action": "progress_update",
      "message": "Completed initial data loading and cleaning"
    },
    {
      "timestamp": "2025-10-04T16:45:00Z",
      "actor": "data-scientist-agent",
      "action": "deliverable_ready",
      "message": "EDA notebook completed and ready for review"
    }
  ]
}
```

## State Transitions

### Valid State Transitions

#### Project States
```
INITIATED → IN_PROGRESS → COMPLETED
INITIATED → CANCELLED
IN_PROGRESS → BLOCKED → IN_PROGRESS
IN_PROGRESS → ON_HOLD → IN_PROGRESS
IN_PROGRESS → CANCELLED
```

#### Phase States  
```
NOT_STARTED → IN_PROGRESS → REVIEW_PENDING → COMPLETED
NOT_STARTED → SKIPPED
REVIEW_PENDING → REVIEW_FAILED → IN_PROGRESS
```

#### Task States
```
ASSIGNED → IN_PROGRESS → DRAFT_READY → UNDER_REVIEW → APPROVED → COMPLETED
UNDER_REVIEW → REVISION_REQUESTED → IN_PROGRESS
```

### Automatic State Triggers

```python
# Example state transition rules
STATE_TRANSITION_RULES = {
    "task_completed": {
        "condition": "all_phase_tasks_approved",
        "action": "set_phase_status(REVIEW_PENDING)"
    },
    "phase_completed": {
        "condition": "quality_gate_passed AND human_approval_received",
        "action": "set_phase_status(COMPLETED) AND start_next_phase()"
    },
    "deliverable_submitted": {
        "condition": "ai_agent_finished_task",
        "action": "set_task_status(DRAFT_READY) AND notify_human_reviewer()"
    },
    "review_completed": {
        "condition": "human_review_submitted",
        "action": "set_task_status(APPROVED/REVISION_REQUESTED)"
    }
}
```

## Progress Tracking

### Phase Progress Calculation

```python
def calculate_phase_progress(phase):
    """Calculate completion percentage for a phase."""
    total_tasks = len(phase.tasks)
    completed_tasks = len([t for t in phase.tasks if t.status == "COMPLETED"])
    return (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0

def calculate_project_progress(project):
    """Calculate overall project completion percentage."""
    phase_weights = {
        "problem_framing": 0.10,
        "requirements": 0.15,
        "architecture": 0.20,
        "development": 0.35,
        "testing": 0.15,
        "deployment": 0.05
    }
    
    total_progress = 0
    for phase in project.phases:
        phase_progress = calculate_phase_progress(phase)
        weight = phase_weights.get(phase.name, 0)
        total_progress += phase_progress * weight
    
    return min(total_progress, 100.0)
```

### Key Performance Indicators

#### Timeline KPIs
- **Phase Duration**: Actual vs estimated time per phase
- **Project Duration**: Overall timeline adherence
- **Cycle Time**: Time from task assignment to completion
- **Review Time**: Time for human review and approval

#### Quality KPIs  
- **First-Pass Approval Rate**: Percentage of AI deliverables approved without revision
- **Rework Rate**: Percentage of tasks requiring revision
- **Quality Gate Pass Rate**: Percentage of phases passing quality gates
- **Defect Density**: Issues found per deliverable

#### Collaboration KPIs
- **Response Time**: Average time for human review responses
- **Agent Utilization**: Percentage of time agents are actively working
- **Handoff Efficiency**: Time between phase transitions
- **Communication Frequency**: Number of status updates per phase

## Quality Gates

### Phase Quality Gates

#### Requirements Phase Gate
```yaml
quality_gate_requirements:
  criteria:
    - all_user_stories_have_acceptance_criteria: true
    - business_analyst_approval: required
    - product_owner_sign_off: required
    - requirements_traceability: complete
  automated_checks:
    - gherkin_syntax_validation: pass
    - story_completeness_check: pass
  minimum_deliverables:
    - user_stories.md
    - acceptance_criteria.md
    - requirements_traceability_matrix.xlsx
```

#### Architecture Phase Gate
```yaml
quality_gate_architecture:
  criteria:
    - architecture_review_completed: true
    - security_review_passed: true
    - performance_requirements_addressed: true
    - solutions_architect_approval: required
  automated_checks:
    - architecture_documentation_complete: pass
    - security_checklist_complete: pass
  minimum_deliverables:
    - system_architecture.md
    - api_specifications.yaml
    - security_threat_model.md
```

#### Development Phase Gate
```yaml
quality_gate_development:
  criteria:
    - code_review_completed: true
    - unit_test_coverage: ">= 80%"
    - security_scan_passed: true
    - performance_tests_passed: true
  automated_checks:
    - ruff_linting: pass
    - mypy_type_checking: pass
    - bandit_security_scan: pass
    - pytest_coverage: ">= 80%"
  minimum_deliverables:
    - source_code_with_tests
    - code_review_report.md
    - performance_test_results.md
```

### Gate Enforcement

```python
class QualityGateChecker:
    """Enforces quality gates for phase transitions."""
    
    def check_gate(self, phase: Phase, gate_config: dict) -> dict:
        """Check if phase meets quality gate criteria."""
        results = {
            "passed": True,
            "criteria_met": {},
            "automated_checks": {},
            "missing_deliverables": [],
            "blockers": []
        }
        
        # Check criteria
        for criterion, required_value in gate_config["criteria"].items():
            actual_value = self._evaluate_criterion(phase, criterion)
            results["criteria_met"][criterion] = actual_value == required_value
            if not results["criteria_met"][criterion]:
                results["passed"] = False
                results["blockers"].append(f"Criterion not met: {criterion}")
        
        # Run automated checks
        for check_name, expected_result in gate_config["automated_checks"].items():
            check_result = self._run_automated_check(phase, check_name)
            results["automated_checks"][check_name] = check_result
            if check_result != expected_result:
                results["passed"] = False
                results["blockers"].append(f"Automated check failed: {check_name}")
        
        # Check deliverables
        for deliverable in gate_config["minimum_deliverables"]:
            if not self._deliverable_exists(phase, deliverable):
                results["missing_deliverables"].append(deliverable)
                results["passed"] = False
                results["blockers"].append(f"Missing deliverable: {deliverable}")
        
        return results
```

## Handoff Management

### Handoff Protocol

```python
class HandoffManager:
    """Manages transitions between agents and phases."""
    
    def initiate_handoff(self, from_agent: str, to_agent: str, context: dict):
        """Start handoff process between agents."""
        handoff_id = self._generate_handoff_id()
        
        handoff = {
            "id": handoff_id,
            "from_agent": from_agent,
            "to_agent": to_agent,
            "status": "initiated",
            "context": context,
            "deliverables": context.get("deliverables", []),
            "created_at": datetime.utcnow(),
            "completion_deadline": self._calculate_deadline(context)
        }
        
        # Create handoff record
        self.state_store.save_handoff(handoff)
        
        # Notify receiving agent
        self._notify_agent(to_agent, "handoff_received", handoff)
        
        # Notify human stakeholders
        self._notify_humans(context.get("stakeholders", []), handoff)
        
        return handoff_id
    
    def complete_handoff(self, handoff_id: str, acceptance: dict):
        """Complete handoff process."""
        handoff = self.state_store.get_handoff(handoff_id)
        
        if acceptance.get("accepted", False):
            handoff["status"] = "completed"
            self._update_task_states(handoff, "COMPLETED")
        else:
            handoff["status"] = "rejected"
            handoff["rejection_reason"] = acceptance.get("reason", "")
            self._update_task_states(handoff, "REVISION_REQUESTED")
        
        self.state_store.save_handoff(handoff)
        self._log_handoff_completion(handoff)
```

### Handoff Documentation Template

```markdown
# Handoff: [From Agent] → [To Agent/Human]

## Context
**Project**: [Project Name]
**Phase**: [Current Phase]
**Date**: [Handoff Date]
**Deadline**: [Review Deadline]

## Deliverables Ready for Review
- [ ] [Deliverable 1] - [File Path] - [Description]
- [ ] [Deliverable 2] - [File Path] - [Description]

## Work Summary
[Brief description of work completed]

### Key Decisions Made
- [Decision 1 and rationale]
- [Decision 2 and rationale]

### Assumptions Made
- [Assumption 1]
- [Assumption 2]

### Blockers Encountered
- [Blocker 1 and resolution]
- [Blocker 2 and current status]

## Next Steps
[What the receiving agent/human should do next]

## Questions/Clarifications Needed
- [Question 1]
- [Question 2]

## Review Checklist
- [ ] All deliverables are complete and accessible
- [ ] Code follows development standards (if applicable)
- [ ] Tests are written and passing (if applicable)
- [ ] Documentation is updated
- [ ] Security considerations addressed
- [ ] Performance requirements met

## Acceptance
**Reviewer**: [Name/Role]
**Review Date**: [Date]
**Status**: [ ] Approved [ ] Needs Revision [ ] Rejected
**Feedback**: [Detailed feedback]
**Next Actions**: [What needs to be done next]
```

## Monitoring Dashboard

### Real-time Status Display

```python
class ProjectDashboard:
    """Real-time project status dashboard."""
    
    def get_project_overview(self, project_id: str) -> dict:
        """Get high-level project status."""
        project = self.state_store.get_project(project_id)
        
        return {
            "project_name": project.name,
            "overall_progress": calculate_project_progress(project),
            "current_phase": project.current_phase,
            "status": project.status,
            "team_size": len(project.team),
            "days_in_progress": (datetime.utcnow() - project.created_at).days,
            "estimated_completion": project.estimated_completion,
            "active_tasks": len([t for t in self._get_all_tasks(project) if t.status == "IN_PROGRESS"]),
            "pending_reviews": len([t for t in self._get_all_tasks(project) if t.status == "UNDER_REVIEW"]),
            "blockers": len(project.blockers)
        }
    
    def get_phase_details(self, project_id: str) -> list:
        """Get detailed phase information."""
        project = self.state_store.get_project(project_id)
        
        phase_details = []
        for phase in project.phases:
            phase_details.append({
                "name": phase.name,
                "status": phase.status,
                "progress": calculate_phase_progress(phase),
                "start_date": phase.start_date,
                "estimated_completion": phase.estimated_completion,
                "agents_involved": phase.agents_involved,
                "deliverables_completed": len([d for d in phase.deliverables if d.status == "completed"]),
                "deliverables_total": len(phase.deliverables),
                "quality_gate_passed": phase.quality_gate_passed
            })
        
        return phase_details
```

### Notification System

```python
class NotificationManager:
    """Manages notifications for state changes."""
    
    def send_notification(self, event_type: str, recipients: list, context: dict):
        """Send notification based on event type."""
        
        notification_templates = {
            "task_ready_for_review": {
                "subject": "Task Ready for Review: {task_title}",
                "template": "A task is ready for your review in project {project_name}.",
                "urgency": "normal"
            },
            "quality_gate_failed": {
                "subject": "Quality Gate Failed: {phase_name}",
                "template": "Phase {phase_name} failed quality gate in project {project_name}.",
                "urgency": "high"
            },
            "project_blocked": {
                "subject": "Project Blocked: {project_name}",
                "template": "Project {project_name} is blocked: {blocker_reason}",
                "urgency": "high"
            }
        }
        
        template = notification_templates.get(event_type)
        if template:
            self._send_email(recipients, template, context)
            self._log_notification(event_type, recipients, context)
```

This comprehensive state management system provides full visibility and control over your agentic SDLC workflows, ensuring nothing falls through the cracks and quality standards are maintained throughout the development process.