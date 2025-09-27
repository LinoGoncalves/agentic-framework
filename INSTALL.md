# Installation and Usage Guide

**🚨 CRITICAL: This framework operates under Human-in-the-Loop (HITL) protocols - AI agents coordinate WITH humans, requiring approval at all quality gates!**

## Installation Methods

### Method 1: GitHub Installation (Latest Version - Recommended)

Install the latest version with all the newest features:

```bash
pip install git+https://github.com/LinoGoncalves/agentic-framework.git
```

### Method 2: Virtual Environment (Prevents PATH Issues)

**Highly recommended to avoid PATH complications:**

```bash
# Create and activate virtual environment
python -m venv agentic-env

# Windows:
agentic-env\Scripts\activate

# macOS/Linux:
source agentic-env/bin/activate

# Install framework
pip install git+https://github.com/LinoGoncalves/agentic-framework.git

# Now all commands work perfectly:
agentic-framework master-agent
```

### Method 3: Development Installation

For contributing or customizing the framework:

```bash
git clone https://github.com/LinoGoncalves/agentic-framework.git
cd agentic-framework
pip install -e ".[dev]"
```

## Quick Verification

After installation, verify it works:

```bash
agentic-framework --version

# Should show: agentic-framework 0.2.0 (or newer)
```

## 🚀 Getting Started

### Step 1: Launch Master Agent (NEW!)

The easiest way to get started:

```bash
agentic-framework master-agent
```

This launches an interactive guide with:
- 🚀 Quick Start Guide
- 📚 Framework Overview  
- 🏗️ Guided Project Creation
- 📋 Template Browser
- ✨ Advanced Features Info
- 📖 Help & Resources

### Step 2: Create Your First Project

```bash
# Option 1: Through Master Agent (recommended)
agentic-framework master-agent
# → Select option 3: Create New Project

# Option 2: Interactive wizard
agentic-new

# Option 3: Direct command
agentic-framework init my-awesome-project --type web-app
```

## 📁 Available Project Types (15+ Options!)

When creating projects, you can choose from these comprehensive types:

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

### Usage Examples

```bash
# Web application (default)
agentic-framework init my-webapp

# Machine learning project
agentic-framework init ml-classifier --type ml-model

# Data dashboard
agentic-framework init sales-dashboard --type dashboard

# Custom project type
agentic-framework init my-project --type other
# Will prompt: "Enter your custom project type: blockchain-dapp"
```

### 3. Working with Created Projects

After creating a project:

```bash
cd my-web-app
After creation, your project will have:

```
cd my-web-app
ls  # You'll see: master-agent.md, project-brief.md, README.md, sub-agents/, etc.

# 🎯 KEY FEATURE: Development standards are in .github/development_standards/ following VS Code/GitHub best practices!
```

### Working with Your Project

```bash
# Customize your requirements
notepad project-brief.md  # Windows
vim project-brief.md      # Linux/Mac

# Add master-agent.md to Claude/ChatGPT context (it's right there at root level!)
# Just drag master-agent.md into your AI chat

# Start the agentic workflow
python agentic-scripts/cli.py start
```

## 📂 Project Structure Explained

After creation, your project will have this organized structure:

```
my-project/
├── master-agent.md               # 🎯 Master orchestration guide (AT ROOT!)
├── project-brief.md              # Your requirements and specifications
├── README.md                     # Project-specific README
├── sub-agents/                   # AI agent specifications
│   ├── business-analyst-agent.md
│   ├── software-developer-agent.md
│   ├── qa-engineer-agent.md
│   └── ... (21 total agents)
├── development-standards/        # Templates and standards
│   ├── coding_styleguide.md
│   ├── testing_strategy.md
│   └── ... (comprehensive standards)
├── templates/                    # Framework templates
│   ├── project-brief-template.md
│   ├── quality-gates.md
│   └── ... (workflow templates)
└── agentic-scripts/             # Framework tools
    └── cli.py                   # Project management CLI
```

**✨ Special Feature:** The `master-agent.md` file is strategically placed at the project root level, making it incredibly easy to add to AI context (Claude, ChatGPT, etc.) when working on your project.

## Troubleshooting

### Command not found

If `agentic-framework` command is not found after installation:

```bash
# Check if it's installed
pip list | grep agentic-framework

# Reinstall with user flag
pip install --user agentic-framework

# Add to PATH (if needed)
export PATH=$PATH:~/.local/bin  # Linux/Mac
```

### Permission errors

On Windows, you might need administrator privileges:
```cmd
# Run as administrator
pip install agentic-framework
```

### Python version compatibility

The framework requires Python 3.8+:
```bash
python --version  # Should be 3.8 or higher
```

## Next Steps

1. **Create your first project** using `agentic-new`
2. **Customize the project brief** in `project-brief.md`
3. **Review the agent roles** in the `sub-agents/` directory
4. **Start development** with `python agentic-scripts/cli.py start`
5. **Follow the workflow** guided by the AI agents

## Getting Help

- Read the main [README.md](README.md) for framework overview
- Check the [project documentation](https://github.com/agentic-framework/agentic-framework)
- Open an [issue](https://github.com/agentic-framework/agentic-framework/issues) for bugs or questions