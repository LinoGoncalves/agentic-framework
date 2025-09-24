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
            self._setup_submodule_project(project_name, project_type)
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
        # Add framework as submodule
        framework_url = f"file://{self.framework_path.absolute()}"
        subprocess.run([
            'git', 'submodule', 'add', 
            framework_url, '.agentic-framework'
        ], check=True)
        
        # Create project structure
        self._create_project_structure()
        
        # Copy and customize templates
        self._setup_project_files(project_name, project_type, use_submodule=True)
        
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

@click.group()
def cli():
    """Agentic SDLC Framework Manager"""
    pass

@cli.command()
@click.argument('project_name')
@click.option('--type', 'project_type', default='web-app', 
              type=click.Choice(['web-app', 'api', 'dashboard', 'ml-model', 'data-pipeline', 'cli']),
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