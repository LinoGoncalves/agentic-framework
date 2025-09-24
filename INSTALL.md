# Installation and Usage Guide

## Installation Methods

### Method 1: PyPI Installation (Recommended)

For most users, the simplest installation method:

```bash
pip install agentic-framework
```

### Method 2: GitHub Installation (Latest Features)

To get the latest development version:

```bash
pip install git+https://github.com/agentic-framework/agentic-framework.git
```

### Method 3: Development Installation

For contributing or customizing the framework:

```bash
git clone https://github.com/agentic-framework/agentic-framework.git
cd agentic-framework
pip install -e ".[dev]"
```

## Quick Verification

After installation, verify it works:

```bash
agentic-framework --version
```

## Usage Examples

### 1. Interactive Project Creation (Recommended for Beginners)

```bash
agentic-new
```

This starts an interactive wizard that guides you through:
- Project name selection
- Project type selection (from 13 options)
- Output directory configuration

### 2. Direct Project Creation (For Experienced Users)

```bash
# Create a web application
agentic-framework init my-web-app --type web-app

# Create an API service
agentic-framework init my-api --type api

# Create with custom output directory
agentic-framework init my-project --type dashboard --output /path/to/projects
```

### 3. Working with Created Projects

After creating a project:

```bash
cd my-web-app
ls  # You'll see: project-brief.md, README.md, sub-agents/, development-standards/, agentic-scripts/

# Customize your requirements
notepad project-brief.md  # Windows
vim project-brief.md      # Linux/Mac

# Start the agentic workflow
python agentic-scripts/cli.py start
```

## Project Structure Explained

After creation, your project will have:

```
my-project/
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
└── agentic-scripts/             # Framework tools
    └── cli.py                   # Project management CLI
```

## Supported Project Types

1. **web-app** - Web Applications (Django/Flask/FastAPI)
2. **api** - REST API Services
3. **dashboard** - Data Dashboards (Streamlit)
4. **ml-model** - ML Model Serving
5. **data-pipeline** - Data Pipeline/ETL
6. **cli** - CLI Tools
7. **jupyter-notebook** - Jupyter Notebook Analysis
8. **desktop-app** - Desktop Applications (PyQt/Tkinter)
9. **microservice** - Microservice Architecture
10. **data-science** - Data Science Research
11. **devops** - DevOps/Infrastructure
12. **testing** - Testing Frameworks
13. **custom** - Custom Project Types

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