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

### Step 4: Activate AI Assistant Integration (CRITICAL!)

**🚨 IMPORTANT: This step is ESSENTIAL for the Human-in-the-Loop (HITL) design to work properly!**

```bash
# 1. Customize your project requirements
notepad project-brief.md  # Windows
vim project-brief.md      # Linux/Mac

# 2. Review the master-agent.md file (it's at root level!)
cat master-agent.md       # Linux/Mac
type master-agent.md      # Windows
```

#### **🤖 AI Assistant Integration (REQUIRED)**

The framework is designed for **Human-in-the-Loop (HITL)** operation. You MUST integrate with an AI assistant:

**For Claude/ChatGPT/Other AI Assistants:**

1. **Add master-agent.md to your AI context:**
   - **Method 1:** Drag and drop `master-agent.md` into your AI chat
   - **Method 2:** Copy the entire contents of `master-agent.md` and paste into AI chat
   - **Method 3:** Use "Add file" or "Attach" feature in your AI assistant

2. **Activate the Master Agent role:**
   ```
   Please read the master-agent.md file I just shared. 
   From now on, you are the Master Agent for this project. 
   Please confirm you understand your role and are ready to coordinate the development workflow according to the HITL protocols defined in the file.
   ```

3. **Provide project context:**
   - Also share your `project-brief.md` with the AI
   - Share any specific requirements or constraints
   - Ask the Master Agent to create the initial project plan

4. **Verify HITL activation:**
   ```
   Master Agent, please confirm:
   1. You will follow the HITL protocols requiring human approval at key decision points
   2. You will coordinate with sub-agents as defined in the framework
   3. You will respect quality gates and development standards
   4. You understand your role is to orchestrate, not replace human judgment
   ```

#### **⚠️ WITHOUT AI INTEGRATION, THE FRAMEWORK WILL NOT FUNCTION AS DESIGNED!**

The Agentic Framework is built on the principle that AI agents orchestrate work **with** humans, not instead of humans. The Master Agent coordinates:
- Task breakdown and delegation
- Quality gate checkpoints  
- Human approval workflows
- Sub-agent coordination
- Progress tracking and reporting

```bash
# 3. Start the framework workflow (after AI integration)
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