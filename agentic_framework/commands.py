#!/usr/bin/env python3
"""
Individual command entry points for better CLI experience
"""

import sys
from .cli import create_parser


def main_init():
    """Entry point for agentic-init command."""
    sys.argv = ['agentic-framework', 'init'] + sys.argv[1:]
    parser = create_parser()
    args = parser.parse_args()
    
    from .core import FrameworkManager
    framework_manager = FrameworkManager()
    framework_manager.init_project(
        project_name=args.name,
        project_type=args.type,
        output_dir=args.output
    )


def main_doctor():
    """Entry point for agentic-doctor command."""
    from .cli import check_cli_installation
    print("🔍 Agentic Framework Installation Diagnostics")
    print("=" * 50)
    check_cli_installation()
    print("\n📚 For more help, visit: https://github.com/LinoGoncalves/agentic-framework#installation")


def main_master_agent():
    """Entry point for agentic-master-agent command."""
    from .master_agent import MasterAgent
    master_agent = MasterAgent()
    master_agent.start_interactive_guide()


if __name__ == "__main__":
    # This allows the module to be run directly for testing
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "init":
            main_init()
        elif command == "doctor":
            main_doctor()
        elif command == "master-agent":
            main_master_agent()
        else:
            print(f"Unknown command: {command}")
    else:
        print("Usage: python -m agentic_framework.commands <command>")