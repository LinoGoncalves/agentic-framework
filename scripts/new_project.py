#!/usr/bin/env python3
"""
Simple Project Starter for Agentic SDLC Framework
Quick way to start new projects with the framework.
"""

import subprocess
import sys
from pathlib import Path

def start_new_project():
    """Interactive project creation wizard."""
    print("🚀 Agentic SDLC Framework - New Project Wizard")
    print("=" * 50)
    
    # Get project details
    project_name = input("Project Name: ").strip()
    if not project_name:
        print("❌ Project name is required!")
        sys.exit(1)
    
    print("\nProject Types:")
    print("1. Web Application (Django/Flask/FastAPI)")
    print("2. REST API Service") 
    print("3. Data Dashboard (Streamlit)")
    print("4. ML Model Serving")
    print("5. Data Pipeline/ETL")
    print("6. CLI Tool")
    
    project_types = {
        "1": "web-app",
        "2": "api", 
        "3": "dashboard",
        "4": "ml-model",
        "5": "data-pipeline",
        "6": "cli"
    }
    
    choice = input("\nSelect project type (1-6): ").strip()
    project_type = project_types.get(choice, "web-app")
    
    print(f"\nFramework Integration:")
    print("1. Submodule (Recommended - easy updates)")
    print("2. Copy (Self-contained - full control)")
    
    integration_choice = input("Select integration method (1-2): ").strip()
    use_copy = integration_choice == "2"
    
    print(f"\n📋 Creating project: {project_name}")
    print(f"   Type: {project_type}")
    print(f"   Integration: {'Copy' if use_copy else 'Submodule'}")
    print(f"   Location: {Path.cwd() / project_name}")
    
    confirm = input("\nProceed? (y/N): ").strip().lower()
    if confirm != 'y':
        print("❌ Project creation cancelled.")
        sys.exit(0)
    
    # Run framework manager
    framework_path = Path(__file__).parent / "framework_manager.py"
    cmd = [
        sys.executable, 
        str(framework_path), 
        "init", 
        project_name,
        "--type", project_type
    ]
    
    if use_copy:
        cmd.append("--copy")
    
    try:
        print(f"\n🔧 Running: {' '.join(cmd)}")
        subprocess.run(cmd, check=True)
        
        print(f"\n✅ Project {project_name} created successfully!")
        print(f"\n🎯 Next Steps:")
        print(f"   1. cd {project_name}")
        print(f"   2. Edit project-brief.md")
        print(f"   3. python agentic-scripts/cli.py start")
        print(f"\n📖 See framework-management-guide.md for detailed usage")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error creating project: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("❌ Framework manager not found. Make sure you're in the agentic SDLC directory.")
        sys.exit(1)

if __name__ == "__main__":
    start_new_project()