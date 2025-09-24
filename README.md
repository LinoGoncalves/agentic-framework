
# Agentic SDLC Framework

A production-ready Human-in-the-Loop (HITL) software development lifecycle framework that orchestrates AI agents with human oversight for systematic project delivery.

## 🚀 Quick Start

### Start Your First Project

```bash
# Interactive wizard (recommended)
python scripts/new_project.py

# Or direct command
python scripts/framework_manager.py init my-project --type web-app
```

### Navigate to Your Project

```bash
cd my-project
notepad project-brief.md  # Customize requirements
python agentic-scripts/cli.py start  # Begin workflow
```

## 🎯 What This Framework Does

Transform complex software projects into manageable, AI-assisted workflows:

- **🤖 AI Agent Orchestra**: 21 specialized agents (Business Analyst, Developer, QA, DevOps, etc.)
- **🧑‍💼 Human-in-the-Loop**: Clear handoff points where humans review and approve
- **📋 Structured Process**: From requirements to deployment with quality gates
- **🔄 Continuous Learning**: Framework improves based on project experience
- **📊 Progress Tracking**: Real-time visibility into project status

## 🏗️ Framework Components

### Core Orchestration
- **Master Agent**: Central workflow coordinator and task dispatcher
- **21 Sub-Agents**: Domain specialists with HITL protocols
5. The Master Agent assembles the results from all the necessary sub-agents to deliver the final, complete response to you.

_Image of a flowchart showing a user prompt going to a Master Agent, which then routes tasks to three different Sub-Agents, and then collects the results to give a final answer._

---

## Getting Started

#### Prerequisites

* Python 3.9+
* An API key for the relevant AI service (e.g., OpenAI, Google AI)

#### Installation

1. **Clone the repository:**

   ```bash
   git clone [https://github.com/your-repo/agent-orchestration-system.git](https://github.com/your-repo/agent-orchestration-system.git)
   cd agent-orchestration-system
   ```
2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```
3. **Configure your API key:**
   Create a `.env` file in the root directory and add your API key:

   ```
   API_KEY="your_api_key_here"
   ```

---

## How to Use the System

You will only ever interact directly with the **Master Agent**. You do not need to call the sub-agents yourself.

To run the master agent, use the `main.py` script from your terminal. Pass your high-level goal as a string argument using the `--goal` flag.

#### Example Usage

Here are a few examples of how you might use it:

* **To get a market analysis:**

  ```bash
  python main.py --goal "Analyze the current market trends for electric vehicles in South Africa and provide a summary with key statistics."
  ```

  *(In the background, the Master Agent might first call the `web_search_agent` to find recent articles and then the `data_analysis_agent` to summarize the findings.)*
* **To generate creative content:**

  ```bash
  python main.py --goal "Write a short, engaging blog post about the benefits of remote work and suggest three catchy titles."
  ```

  *(The Master Agent will likely route this to the `creative_writing_agent`.)*
* **To write code:**

  ```bash
  python main.py --goal "Create a Python function that takes a list of numbers and returns only the even ones."
  ```

  *(This task would be assigned to the `code_generation_agent`.)*

---

## Adding a New Sub-Agent

The power of this system comes from its modularity. You can easily add a new specialist (sub-agent) to the team.

1. **Create the Agent File:** In the `sub_agents/` directory, create a new Python file (e.g., `seo_agent.py`).
2. **Define the Agent's Role:** Inside the file, create a function or class for your agent. Most importantly, write a very clear **docstring** or description that explains the agent's expertise. The Master Agent uses this description to decide when to assign tasks to it.
   ```python
   # sub_agents/seo_agent.py

   def run_seo_analysis(url: str) -> dict:
       """
       Expert at performing SEO analysis on a given URL.
       Takes a URL as input and returns a dictionary containing
       keyword density, mobile-friendliness score, and page load speed.
       Do not use for anything other than SEO analysis.
       """
       # Your agent's logic here...
       pass
   ```
3. **Register the Agent:** In `master_agent/main.py`, import your new agent and add it to the list of available sub-agents. The Master Agent will now be aware of its new "musician."

---

## Troubleshooting

* **"No suitable agent found" error:** This means the Master Agent could not match your goal to any of the sub-agents' descriptions. Try rephrasing your goal to be more specific or check if the right sub-agent for the task exists.
* **API Errors:** Ensure your API key in the `.env` file is correct and has sufficient credits.

Enjoy using the Agent Orchestration System!
