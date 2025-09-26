# Project Types - Complete Guide

The Agentic Framework supports **15+ comprehensive project types** to cover virtually any software development scenario. Each type includes specialized templates, standards, and AI agent configurations.

## 🌐 Web & API Applications

### web-app (Default)
**Full-stack web applications using modern frameworks**
- **Technologies:** Django, Flask, FastAPI, React, Vue.js
- **Includes:** Frontend/backend architecture, database integration, authentication
- **Best for:** Business applications, SaaS products, e-commerce sites
- **Agent Focus:** Full-stack developer, UI/UX designer, database architect

### api
**RESTful API services and microservice backends**
- **Technologies:** FastAPI, Flask, Express.js, Spring Boot
- **Includes:** API design patterns, documentation templates, versioning
- **Best for:** Backend services, microservices, mobile app backends
- **Agent Focus:** API developer, system architect, DevOps engineer

### dashboard
**Data visualization and analytics dashboards**
- **Technologies:** Streamlit, Dash, Grafana, React dashboards
- **Includes:** Data connection patterns, visualization templates
- **Best for:** Business intelligence, monitoring dashboards, analytics
- **Agent Focus:** Data analyst, visualization specialist, frontend developer

### microservice
**Distributed microservice architectures**
- **Technologies:** Docker, Kubernetes, service mesh, message queues
- **Includes:** Service communication patterns, deployment strategies
- **Best for:** Scalable distributed systems, enterprise applications
- **Agent Focus:** Microservices architect, DevOps engineer, API developer

## 🤖 Data Science & Machine Learning

### data-science
**Research and analysis projects with proper methodology**
- **Technologies:** Jupyter, pandas, scikit-learn, R, statistical tools
- **Includes:** Research methodology, experiment tracking, reproducibility
- **Best for:** Research projects, data analysis, statistical studies
- **Agent Focus:** Data scientist, research analyst, statistician

### ml-model
**Production machine learning model development and deployment**
- **Technologies:** TensorFlow, PyTorch, MLflow, model serving frameworks
- **Includes:** MLOps pipelines, model versioning, deployment strategies
- **Best for:** AI/ML products, predictive systems, recommendation engines
- **Agent Focus:** ML engineer, MLOps specialist, data engineer

### data-pipeline
**ETL processes and data engineering workflows**
- **Technologies:** Apache Airflow, Kafka, Spark, data warehouses
- **Includes:** Pipeline orchestration, data quality checks, monitoring
- **Best for:** Data warehousing, real-time processing, data integration
- **Agent Focus:** Data engineer, pipeline architect, DevOps engineer

### jupyter-notebook
**Interactive analysis and research documentation**
- **Technologies:** JupyterLab, notebook best practices, reproducible research
- **Includes:** Documentation standards, version control for notebooks
- **Best for:** Exploratory analysis, research documentation, tutorials
- **Agent Focus:** Data scientist, research analyst, technical writer

## 🛠️ Development Tools & Infrastructure

### cli
**Command-line tools and utilities**
- **Technologies:** Click, argparse, Typer, shell scripting
- **Includes:** User experience patterns, configuration management
- **Best for:** Developer tools, system utilities, automation scripts
- **Agent Focus:** CLI developer, DevOps engineer, system administrator

### desktop-app
**Cross-platform desktop applications**
- **Technologies:** PyQt, Tkinter, Electron, Flutter Desktop
- **Includes:** UI patterns, packaging, distribution strategies
- **Best for:** Desktop software, productivity tools, system applications
- **Agent Focus:** Desktop developer, UI/UX designer, QA engineer

### testing
**Testing frameworks and quality assurance systems**
- **Technologies:** pytest, Jest, Selenium, testing best practices
- **Includes:** Test automation, CI/CD integration, quality gates
- **Best for:** Testing infrastructure, QA automation, quality systems
- **Agent Focus:** QA engineer, test automation specialist, DevOps engineer

### devops
**Infrastructure, deployment, and operations**
- **Technologies:** Terraform, Ansible, Docker, Kubernetes, CI/CD
- **Includes:** Infrastructure as Code, monitoring, deployment pipelines
- **Best for:** Infrastructure management, deployment automation, operations
- **Agent Focus:** DevOps engineer, SRE, infrastructure architect

## 🎯 Flexible Options

### custom
**Pre-configured custom project type**
- **Includes:** Basic framework structure with customizable components
- **Best for:** Specialized domains not covered by standard types
- **Customization:** Use this when you need framework benefits with custom requirements

### other
**Completely user-defined project type**
- **Interactive:** Prompts for your custom project type specification
- **Fully flexible:** You define the project characteristics
- **Best for:** Unique projects, experimental work, specialized domains

**Example usage:**
```bash
agentic-framework init my-project --type other
# Prompts: "Enter your custom project type: blockchain-dapp"
```

## 📊 Project Type Comparison

| Type | Complexity | Team Size | Timeline | Key Technologies |
|------|------------|-----------|----------|------------------|
| web-app | Medium-High | 3-8 | 3-12 months | Django, React, PostgreSQL |
| api | Medium | 2-5 | 1-6 months | FastAPI, Docker, Redis |
| dashboard | Low-Medium | 1-3 | 1-3 months | Streamlit, Plotly, pandas |
| ml-model | High | 2-6 | 3-9 months | TensorFlow, MLflow, Kubernetes |
| data-pipeline | Medium-High | 2-5 | 2-8 months | Airflow, Spark, cloud services |
| cli | Low-Medium | 1-3 | 1-4 months | Click, packaging tools |
| microservice | High | 4-12 | 6-18 months | Docker, Kubernetes, service mesh |

## 🎨 Customization Options

Each project type can be customized with:

### Standards Level
- **Basic:** Essential standards only
- **Standard:** Comprehensive best practices (default)
- **Enterprise:** Full enterprise-grade standards

### Quality Gates
- **Development:** Basic validation
- **Production:** Full quality validation (default)
- **Critical:** Maximum validation for critical systems

### Agent Configuration
- **Core Agents:** Essential agents only
- **Full Suite:** All 21 specialized agents (default)
- **Custom:** Select specific agents for your needs

## 🚀 Usage Examples

### Choosing the Right Type

```bash
# E-commerce website
agentic-framework init ecommerce-site --type web-app

# Mobile app backend
agentic-framework init mobile-api --type api

# Sales analytics dashboard  
agentic-framework init sales-analytics --type dashboard

# Recommendation system
agentic-framework init recommendation-engine --type ml-model

# Data warehouse ETL
agentic-framework init data-warehouse --type data-pipeline

# Developer productivity tool
agentic-framework init dev-tool --type cli

# Distributed service platform
agentic-framework init service-platform --type microservice

# Research analysis
agentic-framework init research-analysis --type data-science

# Custom blockchain project
agentic-framework init blockchain-dapp --type other
```

### Interactive Selection

Use the Master Agent for guided selection:
```bash
agentic-framework master-agent
# Select: 3. Create New Project
# Browse all options with descriptions
```

## 🔄 Migration Between Types

Projects can be migrated between types as requirements evolve:

```bash
# Planned feature
agentic-framework migrate --from web-app --to microservice
```

## 📖 Related Pages

- [Getting Started](Getting-Started) - Create your first project
- [CLI Reference](CLI-Reference) - Command-line usage
- [Development Standards](Development-Standards) - Standards for each type
- [AI Agents](AI-Agents) - Agents included with each type

---

**Tip:** Not sure which type to choose? Use `agentic-framework master-agent` and select "Framework Overview" to understand the differences! 🎯