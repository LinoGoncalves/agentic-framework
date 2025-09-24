#!/usr/bin/env python3
"""
Simplified Project Creator for Agentic SDLC Framework
Automatically handles git submodule setup with fallback to copy method.
"""

import os
import sys
import json
import shutil
import subprocess
from pathlib import Path
from datetime import datetime

class ProjectCreator:
    """Creates new projects with automated framework integration."""
    
    def __init__(self):
        """Initialize project creator."""
        self.framework_path = Path(__file__).parent.parent
        self.current_dir = Path.cwd()
    
    def create_project(self, project_name: str, project_type: str = "web-app"):
        """Create a new project with automatic framework setup."""
        project_dir = self.current_dir / project_name
        
        if project_dir.exists():
            print(f"❌ Directory {project_name} already exists!")
            return False
        
        print(f"🚀 Creating project: {project_name}")
        project_dir.mkdir()
        os.chdir(project_dir)
        
        try:
            # Initialize git repository
            subprocess.run(['git', 'init'], check=True, capture_output=True)
            
            # Try submodule approach first
            if self._setup_with_submodule(project_name, project_type):
                print("✅ Framework integrated as git submodule")
            else:
                print("🔄 Falling back to copy integration...")
                self._setup_with_copy(project_name, project_type)
            
            # Create project files
            self._create_project_files(project_name, project_type)
            
            # Initial commit
            subprocess.run(['git', 'add', '.'], check=True, capture_output=True)
            subprocess.run([
                'git', 'commit', '-m', 
                f"Initial project setup: {project_name}"
            ], check=True, capture_output=True)
            
            print(f"✅ Project {project_name} created successfully!")
            print(f"📁 Location: {project_dir}")
            print("\n🎯 Next Steps:")
            print(f"   1. cd {project_name}")
            print("   2. Edit project-brief.md")
            print("   3. python project_manager.py start")
            
            return True
            
        except Exception as e:
            print(f"❌ Error creating project: {e}")
            # Cleanup on failure
            os.chdir(self.current_dir)
            if project_dir.exists():
                shutil.rmtree(project_dir)
            return False
    
    def _setup_with_submodule(self, project_name: str, project_type: str) -> bool:
        """Try to set up framework as a git submodule."""
        try:
            # Configure git for local repos
            subprocess.run([
                'git', 'config', 'protocol.file.allow', 'always'
            ], check=True, capture_output=True)
            
            # Ensure framework has a remote
            remote_url = self._ensure_framework_remote()
            if not remote_url:
                return False
            
            # Add submodule
            subprocess.run([
                'git', 'submodule', 'add', remote_url, 'framework'
            ], check=True, capture_output=True)
            
            return True
            
        except subprocess.CalledProcessError:
            return False
    
    def _setup_with_copy(self, project_name: str, project_type: str):
        """Set up framework by copying files."""
        framework_dir = Path('framework')
        framework_dir.mkdir()
        
        # Copy framework files
        for item in self.framework_path.iterdir():
            if item.name not in ['.git', '__pycache__', 'scripts']:
                target = framework_dir / item.name
                if item.is_dir():
                    shutil.copytree(item, target)
                else:
                    shutil.copy2(item, target)
        
        # Copy essential scripts
        scripts_dir = framework_dir / 'scripts'
        scripts_dir.mkdir()
        for script in ['agent_integration.py', 'workflow_engine.py']:
            script_path = self.framework_path / 'scripts' / script
            if script_path.exists():
                shutil.copy2(script_path, scripts_dir / script)
    
    def _ensure_framework_remote(self) -> str:
        """Ensure framework has a remote repository."""
        try:
            # Check if framework already has a remote
            result = subprocess.run([
                'git', 'remote', 'get-url', 'origin'
            ], cwd=self.framework_path, capture_output=True, text=True)
            
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip()
        except subprocess.CalledProcessError:
            pass
        
        # Create bare repository for framework
        parent_dir = self.framework_path.parent
        bare_repo = parent_dir / f"{self.framework_path.name}_remote.git"
        
        if not bare_repo.exists():
            subprocess.run([
                'git', 'init', '--bare', str(bare_repo)
            ], check=True, capture_output=True)
        
        # Set up remote and push
        try:
            subprocess.run([
                'git', 'remote', 'add', 'origin', str(bare_repo)
            ], cwd=self.framework_path, check=True, capture_output=True)
        except subprocess.CalledProcessError:
            subprocess.run([
                'git', 'remote', 'set-url', 'origin', str(bare_repo)
            ], cwd=self.framework_path, check=True, capture_output=True)
        
        # Push framework to bare repo
        subprocess.run([
            'git', 'push', '-u', 'origin', 'main'
        ], cwd=self.framework_path, check=True, capture_output=True)
        
        return str(bare_repo)
    
    def _create_project_files(self, project_name: str, project_type: str):
        """Create project-specific files."""
        # Create directory structure
        dirs = ['src', 'tests', 'docs', 'data/raw', 'data/processed', 
                'config', 'results', 'notebooks']
        for dir_path in dirs:
            Path(dir_path).mkdir(parents=True, exist_ok=True)
        
        # Create project manager
        self._create_project_manager(project_name, project_type)
        
        # Create project brief
        self._create_project_brief(project_name, project_type)
        
        # Create config
        self._create_project_config(project_name, project_type)
        
        # Create README
        self._create_readme(project_name, project_type)
    
    def _create_project_manager(self, project_name: str, project_type: str):
        """Create project manager script."""
        content = f'''#!/usr/bin/env python3
"""
{project_name.title()} Project Manager
References the agentic SDLC framework.
"""

import sys
import os
from pathlib import Path
import json

# Add the framework to Python path
FRAMEWORK_PATH = Path(__file__).parent / "framework"
sys.path.insert(0, str(FRAMEWORK_PATH / "scripts"))

# Project configuration
PROJECT_CONFIG = {{
    "project_name": "{project_name}",
    "project_type": "{project_type}", 
    "framework_path": "./framework",
    "use_central_framework": True,
    "agents_enabled": [
        "data-scientist-agent" if "{project_type}" in ["jupyter-notebook", "data-science"] else "software-developer-agent",
        "business-analyst-agent", 
        "qa-engineer-agent"
    ],
    "workflow_type": "data-science" if "{project_type}" in ["jupyter-notebook", "data-science"] else "software"
}}

def start_workflow():
    """Start the agentic workflow."""
    if not FRAMEWORK_PATH.exists():
        print(f"❌ Framework not found at {{FRAMEWORK_PATH}}")
        return
    
    print("🤖 Starting agentic workflow...")
    
    try:
        # Import the framework components
        from agent_integration import AgentRegistry, WorkflowEngine
        
        # Initialize framework components
        registry = AgentRegistry(str(FRAMEWORK_PATH))
        engine = WorkflowEngine(registry)
        
        # Load project-specific agents
        for agent_name in PROJECT_CONFIG["agents_enabled"]:
            agent_path = FRAMEWORK_PATH / "sub-agents" / f"{{agent_name}}.md"
            if agent_path.exists():
                registry.load_agent(agent_name, str(agent_path))
                print(f"📝 Loaded: {{agent_name}}")
        
        print("✅ Workflow initialized!")
        
    except ImportError as e:
        print(f"⚠️  Framework components not available: {{e}}")
        print("📋 Manual workflow mode")

def main():
    """Main project manager interface."""
    import sys
    
    if len(sys.argv) < 2:
        print("{project_name.title()} Project Manager")
        print("Usage:")
        print("  python project_manager.py start    - Start agentic workflow") 
        print("  python project_manager.py status   - Show project status")
        return
    
    command = sys.argv[1]
    
    if command == "start":
        start_workflow()
    elif command == "status":
        print("📊 Project Status")
        print(f"   Framework: {{FRAMEWORK_PATH}}")
        print(f"   Framework Available: {{FRAMEWORK_PATH.exists()}}")
        print(f"   Project Type: {{PROJECT_CONFIG['project_type']}}")
        print(f"   Workflow: {{PROJECT_CONFIG['workflow_type']}}")
    else:
        print(f"❌ Unknown command: {{command}}")

if __name__ == "__main__":
    main()
'''
        
        with open('project_manager.py', 'w') as f:
            f.write(content)
    
    def _create_project_brief(self, project_name: str, project_type: str):
        """Create project brief from template."""
        content = f'''# {project_name.title()} Project

## Project Overview

### Project Name
{project_name.title()}

### Project Type
- {'[x]' if project_type == 'jupyter-notebook' else '[ ]'} Jupyter Notebook Analysis
- {'[x]' if project_type == 'web-app' else '[ ]'} Web Application
- {'[x]' if project_type == 'api' else '[ ]'} REST API Service
- {'[x]' if project_type == 'dashboard' else '[ ]'} Data Dashboard
- [ ] Other: {project_type if project_type not in ['jupyter-notebook', 'web-app', 'api', 'dashboard'] else ''}

### Project Vision

**Problem Statement**:
[Describe the problem this project will solve]

**Solution Overview**:
[Describe the proposed solution]

**Success Criteria**:
- [ ] [Define success criteria]
- [ ] [Add more criteria as needed]

## Scope & Requirements

### Core Functionality
- [List core features]

### Out of Scope
- [List what's explicitly not included]

## Technical Stack

### Framework Integration
- **Agentic SDLC Framework**: Integrated as {'submodule' if Path('framework/.git').exists() else 'copy'}
- **Project Manager**: Available via `python project_manager.py`
- **Agents**: Business Analyst, {'Data Scientist' if project_type in ['jupyter-notebook', 'data-science'] else 'Software Developer'}, QA Engineer

### Next Steps
1. Complete this project brief
2. Run `python project_manager.py start`
3. Begin development with agentic workflow
'''
        
        with open('project-brief.md', 'w') as f:
            f.write(content)
    
    def _create_project_config(self, project_name: str, project_type: str):
        """Create project configuration."""
        config = {
            "project_name": project_name,
            "project_type": project_type,
            "framework_path": "./framework",
            "use_central_framework": True,
            "agents_enabled": [
                "data-scientist-agent" if project_type in ["jupyter-notebook", "data-science"] else "software-developer-agent",
                "business-analyst-agent",
                "qa-engineer-agent"
            ],
            "workflow_type": "data-science" if project_type in ["jupyter-notebook", "data-science"] else "software"
        }
        
        with open('config/project-config.json', 'w') as f:
            json.dump(config, f, indent=2)
    
    def _create_readme(self, project_name: str, project_type: str):
        """Create project README."""
        content = f'''# {project_name.title()}

A {project_type} project using the Agentic SDLC Framework.

## Setup

1. **Review Project Brief**: Edit `project-brief.md` with your specific requirements
2. **Start Workflow**: Run `python project_manager.py start`
3. **Check Status**: Run `python project_manager.py status`

## Framework Integration

This project integrates the Agentic SDLC framework as a {'git submodule' if Path('framework/.git').exists() else 'copy'}.

- **Framework Path**: `./framework/`
- **Agents**: Business Analyst, {'Data Scientist' if project_type in ['jupyter-notebook', 'data-science'] else 'Software Developer'}, QA Engineer
- **Workflow**: {'Data Science' if project_type in ['jupyter-notebook', 'data-science'] else 'Software Development'}

## Directory Structure

```
{project_name}/
├── framework/           # Agentic SDLC framework
├── src/                # Source code
├── tests/              # Test files
├── docs/               # Documentation
├── data/               # Data files
├── config/             # Configuration files
├── project_manager.py  # Project automation
└── project-brief.md    # Project specification
```

## Usage

The project manager provides commands for working with the agentic framework:

```bash
# Start the agentic workflow
python project_manager.py start

# Check project status
python project_manager.py status
```
'''
        
        with open('README.md', 'w') as f:
            f.write(content)

def main():
    """Command line interface for project creation."""
    if len(sys.argv) < 2:
        print("🚀 Agentic SDLC Project Creator")
        print("Usage: python create_project.py <project_name> [project_type]")
        print()
        print("Project Types:")
        print("  web-app         - Web application")
        print("  api             - REST API service")
        print("  jupyter-notebook- Jupyter notebook analysis")
        print("  data-science    - Data science project")
        print("  dashboard       - Data dashboard")
        print("  cli             - Command line tool")
        sys.exit(1)
    
    project_name = sys.argv[1]
    project_type = sys.argv[2] if len(sys.argv) > 2 else "web-app"
    
    creator = ProjectCreator()
    success = creator.create_project(project_name, project_type)
    
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()