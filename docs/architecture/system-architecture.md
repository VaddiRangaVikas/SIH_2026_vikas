# SIH26117 — System Architecture

## 1. Purpose

This document defines the proposed technical architecture for **SIH26117: Sovereign On-Premise Agentic AI Workbench using Open-Weight Multimodal LLMs for Confidential Industrial Work**.

The architecture is designed around the core requirements of the Problem Statement:

* On-premise and sovereign operation
* Multiple open-weight models
* Automatic task-based model selection
* Agentic planning, reasoning, tool use, and iteration
* Multimodal document and image understanding
* Local organizational knowledge retrieval
* Sandboxed code execution
* Real deliverable generation
* Auditability and visible proof of no external calls

The architecture is intentionally **modular and model-agnostic**, so individual components can be developed, tested, and replaced independently.

---

# 2. High-Level Architecture

```text
                              ┌──────────────────────┐
                              │        USER          │
                              └──────────┬───────────┘
                                         │
                                         ▼
                              ┌──────────────────────┐
                              │    WEB WORKBENCH     │
                              │      Frontend        │
                              └──────────┬───────────┘
                                         │
                                         │ HTTP / WebSocket
                                         ▼
                              ┌──────────────────────┐
                              │       API LAYER      │
                              │       FastAPI        │
                              └──────────┬───────────┘
                                         │
                                         ▼
                        ┌─────────────────────────────────┐
                        │      CUSTOM ORCHESTRATION       │
                        │                                 │
                        │ Task lifecycle & coordination   │
                        └───────────────┬─────────────────┘
                                        │
                                        ▼
                        ┌─────────────────────────────────┐
                        │        AGENT RUNTIME             │
                        │            LangGraph             │
                        │                                 │
                        │ Planning • State • Reasoning     │
                        │ Tool Selection • Iteration       │
                        └───────┬─────────┬─────────┬─────┘
                                │         │         │
                ┌───────────────┘         │         └───────────────┐
                ▼                         ▼                         ▼
       ┌────────────────┐       ┌────────────────┐       ┌────────────────┐
       │  MODEL ROUTER  │       │      RAG       │       │  TOOL RUNTIME  │
       │                │       │                │       │                │
       │ Task → Model   │       │ Local Knowledge│       │ Tool Selection │
       │ Model Registry │       │ Retrieval      │       │ Execution      │
       └───────┬────────┘       └───────┬────────┘       └───────┬────────┘
               │                        │                        │
               ▼                        ▼              ┌─────────┼──────────┐
       ┌────────────────┐       ┌────────────────┐     ▼         ▼          ▼
       │ Local Model    │       │ Vector Store   │   Files     Code     Artifacts
       │ Infrastructure │       │ + Documents    │              │
       └────────────────┘       └────────────────┘              ▼
                                                        ┌──────────────┐
                                                        │   SANDBOX    │
                                                        │    Docker    │
                                                        └──────────────┘


        ┌─────────────────────────────────────────────────────────────┐
        │                  MULTIMODAL SERVICES                        │
        │                                                             │
        │       OCR • Vision • Scanned Documents • Images            │
        └────────────────────────────┬────────────────────────────────┘
                                     │
                                     ▼
                              Agent / RAG Layer


        ┌─────────────────────────────────────────────────────────────┐
        │                    SECURITY LAYER                           │
        │                                                             │
        │  Network Controls • Firewall • Monitoring • Audit Logging  │
        │  Access Policies • Sandbox Isolation                       │
        └─────────────────────────────────────────────────────────────┘


        ┌─────────────────────────────────────────────────────────────┐
        │                       DATA LAYER                             │
        │                                                             │
        │       PostgreSQL • Vector Data • Files • Artifacts          │
        └─────────────────────────────────────────────────────────────┘
```

---

# 3. Architectural Principles

## 3.1 Sovereignty First

The intended production deployment must keep confidential industrial data within the organization's controlled environment.

The architecture therefore avoids making external AI services a dependency.

The system should be capable of operating using locally deployed services and models.

---

## 3.2 Model Agnostic

The Agent Runtime must not be tightly coupled to one specific AI model or inference engine.

Instead:

```text
Agent Runtime
      │
      ▼
 Model Router
      │
      ▼
Model Provider Interface
      │
      ├── Model A
      ├── Model B
      ├── Model C
      └── Future Models
```

This allows new open-weight models to be introduced without redesigning the agent architecture.

---

## 3.3 Agent-Centric

The system is not designed as a single-turn chatbot.

The Agent Runtime is responsible for:

* Understanding the task
* Creating a plan
* Maintaining execution state
* Selecting tools
* Executing actions
* Observing results
* Validating results
* Iterating or replanning
* Producing the final result

---

## 3.4 Local Tool Execution

Tools are accessed through a controlled Tool Runtime.

The agent should not directly receive unrestricted access to the host system.

Instead:

```text
Agent
  ↓
Tool Runtime
  ↓
Policy / Permission Check
  ↓
Tool
  ↓
Execution
  ↓
Result
  ↓
Agent
```

---

## 3.5 Security by Boundary

Security is treated as an architectural layer rather than an afterthought.

Sensitive operations should pass through controlled boundaries involving:

* Tool permissions
* Sandbox isolation
* Network restrictions
* Audit logging
* Resource controls
* Access policies

---

# 4. Major Components

## 4.1 Web Workbench

### Responsibility

The frontend is the primary interface through which users interact with the AI workbench.

### Core responsibilities

* Submit tasks
* Upload files
* View task status
* View execution progress
* Display agent plans
* Display model selection
* Display tool activity
* View generated artifacts
* Display security/sovereignty status
* Access task history

### Proposed technology

**Next.js + React + TypeScript**

---

# 5. API Layer

## Responsibility

The API Layer provides the controlled interface between the frontend and the backend system.

### Proposed technology

**FastAPI**

### Responsibilities

* Authentication/session handling
* Task creation
* File uploads
* Task status
* Streaming execution events
* Artifact access
* System status
* Security status
* Communication with the orchestration layer

The frontend should communicate with the backend through the API rather than directly accessing internal components.

---

# 6. Custom Orchestration Layer

## Responsibility

The orchestration layer coordinates the overall lifecycle of a task.

It acts as the bridge between:

```text
API
 ↓
Agent Runtime
 ↓
Models / Tools / RAG
 ↓
Final Result
```

### Responsibilities

* Create and manage task executions
* Initialize agent state
* Coordinate services
* Manage execution lifecycle
* Handle errors
* Track execution events
* Coordinate artifact generation
* Persist task information

The orchestration layer should remain independent from the frontend.

---

# 7. Agent Runtime

## Proposed technology

**LangGraph**

The Agent Runtime is the central intelligence/control layer of the system.

### Responsibilities

### Planning

Break a complex user request into executable steps.

### Reasoning

Determine what information and actions are required.

### State Management

Maintain the state of an ongoing multi-step task.

### Tool Selection

Determine which tools are required.

### Model Selection

Request an appropriate model from the Model Router.

### Iteration

Evaluate intermediate results and continue, correct, or replan when required.

### Completion

Determine when the task has produced a satisfactory result.

---

# 8. Model Router

The Model Router provides a model-agnostic interface between the Agent Runtime and the model-serving infrastructure.

```text
                 Agent Runtime
                       │
                       ▼
                ┌──────────────┐
                │ Model Router │
                └──────┬───────┘
                       │
              Task / Capability
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
      Reasoning      Coding       Vision
        Model         Model        Model
```

### Responsibilities

* Maintain model registry
* Understand model capabilities
* Classify task requirements
* Select an appropriate model
* Route inference requests
* Support multiple models
* Allow future models to be added

### Important design decision

The exact model-serving technology and hardware deployment will be finalized separately.

The rest of the system must not depend directly on that decision.

---

# 9. Tool Runtime

The Tool Runtime provides controlled access to capabilities that allow the agent to perform actual work.

### Initial tool categories

```text
File Tools
├── Read
├── Write
└── Transform

Code Tools
├── Generate
├── Execute
└── Verify

Spreadsheet Tools
├── Read
├── Analyze
└── Generate

Knowledge Tools
└── Search

Artifact Tools
├── DOCX
├── PPTX
├── XLSX
└── Code
```

The Tool Runtime acts as a controlled execution boundary between the agent and these capabilities.

---

# 10. Sandbox

Code execution must not occur directly on the host environment.

Proposed approach:

**Docker-based sandbox**

```text
Generated Code
      ↓
Tool Runtime
      ↓
Policy Check
      ↓
Docker Sandbox
      ↓
Execution
      ↓
Output / Errors
      ↓
Verification
```

The sandbox should eventually enforce appropriate:

* Resource limits
* Execution limits
* File access restrictions
* Network restrictions
* Process isolation

The exact security policies will be defined separately.

---

# 11. RAG / Local Knowledge Base

The system must be capable of grounding its work in organizational knowledge such as:

* Manuals
* SOPs
* Past correspondence
* Internal documents

Proposed pipeline:

```text
Document
   ↓
Ingestion
   ↓
Parsing / OCR
   ↓
Chunking
   ↓
Local Embedding
   ↓
Vector Store
   ↓
Retrieval
   ↓
Agent
```

The knowledge base should remain inside the organization's controlled environment in the intended deployment.

---

# 12. Multimodal Processing Layer

The system must support inputs beyond plain text.

Potential input types include:

* Scanned PDFs
* Handwritten notes
* Engineering drawings
* Photographs
* Other images

Proposed pipeline:

```text
Image / Scanned Document
          ↓
    Document Processor
          ↓
      OCR / Vision
          ↓
 Structured Information
          ↓
      Agent Runtime
```

The exact OCR and vision technologies will be selected according to available hardware and model compatibility.

---

# 13. Deliverable Generation

The system should convert agent results into actual usable artifacts.

```text
                    Agent
                      │
                      ▼
             Structured Result
                      │
                      ▼
              Artifact Generator
                      │
       ┌──────────────┼──────────────┐
       ▼              ▼              ▼
     DOCX            PPTX           XLSX
       │
       └──────────── Code / Reports
```

Priority for the initial prototype should be determined based on the selected demonstration workflow.

The official PS's inspection-report → approval-note example makes **DOCX generation** a particularly strong candidate for the primary demonstration.

---

# 14. Data Layer

The application requires persistent storage for:

### PostgreSQL

Potentially stores:

* Users
* Tasks
* Execution states
* Tool calls
* Model selections
* Audit events
* Artifact metadata

### Vector Store

Stores embeddings and retrieval information for the local knowledge base.

### File Storage

Stores:

* Uploaded documents
* Processed files
* Generated artifacts
* Temporary task files

All storage should be designed for local deployment.

---

# 15. Security and Sovereignty Layer

Security surrounds the entire system.

```text
┌──────────────────────────────────────────────┐
│              SECURITY BOUNDARY               │
│                                              │
│ Authentication / Authorization               │
│                                              │
│ Tool Policies                                │
│                                              │
│ Docker Isolation                             │
│                                              │
│ Network Restrictions                         │
│                                              │
│ Host Firewall                                │
│                                              │
│ Network Monitoring                           │
│                                              │
│ Audit Logging                                │
│                                              │
└──────────────────────────────────────────────┘
```

### Main objectives

1. Prevent unauthorized tool execution.
2. Isolate code execution.
3. Restrict unwanted network communication.
4. Record important system activity.
5. Provide evidence of system behavior.
6. Demonstrate that external calls are not occurring.

---

# 16. End-to-End Task Flow

The general task execution flow is:

```text
USER
 │
 ▼
Frontend
 │
 ▼
API
 │
 ▼
Orchestrator
 │
 ▼
Agent Runtime
 │
 ├──────────────► Model Router
 │                     │
 │                     ▼
 │                  Model
 │                     │
 │◄────────────────────┘
 │
 ├──────────────► RAG
 │                     │
 │                     ▼
 │               Local Knowledge
 │
 ├──────────────► Tool Runtime
 │                     │
 │              ┌──────┼──────┐
 │              ▼      ▼      ▼
 │            Files   Code  Artifact
 │                     │
 │                  Sandbox
 │
 ▼
Validation / Iteration
 │
 ▼
Final Result
 │
 ▼
Artifact
 │
 ▼
Audit Log
 │
 ▼
Frontend
```

---

# 17. Primary Demonstration Architecture

The primary prototype should aim to demonstrate as many PS requirements as possible through one coherent workflow.

### Proposed workflow

```text
SCANNED INSPECTION REPORT
            │
            ▼
         Upload
            │
            ▼
    Multimodal Processing
       OCR / Vision
            │
            ▼
    Extract Key Findings
            │
            ▼
       Agent Planning
            │
            ▼
    Local Knowledge Search
            │
            ▼
        Reasoning
            │
            ▼
    Draft Approval Note
            │
            ▼
      DOCX Generation
            │
            ▼
        Validation
            │
            ▼
      Audit / Logging
            │
            ▼
     Final Deliverable
```

This workflow directly aligns with the official PS example of reading a scanned inspection report, extracting key findings, and drafting an approval note as a Word document.

---

# 18. Secondary Demonstration Flows

## Coding

```text
User Coding Request
        ↓
Agent Planning
        ↓
Code Generation
        ↓
Tool Runtime
        ↓
Docker Sandbox
        ↓
Execution
        ↓
Verification
        ↓
Result
```

The PS explicitly expects a coding task to be run and verified in a sandbox.

---

## Automatic Model Selection

```text
Task A
  ↓
Task Analysis
  ↓
Model Router
  ↓
Model A


Task B
  ↓
Task Analysis
  ↓
Model Router
  ↓
Model B
```

The demonstration should make the routing decision visible to the user.

---

## Sovereignty Proof

```text
Application Activity
       │
       ├── Model Calls
       ├── Tool Calls
       ├── File Operations
       └── Network Activity
                    │
                    ▼
              Audit Layer
                    │
                    ▼
          Sovereignty Monitor
                    │
                    ▼
         External Calls = 0
```

The PS specifically states that logs or a visible network monitor should demonstrate that no external calls are made.

---

# 19. Component Dependency Model

The dependency direction should remain controlled:

```text
Frontend
   ↓
API
   ↓
Orchestrator
   ↓
Agent Runtime
   ↓
┌───────────────┬───────────────┬───────────────┐
│               │               │
▼               ▼               ▼
Model Router    RAG        Tool Runtime
                                │
                                ▼
                             Sandbox
```

Supporting infrastructure such as the database, storage, security, logging, and monitoring services should be consumed through clearly defined interfaces.

### Important rule

**Lower-level infrastructure must not control the Agent Runtime.**

The agent decides what needs to happen.

The infrastructure provides controlled capabilities for making it happen.

---

# 20. n8n's Position

n8n is **not the core orchestration engine**.

It is treated as an optional internal automation/integration component.

```text
Agent Runtime
      │
      ├── Model Router
      ├── RAG
      └── Tool Runtime
               │
               └── n8n
                    │
             Optional Automation
             / Integrations
```

The core agent execution path must remain functional without making n8n the central brain of the system.

---

# 21. Prototype vs Target Architecture

The two-day prototype should implement a **thin vertical slice** of the target architecture.

### Target

```text
Full Sovereign AI Workbench
├── Multiple Models
├── Agent Runtime
├── RAG
├── Multimodal
├── Tools
├── Sandbox
├── Deliverables
├── Security
├── Audit
└── Network Monitoring
```

### Prototype

```text
Minimum End-to-End Flow
├── Frontend
├── API
├── Agent Runtime
├── Model Router
├── Required Tool(s)
├── Multimodal Input
├── RAG
├── DOCX Generation
├── Sandbox
└── Sovereignty Evidence
```

The prototype should prioritize **working end-to-end integration** over implementing every possible feature independently.

---

# 22. Architecture Decision Summary

| Decision       | Direction                                    |
| -------------- | -------------------------------------------- |
| Frontend       | Next.js / React                              |
| Backend API    | FastAPI                                      |
| Agent Runtime  | LangGraph                                    |
| Orchestration  | Custom                                       |
| Model Routing  | Custom Model Router                          |
| Model Serving  | To be finalized                              |
| Tool Execution | Custom Tool Runtime                          |
| Code Sandbox   | Docker                                       |
| Knowledge Base | Local RAG                                    |
| Database       | PostgreSQL                                   |
| Vector Search  | Local vector storage                         |
| Multimodal     | Local OCR + Vision pipeline                  |
| Deliverables   | DOCX / PPTX / XLSX / Code                    |
| Security       | Isolation + policies + firewall + monitoring |
| Auditability   | Application + security audit logs            |
| Automation     | n8n as supporting integration layer          |

---

# 23. Architecture Goal

The final system should feel like a **single AI workbench**, not a collection of unrelated services.

The user should be able to provide a complex industrial task and observe:

```text
Understand
    ↓
Plan
    ↓
Select
    ↓
Retrieve
    ↓
Act
    ↓
Execute
    ↓
Validate
    ↓
Iterate
    ↓
Deliver
    ↓
Audit
```

while the underlying system preserves the central principle of the project:

> **Confidential industrial AI work should remain within the organization's controlled environment.**
