#!/usr/bin/env python3
"""
Project Initializer
Handles interactive project creation wizard
"""

import sys
from .core import FrameworkManager


class ProjectInitializer:
    """Interactive project creation wizard."""
    
    def __init__(self):
        self.framework_manager = FrameworkManager()
        
    def start_wizard(self):
        """Run the interactive project creation wizard."""
        print("🚀 Agentic SDLC Framework - New Project Wizard")
        print("=" * 50)
        
        # Get project details
        project_name = input("Project Name: ").strip()
        if not project_name:
            print("❌ Project name is required!")
            sys.exit(1)
        
        print("\nProject Types:")
        project_types_menu = {
            "1": ("web-app", "Web Application (Django/Flask/FastAPI)"),
            "2": ("api", "REST API Service"),
            "3": ("dashboard", "Data Dashboard (Streamlit)"),
            "4": ("microservice", "Microservice Architecture"),
            "5": ("data-science", "Data Science Research"),
            "6": ("ml-model", "ML Model Serving"),
            "7": ("data-pipeline", "Data Pipeline/ETL"),
            "8": ("jupyter-notebook", "Jupyter Notebook Analysis"),
            "9": ("cli", "CLI Tool"),
            "10": ("desktop-app", "Desktop Application (PyQt/Tkinter)"),
            "11": ("testing", "Testing Framework"),
            "12": ("devops", "DevOps/Infrastructure"),
            "13": ("custom", "Custom Project Type"),
            "14": ("other", "Specify your own completely custom type")
        }
        
        for key, (_, description) in project_types_menu.items():
            print(f"{key}. {description}")
        
        choice = input("\nSelect project type (1-14): ").strip()
        
        if choice not in project_types_menu:
            print("❌ Invalid choice!")
            sys.exit(1)
            
        project_type, _ = project_types_menu[choice]
        
        # Get output directory (optional)
        output_dir = input("\nOutput directory (press Enter for current directory): ").strip()
        output_dir = output_dir if output_dir else None
        
        # Create the project
        try:
            project_path = self.framework_manager.init_project(
                project_name=project_name,
                project_type=project_type,
                output_dir=output_dir
            )
            return project_path
        except Exception as e:
            print(f"❌ Error creating project: {e}")
            sys.exit(1)


def main():
    """Main entry point for project initialization."""
    initializer = ProjectInitializer()
    initializer.start_wizard()


if __name__ == "__main__":
    main()