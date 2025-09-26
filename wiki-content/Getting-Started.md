# Getting Started with Agentic Framework

This guide will help you install and create your first project with the Agentic SDLC Framework.

## 📦 Installation

### Method 1: Virtual Environment (Recommended)

The virtual environment method prevents PATH issues and ensures clean installation:

```bash
# Create virtual environment
python -m venv agentic-env

# Activate virtual environment
# Windows:
agentic-env\Scripts\activate
# macOS/Linux:
source agentic-env/bin/activate

# Install framework
pip install git+https://github.com/LinoGoncalves/agentic-framework.git

# Verify installation
agentic-framework --version
```

### Method 2: System Installation

```bash
# Install directly to system Python
pip install git+https://github.com/LinoGoncalves/agentic-framework.git

# If you get "command not found" errors:
python -m agentic_framework doctor
```

## 🚀 Your First Project

### Step 1: Launch Master Agent

The easiest way to get started is with the interactive Master Agent:

```bash
agentic-framework master-agent
```

This launches an interactive menu with 6 options:
- 🚀 Quick Start Guide
- 📚 Framework Overview  
- 🏗️ Create New Project ← **Start here!**
- 📋 View Templates
- ✨ Advanced Features
- 📖 Help & Resources

### Step 2: Create Your Project

Choose **Option 3: Create New Project** from the Master Agent menu, then:

1. **Enter project name**: `my-awesome-app`
2. **Choose project type** from 15+ options:
   - `web-app` - Web Application (default)
   - `api` - REST API Service
   - `dashboard` - Data Dashboard
   - `ml-model` - ML Model Serving
   - `cli` - CLI Tool
   - And many more!

### Step 3: Navigate to Your Project

```bash
cd my-awesome-app
ls
```

You'll see this structure:
```
my-awesome-app/
├── master-agent.md              # 🎯 Master orchestration guide (ROOT LEVEL!)
├── project-brief.md             # Your project requirements
├── README.md                    # Project documentation
├── sub-agents/                  # 21 AI agent specifications
├── development-standards/       # Coding standards and templates
├── templates/                   # Framework templates
└── agentic-scripts/            # CLI tools
```

### Step 4: Start Development

```bash
# Customize your project requirements
notepad project-brief.md  # Windows
vim project-brief.md      # macOS/Linux

# Add master-agent.md to your AI assistant (Claude, ChatGPT, etc.)
# It's right at the root level - just drag and drop!

# Start the framework workflow
python agentic-scripts/cli.py start
```

## 🎯 Key Features You'll Use

### Master Agent Integration
- The `master-agent.md` file is at the root level for easy AI context access
- Contains complete orchestration workflows and agent coordination
- Perfect for adding to Claude, ChatGPT, or other AI assistants

### 21 Specialized AI Agents
Each project includes specifications for:
- Business Analyst Agent
- Software Developer Agent  
- QA Engineer Agent
- DevOps Engineer Agent
- Security Engineer Agent
- And 16 more specialized roles!

### Development Standards
Your project includes comprehensive standards for:
- Coding style guides
- API design patterns
- Security checklists
- Testing strategies
- MLOps pipelines

## ⚡ Alternative Methods

### Direct CLI Creation
If you prefer command-line:

```bash
# Create web application
agentic-framework init my-web-app --type web-app

# Create API service
agentic-framework init my-api --type api

# Create with custom output directory
agentic-framework init my-project --type dashboard --output /path/to/projects
```

### Interactive Wizard
For detailed project customization:

```bash
agentic-new
```

This opens a comprehensive wizard with all project options.

## 🆘 Troubleshooting

### Commands Not Found
```bash
# Use diagnostic tool
agentic-framework doctor

# Or use module execution
python -m agentic_framework master-agent
python -m agentic_framework init my-project
```

### PATH Issues
The `doctor` command will show you exactly how to fix PATH issues for your operating system.

### Need Help?
- Run `agentic-framework master-agent` and choose **Option 6: Help & Resources**
- Check the [Troubleshooting](Troubleshooting) wiki page
- Open an issue on [GitHub](https://github.com/LinoGoncalves/agentic-framework/issues)

## 🎉 What's Next?

Once your project is created:
1. **Review** the [Master Agent Guide](Master-Agent-Guide) 
2. **Explore** available [Project Types](Project-Types)
3. **Learn** about [AI Agents](AI-Agents) and their roles
4. **Customize** [Development Standards](Development-Standards) for your needs

Welcome to systematic, AI-assisted development! 🚀