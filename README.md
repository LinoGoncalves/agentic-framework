
# Agentic SDLC Framework

A production-ready Human-in-the-Loop (HITL) software development lifecycle framework that orchestrates AI agents with human oversight for systematic project delivery.

[![GitHub Release](https://img.shields.io/github/v/release/LinoGoncalves/agentic-framework)](https://github.com/LinoGoncalves/agentic-framework/releases)
[![Python Support](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Issues](https://img.shields.io/github/issues/LinoGoncalves/agentic-framework)](https://github.com/LinoGoncalves/agentic-framework/issues)

## 📦 Installation

### ✅ Recommended: Virtual Environment (Avoids PATH Issues)

```bash
# Create and activate virtual environment
python -m venv agentic-env

# Windows:
agentic-env\Scripts\activate

# macOS/Linux:
source agentic-env/bin/activate

# Install agentic-framework
pip install git+https://github.com/LinoGoncalves/agentic-framework.git

# Now CLI commands work without PATH issues:
agentic-new
agentic-framework init my-project
```

### 🔧 System Installation (May Require PATH Setup)

```bash
pip install git+https://github.com/LinoGoncalves/agentic-framework.git
```

**If you get "command not found" errors after installation:**

```bash
# Use the diagnostic tool
python -m agentic_framework doctor

# Or use module execution as alternative:
python -m agentic_framework new
python -m agentic_framework init my-project
```

### For Development

```bash
git clone https://github.com/LinoGoncalves/agentic-framework.git
cd agentic-framework
pip install -e ".[dev]"
```

### ⚠️ Windows PATH Notes

If you get a PATH warning during installation, the CLI commands are installed but may not be accessible from any directory. You can:

1. **Use the recommended virtual environment approach above** (prevents PATH issues)
2. **Add to PATH manually**: Add `%APPDATA%\Python\Python3XX\Scripts` to your system PATH
3. **Run with full path**: Use `python -m agentic_framework.cli` instead of `agentic-framework`

## 🚀 Quick Start

### Create Your First Project

```bash
# Interactive wizard (recommended for beginners)
agentic-new

# Or direct command for experienced users  
agentic-framework init my-web-app --type web-app

# If commands not found, use module execution:
python -m agentic_framework new
python -m agentic_framework init my-web-app --type web-app
```

### Troubleshooting Installation

```bash
# Run diagnostics to check installation
python -m agentic_framework doctor

# This will show you exactly how to fix PATH issues
```

### Navigate and Start Development

```bash
cd my-web-app
python agentic-scripts/cli.py start
```

### Available Commands

After installation, you have access to these commands:

- `agentic-framework init <name>` - Create a new project directly  
- `agentic-new` - Interactive project creation wizard
- `agentic-framework --version` - Show version information

## 🎯 What This Framework Does

Transform complex software projects into manageable, AI-assisted workflows:

- **🤖 AI Agent Orchestra**: 21 specialized agents (Business Analyst, Developer, QA, DevOps, etc.)
- **🧑‍💼 Human-in-the-Loop**: Clear handoff points where humans review and approve
- **📋 Structured Process**: From requirements to deployment with quality gates
- **🔄 Continuous Learning**: Framework improves based on project experience
- **📊 Progress Tracking**: Real-time visibility into project status

## 🏗️ Framework Components

### Core Orchestration
- **Master Agent**: Central workflow coordinator and task dispatcher  
- **21 Sub-Agents**: Domain specialists with HITL protocols
- **Quality Gates**: Automated validation at key project milestones
- **Template Library**: Pre-configured project structures and standards

### Development Standards Suite
- **Coding Standards**: Style guides, security checklists, testing strategies
- **API Design**: RESTful patterns, documentation templates, versioning
- **Cloud Architecture**: Infrastructure as Code, security policies, tagging
- **MLOps Pipeline**: Data science workflows, model deployment, monitoring

## 📁 Project Types Supported

Choose from 13 specialized project templates:

1. **Web Applications** - Full-stack web development with modern frameworks
2. **Mobile Apps** - iOS/Android development with cross-platform support  
3. **Data Science** - ML/AI projects with proper MLOps integration
4. **Cloud Infrastructure** - IaC templates for AWS/Azure/GCP
5. **API Services** - Microservices and REST API development
6. **Desktop Applications** - Cross-platform desktop app frameworks
7. **IoT Solutions** - Internet of Things device integration
8. **Blockchain Projects** - Smart contracts and DeFi applications
9. **Game Development** - 2D/3D game engines and frameworks
10. **DevOps Automation** - CI/CD pipelines and infrastructure automation
11. **Security Tools** - Cybersecurity utilities and penetration testing
12. **Analytics Dashboards** - Business intelligence and data visualization
13. **Research Projects** - Academic and R&D project structures

## 🚀 Architecture Overview

```
Agentic Framework
├── Master Agent (Orchestrator)
├── Sub-Agents (21 Specialists)
│   ├── Business Analyst
│   ├── Solutions Architect  
│   ├── Software Developer
│   ├── QA Engineer
│   ├── DevOps Engineer
│   └── ... (16 more)
├── Development Standards
├── Quality Gates
└── Template Library
```

## 🔧 Advanced Usage

### Custom Project Configuration

```python
from agentic_framework import FrameworkManager

# Initialize with custom settings
framework = FrameworkManager()
framework.init_project(
    name="my-custom-project",
    project_type="web-app",
    standards_level="enterprise",
    enable_quality_gates=True
)
```

### Integration with Existing Projects

```bash
# Add agentic framework to existing project
cd existing-project
agentic-framework enhance --add-standards --add-agents
```

## 📖 Documentation

- [Installation Guide](INSTALL.md) - Detailed setup instructions
- [Framework Management Guide](framework-management-guide.md) - Core concepts
- [Master Agent Guide](master-agent.md) - Orchestration workflows  
- [Quality Gates](quality-gates.md) - Validation and testing strategies
- [Development Standards](development-standards/) - Complete standards library

## 🤝 Contributing

We welcome contributions! See our [contributing guidelines](CONTRIBUTING.md) for details on:

- Adding new sub-agents
- Creating project templates  
- Improving development standards
- Enhancing quality gates

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **GitHub Issues**: [Report bugs or request features](https://github.com/LinoGoncalves/agentic-framework/issues)
- **Documentation**: [Full documentation](https://github.com/LinoGoncalves/agentic-framework/wiki)
- **Community**: [Discussions and Q&A](https://github.com/LinoGoncalves/agentic-framework/discussions)
