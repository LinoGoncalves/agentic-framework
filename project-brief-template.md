# Project Brief Template

## Project Overview

### Project Name

[Enter project name]

### Project Type

- [ ] Web Application (Django/Flask/FastAPI)
- [ ] REST API Service
- [ ] Data Dashboard/Analytics (Streamlit)
- [ ] ML Model Serving
- [ ] Data Pipeline/ETL
- [ ] CLI Tool
- [ ] Other: _______________

### Project Vision

**Problem Statement**:
[Describe the business problem or opportunity this project addresses]

**Solution Overview**:
[High-level description of the proposed solution]

**Success Criteria**:
[How will you measure success? Include specific, measurable outcomes]

## Scope & Requirements

### Core Functionality

[List the essential features and capabilities]

### Out of Scope

[Explicitly list what will NOT be included in this project]

### User Stories (High-Level)

[Major user stories or epics - detailed stories will be created by Business Analyst]

**Epic 1**: [Epic Name]

- As a [user type], I want [capability] so that [benefit]

**Epic 2**: [Epic Name]

- As a [user type], I want [capability] so that [benefit]

## Technical Specifications

### Technology Stack

**Backend Framework**:

- [ ] Django (full-featured web apps)
- [ ] Flask (lightweight services)
- [ ] FastAPI (modern APIs)
- [ ] Streamlit (data dashboards)
- [ ] Other: _______________

**Database**:

- [ ] PostgreSQL (primary relational)
- [ ] MongoDB (document storage)
- [ ] InfluxDB (time series)
- [ ] Redis (caching/sessions)
- [ ] Other: _______________

**Data Processing**:

- [ ] Pandas (small/medium datasets)
- [ ] Polars (large datasets/performance)
- [ ] PySpark (distributed processing)
- [ ] Apache Kafka (streaming)
- [ ] Other: _______________

**Cloud Infrastructure**:

- [ ] AWS
- [ ] Azure
- [ ] On-premises
- [ ] Hybrid
- [ ] Docker/Kubernetes required: Yes/No

### Performance Requirements

- **Expected Load**: [e.g., 1000 users, 10k requests/day]
- **Response Time**: [e.g., < 200ms for API calls]
- **Data Volume**: [e.g., 1GB daily, 100GB total]
- **Availability**: [e.g., 99.9% uptime]

### Security & Compliance

- **Authentication**:

  - [ ] OAuth 2.0
  - [ ] SAML
  - [ ] JWT tokens
  - [ ] Other: _______________
- **Compliance Requirements**:

  - [ ] Fintech regulations (if applicable)
  - [ ] GDPR
  - [ ] SOC 2
  - [ ] Other: _______________
- **Data Sensitivity**:

  - [ ] PII (Personally Identifiable Information)
  - [ ] Financial data
  - [ ] Health data
  - [ ] Trade secrets
  - [ ] Other: _______________

## Architecture & Design

### System Architecture Approach

- [ ] Monolithic application
- [ ] Microservices
- [ ] Serverless functions
- [ ] Event-driven architecture
- [ ] Other: _______________

### Integration Requirements

**External Systems**:
[List systems this project needs to integrate with]

1. [System Name] - [Integration Type] - [Purpose]
2. 
3. 

**APIs to Consume**:
[List third-party APIs or services]

1. [API Name] - [Purpose] - [Documentation URL]
2. 
3. 

**APIs to Provide**:
[List APIs this system will expose]

1. [Endpoint Description] - [Consumer] - [Data Format]
2. 
3. 

## Project Timeline & Milestones

### Target Dates

- **Project Start**: [Date]
- **MVP Delivery**: [Date]
- **Production Launch**: [Date]
- **Project Completion**: [Date]

### Key Milestones

1. **Requirements & Design Complete**: [Date]
2. **Core Development Complete**: [Date]
3. **Testing & QA Complete**: [Date]
4. **Deployment & Launch**: [Date]

### Dependencies

[List external dependencies that could impact timeline]

- [ ] [Dependency Description] - [Impact] - [Mitigation Plan]
- [ ]
- [ ]

## Team & Resources

### Core Team Roles

- **Product Owner**: [Name] - [Contact]
- **Solutions Architect**: [Name] - [Contact]
- **Lead Developer**: [Name] - [Contact]
- **DevOps Engineer**: [Name] - [Contact]
- **QA Engineer**: [Name] - [Contact]

### Additional Specialists (if needed)

- [ ] **Data Scientist**: [Name] - [Contact]
- [ ] **ML Engineer**: [Name] - [Contact]
- [ ] **Security Expert**: [Name] - [Contact]
- [ ] **UI/UX Designer**: [Name] - [Contact]
- [ ] **Database Engineer**: [Name] - [Contact]

### Budget & Resources

- **Development Budget**: $___________
- **Infrastructure Budget**: $___________/month
- **Third-party Services**: $___________/month
- **Timeline**: _______ months

## Risk Assessment

### Technical Risks

| Risk               | Impact       | Likelihood   | Mitigation Strategy |
| ------------------ | ------------ | ------------ | ------------------- |
| [Risk description] | High/Med/Low | High/Med/Low | [How to mitigate]   |
|                    |              |              |                     |
|                    |              |              |                     |

### Business Risks

| Risk               | Impact       | Likelihood   | Mitigation Strategy |
| ------------------ | ------------ | ------------ | ------------------- |
| [Risk description] | High/Med/Low | High/Med/Low | [How to mitigate]   |
|                    |              |              |                     |
|                    |              |              |                     |

## Quality & Testing Strategy

### Testing Requirements

- **Unit Test Coverage**: 80% minimum
- **Integration Testing**: Required for all external integrations
- **Performance Testing**: Required if load > 100 concurrent users
- **Security Testing**: Required for all external-facing applications
- **User Acceptance Testing**: Required before production deployment

### Definition of Done

A feature is considered "done" when:

- [ ] Code is written and peer-reviewed
- [ ] Unit tests written and passing (80% coverage)
- [ ] Integration tests passing
- [ ] Security scan passed
- [ ] Documentation updated
- [ ] QA testing completed
- [ ] Performance requirements met
- [ ] Deployed to staging environment
- [ ] Product Owner approval received

## Monitoring & Success Metrics

### Key Performance Indicators (KPIs)

[How will you measure the success of this project after launch?]

**Technical Metrics**:

- Response time: < _____ ms
- Uptime: > _____%
- Error rate: < _____%
- CPU usage: < _____%

**Business Metrics**:

- [Metric 1]: [Target]
- [Metric 2]: [Target]
- [Metric 3]: [Target]

### Monitoring Strategy

- [ ] Application Performance Monitoring (APM)
- [ ] Infrastructure Monitoring
- [ ] Business Metrics Dashboard
- [ ] Log Aggregation
- [ ] Error Tracking

## Deployment & Operations

### Deployment Strategy

- [ ] Blue-Green Deployment
- [ ] Rolling Deployment
- [ ] Canary Deployment
- [ ] Feature Flags

### Environment Strategy

- **Development**: [Description/URL]
- **Staging**: [Description/URL]
- **Production**: [Description/URL]

### Backup & Recovery

- **Data Backup**: [Frequency and retention policy]
- **Recovery Time Objective (RTO)**: [Maximum acceptable downtime]
- **Recovery Point Objective (RPO)**: [Maximum acceptable data loss]

## Sign-off & Approvals

### Stakeholder Approval

- [ ] **Business Sponsor**: _________________ Date: _______
- [ ] **Product Owner**: _________________ Date: _______
- [ ] **Technical Lead**: _________________ Date: _______
- [ ] **Security Team**: _________________ Date: _______
- [ ] **Operations Team**: _________________ Date: _______

### Project Kickoff

**Kickoff Meeting Scheduled**: [Date/Time]
**Project Repository Created**: [GitHub URL]
**Development Environment Setup**: [Date]

---

## Instructions for Master Agent

When this project brief is complete and approved:

1. **Load the appropriate workflow** from master-agent.md based on project type
2. **Begin Phase 1**: Requirements & Design with the appropriate sub-agents
3. **Create project repository** with standard Python project structure
4. **Set up development environment** according to development standards
5. **Initialize project tracking** with milestones and dependencies

**Master Agent Response**: "Master Agent initialized. I have reviewed the project brief and development standards. Here is the proposed high-level project plan for your approval."
