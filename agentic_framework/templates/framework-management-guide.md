# Framework Management & Project Initialization Guide

## Overview

This guide explains how to use the agentic SDLC framework across multiple projects while ensuring framework enhancements flow back to the core template for continuous improvement.

## Framework Structure

The agentic SDLC framework has two distinct layers:

### 1. Core Framework (Template Repository)

- **Location**: `c:\DEV\agentic_SDLC` (your template/trunk)
- **Purpose**: Master template with reusable components
- **Contents**: Agent definitions, development standards, workflow templates, automation scripts
- **Maintenance**: Enhanced based on project learnings and improvements

### 2. Project Instances (Working Copies)

- **Location**: Individual project directories
- **Purpose**: Active development with project-specific customizations
- **Contents**: Framework copy + project-specific code, data, configurations
- **Lifecycle**: Created from template, customized for project, contributes back to template

## Project Initialization Strategies

### Option 1: Framework-as-Submodule (Recommended)

This approach keeps the framework separate from project code while allowing easy updates:

```bash
# Step 1: Create new project directory
mkdir my-new-project
cd my-new-project

# Step 2: Initialize project git repo
git init

# Step 3: Add agentic SDLC as a submodule
git submodule add file:///c:/DEV/agentic_SDLC .agentic-framework

# Step 4: Create project structure
mkdir src tests docs data
mkdir -p config/environments

# Step 5: Create project-specific files
cp .agentic-framework/project-brief-template.md project-brief.md

# Step 6: Initialize project with enhanced CLI
python scripts/framework_manager.py init my-project --type web-app
```

**Advantages**:

- Framework updates can be pulled easily: `git submodule update --remote`
- Clear separation between framework and project code
- Framework improvements can be pushed back to trunk
- Multiple projects share the same framework version or can upgrade independently

### Option 2: Framework-as-Copy (Simpler Setup)

For simpler scenarios where you want full control:

```bash
# Step 1: Use the framework manager
cd c:\DEV\agentic_SDLC
python scripts/framework_manager.py init my-project --type api --copy

# This creates a complete copy with:
# - All framework files copied
# - Git repository initialized
# - Project-specific structure created
# - Configuration files customized
```

**Advantages**:

- Self-contained project
- No submodule complexity
- Full customization freedom

**Disadvantages**:

- Manual effort to sync framework improvements
- Framework changes need to be manually merged back

### Option 3: Framework-as-Template-Repo (GitHub/GitLab)

For organizations with multiple teams:

1. **Setup** (done once by framework maintainer):

   ```bash
   # Create template repository from framework
   git clone c:\DEV\agentic_SDLC agentic-sdlc-template
   cd agentic-sdlc-template
   # Push to your Git hosting service as template repository
   ```

2. **Usage** (for each new project):
   ```bash
   # Use "Use this template" button in GitHub/GitLab
   # Or clone and reinitialize:
   git clone https://github.com/yourorg/agentic-sdlc-template.git my-new-project
   cd my-new-project
   python scripts/framework_manager.py init my-project --type dashboard
   ```

## Recommended Project Structure

```
my-project/
├── .agentic-framework/          # Framework submodule (Option 1)
│   ├── master-agent.md
│   ├── sub-agents/
│   ├── development-standards/
│   ├── scripts/
│   └── quality-gates.md
├── project-brief.md             # Customized from template
├── .agentic-state/              # Project workflow state
│   ├── current-state.json
│   ├── agent-assignments.json
│   └── quality-gates-status.json
├── src/                         # Your project code
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   ├── services/
│   └── utils/
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── data/                        # Project-specific data
│   ├── raw/
│   ├── processed/
│   └── external/
├── docs/
│   ├── architecture.md
│   ├── api-documentation.md
│   └── deployment-guide.md
├── config/
│   ├── agentic-config.json      # Project-specific agent config
│   └── environments/
│       ├── development.env
│       ├── staging.env
│       └── production.env
├── agentic-scripts/             # Local automation scripts
│   ├── cli.py                   # Project CLI wrapper
│   └── project_manager.py
└── agentic-enhancements/        # Framework improvements to merge back
    ├── new-agents/
    ├── standard-updates/
    └── script-improvements/
```

## Framework Enhancement Workflow

### 1. Identify Enhancement During Project

During development, you may discover improvements that would benefit the core framework:

```markdown
# File: agentic-enhancements/enhancement-log.md

## Enhancement: Better Error Handling in Agent Integration

- **Date**: 2025-09-24
- **Project**: Customer Analytics Platform
- **Issue**: Agent integration script doesn't handle API timeouts gracefully
- **Solution**: Add retry logic with exponential backoff
- **Files Modified**: scripts/agent_integration.py
- **Impact**: All projects using agent automation
```

### 2. Implement Enhancement in Project Context

```bash
# Create enhancement branch
python agentic-scripts/cli.py enhance "better-error-handling" "Add retry logic to agent integration"

# Implement your improvements
# Test thoroughly in project context
# Document the changes in agentic-enhancements/better-error-handling/
```

### 3. Merge Enhancement Back to Framework

```bash
# For submodule approach
cd .agentic-framework
git checkout -b enhancement/better-error-handling

# Copy your improvements
cp ../agentic-enhancements/better-error-handling/agent_integration.py scripts/

# Commit and create PR
git add .
git commit -m "Enhancement: Add retry logic to agent integration

- Adds exponential backoff for API timeouts
- Improves resilience in agent communication  
- Tested in Customer Analytics Platform project
- Addresses issue: agents failing on network hiccups"

git push origin enhancement/better-error-handling
```

## Practical Usage Commands

### Starting a New Project

```bash
# Option 1: Submodule approach (recommended)
cd c:\DEV\agentic_SDLC
python scripts/framework_manager.py init customer-analytics --type dashboard

# Option 2: Copy approach
python scripts/framework_manager.py init customer-analytics --type dashboard --copy

# Navigate to project
cd customer-analytics

# Check status
python agentic-scripts/cli.py status

# Start workflow
python agentic-scripts/cli.py start
```

### Managing Framework Updates

```bash
# Update framework in submodule project
cd my-project
python agentic-scripts/cli.py update

# Check what changed
git diff HEAD~1 .agentic-framework

# Test with updated framework
python agentic-scripts/cli.py status
```

### Contributing Enhancements

```bash
# In your project directory
# Document enhancement need
python agentic-scripts/cli.py enhance "performance-optimization" "Optimize workflow state persistence"

# Implement and test changes
# ... development work ...

# Prepare for merge back
python agentic-scripts/cli.py merge performance-optimization

# Follow the guided process to create PR
```

## Quality Assurance for Framework Changes

### Before Merging to Framework

1. **Test in Multiple Project Types**:

   ```bash
   # Test enhancement in different project types
   python scripts/framework_manager.py init test-web-app --type web-app
   python scripts/framework_manager.py init test-ml-model --type ml-model
   python scripts/framework_manager.py init test-pipeline --type data-pipeline
   ```

2. **Backward Compatibility Check**:

   ```bash
   # Ensure existing projects still work
   cd existing-project
   python agentic-scripts/cli.py status  # Should work without errors
   ```

3. **Documentation Update**:
   - Update relevant agent files
   - Update development standards if needed
   - Update this guide if process changes

### Framework Release Management

```bash
# In framework repository
git tag -a v1.1.0 -m "Release v1.1.0: Enhanced agent integration with retry logic"
git push origin v1.1.0

# Notify all project teams
# Update template repository if using Option 3
```

## Example: Complete Project Lifecycle

### 1. Project Start

```bash
# Initialize new fintech dashboard project
cd c:\DEV\agentic_SDLC
python scripts/framework_manager.py init fintech-dashboard --type dashboard

cd fintech-dashboard
# Edit project-brief.md with specific requirements
# Commit initial setup
git add . && git commit -m "Initial project setup"
```

### 2. Development Phase

```bash
# Start agentic workflow
python agentic-scripts/cli.py start

# Work with agents through the workflow
# Monitor status
python agentic-scripts/cli.py status

# During development, identify framework improvement
python agentic-scripts/cli.py enhance "streamlit-components" "Add reusable Streamlit components for financial charts"
```

### 3. Enhancement Implementation

```bash
# Implement the enhancement
# Create: agentic-enhancements/streamlit-components/financial_charts.py
# Document: agentic-enhancements/streamlit-components/README.md
# Test in project context
```

### 4. Contributing Back

```bash
# Prepare enhancement for framework
python agentic-scripts/cli.py merge streamlit-components

# Follow prompts to:
# - Copy files to framework
# - Create feature branch
# - Commit changes
# - Push for review
```

### 5. Framework Update

```bash
# After enhancement is approved and merged
python agentic-scripts/cli.py update

# Framework now includes your improvement
# Available for all future projects
```

## Troubleshooting Common Issues

### Submodule Update Conflicts

```bash
# If submodule update creates conflicts
cd .agentic-framework
git stash  # Save any local changes
git pull origin main
cd ..
git add .agentic-framework
git commit -m "Update framework to latest version"
```

### Framework Manager Not Found

```bash
# If framework_manager.py is missing
cd c:\DEV\agentic_SDLC
git pull  # Update to latest framework version

# Or if you have a copy-based project:
# Manually copy the new framework_manager.py from the master template
```

### Project Configuration Issues

```bash
# Reset project configuration
python agentic-scripts/cli.py status --reset
python agentic-scripts/cli.py init --reconfigure
```

## Best Practices Summary

1. **Always use the framework manager** for project initialization
2. **Document enhancements** as you identify them during development  
3. **Test framework changes** in multiple project contexts before merging
4. **Keep enhancements focused** - one improvement per enhancement branch
5. **Update framework regularly** in active projects
6. **Communicate changes** to team members when framework updates
7. **Version your enhancements** for better tracking and rollback capability

This approach ensures your agentic SDLC framework continuously evolves and improves based on real project experience while maintaining consistency across all your development efforts.