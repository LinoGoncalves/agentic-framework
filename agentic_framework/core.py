#!/usr/bin/env python3
"""
Core Framework Manager
Refactored from scripts/framework_manager.py for package distribution
"""

import shutil
from pathlib import Path
from typing import Optional
from datetime import datetime


class FrameworkManager:
    """Manages agentic SDLC framework across projects."""
    
    def __init__(self, framework_path: Optional[str] = None):
        """Initialize framework manager.
        
        Args:
            framework_path: Path to framework installation (auto-detected if None)
        """
        if framework_path:
            self.framework_path = Path(framework_path)
        else:
            # Auto-detect package installation path
            import agentic_framework
            self.framework_path = Path(agentic_framework.__file__).parent
            
        self.templates_path = self.framework_path / "templates"
        self.sub_agents_path = self.framework_path / "sub_agents"
        self.development_standards_path = self.framework_path / "development_standards"
    
    def init_project(self, project_name: str, project_type: str = "web-app", 
                    output_dir: Optional[str] = None) -> Path:
        """Initialize a new project with the framework.
        
        Args:
            project_name: Name of the project
            project_type: Type of project (web-app, api, etc.)
            output_dir: Directory to create project in (current dir if None)
            
        Returns:
            Path to created project directory
        """
        if output_dir:
            project_dir = Path(output_dir) / project_name
        else:
            project_dir = Path.cwd() / project_name
            
        print(f"🚀 Creating project '{project_name}' of type '{project_type}'...")
        
        # Create project structure
        project_dir.mkdir(exist_ok=True)
        
        # Copy framework files
        self._copy_framework_files(project_dir)
        
        # Create project-specific files
        self._create_project_files(project_dir, project_name, project_type)
        
        print(f"✅ Project '{project_name}' created successfully!")
        print(f"📂 Location: {project_dir}")
        print("\n🎯 Next steps:")
        print(f"   cd {project_name}")
        print("   python agentic-scripts/cli.py start")
        
        return project_dir
    
    def _copy_framework_files(self, project_dir: Path):
        """Copy framework files to project directory."""
        # Create agentic-scripts directory
        scripts_dir = project_dir / "agentic-scripts"
        scripts_dir.mkdir(exist_ok=True)
        
        # Copy sub-agents
        if self.sub_agents_path.exists():
            shutil.copytree(self.sub_agents_path, project_dir / "sub-agents", dirs_exist_ok=True)
        
        # Copy development standards
        if self.development_standards_path.exists():
            shutil.copytree(self.development_standards_path, project_dir / "development-standards", dirs_exist_ok=True)
            
        # Copy CLI script
        cli_source = self.framework_path / "scripts" / "cli.py"
        if cli_source.exists():
            shutil.copy2(cli_source, scripts_dir / "cli.py")
    
    def _create_project_files(self, project_dir: Path, project_name: str, project_type: str):
        """Create project-specific configuration files."""
        
        # Create project brief template
        project_brief = f"""# {project_name} - Project Brief

## Project Overview
**Type**: {project_type}
**Created**: {datetime.now().strftime('%Y-%m-%d')}

## Requirements
<!-- Define your project requirements here -->

## Architecture
<!-- Describe the high-level architecture -->

## Technology Stack
<!-- List the technologies to be used -->

## Success Criteria
<!-- Define what success looks like -->

## Timeline
<!-- Estimated timeline and milestones -->
"""
        (project_dir / "project-brief.md").write_text(project_brief)
        
        # Create basic README
        readme_content = f"""# {project_name}

A project created with the Agentic SDLC Framework.

## Getting Started

1. Review and customize the project requirements in `project-brief.md`
2. Start the agentic workflow:
   ```bash
   python agentic-scripts/cli.py start
   ```

## Framework Components

- `sub-agents/`: AI agent specifications
- `development-standards/`: Coding standards and templates  
- `agentic-scripts/`: Framework CLI tools

## Next Steps

Run the following to begin your project workflow:
```bash
python agentic-scripts/cli.py start
```
"""
        (project_dir / "README.md").write_text(readme_content)


def get_version():
    """Get framework version."""
    from agentic_framework import __version__
    return __version__