#!/usr/bin/env python3
"""
Master Agent - Interactive Guide for Agentic Framework
Provides guided experience for users after installation
"""

import sys
from .core import FrameworkManager
from .project import ProjectInitializer


class MasterAgent:
    """Master Agent provides interactive guidance for framework usage."""
    
    def __init__(self):
        self.framework_manager = FrameworkManager()
        self.project_initializer = ProjectInitializer()
    
    def start_interactive_guide(self):
        """Start the Master Agent interactive guide."""
        self.display_welcome()
        
        while True:
            try:
                choice = self.display_main_menu()
                if choice == "1":
                    self.quick_start_guide()
                elif choice == "2":
                    self.framework_overview()
                elif choice == "3":
                    self.create_new_project()
                elif choice == "4":
                    self.view_templates()
                elif choice == "5":
                    self.advanced_features()
                elif choice == "6":
                    self.help_and_resources()
                elif choice == "0":
                    self.display_goodbye()
                    break
                else:
                    print("❌ Invalid choice. Please try again.")
                
                if choice != "0":
                    try:
                        input("\n✨ Press Enter to continue...")
                    except EOFError:
                        print("\n\n👋 Master Agent session ended. Goodbye!")
                        break
                    
            except KeyboardInterrupt:
                print("\n\n👋 Master Agent session ended. Goodbye!")
                break
    
    def display_welcome(self):
        """Display welcome message and Master Agent introduction."""
        print("\n🤖 " + "=" * 60)
        print("   AGENTIC FRAMEWORK - MASTER AGENT ACTIVATED")
        print("=" * 62)
        print("\n🎯 Welcome to the Agentic SDLC Framework!")
        print("   I'm your Master Agent, here to guide you through")
        print("   the framework and help you get started quickly.")
        print("\n📋 What I can help you with:")
        print("   • Framework overview and capabilities")
        print("   • Creating your first project")
        print("   • Understanding templates and agents")
        print("   • Advanced features and enhancements")
        print("   • Resources and documentation")
    
    def display_main_menu(self):
        """Display main menu and get user choice."""
        print("\n" + "="*50)
        print("🤖 MASTER AGENT - Main Menu")
        print("="*50)
        print("\n1️⃣  Quick Start Guide - Get up and running fast")
        print("2️⃣  Framework Overview - Learn about the framework")
        print("3️⃣  Create New Project - Start your first project")
        print("4️⃣  View Templates - Explore available templates")
        print("5️⃣  Advanced Features - Domain experts, validation")
        print("6️⃣  Help & Resources - Documentation and support")
        print("0️⃣  Exit - End Master Agent session")
        print("\n" + "-"*50)
        
        try:
            return input("🎯 Select option (0-6): ").strip()
        except EOFError:
            print("\n\n👋 Master Agent session ended. Goodbye!")
            sys.exit(0)
    
    def quick_start_guide(self):
        """Provide quick start instructions."""
        print("\n🚀 " + "="*50)
        print("   QUICK START GUIDE")
        print("="*52)
        
        print("\n📋 3-Step Quick Start:")
        print("   1️⃣  Create a new project")
        print("   2️⃣  Navigate to project directory") 
        print("   3️⃣  Start the agentic workflow")
        
        print("\n💡 Step-by-step instructions:")
        print("   → Create project: agentic-framework init my-project")
        print("   → Navigate: cd my-project")
        print("   → Start workflow: python agentic-scripts/cli.py start")
        
        print("\n🎯 What you'll get:")
        print("   ✅ Complete project structure")
        print("   ✅ AI agent specifications")
        print("   ✅ Development standards")
        print("   ✅ Framework templates")
        print("   ✅ Ready-to-use CLI tools")
        
        print("\n📦 Supported Project Types:")
        print("   • Web apps, APIs, dashboards, ML models")
        print("   • Data pipelines, CLI tools, microservices")
        print("   • Desktop apps, DevOps, testing frameworks")
        print("   • Custom types and more!")
        
        create_now = input("\n🤔 Would you like to create a project now? (y/n): ").lower().strip()
        if create_now in ['y', 'yes']:
            self.create_new_project()
    
    def framework_overview(self):
        """Provide framework overview."""
        print("\n📚 " + "="*50)
        print("   FRAMEWORK OVERVIEW")
        print("="*52)
        
        print("\n🎯 Agentic SDLC Framework Features:")
        print("   • Human-in-the-Loop (HITL) development")
        print("   • AI agent orchestration")
        print("   • Systematic project delivery")
        print("   • Production-ready templates")
        
        print("\n🤖 Core Components:")
        print("   📁 sub-agents/          - AI agent specifications")
        print("   📁 development-standards/ - Coding standards & templates")
        print("   📁 templates/           - Framework templates")
        print("   📁 agentic-scripts/     - CLI tools and automation")
        
        print("\n✨ Key Benefits:")
        print("   ✅ Systematic approach to AI-assisted development")
        print("   ✅ Consistent quality across projects")
        print("   ✅ Built-in best practices and standards")
        print("   ✅ Scalable agent orchestration")
        print("   ✅ Professional project structure")
    
    def create_new_project(self):
        """Guide user through project creation."""
        print("\n🏗️  " + "="*50)
        print("   CREATE NEW PROJECT")
        print("="*52)
        
        print("\n💡 I can help you create a project in two ways:")
        print("   1️⃣  Quick creation (I'll ask a few questions)")
        print("   2️⃣  Interactive wizard (detailed customization)")
        
        choice = input("\n🤔 Which would you prefer? (1/2): ").strip()
        
        if choice == "1":
            # Quick creation
            project_name = input("\n📝 Enter project name: ").strip()
            if not project_name:
                print("❌ Project name is required.")
                return
                
            print("\n🎯 Available project types:")
            print("   1. web-app (default) - Web Application (Django/Flask/FastAPI)")
            print("   2. api - REST API Service")
            print("   3. dashboard - Data Dashboard (Streamlit)")
            print("   4. microservice - Microservice Architecture")
            print("   5. data-science - Data Science Research")
            print("   6. ml-model - ML Model Serving")
            print("   7. data-pipeline - Data Pipeline/ETL")
            print("   8. jupyter-notebook - Jupyter Notebook Analysis")
            print("   9. cli - CLI Tool")
            print("   10. desktop-app - Desktop Application (PyQt/Tkinter)")
            print("   11. testing - Testing Framework")
            print("   12. devops - DevOps/Infrastructure")
            print("   13. custom - Custom Project Type")
            print("   14. other - Other (specify your own)")
            
            project_type = input("\n📋 Project type (1-14, press Enter for web-app): ").strip().lower()
            
            # Map numeric choices to project types
            type_map = {
                "1": "web-app", "2": "api", "3": "dashboard", "4": "microservice",
                "5": "data-science", "6": "ml-model", "7": "data-pipeline", 
                "8": "jupyter-notebook", "9": "cli", "10": "desktop-app",
                "11": "testing", "12": "devops", "13": "custom", "14": "other"
            }
            
            if not project_type:
                project_type = "web-app"
            elif project_type in type_map:
                project_type = type_map[project_type]
            elif project_type == "other":
                custom_type = input("📝 Enter your custom project type: ").strip()
                project_type = custom_type if custom_type else "custom"
            
            print(f"\n🚀 Creating project '{project_name}' of type '{project_type}'...")
            try:
                project_dir = self.framework_manager.init_project(project_name, project_type)
                print("\n✅ Project created successfully!")
                print(f"📂 Location: {project_dir}")
                
                print("\n🎯 Next steps:")
                print(f"   cd {project_name}")
                print("   python agentic-scripts/cli.py start")
                
            except Exception as e:
                print(f"❌ Error creating project: {e}")
                
        elif choice == "2":
            # Interactive wizard
            print("\n🧙 Starting interactive project wizard...")
            self.project_initializer.start_wizard()
        else:
            print("❌ Invalid choice. Returning to main menu.")
    
    def view_templates(self):
        """Show available templates and their purposes."""
        print("\n📋 " + "="*50)
        print("   FRAMEWORK TEMPLATES")
        print("="*52)
        
        # Check if templates exist
        templates_path = self.framework_manager.templates_path
        if templates_path and templates_path.exists():
            print("\n📄 Available Templates:")
            for template_file in templates_path.glob("*.md"):
                template_name = template_file.name
                print(f"   📋 {template_name}")
                
                # Add descriptions for key templates
                if "master-agent" in template_name:
                    print("      → Master orchestration and workflow coordination")
                elif "project-brief" in template_name:
                    print("      → Project requirements and planning template")
                elif "workflow-state" in template_name:
                    print("      → State management for development workflows")
                elif "framework-management" in template_name:
                    print("      → Framework setup and management guide")
                elif "quality-gates" in template_name:
                    print("      → Quality assurance and validation processes")
        else:
            print("\n📄 Standard Templates Available:")
            print("   📋 master-agent.md - Master orchestration guide")
            print("   📋 project-brief-template.md - Project planning")
            print("   📋 workflow-state-management.md - Workflow states")
            print("   📋 framework-management-guide.md - Setup guide")
            print("   📋 quality-gates.md - Quality processes")
        
        print("\n📁 Template Categories:")
        print("   🤖 Agent Specifications - Define AI agent behaviors")
        print("   📚 Development Standards - Coding and quality standards")
        print("   🔧 Process Templates - Workflow and project management")
        print("   📖 Documentation - Guides and references")
        
        print("\n💡 Templates are automatically included in new projects")
        print("   and can be customized for your specific needs.")
        print("\n✨ Special Note: master-agent.md is placed at project root")
        print("   for easy access when adding to AI context (Claude, etc.)")
    
    def advanced_features(self):
        """Show advanced framework features and enhancements."""
        print("\n🚀 " + "="*50)
        print("   ADVANCED FEATURES")
        print("="*52)
        
        print("\n✨ Framework Enhancements:")
        
        print("\n🔬 Domain Expert Integration")
        print("   → Integrate specialized domain expertise")
        print("   → Perfect for legal, medical, financial projects")
        print("   → Prevents critical domain-specific errors")
        
        print("\n🔍 Dual Validation Framework")
        print("   → Separate process validation (AI) from domain validation (expert)")
        print("   → Comprehensive validation covering technical and domain accuracy")
        print("   → Prevents AI testing gaps in specialized knowledge")
        
        print("\n🎯 Enhanced Business Analyst Agent")
        print("   → Autonomous operation capabilities")
        print("   → Project continuity during team transitions")
        print("   → Automated knowledge transfer and documentation")
        
        print("\n📂 Enhancement Location:")
        print("   All enhancements are in agentic-enhancements/ directory")
        print("   Ready-to-use templates for any specialized domain")
        
        print("\n🎓 When to use Advanced Features:")
        print("   ✅ Projects requiring specialized domain knowledge")
        print("   ✅ High-stakes projects with accuracy requirements")
        print("   ✅ Teams needing autonomous operation capabilities")
        print("   ✅ Organizations building specialized expertise")
    
    def help_and_resources(self):
        """Provide help resources and documentation links."""
        print("\n📚 " + "="*50)
        print("   HELP & RESOURCES")
        print("="*52)
        
        print("\n🌐 Online Resources:")
        print("   📖 GitHub Repository:")
        print("      https://github.com/LinoGoncalves/agentic-framework")
        print("   🐛 Issue Tracker:")
        print("      https://github.com/LinoGoncalves/agentic-framework/issues")
        
        print("\n🔧 CLI Commands Reference:")
        print("   📋 agentic-framework init <name>    - Create new project")
        print("   🧙 agentic-new                      - Interactive wizard")
        print("   🔍 agentic-framework doctor          - Diagnose installation")
        print("   🤖 agentic-framework master-agent    - Start this guide")
        
        print("\n🆘 Alternative Commands (if PATH issues):")
        print("   📋 python -m agentic_framework init <name>")
        print("   🧙 python -m agentic_framework new")
        print("   🔍 python -m agentic_framework doctor")
        print("   🤖 python -m agentic_framework master-agent")
        
        print("\n📋 Quick Reference:")
        print("   • Virtual environment recommended for installation")
        print("   • Use 'doctor' command to diagnose PATH issues")
        print("   • Templates are customizable for your needs")
        print("   • Advanced features available for specialized projects")
        
        print("\n💡 Need help? Check the documentation or open an issue!")
    
    def display_goodbye(self):
        """Display goodbye message."""
        print("\n👋 " + "="*50)
        print("   MASTER AGENT SESSION COMPLETE")
        print("="*52)
        print("\n🎯 Thank you for using the Agentic Framework!")
        print("   Remember: I'm always here to help.")
        print("   Just run: agentic-framework master-agent")
        print("\n🚀 Happy coding with your AI agents!")
        print("   May your projects be bug-free and your")
        print("   workflows be smooth! 🤖✨")


if __name__ == "__main__":
    master_agent = MasterAgent()
    master_agent.start_interactive_guide()