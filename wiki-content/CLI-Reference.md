# CLI Reference - Complete Command Guide

This page provides comprehensive documentation for all Agentic Framework CLI commands.

## 🚀 Main Commands

### Master Agent (Interactive Guide)
```bash
agentic-framework master-agent
```
Launches the interactive Master Agent with 6 main options:
- **Quick Start Guide** - Step-by-step instructions
- **Framework Overview** - Core concepts and architecture  
- **Create New Project** - Guided project creation
- **View Templates** - Browse available templates
- **Advanced Features** - Domain experts and validation
- **Help & Resources** - Documentation and troubleshooting

**Shortcut:** `agentic-master-agent`

### Project Creation
```bash
# Direct project creation
agentic-framework init <project-name> [--type <type>] [--output <directory>]

# Interactive wizard
agentic-new

# Examples:
agentic-framework init my-web-app --type web-app
agentic-framework init ml-classifier --type ml-model
agentic-framework init my-api --type api --output /projects
```

**Shortcuts:** 
- `agentic-init <name>` 
- `agentic-new`

### Diagnostics
```bash
agentic-framework doctor
```
Diagnoses installation issues and provides PATH setup guidance.

**Shortcut:** `agentic-doctor`

### Version Information
```bash
agentic-framework --version
agentic-framework -h  # Help
```

## 📁 Project Types (15+ Options)

### Web & API Applications
- `web-app` - Web Application (Django/Flask/FastAPI) **[DEFAULT]**
- `api` - REST API Service
- `dashboard` - Data Dashboard (Streamlit)
- `microservice` - Microservice Architecture

### Data Science & ML
- `data-science` - Data Science Research
- `ml-model` - ML Model Serving
- `data-pipeline` - Data Pipeline/ETL
- `jupyter-notebook` - Jupyter Notebook Analysis

### Development Tools
- `cli` - CLI Tool
- `desktop-app` - Desktop Application (PyQt/Tkinter)
- `testing` - Testing Framework
- `devops` - DevOps/Infrastructure

### Flexible Options
- `custom` - Custom Project Type
- `other` - Specify your own completely custom type

## 🔧 Alternative Command Forms

If you encounter PATH issues, all commands can be run using Python module execution:

```bash
# Instead of: agentic-framework master-agent
python -m agentic_framework master-agent

# Instead of: agentic-new
python -m agentic_framework new

# Instead of: agentic-framework init my-project
python -m agentic_framework init my-project

# Instead of: agentic-framework doctor
python -m agentic_framework doctor
```

## 📋 Command Examples

### Creating Different Project Types

```bash
# Web application (default)
agentic-framework init my-webapp

# Machine learning project
agentic-framework init ml-classifier --type ml-model

# Data dashboard
agentic-framework init sales-dashboard --type dashboard

# CLI tool
agentic-framework init my-cli-tool --type cli

# Custom project type
agentic-framework init blockchain-app --type other
# Will prompt: "Enter your custom project type: blockchain-dapp"

# Specify output directory
agentic-framework init my-project --type api --output C:\Projects
```

### Using Master Agent Features

```bash
# Launch Master Agent
agentic-framework master-agent

# Then select:
# 1 - Quick Start Guide (learn the basics)
# 2 - Framework Overview (understand architecture)  
# 3 - Create New Project (guided creation)
# 4 - View Templates (browse available files)
# 5 - Advanced Features (domain experts, validation)
# 6 - Help & Resources (troubleshooting, documentation)
# 0 - Exit
```

### Troubleshooting Commands

```bash
# Check installation
agentic-framework --version

# Diagnose PATH issues
agentic-framework doctor

# Alternative if commands not found
python -m agentic_framework doctor

# Get help
agentic-framework --help
agentic-framework master-agent  # Choose option 6
```

## ⚙️ Advanced Usage

### Environment Variables

The framework respects these environment variables:

- `AGENTIC_OUTPUT_DIR` - Default output directory for new projects
- `AGENTIC_PROJECT_TYPE` - Default project type
- `AGENTIC_SKIP_VALIDATION` - Skip project validation (development only)

### Configuration Files

Projects include these configuration files:

- `project-brief.md` - Project requirements and specifications
- `master-agent.md` - Master orchestration guide (at root level!)
- `agentic-scripts/cli.py` - Project-specific CLI tools

### Integration with Existing Projects

```bash
# Add agentic framework to existing project (planned feature)
cd existing-project
agentic-framework enhance --add-standards --add-agents
```

## 🆘 Common Issues

### "Command not found"
```bash
# Solution 1: Use module execution
python -m agentic_framework master-agent

# Solution 2: Run diagnostics
python -m agentic_framework doctor

# Solution 3: Use virtual environment
python -m venv agentic-env
agentic-env\Scripts\activate  # Windows
pip install git+https://github.com/LinoGoncalves/agentic-framework.git
```

### PATH Issues
Run the doctor command for your operating system:
```bash
agentic-framework doctor
# or
python -m agentic_framework doctor
```

### Permission Issues
```bash
# Windows: Run as administrator
# macOS/Linux: Use pip install --user
pip install --user git+https://github.com/LinoGoncalves/agentic-framework.git
```

## 📖 Related Pages

- [Getting Started](Getting-Started) - Installation and first project
- [Master Agent Guide](Master-Agent-Guide) - Interactive guide details
- [Project Types](Project-Types) - Detailed project type descriptions
- [Troubleshooting](Troubleshooting) - Common issues and solutions

---

**Tip:** The Master Agent interactive guide (`agentic-framework master-agent`) provides contextual help and is often the best place to start! 🎯