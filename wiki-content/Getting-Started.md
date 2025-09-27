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
├── templates/                   # Framework templates  
└── agentic-scripts/            # CLI tools

# At WORKSPACE level (outside project folder):
workspace/
├── .github/                     # 📁 VS Code/GitHub integration (NEW in v0.3.1!)
│   ├── copilot-instructions.md  #    AI assistant configuration
│   ├── chatmodes/               #    Custom AI chat modes for VS Code
│   │   └── Master Agent.md      #    HITL-enforced coordination mode
│   └── development_standards/   #    Professional coding standards
└── my-awesome-app/             # Your project directory
```

**🎯 Key Structure Changes in v0.3.1:**
- `.github/` directory now correctly placed at **workspace level** (not inside project)
- VS Code integration files apply to entire workspace
- Follows official VS Code and GitHub best practices

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

**🆕 VS Code Integration Features:**

The `.github/` directory in your project includes VS Code-specific integration:
- **`copilot-instructions.md`** - Automatically recognized by VS Code Copilot for coding standards
- **`chatmodes/Master Agent.md`** - Custom chat mode available in VS Code's chat mode dropdown
- **`development_standards/`** - Professional GitHub repository structure following official guidelines

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
- Coding style guides (in `.github/development_standards/` following VS Code/GitHub best practices)
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

## 🧠 Enterprise Features (v0.3.2+)

### Context Management for Large Projects

The framework now includes intelligent context management for enterprise-scale codebases:

**Hierarchical Context Architecture:**
- **High Priority (20%):** Master instructions, current phase, recent decisions
- **Medium Priority (50%):** Agent persona, technical context, phase standards
- **Low Priority (30%):** Historical discussions, archived decisions, references

**Phase Transition Management:**
- Automated context compression with human validation
- Decision registry tracking all human approvals
- Context quality monitoring and drift detection
- Early warning alerts when context limits approach

**Usage:**
The context management protocols are automatically active in both the root-level `master-agent.md` and VS Code chat mode. No additional configuration required - the system will prompt for human approval when context optimization is needed.

## 🎯 Development Roadmap

The framework follows a comprehensive 4-phase roadmap for enterprise scaling:

- **Phase 1 (v0.3.2):** ✅ Context Compression & Hierarchical Architecture
- **Phase 2 (v0.4.0):** Smart Checkpointing System (4-6 weeks)
- **Phase 3 (v0.5.0):** External Memory Integration (8-12 weeks) 
- **Phase 4 (v0.6.0+):** Advanced Context Intelligence (12+ weeks)

See [ROADMAP.md](https://github.com/LinoGoncalves/agentic-framework/blob/main/ROADMAP.md) for complete details.

Welcome to systematic, AI-assisted development with enterprise-scale capabilities! 🚀