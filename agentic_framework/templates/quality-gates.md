# Quality Gates and Approval Criteria

## Overview

This document defines specific quality gates and approval criteria for each handoff point in the agentic SDLC workflows. Quality gates ensure that deliverables meet required standards before progressing to the next phase, maintaining high-quality outcomes throughout the development process.

## Quality Gate Framework

### Gate Structure

Each quality gate consists of:
- **Entry Criteria**: Requirements that must be met to begin the gate review
- **Automated Checks**: Tests and validations run automatically
- **Manual Review Criteria**: Human evaluation requirements
- **Exit Criteria**: Requirements to pass the gate and proceed
- **Escalation Path**: What happens if the gate fails

### Gate Types

1. **Phase Gates**: Major checkpoints between workflow phases
2. **Task Gates**: Smaller checkpoints for individual deliverables
3. **Security Gates**: Security-focused reviews at critical points
4. **Performance Gates**: Performance validation checkpoints

## Software/Systems Workflow Gates

### Gate 1: Requirements Validation

**Phase**: Definition & Design → Requirements Complete
**Stakeholders**: Business Analyst (AI) → Human Business Analyst → Product Owner

#### Entry Criteria
- [ ] All epics have been decomposed into user stories
- [ ] Each user story has Gherkin acceptance criteria
- [ ] Business requirements document exists
- [ ] Stakeholder interviews completed

#### Automated Checks
```yaml
automated_checks:
  gherkin_syntax_validation:
    tool: "custom_gherkin_parser"
    criteria: "All acceptance criteria use valid Gherkin syntax"
    pass_threshold: "100%"
  
  story_completeness:
    tool: "story_analyzer"
    criteria: "All user stories have title, description, and acceptance criteria"
    pass_threshold: "100%"
  
  requirements_traceability:
    tool: "traceability_checker" 
    criteria: "All user stories trace back to business objectives"
    pass_threshold: "100%"
```

#### Manual Review Criteria

**Business Analyst Review**:
- [ ] User stories accurately reflect business requirements
- [ ] Acceptance criteria are testable and unambiguous
- [ ] Edge cases and error scenarios are covered
- [ ] Non-functional requirements are documented
- [ ] User personas and journeys are complete

**Product Owner Approval**:
- [ ] Stories align with product vision and strategy
- [ ] Priority ranking is appropriate for business value
- [ ] Dependencies between stories are identified
- [ ] Scope is manageable within timeline constraints
- [ ] Success metrics are defined and measurable

#### Exit Criteria
- [ ] All automated checks pass
- [ ] Business Analyst sign-off received
- [ ] Product Owner approval documented
- [ ] Requirements baseline established in version control
- [ ] Next phase team members notified

#### Failure Handling
```yaml
failure_escalation:
  minor_issues:
    action: "Return to Business Analyst AI for revision"
    max_iterations: 3
    escalation_time: "2 business days"
  
  major_issues:
    action: "Escalate to Product Owner and Project Manager"
    required_meeting: "Requirements review session"
    timeline_impact: "Assess and communicate delays"
```

### Gate 2: Architecture Approval

**Phase**: Requirements → Architecture Design Complete  
**Stakeholders**: Solutions Architect (AI) → Human Architect → Architecture Review Board

#### Entry Criteria
- [ ] Requirements gate passed
- [ ] Non-functional requirements documented
- [ ] Technology constraints identified
- [ ] Integration requirements defined

#### Automated Checks
```yaml
automated_checks:
  architecture_documentation:
    tool: "doc_completeness_checker"
    criteria: "C4 diagrams, API specs, and data models present"
    pass_threshold: "100%"
  
  security_architecture:
    tool: "security_architecture_scanner"
    criteria: "Security controls documented for all data flows"
    pass_threshold: "100%"
  
  performance_modeling:
    tool: "performance_calculator"
    criteria: "Load estimates and capacity planning complete"
    pass_threshold: "All scenarios covered"
  
  technology_compliance:
    tool: "tech_stack_validator"
    criteria: "All technologies in approved libraries list"
    pass_threshold: "100%"
```

#### Manual Review Criteria

**Solutions Architect Review**:
- [ ] Architecture addresses all functional requirements
- [ ] Scalability and performance requirements met
- [ ] Integration patterns are appropriate
- [ ] Data architecture supports business needs
- [ ] Technology choices are justified

**Security Expert Review**:
- [ ] Threat modeling completed for all components
- [ ] Security controls address identified risks
- [ ] Data protection measures are adequate
- [ ] Authentication and authorization design is sound
- [ ] Compliance requirements are addressed

#### Exit Criteria
- [ ] All automated checks pass
- [ ] Solutions Architect approval documented
- [ ] Security team sign-off received
- [ ] Architecture Decision Records (ADRs) published
- [ ] Development team briefed on architecture

### Gate 3: Code Quality Validation

**Phase**: Development → Code Complete
**Stakeholders**: Software Developer (AI) → Human Developer → Tech Lead

#### Entry Criteria
- [ ] Architecture gate passed
- [ ] Development environment set up
- [ ] Coding standards configured
- [ ] CI/CD pipeline operational

#### Automated Checks
```yaml
automated_checks:
  code_quality:
    tool: "ruff"
    criteria: "Zero linting errors"
    pass_threshold: "100%"
    config_file: "pyproject.toml"
  
  type_safety:
    tool: "mypy"
    criteria: "No type errors"
    pass_threshold: "100%"
    config_file: "pyproject.toml"
  
  security_scan:
    tool: "bandit"
    criteria: "No high or medium severity issues"
    pass_threshold: "100%"
    config_file: "pyproject.toml"
  
  test_coverage:
    tool: "pytest-cov"
    criteria: "Minimum test coverage met"
    pass_threshold: "80%"
    critical_path_threshold: "95%"
  
  dependency_check:
    tool: "safety"
    criteria: "No known vulnerabilities in dependencies"
    pass_threshold: "100%"
  
  documentation:
    tool: "doc_coverage"
    criteria: "All public APIs documented"
    pass_threshold: "100%"
```

#### Manual Review Criteria

**Human Developer Review**:
- [ ] Code follows architectural patterns
- [ ] Error handling is comprehensive
- [ ] Performance considerations addressed
- [ ] Code is maintainable and readable
- [ ] Unit tests cover business logic effectively

**Tech Lead Approval**:
- [ ] Implementation aligns with technical vision
- [ ] Code review feedback addressed
- [ ] Integration points tested
- [ ] Deployment considerations addressed
- [ ] Technical debt is minimal and documented

#### Exit Criteria
- [ ] All automated checks pass with 100% score
- [ ] Peer code review completed and approved
- [ ] Tech Lead sign-off documented
- [ ] CI/CD pipeline passes all stages
- [ ] Code merged to main branch

### Gate 4: Testing Validation

**Phase**: Code Complete → Testing Complete
**Stakeholders**: QA Engineer (AI) → Human QA Engineer → Test Manager

#### Entry Criteria
- [ ] Code quality gate passed
- [ ] Test environment deployed
- [ ] Test data prepared
- [ ] Test automation scripts ready

#### Automated Checks
```yaml
automated_checks:
  unit_tests:
    tool: "pytest"
    criteria: "All unit tests pass"
    pass_threshold: "100%"
    timeout: "5 minutes"
  
  integration_tests:
    tool: "pytest"
    criteria: "All integration tests pass"
    pass_threshold: "100%"
    timeout: "15 minutes"
  
  api_tests:
    tool: "postman/newman"
    criteria: "All API endpoint tests pass"
    pass_threshold: "100%"
    include_negative_tests: true
  
  performance_tests:
    tool: "locust"
    criteria: "Response times within SLA"
    sla_requirements:
      - "95th percentile < 500ms"
      - "Error rate < 0.1%"
      - "Throughput > 100 RPS"
  
  security_tests:
    tool: "owasp_zap"
    criteria: "No high severity vulnerabilities"
    scan_types: ["active", "passive"]
```

#### Manual Review Criteria

**QA Engineer Review**:
- [ ] Test cases cover all acceptance criteria
- [ ] Edge cases and error scenarios tested
- [ ] User interface testing completed
- [ ] Cross-browser/platform compatibility verified
- [ ] Accessibility requirements validated

**Test Manager Approval**:
- [ ] Test strategy executed completely
- [ ] Defect resolution meets quality standards
- [ ] Test automation coverage is adequate
- [ ] Performance meets non-functional requirements
- [ ] User acceptance testing criteria defined

#### Exit Criteria
- [ ] All automated tests pass
- [ ] Manual test execution completed
- [ ] Critical and high-priority defects resolved
- [ ] Performance benchmarks met
- [ ] QA sign-off documented

### Gate 5: Deployment Readiness

**Phase**: Testing Complete → Production Deployment
**Stakeholders**: DevOps Engineer (AI) → Human DevOps Engineer → Operations Team

#### Entry Criteria
- [ ] Testing gate passed
- [ ] Production environment prepared
- [ ] Deployment scripts tested
- [ ] Rollback procedures documented

#### Automated Checks
```yaml
automated_checks:
  infrastructure_validation:
    tool: "terraform_validate"
    criteria: "Infrastructure code is valid"
    pass_threshold: "100%"
  
  security_configuration:
    tool: "checkov"
    criteria: "Infrastructure security best practices"
    pass_threshold: "No high severity issues"
  
  deployment_pipeline:
    tool: "pipeline_validator"
    criteria: "CI/CD pipeline executes successfully"
    environments: ["staging", "pre-production"]
  
  monitoring_setup:
    tool: "monitoring_validator"
    criteria: "All required monitoring in place"
    components: ["logs", "metrics", "alerts", "dashboards"]
  
  backup_verification:
    tool: "backup_tester"
    criteria: "Backup and restore procedures tested"
    pass_threshold: "100% success rate"
```

#### Manual Review Criteria

**DevOps Engineer Review**:
- [ ] Deployment automation is complete and tested
- [ ] Monitoring and alerting configured
- [ ] Backup and disaster recovery procedures ready
- [ ] Security configurations reviewed
- [ ] Scaling policies defined

**Operations Team Approval**:
- [ ] Production support procedures documented
- [ ] Incident response plan updated
- [ ] Capacity planning completed
- [ ] Service level agreements defined
- [ ] Change management process followed

## Data Science/ML Workflow Gates

### Gate 6: Data Quality Validation

**Phase**: Problem Framing → Data Engineering Complete
**Stakeholders**: Data Engineer (AI) → Human Data Engineer → Data Science Lead

#### Entry Criteria
- [ ] Business problem clearly defined
- [ ] Data sources identified and accessible
- [ ] Data governance requirements understood
- [ ] Pipeline architecture designed

#### Automated Checks
```yaml
automated_checks:
  data_quality:
    tool: "great_expectations"
    criteria: "Data quality checks pass"
    validations:
      - "completeness > 95%"
      - "uniqueness constraints met"
      - "value ranges within bounds"
      - "schema consistency verified"
  
  data_lineage:
    tool: "lineage_tracker"
    criteria: "Data lineage documented"
    pass_threshold: "100% of sources traced"
  
  pipeline_tests:
    tool: "pytest"
    criteria: "Data pipeline tests pass"
    coverage_threshold: "80%"
  
  performance_validation:
    tool: "pipeline_profiler"
    criteria: "Processing time within limits"
    sla: "Process daily data < 4 hours"
```

#### Manual Review Criteria

**Data Engineer Review**:
- [ ] Data sources are reliable and accessible
- [ ] Data transformation logic is correct
- [ ] Pipeline handles edge cases appropriately
- [ ] Data quality monitoring implemented
- [ ] Error handling and alerting configured

**Data Science Lead Approval**:
- [ ] Data meets analytical requirements
- [ ] Feature engineering pipeline ready
- [ ] Data documentation is comprehensive
- [ ] Privacy and compliance requirements met
- [ ] Data refresh procedures documented

### Gate 7: Model Validation

**Phase**: Analysis & Experimentation → Model Ready
**Stakeholders**: Data Scientist (AI) → Human Data Scientist → ML Engineering Lead

#### Entry Criteria
- [ ] Data quality gate passed
- [ ] Baseline models trained
- [ ] Feature engineering completed
- [ ] Model evaluation framework ready

#### Automated Checks
```yaml
automated_checks:
  model_performance:
    tool: "model_validator"
    criteria: "Model meets performance thresholds"
    metrics:
      - "accuracy > 85%"
      - "precision > 80%"
      - "recall > 80%"
      - "f1_score > 82%"
  
  model_bias_check:
    tool: "fairness_validator"
    criteria: "Model bias within acceptable limits"
    protected_attributes: ["age", "gender", "ethnicity"]
    max_bias_difference: "5%"
  
  model_stability:
    tool: "stability_tester"
    criteria: "Model performance stable across time periods"
    time_windows: ["weekly", "monthly"]
    stability_threshold: "< 2% variance"
  
  feature_importance:
    tool: "feature_analyzer"
    criteria: "Feature importance makes business sense"
    validation: "Manual review required"
```

#### Manual Review Criteria

**Data Scientist Review**:
- [ ] Model architecture is appropriate for problem
- [ ] Feature selection is justified by analysis
- [ ] Cross-validation methodology is sound
- [ ] Model interpretability meets requirements
- [ ] Business impact is quantified

**ML Engineering Lead Approval**:
- [ ] Model can be productionized with current infrastructure
- [ ] Model serving requirements are feasible
- [ ] Monitoring and drift detection planned
- [ ] Model versioning strategy defined
- [ ] Rollback procedures for model updates

### Gate 8: Production Model Deployment

**Phase**: Model Ready → Production Deployment
**Stakeholders**: ML Engineer (AI) → Human ML Engineer → MLOps Team

#### Entry Criteria
- [ ] Model validation gate passed
- [ ] Production environment configured
- [ ] Model serving infrastructure ready
- [ ] Monitoring systems deployed

#### Automated Checks
```yaml
automated_checks:
  model_serving_tests:
    tool: "model_server_tester"
    criteria: "Model serving API functional"
    tests: ["prediction_accuracy", "response_time", "error_handling"]
  
  infrastructure_validation:
    tool: "k8s_validator"
    criteria: "Kubernetes deployment successful"
    components: ["model_server", "monitoring", "logging"]
  
  data_pipeline_integration:
    tool: "pipeline_tester"
    criteria: "End-to-end pipeline functional"
    test_data: "Production-like sample"
  
  monitoring_validation:
    tool: "monitoring_tester"
    criteria: "All monitoring components active"
    metrics: ["model_drift", "data_drift", "performance_metrics"]
```

#### Manual Review Criteria

**ML Engineer Review**:
- [ ] Model deployment pipeline automated
- [ ] Model monitoring and alerting configured
- [ ] A/B testing framework ready (if applicable)
- [ ] Model versioning and rollback tested
- [ ] Documentation for operations team complete

**MLOps Team Approval**:
- [ ] Production deployment procedures followed
- [ ] Model governance requirements met
- [ ] Incident response procedures updated
- [ ] Model registry properly configured
- [ ] Compliance and audit trails established

## Cross-Cutting Quality Gates

### Security Gate (All Workflows)

**Trigger**: Before any production deployment
**Stakeholders**: Security Expert (AI) → Human Security Expert → CISO

#### Automated Security Checks
```yaml
security_checks:
  vulnerability_scan:
    tool: "trivy"
    criteria: "No critical or high vulnerabilities"
    scan_targets: ["code", "dependencies", "container_images"]
  
  secrets_scan:
    tool: "truffleHog"
    criteria: "No hardcoded secrets detected"
    scope: ["source_code", "configuration_files"]
  
  compliance_check:
    tool: "compliance_scanner"
    criteria: "Regulatory requirements met"
    standards: ["SOC2", "GDPR", "fintech_regulations"]
  
  access_control_validation:
    tool: "access_analyzer"
    criteria: "Least privilege access implemented"
    components: ["apis", "databases", "infrastructure"]
```

#### Manual Security Review
- [ ] Threat model reviewed and updated
- [ ] Security controls tested
- [ ] Data protection measures validated
- [ ] Incident response procedures updated
- [ ] Security training requirements met

### Performance Gate (Critical Systems)

**Trigger**: Before high-load production systems
**Stakeholders**: Performance team

#### Performance Validation
```yaml
performance_tests:
  load_testing:
    tool: "locust"
    criteria: "System handles expected load"
    scenarios: ["normal_load", "peak_load", "stress_test"]
  
  response_time:
    criteria: "95th percentile response time < 500ms"
    measurement_period: "10 minutes"
  
  throughput:
    criteria: "System processes > 1000 requests/second"
    sustained_period: "30 minutes"
  
  resource_utilization:
    criteria: "CPU and memory usage < 80%"
    measurement_period: "Peak load test"
```

## Quality Gate Enforcement

### Automated Gate Execution

```python
class QualityGateExecutor:
    """Executes quality gates with automated and manual checks."""
    
    def execute_gate(self, gate_config: dict, project_context: dict) -> dict:
        """Execute a quality gate."""
        results = {
            "gate_name": gate_config["name"],
            "status": "running",
            "automated_checks": {},
            "manual_reviews": {},
            "overall_result": "pending",
            "blockers": [],
            "recommendations": []
        }
        
        # Execute automated checks
        for check_name, check_config in gate_config["automated_checks"].items():
            check_result = self._run_automated_check(check_name, check_config, project_context)
            results["automated_checks"][check_name] = check_result
            
            if not check_result["passed"]:
                results["blockers"].append(f"Automated check failed: {check_name}")
        
        # Initiate manual reviews
        for reviewer_role, review_criteria in gate_config["manual_reviews"].items():
            review_request = self._create_review_request(reviewer_role, review_criteria, project_context)
            results["manual_reviews"][reviewer_role] = review_request
        
        # Determine overall result
        all_automated_passed = all(check["passed"] for check in results["automated_checks"].values())
        
        if all_automated_passed and not results["blockers"]:
            results["status"] = "automated_checks_passed"
            results["overall_result"] = "pending_manual_review"
        else:
            results["status"] = "failed"
            results["overall_result"] = "blocked"
        
        return results
    
    def _run_automated_check(self, check_name: str, check_config: dict, context: dict) -> dict:
        """Run a single automated check."""
        try:
            # This would integrate with actual tools (ruff, pytest, etc.)
            tool = check_config["tool"]
            criteria = check_config["criteria"] 
            
            # Simulate tool execution
            result = self._execute_tool(tool, context)
            
            return {
                "check_name": check_name,
                "tool": tool,
                "criteria": criteria,
                "result": result,
                "passed": result["success"],
                "details": result.get("details", ""),
                "timestamp": datetime.utcnow().isoformat()
            }
            
        except Exception as e:
            return {
                "check_name": check_name,
                "passed": False,
                "error": str(e),
                "timestamp": datetime.utcnow().isoformat()
            }
```

### Gate Status Dashboard

```python
class QualityGateDashboard:
    """Dashboard for monitoring quality gate status."""
    
    def get_gate_status(self, project_id: str) -> dict:
        """Get current quality gate status for a project."""
        return {
            "project_id": project_id,
            "gates_passed": 3,
            "gates_failed": 0,
            "gates_pending": 2,
            "current_gate": "Code Quality Validation",
            "blockers": [
                {
                    "gate": "Code Quality Validation",
                    "check": "test_coverage",
                    "issue": "Coverage is 75%, minimum required is 80%",
                    "assigned_to": "development_team"
                }
            ],
            "next_reviews_due": [
                {
                    "gate": "Testing Validation", 
                    "reviewer": "qa_lead@company.com",
                    "due_date": "2025-09-28"
                }
            ]
        }
```

This comprehensive quality gate system ensures that every deliverable meets your high standards before progressing through the agentic SDLC workflow, maintaining quality while enabling efficient automation.