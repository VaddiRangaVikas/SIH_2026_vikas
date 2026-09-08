\# SIH26117 — System Architecture



\## 1. Purpose



This document defines the proposed technical architecture for \*\*SIH26117: Sovereign On-Premise Agentic AI Workbench using Open-Weight Multimodal LLMs for Confidential Industrial Work\*\*.



The architecture is designed around the core requirements of the Problem Statement:



\* On-premise and sovereign operation

\* Multiple open-weight models

\* Automatic task-based model selection

\* Agentic planning, reasoning, tool use, and iteration

\* Multimodal document and image understanding

\* Local organizational knowledge retrieval

\* Sandboxed code execution

\* Real deliverable generation

\* Auditability and visible proof of no external calls



The architecture is intentionally \*\*modular and model-agnostic\*\*, so individual components can be developed, tested, and replaced independently.



\---



\# 2. High-Level Architecture



```text

&#x20;                             ┌──────────────────────┐

&#x20;                             │        USER          │

&#x20;                             └──────────┬───────────┘

&#x20;                                        │

&#x20;                                        ▼

&#x20;                             ┌──────────────────────┐

&#x20;                             │    WEB WORKBENCH     │

&#x20;                             │      Frontend        │

&#x20;                             └──────────┬───────────┘

&#x20;                                        │

&#x20;                                        │ HTTP / WebSocket

&#x20;                                        ▼

&#x20;                             ┌──────────────────────┐

&#x20;                             │       API LAYER      │

&#x20;                             │       FastAPI        │

&#x20;                             └──────────┬───────────┘

&#x20;                                        │

&#x20;                                        ▼

&#x20;                       ┌─────────────────────────────────┐

&#x20;                       │      CUSTOM ORCHESTRATION       │

&#x20;                       │                                 │

&#x20;                       │ Task lifecycle \& coordination   │

&#x20;                       └───────────────┬─────────────────┘

&#x20;                                       │

&#x20;                                       ▼

&#x20;                       ┌─────────────────────────────────┐

&#x20;                       │        AGENT RUNTIME             │

&#x20;                       │            LangGraph             │

&#x20;                       │                                 │

&#x20;                       │ Planning • State • Reasoning     │

&#x20;                       │ Tool Selection • Iteration       │

&#x20;                       └───────┬─────────┬─────────┬─────┘

&#x20;                               │         │         │

&#x20;               ┌───────────────┘         │         └───────────────┐

&#x20;               ▼                         ▼                         ▼

&#x20;      ┌────────────────┐       ┌────────────────┐       ┌────────────────┐

&#x20;      │  MODEL ROUTER  │       │      RAG       │       │  TOOL RUNTIME  │

&#x20;      │                │       │                │       │                │

&#x20;      │ Task → Model   │       │ Local Knowledge│       │ Tool Selection │

&#x20;      │ Model Registry │       │ Retrieval      │       │ Execution      │

&#x20;      └───────┬────────┘       └───────┬────────┘       └───────┬────────┘

&#x20;              │                        │                        │

&#x20;              ▼                        ▼              ┌─────────┼──────────┐

&#x20;      ┌────────────────┐       ┌────────────────┐     ▼         ▼          ▼

&#x20;      │ Local Model    │       │ Vector Store   │   Files     Code     Artifacts

&#x20;      │ Infrastructure │       │ + Documents    │              │

&#x20;      └────────────────┘       └────────────────┘              ▼

&#x20;                                                       ┌──────────────┐

&#x20;                                                       │   SANDBOX    │

&#x20;                                                       │    Docker    │

&#x20;                                                       └──────────────┘





&#x20;       ┌─────────────────────────────────────────────────────────────┐

&#x20;       │                  MULTIMODAL SERVICES                        │

&#x20;       │                                                             │

&#x20;       │       OCR • Vision • Scanned Documents • Images            │

&#x20;       └────────────────────────────┬────────────────────────────────┘

&#x20;                                    │

&#x20;                                    ▼

&#x20;                             Agent / RAG Layer





&#x20;       ┌─────────────────────────────────────────────────────────────┐

&#x20;       │                    SECURITY LAYER                           │

&#x20;       │                                                             │

&#x20;       │  Network Controls • Firewall • Monitoring • Audit Logging  │

&#x20;       │  Access Policies • Sandbox Isolation                       │

&#x20;       └─────────────────────────────────────────────────────────────┘





&#x20;       ┌─────────────────────────────────────────────────────────────┐

&#x20;       │                       DATA LAYER                             │

&#x20;       │                                                             │

&#x20;       │       PostgreSQL • Vector Data • Files • Artifacts          │

&#x20;       └─────────────────────────────────────────────────────────────┘

```



\---



\# 3. Architectural Principles



\## 3.1 Sovereignty First



The intended production deployment must keep confidential industrial data within the organization's controlled environment.



The architecture therefore avoids making external AI services a dependency.



The system should be capable of operating using locally deployed services and models.



\---



\## 3.2 Model Agnostic



The Agent Runtime must not be tightly coupled to one specific AI model or inference engine.



Instead:



```text

Agent Runtime

&#x20;     │

&#x20;     ▼

&#x20;Model Router

&#x20;     │

&#x20;     ▼

Model Provider Interface

&#x20;     │

&#x20;     ├── Model A

&#x20;     ├── Model B

&#x20;     ├── Model C

&#x20;     └── Future Models

```



This allows new open-weight models to be introduced without redesigning the agent architecture.



\---



\## 3.3 Agent-Centric



The system is not designed as a single-turn chatbot.



The Agent Runtime is responsible for:



\* Understanding the task

\* Creating a plan

\* Maintaining execution state

\* Selecting tools

\* Executing actions

\* Observing results

\* Validating results

\* Iterating or replanning

\* Producing the final result



\---



\## 3.4 Local Tool Execution



Tools are accessed through a controlled Tool Runtime.



The agent should not directly receive unrestricted access to the host system.



Instead:



```text

Agent

&#x20; ↓

Tool Runtime

&#x20; ↓

Policy / Permission Check

&#x20; ↓

Tool

&#x20; ↓

Execution

&#x20; ↓

Result

&#x20; ↓

Agent

```



\---



\## 3.5 Security by Boundary



Security is treated as an architectural layer rather than an afterthought.



Sensitive operations should pass through controlled boundaries involving:



\* Tool permissions

\* Sandbox isolation

\* Network restrictions

\* Audit logging

\* Resource controls

\* Access policies



\---



\# 4. Major Components



\## 4.1 Web Workbench



\### Responsibility



The frontend is the primary interface through which users interact with the AI workbench.



\### Core responsibilities



\* Submit tasks

\* Upload files

\* View task status

\* View execution progress

\* Display agent plans

\* Display model selection

\* Display tool activity

\* View generated artifacts

\* Display security/sovereignty status

\* Access task history



\### Proposed technology



\*\*Next.js + React + TypeScript\*\*



\---



\# 5. API Layer



\## Responsibility



The API Layer provides the controlled interface between the frontend and the backend system.



\### Proposed technology



\*\*FastAPI\*\*



\### Responsibilities



\* Authentication/session handling

\* Task creation

\* File uploads

\* Task status

\* Streaming execution events

\* Artifact access

\* System status

\* Security status

\* Communication with the orchestration layer



The frontend should communicate with the backend through the API rather than directly accessing internal components.



\---



\# 6. Custom Orchestration Layer



\## Responsibility



The orchestration layer coordinates the overall lifecycle of a task.



It acts as the bridge between:



```text

API

&#x20;↓

Agent Runtime

&#x20;↓

Models / Tools / RAG

&#x20;↓

Final Result

```



\### Responsibilities



\* Create and manage task executions

\* Initialize agent state

\* Coordinate services

\* Manage execution lifecycle

\* Handle errors

\* Track execution events

\* Coordinate artifact generation

\* Persist task information



The orchestration layer should remain independent from the frontend.



\---



\# 7. Agent Runtime



\## Proposed technology



\*\*LangGraph\*\*



The Agent Runtime is the central intelligence/control layer of the system.



\### Responsibilities



\### Planning



Break a complex user request into executable steps.



\### Reasoning



Determine what information and actions are required.



\### State Management



Maintain the state of an ongoing multi-step task.



\### Tool Selection



Determine which tools are required.



\### Model Selection



Request an appropriate model from the Model Router.



\### Iteration



Evaluate intermediate results and continue, correct, or replan when required.



\### Completion



Determine when the task has produced a satisfactory result.



\---



\# 8. Model Router



The Model Router provides a model-agnostic interface between the Agent Runtime and the model-serving infrastructure.



```text

&#x20;                Agent Runtime

&#x20;                      │

&#x20;                      ▼

&#x20;               ┌──────────────┐

&#x20;               │ Model Router │

&#x20;               └──────┬───────┘

&#x20;                      │

&#x20;             Task / Capability

&#x20;                      │

&#x20;         ┌────────────┼────────────┐

&#x20;         ▼            ▼            ▼

&#x20;     Reasoning      Coding       Vision

&#x20;       Model         Model        Model

```



\### Responsibilities



\* Maintain model registry

\* Understand model capabilities

\* Classify task requirements

\* Select an appropriate model

\* Route inference requests

\* Support multiple models

\* Allow future models to be added



\### Important design decision



The exact model-serving technology and hardware deployment will be finalized separately.



The rest of the system must not depend directly on that decision.



\---



\# 9. Tool Runtime



The Tool Runtime provides controlled access to capabilities that allow the agent to perform actual work.



\### Initial tool categories



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



\---



\# 10. Sandbox



Code execution must not occur directly on the host environment.



Proposed approach:



\*\*Docker-based sandbox\*\*



```text

Generated Code

&#x20;     ↓

Tool Runtime

&#x20;     ↓

Policy Check

&#x20;     ↓

Docker Sandbox

&#x20;     ↓

Execution

&#x20;     ↓

Output / Errors

&#x20;     ↓

Verification

```



The sandbox should eventually enforce appropriate:



\* Resource limits

\* Execution limits

\* File access restrictions

\* Network restrictions

\* Process isolation



The exact security policies will be defined separately.



\---



\# 11. RAG / Local Knowledge Base



The system must be capable of grounding its work in organizational knowledge such as:



\* Manuals

\* SOPs

\* Past correspondence

\* Internal documents



Proposed pipeline:



```text

Document

&#x20;  ↓

Ingestion

&#x20;  ↓

Parsing / OCR

&#x20;  ↓

Chunking

&#x20;  ↓

Local Embedding

&#x20;  ↓

Vector Store

&#x20;  ↓

Retrieval

&#x20;  ↓

Agent

```



The knowledge base should remain inside the organization's controlled environment in the intended deployment.



\---



\# 12. Multimodal Processing Layer



The system must support inputs beyond plain text.



Potential input types include:



\* Scanned PDFs

\* Handwritten notes

\* Engineering drawings

\* Photographs

\* Other images



Proposed pipeline:



```text

Image / Scanned Document

&#x20;         ↓

&#x20;   Document Processor

&#x20;         ↓

&#x20;     OCR / Vision

&#x20;         ↓

&#x20;Structured Information

&#x20;         ↓

&#x20;     Agent Runtime

```



The exact OCR and vision technologies will be selected according to available hardware and model compatibility.



\---



\# 13. Deliverable Generation



The system should convert agent results into actual usable artifacts.



```text

&#x20;                   Agent

&#x20;                     │

&#x20;                     ▼

&#x20;            Structured Result

&#x20;                     │

&#x20;                     ▼

&#x20;             Artifact Generator

&#x20;                     │

&#x20;      ┌──────────────┼──────────────┐

&#x20;      ▼              ▼              ▼

&#x20;    DOCX            PPTX           XLSX

&#x20;      │

&#x20;      └──────────── Code / Reports

```



Priority for the initial prototype should be determined based on the selected demonstration workflow.



The official PS's inspection-report → approval-note example makes \*\*DOCX generation\*\* a particularly strong candidate for the primary demonstration.



\---



\# 14. Data Layer



The application requires persistent storage for:



\### PostgreSQL



Potentially stores:



\* Users

\* Tasks

\* Execution states

\* Tool calls

\* Model selections

\* Audit events

\* Artifact metadata



\### Vector Store



Stores embeddings and retrieval information for the local knowledge base.



\### File Storage



Stores:



\* Uploaded documents

\* Processed files

\* Generated artifacts

\* Temporary task files



All storage should be designed for local deployment.



\---



\# 15. Security and Sovereignty Layer



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



\### Main objectives



1\. Prevent unauthorized tool execution.

2\. Isolate code execution.

3\. Restrict unwanted network communication.

4\. Record important system activity.

5\. Provide evidence of system behavior.

6\. Demonstrate that external calls are not occurring.



\---



\# 16. End-to-End Task Flow



The general task execution flow is:



```text

USER

&#x20;│

&#x20;▼

Frontend

&#x20;│

&#x20;▼

API

&#x20;│

&#x20;▼

Orchestrator

&#x20;│

&#x20;▼

Agent Runtime

&#x20;│

&#x20;├──────────────► Model Router

&#x20;│                     │

&#x20;│                     ▼

&#x20;│                  Model

&#x20;│                     │

&#x20;│◄────────────────────┘

&#x20;│

&#x20;├──────────────► RAG

&#x20;│                     │

&#x20;│                     ▼

&#x20;│               Local Knowledge

&#x20;│

&#x20;├──────────────► Tool Runtime

&#x20;│                     │

&#x20;│              ┌──────┼──────┐

&#x20;│              ▼      ▼      ▼

&#x20;│            Files   Code  Artifact

&#x20;│                     │

&#x20;│                  Sandbox

&#x20;│

&#x20;▼

Validation / Iteration

&#x20;│

&#x20;▼

Final Result

&#x20;│

&#x20;▼

Artifact

&#x20;│

&#x20;▼

Audit Log

&#x20;│

&#x20;▼

Frontend

```



\---



\# 17. Primary Demonstration Architecture



The primary prototype should aim to demonstrate as many PS requirements as possible through one coherent workflow.



\### Proposed workflow



```text

SCANNED INSPECTION REPORT

&#x20;           │

&#x20;           ▼

&#x20;        Upload

&#x20;           │

&#x20;           ▼

&#x20;   Multimodal Processing

&#x20;      OCR / Vision

&#x20;           │

&#x20;           ▼

&#x20;   Extract Key Findings

&#x20;           │

&#x20;           ▼

&#x20;      Agent Planning

&#x20;           │

&#x20;           ▼

&#x20;   Local Knowledge Search

&#x20;           │

&#x20;           ▼

&#x20;       Reasoning

&#x20;           │

&#x20;           ▼

&#x20;   Draft Approval Note

&#x20;           │

&#x20;           ▼

&#x20;     DOCX Generation

&#x20;           │

&#x20;           ▼

&#x20;       Validation

&#x20;           │

&#x20;           ▼

&#x20;     Audit / Logging

&#x20;           │

&#x20;           ▼

&#x20;    Final Deliverable

```



This workflow directly aligns with the official PS example of reading a scanned inspection report, extracting key findings, and drafting an approval note as a Word document.



\---



\# 18. Secondary Demonstration Flows



\## Coding



```text

User Coding Request

&#x20;       ↓

Agent Planning

&#x20;       ↓

Code Generation

&#x20;       ↓

Tool Runtime

&#x20;       ↓

Docker Sandbox

&#x20;       ↓

Execution

&#x20;       ↓

Verification

&#x20;       ↓

Result

```



The PS explicitly expects a coding task to be run and verified in a sandbox.



\---



\## Automatic Model Selection



```text

Task A

&#x20; ↓

Task Analysis

&#x20; ↓

Model Router

&#x20; ↓

Model A





Task B

&#x20; ↓

Task Analysis

&#x20; ↓

Model Router

&#x20; ↓

Model B

```



The demonstration should make the routing decision visible to the user.



\---



\## Sovereignty Proof



```text

Application Activity

&#x20;      │

&#x20;      ├── Model Calls

&#x20;      ├── Tool Calls

&#x20;      ├── File Operations

&#x20;      └── Network Activity

&#x20;                   │

&#x20;                   ▼

&#x20;             Audit Layer

&#x20;                   │

&#x20;                   ▼

&#x20;         Sovereignty Monitor

&#x20;                   │

&#x20;                   ▼

&#x20;        External Calls = 0

```



The PS specifically states that logs or a visible network monitor should demonstrate that no external calls are made.



\---



\# 19. Component Dependency Model



The dependency direction should remain controlled:



```text

Frontend

&#x20;  ↓

API

&#x20;  ↓

Orchestrator

&#x20;  ↓

Agent Runtime

&#x20;  ↓

┌───────────────┬───────────────┬───────────────┐

│               │               │

▼               ▼               ▼

Model Router    RAG        Tool Runtime

&#x20;                               │

&#x20;                               ▼

&#x20;                            Sandbox

```



Supporting infrastructure such as the database, storage, security, logging, and monitoring services should be consumed through clearly defined interfaces.



\### Important rule



\*\*Lower-level infrastructure must not control the Agent Runtime.\*\*



The agent decides what needs to happen.



The infrastructure provides controlled capabilities for making it happen.



\---



\# 20. n8n's Position



n8n is \*\*not the core orchestration engine\*\*.



It is treated as an optional internal automation/integration component.



```text

Agent Runtime

&#x20;     │

&#x20;     ├── Model Router

&#x20;     ├── RAG

&#x20;     └── Tool Runtime

&#x20;              │

&#x20;              └── n8n

&#x20;                   │

&#x20;            Optional Automation

&#x20;            / Integrations

```



The core agent execution path must remain functional without making n8n the central brain of the system.



\---



\# 21. Prototype vs Target Architecture



The two-day prototype should implement a \*\*thin vertical slice\*\* of the target architecture.



\### Target



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



\### Prototype



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



The prototype should prioritize \*\*working end-to-end integration\*\* over implementing every possible feature independently.



\---



\# 22. Architecture Decision Summary



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



\---



\# 23. Architecture Goal



The final system should feel like a \*\*single AI workbench\*\*, not a collection of unrelated services.



The user should be able to provide a complex industrial task and observe:



```text

Understand

&#x20;   ↓

Plan

&#x20;   ↓

Select

&#x20;   ↓

Retrieve

&#x20;   ↓

Act

&#x20;   ↓

Execute

&#x20;   ↓

Validate

&#x20;   ↓

Iterate

&#x20;   ↓

Deliver

&#x20;   ↓

Audit

```



while the underlying system preserves the central principle of the project:



> \*\*Confidential industrial AI work should remain within the organization's controlled environment.\*\*



