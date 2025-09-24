#!/usr/bin/env python3
"""
Enhanced Agentic SDLC CLI with Framework Management
Handles project initialization, framework updates, and enhancement merging.
"""

import os
import sys
import json
import shutil
import subprocess
from pathlib import Path
from typing import Dict, List, Optional
import click
from datetime import datetime

import os
import sys
import json
import shutil
import subprocess
from pathlib import Path
from typing import Dict, List, Optional
import click
from datetime import datetime

class FrameworkManager:
    """Manages agentic SDLC framework across projects."""
    
    def __init__(self, framework_path: Optional[str] = None):
        """Initialize framework manager."""
        self.framework_path = Path(framework_path) if framework_path else self._detect_framework_path()
        self.project_root = Path.cwd()
        
    def _detect_framework_path(self) -> Path:
        """Detect framework path based on current context."""
        # Check if we're in a project with submodule
        if (Path.cwd() / '.agentic-framework').exists():
            return Path.cwd() / '.agentic-framework'
        
        # Check if we're in the framework itself
        if (Path.cwd() / 'master-agent.md').exists():
            return Path.cwd()
            
        # Default fallback
        return Path('c:/DEV/agentic_SDLC')
    
    def init_project(self, project_name: str, project_type: str = "web-app", use_submodule: bool = True):
        """Initialize a new project with agentic SDLC framework."""
        project_dir = Path.cwd() / project_name
        
        if project_dir.exists():
            raise click.ClickException(f"Directory {project_name} already exists!")
        
        click.echo(f"🚀 Initializing project: {project_name}")
        project_dir.mkdir()
        os.chdir(project_dir)
        
        # Initialize git repo
        subprocess.run(['git', 'init'], check=True)
        
        if use_submodule:
            try:
                self._setup_submodule_project(project_name, project_type)
            except (subprocess.CalledProcessError, Exception) as e:
                click.echo(f"⚠️  Submodule setup failed: {e}")
                click.echo("🔄 Falling back to copy approach...")
                use_submodule = False
                self._setup_copy_project(project_name, project_type)
        else:
            self._setup_copy_project(project_name, project_type)
        
        click.echo(f"✅ Project {project_name} initialized successfully!")
        click.echo(f"📁 Location: {project_dir}")
        click.echo(f"🔧 Next steps:")
        click.echo(f"   1. cd {project_name}")
        click.echo(f"   2. Edit project-brief.md")
        click.echo(f"   3. python agentic-scripts/cli.py start")
    
    def _setup_submodule_project(self, project_name: str, project_type: str):
        """Setup project using submodule approach."""
        # Add framework as submodule using absolute path
        framework_path = str(self.framework_path.absolute()).replace('\\', '/')
        
        try:
            subprocess.run([
                'git', 'submodule', 'add', 
                framework_path, '.agentic-framework'
            ], check=True, cwd=Path.cwd())
        except subprocess.CalledProcessError:
            # Fallback: copy approach if submodule fails
            click.echo("⚠️  Submodule failed, using copy approach instead...")
            return self._setup_copy_project(project_name, project_type)
        
        # Create project structure
        self._create_project_structure()
        
        # Copy and customize templates
        self._setup_project_files(project_name, project_type, use_submodule=True)
        self._create_project_type_specific_files(project_name, project_type)
        
        # Initial commit
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run([
            'git', 'commit', '-m', 
            f"Initial setup: {project_name} with agentic SDLC framework"
        ], check=True)
    
    def _setup_copy_project(self, project_name: str, project_type: str):
        """Setup project using copy approach."""
        # Copy framework files
        for item in self.framework_path.iterdir():
            if item.name not in ['.git', '__pycache__']:
                if item.is_dir():
                    shutil.copytree(item, item.name)
                else:
                    shutil.copy2(item, item.name)
        
        # Create project-specific structure
        self._create_project_structure()
        self._setup_project_files(project_name, project_type, use_submodule=False)
        self._create_project_type_specific_files(project_name, project_type)
        
        # Initial commit
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run([
            'git', 'commit', '-m', 
            f"Initial setup: {project_name} from agentic SDLC framework"
        ], check=True)
    
    def _create_project_structure(self):
        """Create standard project directory structure."""
        dirs = [
            'src', 'tests', 'docs', 'data', 
            'config/environments', '.agentic-state', 
            'agentic-enhancements/new-agents',
            'agentic-enhancements/standard-updates',
            'agentic-enhancements/script-improvements'
        ]
        
        for dir_path in dirs:
            Path(dir_path).mkdir(parents=True, exist_ok=True)
    
    def _setup_project_files(self, project_name: str, project_type: str, use_submodule: bool):
        """Setup project-specific configuration files."""
        # Copy and customize project brief
        template_path = '.agentic-framework/project-brief-template.md' if use_submodule else 'project-brief-template.md'
        shutil.copy2(template_path, 'project-brief.md')
        
        # Create project config
        config = {
            "project_name": project_name,
            "project_type": project_type,
            "framework_version": "1.0",
            "created_date": datetime.now().isoformat(),
            "use_submodule": use_submodule,
            "agents": {
                "enabled": ["business-analyst-agent", "software-developer-agent", "qa-engineer-agent"],
                "workflow_type": "software" if project_type in ["web-app", "api", "cli"] else "data-science"
            }
        }
        
        with open('config/agentic-config.json', 'w') as f:
            json.dump(config, f, indent=2)
        
        # Copy automation scripts
        script_dir = 'agentic-scripts'
        Path(script_dir).mkdir(exist_ok=True)
        
        if use_submodule:
            # Create wrapper scripts that reference submodule
            self._create_wrapper_scripts(script_dir)
        else:
            # Copy scripts directly
            shutil.copytree('scripts', script_dir, dirs_exist_ok=True)
        
        # Initialize workflow state
        initial_state = {
            "current_phase": "initialization",
            "workflow_type": config["agents"]["workflow_type"],
            "active_agents": [],
            "completed_tasks": [],
            "quality_gates_passed": []
        }
        
        with open('.agentic-state/current-state.json', 'w') as f:
            json.dump(initial_state, f, indent=2)
    
    def _create_wrapper_scripts(self, script_dir: str):
        """Create wrapper scripts that reference framework submodule."""
        # CLI wrapper
        cli_wrapper = f'''#!/usr/bin/env python3
"""Project CLI wrapper for agentic SDLC framework."""
import sys
from pathlib import Path

# Add framework scripts to path
framework_scripts = Path(__file__).parent.parent / '.agentic-framework' / 'scripts'
sys.path.insert(0, str(framework_scripts))

# Import and run main CLI
from cli import main

if __name__ == '__main__':
    main()
'''
        
        with open(f'{script_dir}/cli.py', 'w') as f:
            f.write(cli_wrapper)
        
        # Make executable
        os.chmod(f'{script_dir}/cli.py', 0o755)
    
    def update_framework(self):
        """Update framework to latest version."""
        if not (Path.cwd() / '.agentic-framework').exists():
            raise click.ClickException("No framework submodule found. Are you in a project directory?")
        
        click.echo("🔄 Updating agentic SDLC framework...")
        
        os.chdir('.agentic-framework')
        subprocess.run(['git', 'pull', 'origin', 'main'], check=True)
        os.chdir('..')
        
        subprocess.run(['git', 'add', '.agentic-framework'], check=True)
        subprocess.run([
            'git', 'commit', '-m', 
            "Update agentic SDLC framework to latest version"
        ], check=True)
        
        click.echo("✅ Framework updated successfully!")
    
    def create_enhancement(self, enhancement_name: str, description: str):
        """Create enhancement template for contributing back to framework."""
        enhancement_dir = Path('agentic-enhancements') / enhancement_name
        enhancement_dir.mkdir(parents=True, exist_ok=True)
        
        enhancement_doc = f"""# Enhancement: {enhancement_name}

## Description
{description}

## Date Created
{datetime.now().strftime('%Y-%m-%d')}

## Project Context
{Path.cwd().name}

## Problem Solved
[Describe the issue this enhancement addresses]

## Solution
[Describe your solution approach]

## Files Modified
[List the framework files that need to be updated]

## Testing
[How was this enhancement tested?]

## Impact Assessment
- [ ] Affects all projects using the framework
- [ ] Backward compatible
- [ ] Requires documentation updates
- [ ] Needs new dependencies

## Merge Checklist
- [ ] Enhancement tested in project context  
- [ ] Framework files updated
- [ ] Documentation updated
- [ ] Example usage provided
- [ ] Backward compatibility maintained
"""
        
        with open(enhancement_dir / 'README.md', 'w') as f:
            f.write(enhancement_doc)
        
        click.echo(f"📝 Enhancement template created: agentic-enhancements/{enhancement_name}/")
        click.echo("👉 Document your changes and use 'merge-enhancement' when ready")
    
    def merge_enhancement(self, enhancement_name: str):
        """Merge enhancement back to framework trunk."""
        enhancement_dir = Path('agentic-enhancements') / enhancement_name
        
        if not enhancement_dir.exists():
            raise click.ClickException(f"Enhancement {enhancement_name} not found!")
        
        if not (Path.cwd() / '.agentic-framework').exists():
            click.echo("⚠️  No submodule found. Manual merge required to framework trunk.")
            return
        
        click.echo(f"🔀 Merging enhancement: {enhancement_name}")
        
        # Create branch in framework
        os.chdir('.agentic-framework')
        branch_name = f"enhancement/{enhancement_name}"
        subprocess.run(['git', 'checkout', '-b', branch_name], check=True)
        
        # Copy enhancement files (user needs to specify which files)
        click.echo("📋 Enhancement ready for manual file copying.")
        click.echo("📁 Copy your improved files to .agentic-framework/")
        click.echo("🔧 Then run: git add . && git commit -m 'Enhancement: ...'")
        click.echo("📤 Finally: git push origin {branch_name}")
        
        os.chdir('..')
    
    def _create_project_type_specific_files(self, project_name: str, project_type: str):
        """Create project-type-specific files and structure."""
        if project_type == "jupyter-notebook":
            self._create_jupyter_project_files(project_name)
        elif project_type == "desktop-app":
            self._create_desktop_app_files(project_name)
        elif project_type == "microservice":
            self._create_microservice_files(project_name)
        elif project_type == "data-science":
            self._create_data_science_files(project_name)
        elif project_type == "devops":
            self._create_devops_files(project_name)
        elif project_type == "testing":
            self._create_testing_framework_files(project_name)
        elif project_type == "custom":
            self._create_custom_project_files(project_name)
    
    def _create_jupyter_project_files(self, project_name: str):
        """Create Jupyter notebook project specific files."""
        # Create notebooks directory
        Path("notebooks").mkdir(exist_ok=True)
        Path("notebooks/exploratory").mkdir(exist_ok=True)
        Path("notebooks/analysis").mkdir(exist_ok=True)
        Path("notebooks/reporting").mkdir(exist_ok=True)
        
        # Create sample notebook
        sample_notebook = {
            "cells": [
                {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        f"# {project_name} Analysis\n",
                        "\n",
                        "## Project Overview\n",
                        f"Welcome to the data analysis for {project_name}.\n",
                        "\n",
                        "## Setup\n",
                        "Import required libraries and configure the environment."
                    ]
                },
                {
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": [
                        "# Import required libraries\n",
                        "import pandas as pd\n",
                        "import numpy as np\n",
                        "import matplotlib.pyplot as plt\n",
                        "import seaborn as sns\n",
                        "\n",
                        "# Configure plotting\n",
                        "plt.style.use('default')\n",
                        "sns.set_palette('husl')\n",
                        "\n",
                        "print('Environment setup complete!')"
                    ]
                }
            ],
            "metadata": {
                "kernelspec": {
                    "display_name": "Python 3",
                    "language": "python",
                    "name": "python3"
                },
                "language_info": {
                    "name": "python",
                    "version": "3.13.0"
                }
            },
            "nbformat": 4,
            "nbformat_minor": 4
        }
        
        with open('notebooks/01_initial_analysis.ipynb', 'w') as f:
            json.dump(sample_notebook, f, indent=2)
        
        # Create requirements specific to Jupyter
        jupyter_requirements = [
            "jupyter",
            "jupyterlab", 
            "pandas",
            "numpy",
            "matplotlib",
            "seaborn",
            "plotly",
            "ipywidgets"
        ]
        
        with open('requirements-jupyter.txt', 'w') as f:
            f.write('\n'.join(jupyter_requirements))
    
    def _create_desktop_app_files(self, project_name: str):
        """Create desktop application specific files."""
        # Create GUI structure
        Path("src/gui").mkdir(parents=True, exist_ok=True)
        Path("src/models").mkdir(exist_ok=True)
        Path("src/controllers").mkdir(exist_ok=True)
        Path("resources/icons").mkdir(parents=True, exist_ok=True)
        Path("resources/styles").mkdir(exist_ok=True)
        
        # Create main app file
        main_app = f'''#!/usr/bin/env python3
"""
{project_name} Desktop Application
Main application entry point.
"""

import sys
from pathlib import Path

# Add src to Python path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from gui.main_window import MainWindow

def main():
    """Main application entry point."""
    import tkinter as tk
    from tkinter import ttk
    
    root = tk.Tk()
    root.title("{project_name}")
    root.geometry("800x600")
    
    app = MainWindow(root)
    
    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("Application interrupted by user")
        sys.exit(0)

if __name__ == "__main__":
    main()
'''
        
        with open('main.py', 'w') as f:
            f.write(main_app)
        
        # Create main window
        main_window = '''"""
Main application window.
"""

import tkinter as tk
from tkinter import ttk, messagebox

class MainWindow:
    """Main application window."""
    
    def __init__(self, root):
        """Initialize the main window."""
        self.root = root
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the user interface."""
        # Create main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(0, weight=1)
        
        # Add welcome label
        welcome_label = ttk.Label(
            main_frame, 
            text="Welcome to your desktop application!",
            font=('Arial', 16, 'bold')
        )
        welcome_label.grid(row=0, column=0, pady=20)
        
        # Add sample button
        sample_button = ttk.Button(
            main_frame,
            text="Click Me",
            command=self.on_button_click
        )
        sample_button.grid(row=1, column=0, pady=10)
    
    def on_button_click(self):
        """Handle button click event."""
        messagebox.showinfo("Hello", "Button clicked! Start building your app.")
'''
        
        with open('src/gui/main_window.py', 'w') as f:
            f.write(main_window)
    
    def _create_microservice_files(self, project_name: str):
        """Create microservice architecture files."""
        # Create microservice structure
        Path("services").mkdir(exist_ok=True)
        Path("api/v1").mkdir(parents=True, exist_ok=True)
        Path("docker").mkdir(exist_ok=True)
        Path("k8s").mkdir(exist_ok=True)
        
        # Create Docker compose for development
        docker_compose = f'''version: '3.8'

services:
  {project_name}:
    build: .
    ports:
      - "8000:8000"
    environment:
      - ENV=development
    volumes:
      - ./src:/app/src
    depends_on:
      - redis
      - postgres
  
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
  
  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: {project_name}
      POSTGRES_USER: dev
      POSTGRES_PASSWORD: devpass
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
'''
        
        with open('docker-compose.yml', 'w') as f:
            f.write(docker_compose)
        
        # Create Dockerfile
        dockerfile = '''FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
'''
        
        with open('Dockerfile', 'w') as f:
            f.write(dockerfile)
    
    def _create_data_science_files(self, project_name: str):
        """Create data science project files."""
        # Create data science structure
        dirs = [
            "data/raw", "data/processed", "data/external",
            "notebooks/exploratory", "notebooks/analysis", "notebooks/modeling",
            "src/data", "src/features", "src/models", "src/visualization",
            "models", "reports/figures"
        ]
        
        for dir_path in dirs:
            Path(dir_path).mkdir(parents=True, exist_ok=True)
        
        # Create data science requirements
        ds_requirements = [
            "pandas", "numpy", "scipy", "scikit-learn",
            "matplotlib", "seaborn", "plotly",
            "jupyter", "jupyterlab",
            "polars", "pyarrow",
            "optuna", "mlflow"
        ]
        
        with open('requirements-ds.txt', 'w') as f:
            f.write('\n'.join(ds_requirements))
    
    def _create_devops_files(self, project_name: str):
        """Create DevOps/Infrastructure project files."""
        # Create DevOps structure
        dirs = [
            "terraform", "ansible", "docker", "k8s",
            "scripts/deployment", "scripts/monitoring",
            "configs/nginx", "configs/prometheus"
        ]
        
        for dir_path in dirs:
            Path(dir_path).mkdir(parents=True, exist_ok=True)
        
        # Create sample Terraform main.tf
        terraform_main = f'''# {project_name} Infrastructure

terraform {{
  required_version = ">= 1.0"
  
  required_providers {{
    aws = {{
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }}
  }}
}}

provider "aws" {{
  region = var.aws_region
}}

# Variables
variable "aws_region" {{
  description = "AWS region"
  type        = string
  default     = "us-west-2"
}}

variable "project_name" {{
  description = "Project name"
  type        = string
  default     = "{project_name}"
}}
'''
        
        with open('terraform/main.tf', 'w') as f:
            f.write(terraform_main)
    
    def _create_testing_framework_files(self, project_name: str):
        """Create testing framework project files."""
        # Create testing structure
        dirs = [
            "tests/unit", "tests/integration", "tests/e2e",
            "tests/fixtures", "tests/utils",
            "performance", "load_tests"
        ]
        
        for dir_path in dirs:
            Path(dir_path).mkdir(parents=True, exist_ok=True)
        
        # Create pytest configuration
        pytest_ini = '''[tool:pytest]
testpaths = tests
python_files = test_*.py *_test.py
python_classes = Test*
python_functions = test_*
addopts = 
    --strict-markers
    --strict-config
    --verbose
    --cov=src
    --cov-report=term-missing
    --cov-report=html
    --cov-fail-under=80

markers =
    unit: Unit tests
    integration: Integration tests
    e2e: End-to-end tests
    slow: Slow running tests
'''
        
        with open('pytest.ini', 'w') as f:
            f.write(pytest_ini)
    
    def _create_custom_project_files(self, project_name: str):
        """Create custom project files with basic structure."""
        # Create basic custom structure
        Path("custom").mkdir(exist_ok=True)
        
        # Create custom project README
        custom_readme = f'''# {project_name} - Custom Project

This is a custom project created with the agentic SDLC framework.

## Project Structure

You have the basic agentic framework structure. Customize as needed:

- `src/` - Your main source code
- `tests/` - Your test files  
- `docs/` - Documentation
- `config/` - Configuration files
- `custom/` - Custom project-specific files

## Customization Guide

1. Edit `project-brief.md` to define your specific requirements
2. Modify the directory structure as needed for your project type
3. Update `config/agentic-config.json` with your specific agents and workflow
4. Add your custom dependencies to requirements files
5. Use the agentic workflow: `python agentic-scripts/cli.py start`

## Framework Features Available

- 21 specialized AI agents for different tasks
- Quality gates and validation
- Workflow state management  
- Human-in-the-loop protocols
- Enhancement contribution system

Refer to `framework-management-guide.md` for detailed usage instructions.
'''
        
        with open('custom/README.md', 'w') as f:
            f.write(custom_readme)

@click.group()
def cli():
    """Agentic SDLC Framework Manager"""
    pass

@cli.command()
@click.argument('project_name')
@click.option('--type', 'project_type', default='web-app', 
              type=click.Choice(['web-app', 'api', 'dashboard', 'ml-model', 'data-pipeline', 'cli', 
                                'jupyter-notebook', 'desktop-app', 'microservice', 'data-science', 
                                'devops', 'testing', 'custom']),
              help='Type of project to create')
@click.option('--copy/--submodule', default=False, 
              help='Copy framework vs use as submodule (default: submodule)')
def init(project_name, project_type, copy):
    """Initialize a new project with agentic SDLC framework."""
    fm = FrameworkManager()
    fm.init_project(project_name, project_type, use_submodule=not copy)

@cli.command()
def update():
    """Update framework to latest version (submodule projects only)."""
    fm = FrameworkManager()
    fm.update_framework()

@cli.command()
@click.argument('name')
@click.argument('description')
def enhance(name, description):
    """Create enhancement template for framework contribution."""
    fm = FrameworkManager()
    fm.create_enhancement(name, description)

@cli.command()
@click.argument('enhancement_name')
def merge(enhancement_name):
    """Merge enhancement back to framework trunk."""
    fm = FrameworkManager()
    fm.merge_enhancement(enhancement_name)

@cli.command()
def status():
    """Show current project and framework status."""
    # Load project config
    config_file = Path('config/agentic-config.json')
    if config_file.exists():
        with open(config_file) as f:
            config = json.load(f)
        
        click.echo("📊 Project Status")
        click.echo(f"   Name: {config['project_name']}")
        click.echo(f"   Type: {config['project_type']}")
        click.echo(f"   Framework: {'Submodule' if config['use_submodule'] else 'Copy'}")
        click.echo(f"   Created: {config['created_date'][:10]}")
    
    # Load workflow state
    state_file = Path('.agentic-state/current-state.json')
    if state_file.exists():
        with open(state_file) as f:
            state = json.load(f)
        
        click.echo("🔄 Workflow Status")
        click.echo(f"   Phase: {state['current_phase']}")
        click.echo(f"   Type: {state['workflow_type']}")
        click.echo(f"   Active Agents: {len(state['active_agents'])}")
        click.echo(f"   Tasks Done: {len(state['completed_tasks'])}")
    
    # Check for enhancements
    enhancement_dir = Path('agentic-enhancements')
    if enhancement_dir.exists():
        enhancements = [d.name for d in enhancement_dir.iterdir() if d.is_dir()]
        if enhancements:
            click.echo("🔧 Pending Enhancements")
            for enh in enhancements:
                click.echo(f"   - {enh}")

if __name__ == '__main__':
    cli()