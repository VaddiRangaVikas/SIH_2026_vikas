\# SIH26117 — Sovereign On-Premise Agentic AI Workbench



> \*\*Problem Statement ID:\*\* 26117

> \*\*Organization:\*\* Mangalore Refinery and Petrochemicals Limited (MRPL)

> \*\*Category:\*\* Software

> \*\*Theme:\*\* Smart Automation



\---



\# 1. Problem Statement



\## 1.1 Official Title



\*\*Sovereign On-Premise Agentic AI Workbench using Open-Weight Multimodal LLMs for Confidential Industrial Work\*\*



\---



\# 2. Executive Summary



Industrial organizations such as refineries, PSUs, defence-linked manufacturing units, and government offices handle large amounts of routine knowledge work that contains sensitive or confidential information.



Examples include:



\* Approval notes

\* Board presentations

\* Engineering calculations

\* Internal software/code

\* Scanned drawings

\* Inspection reports

\* Piping \& Instrumentation Diagrams (P\&IDs)

\* Financial information

\* Vendor negotiations

\* Unreleased designs

\* Internal correspondence

\* Confidential business strategies



This information cannot safely be submitted to public cloud AI assistants because doing so may expose confidential organizational data outside the organization's controlled environment.



As a result, employees are forced to perform many tasks manually. There is also a risk that employees may unofficially paste confidential material into public AI tools.



The problem asks for a \*\*self-hosted, sovereign AI workbench\*\* that brings the capabilities of modern agentic AI into the organization's own environment while keeping sensitive information inside the organization.



The system must run locally, support multiple open-weight models, automatically select appropriate models for different tasks, use local tools, perform multi-step agentic work, understand multimodal inputs, retrieve information from a local organizational knowledge base, generate real business deliverables, and provide visible proof that no external calls are made.



\---



\# 3. The Core Problem We Must Solve



The PS is \*\*not asking for a chatbot\*\*.



The intended system is an AI workbench capable of performing actual industrial knowledge work.



The core requirement can be expressed as:



```text

Confidential Industrial Data

&#x20;           ↓

&#x20;    Local AI Workbench

&#x20;           ↓

&#x20;Understand → Plan → Reason → Act → Verify → Deliver

&#x20;           ↓

&#x20;    Useful Business Output

&#x20;           ↓

&#x20;  Nothing leaves the premises

```



The system must therefore combine:



1\. \*\*Sovereign local deployment\*\*

2\. \*\*Multiple open-weight models\*\*

3\. \*\*Automatic model selection\*\*

4\. \*\*Agentic planning and execution\*\*

5\. \*\*Local tool usage\*\*

6\. \*\*Multimodal understanding\*\*

7\. \*\*Local organizational knowledge grounding\*\*

8\. \*\*Real deliverable generation\*\*

9\. \*\*Sandboxed code execution\*\*

10\. \*\*Visible proof of zero external calls\*\*



\---



\# 4. Requirement Classification



We divide the PS into four categories.



| Category                             | Meaning                                                                |

| ------------------------------------ | ---------------------------------------------------------------------- |

| \*\*Core Functional Requirement\*\*      | The system must provide this capability                                |

| \*\*Architecture Requirement\*\*         | The system must be designed to support this capability                 |

| \*\*Demonstration Requirement\*\*        | The capability must be visibly demonstrated                            |

| \*\*Sovereignty/Security Requirement\*\* | The system must preserve the local/confidential nature of the workload |



The distinction is important because a feature that merely exists in code but cannot be demonstrated may not provide sufficient evidence during evaluation.



\---



\# 5. Master Requirements Matrix



| ID  | Requirement                                | What the PS Means                                                                     | Our Implementation Direction                     | Evidence / Demo                                        |

| --- | ------------------------------------------ | ------------------------------------------------------------------------------------- | ------------------------------------------------ | ------------------------------------------------------ |

| R01 | \*\*On-premise deployment\*\*                  | The workbench must be deployable within the organization's own environment            | Containerized local deployment                   | Show complete application running locally              |

| R02 | \*\*Air-gapped operation\*\*                   | The system should operate without depending on external network services              | Local services + network restrictions            | Network monitor / firewall evidence                    |

| R03 | \*\*No data leaving premises\*\*               | Confidential information must remain inside the organization's controlled environment | Local processing and controlled network boundary | Show zero external calls                               |

| R04 | \*\*Open-weight models\*\*                     | The AI models must be open-weight rather than proprietary cloud-only models           | Pluggable local model-serving layer              | Show model registry / local inference                  |

| R05 | \*\*Multiple models\*\*                        | Backend must support more than one model simultaneously                               | Model registry + Model Router                    | Show at least two models                               |

| R06 | \*\*Automatic model selection\*\*              | Different tasks should be routed to suitable models                                   | Task-aware Model Router                          | Demonstrate different tasks selecting different models |

| R07 | \*\*Future model extensibility\*\*             | New models must be addable without redesigning the system                             | Model provider abstraction + registry            | Demonstrate model registration architecture            |

| R08 | \*\*Agentic behavior\*\*                       | Assistant must perform multi-step work rather than answer once                        | LangGraph Agent Runtime                          | Show execution graph                                   |

| R09 | \*\*Planning\*\*                               | Agent must break complex work into steps                                              | Planner node / planning stage                    | Show generated execution plan                          |

| R10 | \*\*Tool use\*\*                               | Agent must call local tools to perform work                                           | Tool Runtime + tool registry                     | Show tool calls during execution                       |

| R11 | \*\*Iteration\*\*                              | Agent must evaluate results and continue or adjust work                               | Stateful execution + validation/replanning       | Show multi-step execution                              |

| R12 | \*\*Local file operations\*\*                  | Agent should read and write local files                                               | File tools                                       | Demonstrate document processing                        |

| R13 | \*\*Sandboxed code execution\*\*               | Code must run in an isolated environment                                              | Docker-based sandbox                             | Run and verify a coding task                           |

| R14 | \*\*Spreadsheet work\*\*                       | Agent should be capable of working with spreadsheets                                  | Spreadsheet tool                                 | Show spreadsheet processing/generation                 |

| R15 | \*\*Internal document search\*\*               | Agent should search organizational documents locally                                  | Local RAG / knowledge connector                  | Demonstrate retrieval                                  |

| R16 | \*\*Multimodal input\*\*                       | System must process more than plain text                                              | Multimodal processing service                    | Upload image/scanned document                          |

| R17 | \*\*Scanned PDF understanding\*\*              | System must understand scanned documents                                              | OCR + vision pipeline                            | Demonstrate scanned inspection report                  |

| R18 | \*\*Handwritten notes\*\*                      | System should handle handwritten information                                          | On-device OCR / vision processing                | Multimodal demonstration where feasible                |

| R19 | \*\*Engineering drawings\*\*                   | System should process engineering drawings                                            | Vision/document pipeline                         | Demonstrate or show supported workflow                 |

| R20 | \*\*Photographs\*\*                            | System should process image inputs                                                    | Local vision processing                          | Image-based task                                       |

| R21 | \*\*On-device OCR\*\*                          | OCR must happen locally                                                               | Local OCR service                                | Show local OCR processing                              |

| R22 | \*\*Vision models\*\*                          | Visual understanding must happen locally                                              | Local vision model integration                   | Show image/scanned document analysis                   |

| R23 | \*\*Real deliverables\*\*                      | Output must be usable files, not only chat text                                       | Artifact generation service                      | Download/view generated artifact                       |

| R24 | \*\*Approval notes\*\*                         | System should generate business-ready approval notes                                  | DOCX generation                                  | Inspection report → approval note                      |

| R25 | \*\*PPT generation\*\*                         | System should generate presentations                                                  | PPTX generator                                   | Generate presentation artifact where feasible          |

| R26 | \*\*Word generation\*\*                        | System should generate Word documents                                                 | DOCX generator                                   | Generate approval note                                 |

| R27 | \*\*Excel generation\*\*                       | System should generate spreadsheets                                                   | XLSX generator                                   | Generate spreadsheet                                   |

| R28 | \*\*Working code generation\*\*                | System should produce usable code                                                     | Code generation + sandbox verification           | Generate and execute code                              |

| R29 | \*\*Calculations with steps\*\*                | System should provide calculations with visible reasoning/steps                       | Calculation tool + structured output             | Show calculation and result                            |

| R30 | \*\*Local knowledge base\*\*                   | AI must use organization's own knowledge                                              | Local RAG pipeline                               | Query organizational documents                         |

| R31 | \*\*Manuals/SOPs grounding\*\*                 | Responses should use organizational manuals and SOPs                                  | Document ingestion + retrieval                   | Show retrieved evidence                                |

| R32 | \*\*Past correspondence grounding\*\*          | System should use relevant previous organizational correspondence                     | Local knowledge repository                       | Demonstrate retrieval where sample data exists         |

| R33 | \*\*Single-machine demonstrability\*\*         | System should work on a workstation/server                                            | Containerized deployment                         | Run prototype on one machine                           |

| R34 | \*\*Mid-range GPU accommodation\*\*            | System must support smaller models when high-end hardware is unavailable              | Hardware-aware model configuration               | Demonstrate smaller model configuration                |

| R35 | \*\*Two task types / model selection proof\*\* | Model auto-selection must be demonstrated across at least two different task types    | Router selects different suitable models         | Perform two different tasks                            |

| R36 | \*\*End-to-end agentic demonstration\*\*       | At least one meaningful task must travel through the complete agent pipeline          | Inspection report workflow                       | Report → findings → approval note                      |

| R37 | \*\*Coding verification demonstration\*\*      | Code generation must be executed and verified in a sandbox                            | Tool Runtime + Sandbox                           | Show code execution and verification                   |

| R38 | \*\*Multimodal demonstration\*\*               | A visual/scanned input must actually be processed                                     | OCR/Vision pipeline                              | Show scanned/image analysis                            |

| R39 | \*\*Zero external-call proof\*\*               | Sovereignty must be demonstrated rather than merely claimed                           | Network monitoring + firewall + audit logs       | Show external calls = 0                                |

| R40 | \*\*Public/open demonstration data\*\*         | Proprietary data is not required for the demo                                         | Public/open document samples                     | Use sample scanned PDFs/P\&IDs                          |



\---



\# 6. Detailed Requirement Interpretation



\## R01-R03: Sovereignty and Deployment



\### Requirement



The system must be:



\* Self-hosted

\* On-premise

\* Air-gapped in the intended deployment

\* Designed so confidential information does not leave the premises



\### What this means technically



The application should not depend on:



\* Cloud-hosted AI APIs

\* External inference APIs

\* Public AI assistants

\* External document-processing services

\* External OCR APIs

\* External vector databases

\* External knowledge services



The intended production architecture should keep processing within the organization's controlled environment.



\### Required proof



The system should provide \*\*observable evidence\*\*, not simply a statement.



Evidence can include:



\* Network monitoring

\* Firewall rules

\* Connection logs

\* Application audit logs

\* Visible "external calls = 0" status



\*\*Critical principle:\*\*



> "Local" is an architectural claim.

> "Zero external calls" is demonstrable evidence.



The PS explicitly emphasizes the latter.



\---



\# 7. Multiple Open-Weight Models



\## Requirement



The backend must not be locked to a single model.



The system must:



\* Support multiple open-weight models

\* Use different models for different tasks

\* Automatically select an appropriate model

\* Allow new models to be added later



\### Required architecture



```text

&#x20;                   MODEL ROUTER

&#x20;                        │

&#x20;            ┌───────────┼───────────┐

&#x20;            ▼           ▼           ▼

&#x20;        Reasoning     Coding       Vision

&#x20;          Model        Model        Model

&#x20;            │           │           │

&#x20;            └───────────┼───────────┘

&#x20;                        ▼

&#x20;                Local Model Layer

```



The Agent Runtime should not directly depend on one specific model.



Instead:



```text

Agent

&#x20; ↓

Model Router

&#x20; ↓

Model Provider Interface

&#x20; ↓

Selected Model

```



This keeps the workbench model-agnostic.



\---



\# 8. Automatic Model Selection



This is a \*\*mandatory demonstration target\*\*, not merely an architectural idea.



The PS specifically expects the prototype to demonstrate automatic model selection across \*\*at least two different task types\*\*.



Example:



```text

Task 1:

"Analyze this inspection report."



&#x20;       ↓



&#x20;     Router



&#x20;       ↓



Multimodal / Reasoning Model

```



and:



```text

Task 2:

"Write and test a Python utility."



&#x20;       ↓



&#x20;     Router



&#x20;       ↓



Coding Model

```



The user should be able to see:



```text

Task

&#x20;↓

Detected task type

&#x20;↓

Selected model

&#x20;↓

Reason

```



\---



\# 9. Agentic Execution



The assistant must behave as an \*\*agent\*\*, not a single-turn chatbot.



The expected behavior is:



```text

User Request

&#x20;    ↓

Understand

&#x20;    ↓

Plan

&#x20;    ↓

Select Model

&#x20;    ↓

Select Tools

&#x20;    ↓

Execute

&#x20;    ↓

Observe

&#x20;    ↓

Validate

&#x20;    ↓

&#x20;┌───┴────┐

&#x20;│        │

Fail    Success

&#x20;│        │

&#x20;▼        ▼

Replan   Deliver

```



The agent must be able to:



\* Plan multi-step work

\* Call local tools

\* Observe results

\* Continue execution

\* Iterate when necessary

\* Produce a final deliverable



\---



\# 10. Local Tool Runtime



The PS expects the agent to use local tools.



The important tool categories include:



\### File Tools



```text

Read file

Write file

Inspect file

Transform file

```



\### Code Tools



```text

Generate code

Execute code

Verify result

```



\### Spreadsheet Tools



```text

Read spreadsheet

Analyze data

Create spreadsheet

```



\### Knowledge Tools



```text

Search internal documents

Retrieve relevant content

Ground response

```



\### Deliverable Tools



```text

Create DOCX

Create PPTX

Create XLSX

Create code artifact

```



These tools should be controlled by the Tool Runtime rather than allowing the agent to execute arbitrary host operations directly.



\---



\# 11. Sandboxed Code Execution



The PS explicitly expects a coding task to be \*\*run and verified in a sandbox\*\*.



Our architecture should therefore be:



```text

Agent

&#x20; ↓

Tool Runtime

&#x20; ↓

Policy Check

&#x20; ↓

Sandbox

&#x20; ↓

Code Execution

&#x20; ↓

Output

&#x20; ↓

Verification

&#x20; ↓

Agent

```



The sandbox should provide controlled execution boundaries.



For the prototype, Docker isolation is the preferred implementation direction.



\---



\# 12. Multimodal Processing



The system cannot be text-only.



The PS explicitly mentions:



\* Scanned PDFs

\* Handwritten notes

\* Engineering drawings

\* Photographs



The intended processing pipeline is:



```text

Image / Scanned PDF

&#x20;       ↓

Local Document Processor

&#x20;       ↓

Local OCR / Vision

&#x20;       ↓

Structured Information

&#x20;       ↓

Agent Runtime

&#x20;       ↓

Reasoning / Action

```



The PS specifically calls for \*\*on-device OCR and vision models\*\*.



\---



\# 13. Local Knowledge Base / RAG



The system must be capable of grounding itself in organizational information such as:



\* Manuals

\* SOPs

\* Past correspondence

\* Internal documents



The intended architecture is:



```text

Documents

&#x20;   ↓

Ingestion

&#x20;   ↓

Parsing / OCR

&#x20;   ↓

Chunking

&#x20;   ↓

Local Embeddings

&#x20;   ↓

Local Vector Store

&#x20;   ↓

Retriever

&#x20;   ↓

Agent

```



The knowledge base must remain local in the intended sovereign deployment.



\---



\# 14. Deliverable Generation



The PS specifically distinguishes between a chatbot response and a \*\*real deliverable\*\*.



Expected outputs include:



\* Approval notes

\* PPT files

\* Word files

\* Excel files

\* Working code

\* Calculations with steps



Therefore:



```text

Agent Result

&#x20;    ↓

Structured Artifact

&#x20;    ↓

Artifact Generator

&#x20;    ↓

Actual File

```



The generated file should be usable outside the chat interface.



\---



\# 15. Primary End-to-End Demonstration



The strongest official example in the PS is:



```text

SCANNED INSPECTION REPORT

&#x20;           ↓

&#x20;       Upload

&#x20;           ↓

&#x20;    OCR / Vision

&#x20;           ↓

&#x20;    Extract Findings

&#x20;           ↓

&#x20;     Agent Planning

&#x20;           ↓

&#x20;  Local Knowledge Search

&#x20;           ↓

&#x20;   Reasoning / Drafting

&#x20;           ↓

&#x20;    Approval Note

&#x20;           ↓

&#x20;         DOCX

&#x20;           ↓

&#x20;      Audit Trail

```



This one workflow can demonstrate multiple requirements simultaneously:



\* Multimodal processing

\* OCR

\* Agentic planning

\* Local document processing

\* Knowledge retrieval

\* Reasoning

\* Tool usage

\* Deliverable generation

\* Sovereignty

\* Auditability



\*\*Therefore, this should be the primary prototype flow unless we later identify a stronger demonstration.\*\*



\---



\# 16. Required Prototype Demonstrations



The PS explicitly identifies the following demonstrations.



\## Demo 1 — Automatic Model Selection



Demonstrate model selection across \*\*at least two different task types\*\*.



```text

Task A → Model A

Task B → Model B

```



\---



\## Demo 2 — Agentic Industrial Workflow



Demonstrate:



```text

Scanned Inspection Report

&#x20;       ↓

Key Findings

&#x20;       ↓

Approval Note

&#x20;       ↓

Word File

```



\---



\## Demo 3 — Coding



Demonstrate:



```text

Coding Request

&#x20;     ↓

Code Generation

&#x20;     ↓

Sandbox Execution

&#x20;     ↓

Verification

```



\---



\## Demo 4 — Multimodal



Demonstrate processing of:



\* Scanned document

\* Image

\* Engineering drawing

\* Or another supported visual input



\---



\## Demo 5 — Sovereignty



Demonstrate:



```text

External Calls: 0

```



using actual logs/network monitoring rather than only UI text.



The PS explicitly identifies this as the proof of the sovereign claim.



\---



\# 17. Data Requirements



The PS does \*\*not\*\* require proprietary industrial data for the demonstration.



It explicitly allows:



\* Open-source models

\* Publicly available document samples

\* Sample scanned PDFs

\* Public/open P\&ID datasets



Therefore:



```text

No proprietary MRPL data required

&#x20;               ↓

Public demonstration data

&#x20;               ↓

Local processing

&#x20;               ↓

Demonstrable workflow

```



This is important for both development speed and confidentiality.



\---



\# 18. Proposed System Components



Our implementation should be organized around these major components.



```text

┌─────────────────────────────────────────────────────┐

│                    FRONTEND                         │

│             Sovereign AI Workbench UI               │

└──────────────────────┬──────────────────────────────┘

&#x20;                      │

&#x20;                      ▼

┌─────────────────────────────────────────────────────┐

│                    API LAYER                         │

│                    FastAPI                           │

└──────────────────────┬──────────────────────────────┘

&#x20;                      │

&#x20;                      ▼

┌─────────────────────────────────────────────────────┐

│              CUSTOM ORCHESTRATION                   │

└──────────────────────┬──────────────────────────────┘

&#x20;                      │

&#x20;                      ▼

┌─────────────────────────────────────────────────────┐

│                 AGENT RUNTIME                       │

│                   LangGraph                         │

│                                                     │

│ Planning • State • Reasoning • Iteration            │

└───────┬─────────────────┬──────────────────┬────────┘

&#x20;       │                 │                  │

&#x20;       ▼                 ▼                  ▼

┌──────────────┐   ┌──────────────┐   ┌──────────────┐

│ Model Router │   │     RAG      │   │ Tool Runtime │

└──────────────┘   └──────────────┘   └──────┬───────┘

&#x20;                                            │

&#x20;                         ┌──────────────────┼─────────────┐

&#x20;                         ▼                  ▼             ▼

&#x20;                      Files              Code       Deliverables

&#x20;                                          │

&#x20;                                          ▼

&#x20;                                      SANDBOX



&#x20;       ┌─────────────────────────────────────────┐

&#x20;       │         MULTIMODAL SERVICES             │

&#x20;       │      OCR • Vision • Documents           │

&#x20;       └─────────────────────────────────────────┘



&#x20;       ┌─────────────────────────────────────────┐

&#x20;       │          SECURITY LAYER                 │

&#x20;       │ Docker • Firewall • Network Monitor     │

&#x20;       │ Audit Logs • Access Policies            │

&#x20;       └─────────────────────────────────────────┘



&#x20;       ┌─────────────────────────────────────────┐

&#x20;       │             DATA LAYER                  │

&#x20;       │ PostgreSQL • Vector Store • Files       │

&#x20;       └─────────────────────────────────────────┘

```



\---



\# 19. Non-Negotiable Requirements



The following should be treated as \*\*red-line requirements\*\* for the prototype and final solution:



\### 🔴 Sovereignty



The intended deployment must be local/on-premise.



\### 🔴 Multiple Models



The architecture cannot be hardcoded around one model.



\### 🔴 Automatic Model Routing



At least two task types must demonstrate automatic model selection.



\### 🔴 Agentic Execution



The system must plan and execute multi-step work.



\### 🔴 Tool Use



The agent must actually invoke tools.



\### 🔴 Sandboxed Coding



Generated code must be executed and verified inside a sandbox.



\### 🔴 Multimodal Processing



At least one real visual/scanned input must be processed.



\### 🔴 Deliverable Generation



The system must produce a real file, not only text.



\### 🔴 Local Knowledge



The architecture must support grounding against local organizational documents.



\### 🔴 Zero External Calls



The system must provide visible evidence that external calls are not being made.



These requirements come directly from the PS's description and expected solution.



\---



\# 20. What Is NOT the Goal



We should explicitly avoid turning the project into:



\* A normal chatbot

\* A ChatGPT clone

\* A single-model wrapper

\* An n8n-only workflow

\* A cloud AI API aggregator

\* A simple RAG chatbot

\* A document summarizer with a fancy UI

\* A collection of disconnected AI demos



The intended product is a \*\*unified agentic workbench\*\*.



The individual capabilities must work together.



\---



\# 21. Our Architectural Principle



The system should follow:



```text

&#x20;                USER

&#x20;                  ↓

&#x20;             WORKBENCH

&#x20;                  ↓

&#x20;            ORCHESTRATOR

&#x20;                  ↓

&#x20;            AGENT RUNTIME

&#x20;                  ↓

&#x20;       ┌──────────┼───────────┐

&#x20;       ↓          ↓           ↓

&#x20;     MODEL       TOOLS       RAG

&#x20;     ROUTER       │            │

&#x20;       │          │            │

&#x20;       │       SANDBOX        KB

&#x20;       │          │            │

&#x20;       └──────────┼────────────┘

&#x20;                  ↓

&#x20;             DELIVERABLE

&#x20;                  ↓

&#x20;               AUDIT

&#x20;                  ↓

&#x20;         SOVEREIGN RESULT

```



The AI model is a component of the workbench.



\*\*It is not the workbench itself.\*\*



\---



\# 22. Definition of Success



The prototype should be considered successful if a judge can observe the following sequence:



> \*\*I give the system a real industrial-style task.\*\*



↓



> \*\*The system understands the task and creates a plan.\*\*



↓



> \*\*It automatically selects an appropriate local model.\*\*



↓



> \*\*It reads/processes the required documents or images.\*\*



↓



> \*\*It retrieves relevant local knowledge when necessary.\*\*



↓



> \*\*It invokes tools.\*\*



↓



> \*\*It executes code safely when required.\*\*



↓



> \*\*It iterates/validates the result.\*\*



↓



> \*\*It produces a real business deliverable.\*\*



↓



> \*\*I can see evidence that the confidential information never left the controlled environment.\*\*



If we can demonstrate that chain reliably, we are demonstrating the \*\*core intent of SIH26117\*\*, rather than merely presenting an AI interface.



\---



\# 23. Implementation Philosophy



\### Build the smallest system that proves the largest number of PS requirements.



We have only a limited development window.



Therefore:



```text

BAD STRATEGY



Build 25 features

&#x20;    ↓

Nothing works end-to-end

```



Instead:



```text

GOOD STRATEGY



Build 1 complete workflow

&#x20;    ↓

Prove 8–10 requirements

&#x20;    ↓

Add supporting capabilities

```



Our primary vertical slice should therefore be:



```text

Inspection Report

&#x20;     ↓

Multimodal Understanding

&#x20;     ↓

Agent Planning

&#x20;     ↓

Local Knowledge Retrieval

&#x20;     ↓

Reasoning

&#x20;     ↓

Tool Execution

&#x20;     ↓

Approval Note

&#x20;     ↓

DOCX

&#x20;     ↓

Audit / Sovereignty Proof

```



\---



\# 24. Final Requirement Hierarchy



The entire PS can be reduced to five layers:



\## Layer 1 — Sovereignty



\*\*Keep confidential work inside the organization's controlled environment.\*\*



\## Layer 2 — Intelligence



\*\*Use multiple open-weight models and select the appropriate model for each task.\*\*



\## Layer 3 — Agency



\*\*Plan, reason, use tools, execute, observe, and iterate.\*\*



\## Layer 4 — Multimodal Work



\*\*Understand documents, images, scans, handwriting, and engineering material.\*\*



\## Layer 5 — Business Output



\*\*Turn the reasoning into actual deliverables such as Word, PowerPoint, Excel, code, and calculations.\*\*



The system is successful only when these layers operate together.



\---



\# 25. One-Sentence Product Definition



> \*\*SIH26117 asks us to build a sovereign, self-hosted AI workbench that can perform confidential industrial knowledge work end-to-end using open-weight multimodal models, local tools, local organizational knowledge, and real deliverable generation, while providing demonstrable proof that no external calls are made.\*\*



That sentence should remain the \*\*north star for the entire project\*\*.



