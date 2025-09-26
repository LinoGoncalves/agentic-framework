# Repository Structure vs Project Structure

## 📂 GitHub Repository Structure (for browsing/contributing)

When browsing this repository on GitHub, the structure uses underscores:

```
agentic-framework/
├── agentic_framework/                    # Main Python package
│   ├── development_standards/           # 📚 Browse development standards
│   ├── sub_agents/                      # 🤖 Browse AI agent specifications  
│   ├── templates/                       # 📋 Framework templates
│   └── ...
```

**Browse development standards:** [`agentic_framework/development_standards/`](agentic_framework/development_standards/)

**Browse AI agents:** [`agentic_framework/sub_agents/`](agentic_framework/sub_agents/)

## 🏗️ Created Project Structure (when you run `agentic-framework init`)

When you create a new project, the structure uses hyphens for better readability:

```
my-project/
├── master-agent.md                      # 🎯 At root for easy AI context access
├── sub-agents/                          # 🤖 AI agent specifications (copied from repo)
├── development-standards/               # 📚 Coding standards (copied from repo)
├── project-brief.md                     # 📋 Your project requirements
└── ...
```

This distinction exists because:
- **Repository structure** follows Python package naming conventions (underscores)
- **Project structure** uses readable names (hyphens) for end users

## 🔗 Correct GitHub URLs

- **Development Standards Directory:** https://github.com/LinoGoncalves/agentic-framework/tree/main/agentic_framework/development_standards
- **Sub Agents Directory:** https://github.com/LinoGoncalves/agentic-framework/tree/main/agentic_framework/sub_agents
- **Templates Directory:** https://github.com/LinoGoncalves/agentic-framework/tree/main/agentic_framework/templates