# Agentic Framework - GitHub Copilot Instructions

## 🚨 CRITICAL: Human-in-the-Loop (HITL) Protocol

**MANDATORY:** This framework operates under strict Human-in-the-Loop protocols. AI assistants must:
- Seek explicit human approval for all critical decisions
- Present plans and proposals for human review before implementation
- Coordinate with humans, never replace human judgment
- Follow the master-agent.md protocols at the root level

## Project Coding Guidelines

### Code Style
- Use semantic HTML5 elements (header, main, section, article, etc.)
- Prefer modern JavaScript (ES6+) features like const/let, arrow functions, template literals
- Follow Python PEP 8 standards for Python code
- Use TypeScript for type safety when applicable

### Naming Conventions  
- Use PascalCase for component names, interfaces, and type aliases
- Use camelCase for variables, functions, and methods
- Use kebab-case for file names and directories
- Use UPPER_CASE for constants and environment variables
- Prefix private class members with underscore (_)

### Code Quality
- Write meaningful variable and function names that clearly describe purpose
- Include helpful comments for complex logic
- Add comprehensive error handling for user inputs and API calls
- Follow the testing strategies defined in development_standards/testing_strategy.md
- Implement security measures per development_standards/secure_coding_checklist.md

### Architecture & Design
- Follow the architectural principles in development_standards/architectural-principles.md
- Use the API design patterns specified in development_standards/api_design_patterns.md
- Implement proper database schema standards per development_standards/database_schema_standards.md
- Follow cloud resource tagging policies in development_standards/cloud_resource_tagging_policy.md

### Documentation
- Follow documentation style guide in development_standards/documentation_styleguide.md
- Create user guides using development_standards/user_guide_template.md
- Document APIs using development_standards/api_reference_template.md
- Include proper README files for all projects

### Development Process
- Follow agile ceremonies guide in development_standards/agile_ceremonies_guide.md
- Use user story template from development_standards/user_story_template.md
- Implement requirements per development_standards/requirements_definition_standard.md
- Follow MLOps pipeline standards for ML projects

## Framework-Specific Guidelines

### Project Structure
- All projects must include the 21 specialized sub-agents from sub_agents/ directory
- Development standards from .github/development_standards/ must be copied to projects
- Master agent coordination through master-agent.md protocols
- Quality gates enforcement at all project phases

### Human-AI Collaboration
- AI agents provide initial drafts and suggestions
- Human stakeholders review, approve, and refine all work
- Explicit handoffs between AI and human team members
- No autonomous implementation without human approval

### Quality Assurance
- Follow testing strategy and secure coding checklist
- Implement proper error handling and validation
- Ensure accessibility and user experience standards
- Maintain code review processes with human oversight

## File References

All development standards are located in `.github/development_standards/`:
- Architectural principles, API patterns, security policies
- Coding style guides, testing strategies, documentation templates  
- Cloud standards, database schemas, MLOps pipelines
- Agile processes, user story templates, requirement standards

Refer to these standards for detailed guidelines on specific aspects of development.