# Agentic Framework Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.3] - 2025-09-27

### Fixed  
- **🚨 CRITICAL: Strengthened HITL Protocol Enforcement in master-agent.md**
  - Added mandatory HITL activation section at the very beginning of file
  - Enhanced all Core Directives with explicit human approval checkpoints
  - Updated Project Kick-off Command with 4-step HITL activation requirement
  - Added final protocol reminder section with specific examples of required approvals
  - AI assistants must now explicitly confirm HITL activation before any work
  - Prevents autonomous operation - forces coordination and planning role only

### Impact
- **AI assistants loading master-agent.md will immediately activate strict HITL mode**
- **No more autonomous decisions - all critical actions require explicit human approval**
- **Clear examples provided for what requires human approval (code, architecture, deployment, etc.)**

## [0.2.2] - 2025-09-27

### Fixed
- **🎯 UI Consistency in Master Agent** - Fixed project type display inconsistency
  - Master Agent's "Create New Project" now shows numbered options (1-14) instead of bullet points
  - Added support for both numeric (1-14) and text input (web-app, api, etc.) for project types
  - Reordered project types to match documentation groupings (Web/API, Data Science/ML, Dev Tools)
  - Consistent user experience across all project creation interfaces

## [0.2.1] - 2025-09-27

### Fixed
- **📝 Project Types Alignment** - Fixed mismatch between interactive wizard and documentation
  - Updated `agentic-new` wizard to show all 14 project types (previously showed 13)  
  - Added missing "other" project type option for completely custom specifications
  - Reordered project types to match documentation groupings (Web/API, Data Science/ML, Dev Tools)
  - Interactive wizard now correctly shows 1-14 options instead of 1-13

## [0.2.0] - 2025-09-27

### Added
- **🤖 Master Agent Interactive Guide** - New `agentic-framework master-agent` command
  - Interactive menu system with 6 main options
  - Quick Start Guide with step-by-step instructions
  - Framework Overview explaining core concepts
  - Guided Project Creation with expanded project types
  - Template Browser showing all available templates
  - Advanced Features guide for domain experts and validation
  - Help & Resources with complete CLI reference
- **📁 Expanded Project Types** - Increased from 4 to 15+ project types
  - Web & API Applications: web-app, api, dashboard, microservice
  - Data Science & ML: data-science, ml-model, data-pipeline, jupyter-notebook
  - Development Tools: cli, desktop-app, testing, devops
  - Flexible Options: custom, other (specify your own)
- **🎯 Master-Agent.md at Root Level** - UX improvement for AI context access
  - master-agent.md now placed at project root (not buried in subfolders)
  - Easy to drag & drop into Claude, ChatGPT, etc.
  - Automatic move during project creation with user notification
- **🔧 Enhanced CLI Commands** - New individual entry points
  - `agentic-master-agent` - Direct access to Master Agent guide
  - `agentic-init <name>` - Quick project creation
  - `agentic-doctor` - Installation diagnostics
  - All commands work with both main CLI and individual shortcuts

### Improved
- **📖 Complete Documentation Overhaul**
  - Updated README.md with current features and project types
  - Refreshed INSTALL.md with Master Agent guidance
  - Added proper project structure visualization
  - Enhanced installation instructions with virtual environment recommendations
- **🚀 User Experience**
  - Interactive guidance reduces learning curve for new users
  - Master Agent provides contextual help and explanations
  - Clear project creation workflow with immediate next steps
  - Better error handling and graceful exits in CLI

### Fixed
- **🔍 Master-Agent Command Availability** - Fixed issue where master-agent command wasn't available after pip install
  - Added proper entry points in pyproject.toml
  - Created dedicated commands.py module with individual entry point functions
  - Bumped version to 0.2.0 to ensure fresh installation without cache issues

### Technical
- Enhanced project creation logic in core.py
- Added comprehensive input handling with EOF protection
- Improved CLI argument parsing and command routing
- Updated package metadata and dependencies

## [0.1.0] - 2025-09-24

### Added
- Initial release of the Agentic SDLC Framework
- 21 specialized AI agents for comprehensive project coverage
- Human-in-the-Loop (HITL) workflows with quality gates
- Interactive project creation wizard
- Command-line interface for project management
- Comprehensive development standards and templates
- Support for 13 different project types
- Professional Python package structure
- PyPI and GitHub distribution ready

### Framework Components
- Master Agent orchestration system
- Business Analyst, Developer, QA, DevOps agents and more
- Development standards templates
- Project brief and workflow management
- CLI tools for easy project initialization

### Project Types Supported
- Web Applications (Django/Flask/FastAPI)
- REST API Services
- Data Dashboards (Streamlit)
- ML Model Serving
- Data Pipelines/ETL
- CLI Tools
- Jupyter Notebook Analysis
- Desktop Applications
- Microservice Architecture
- Data Science Research
- DevOps/Infrastructure
- Testing Frameworks
- Custom Project Types