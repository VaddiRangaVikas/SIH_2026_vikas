# SIH 2026

# Sovereign On-Premise Agentic AI Workbench

## Backend Architecture & Implementation Specification

**Project:** SIH 2026
**Problem Statement:** 26117
**Architecture:** Sovereign, On-Premise, Distributed AI Inference
**Primary Backend Language:** Python
**API Framework:** FastAPI
**Database:** PostgreSQL

---

# 1. Purpose

This document defines the backend architecture, technology stack, project structure, responsibilities, and implementation boundaries for the SIH 2026 Sovereign On-Premise Agentic AI Workbench.

The backend is responsible for:

* Exposing APIs to the frontend
* Managing users and workspaces
* Managing conversations and messages
* Managing agents
* Managing knowledge bases and documents
* Managing AI model workers
* Routing inference requests to appropriate local models
* Supporting RAG
* Managing tools and agent execution
* Maintaining audit logs
* Maintaining system state and metadata

The backend must be designed so that AI inference remains inside the organization's trusted infrastructure.

---

# 2. Core Architectural Principle

The system follows a separation between the **control plane** and the **AI inference plane**.

```text
                    USER
                      │
                      ▼
                  FRONTEND
                      │
                    HTTP
                      │
                      ▼
             ┌─────────────────┐
             │  FASTAPI        │
             │  BACKEND        │
             │                 │
             │  API Layer      │
             │  Auth           │
             │  Agents         │
             │  RAG            │
             │  Model Gateway  │
             │  Audit          │
             └───────┬─────────┘
                     │
          ┌──────────┴───────────┐
          │                      │
          ▼                      ▼
   ┌─────────────┐       ┌─────────────────┐
   │ PostgreSQL  │       │ Model Workers   │
   │             │       │                 │
   │ Application │       │ Local AI Models │
   │ State       │       │                 │
   │ Metadata    │       │ LLM / VLM / etc │
   │ Vectors     │       │                 │
   └─────────────┘       └─────────────────┘
```

The central backend does not need to contain the actual model weights.

Instead, models are exposed through local **Model Worker services**.

---

# 3. Technology Stack

## 3.1 Python

Python is the primary backend programming language.

### Responsibilities

* API implementation
* Business logic
* Agent orchestration
* RAG pipeline
* Model routing
* Document processing
* Integration with AI runtimes

---

## 3.2 FastAPI

FastAPI is the primary backend API framework.

### Responsibilities

* REST API endpoints
* Request handling
* Response serialization
* Dependency injection
* API validation
* OpenAPI documentation

FastAPI should remain focused on HTTP/API concerns.

Business logic should live in service modules.

---

## 3.3 PostgreSQL

PostgreSQL is the primary relational database.

### Responsibilities

* Users
* Roles
* Workspaces
* Agents
* Conversations
* Messages
* Models
* Model workers
* Documents
* Knowledge bases
* Agent runs
* Tool executions
* Audit logs
* System metadata

---

## 3.4 SQLAlchemy

SQLAlchemy is the database abstraction layer.

### Responsibilities

* Database connections
* ORM models
* Queries
* Transactions
* Session management

The backend should use modern SQLAlchemy 2.x patterns.

---

## 3.5 Alembic

Alembic manages database migrations.

### Responsibilities

* Schema versioning
* Database structure changes
* Reproducible database setup
* Migration history

Every intentional database schema change should be represented through a migration.

---

## 3.6 Pydantic

Pydantic is used for:

* API request validation
* API response validation
* Configuration validation
* Data serialization

API schemas should be separate from SQLAlchemy database models.

---

## 3.7 pgvector

PostgreSQL may use the `pgvector` extension for vector storage and similarity search.

It will support:

* Document embeddings
* Semantic retrieval
* RAG

The embedding dimension must match the selected embedding model.

---

# 4. Backend Directory Structure

The backend should follow this structure:

```text
backend/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── health.py
│   │   ├── auth.py
│   │   ├── users.py
│   │   ├── workspaces.py
│   │   ├── chat.py
│   │   ├── agents.py
│   │   ├── documents.py
│   │   ├── knowledge_bases.py
│   │   ├── models.py
│   │   ├── workers.py
│   │   └── tools.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── security.py
│   │   ├── logging.py
│   │   └── exceptions.py
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   ├── base.py
│   │   └── repositories/
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── role.py
│   │   ├── workspace.py
│   │   ├── conversation.py
│   │   ├── message.py
│   │   ├── agent.py
│   │   ├── model.py
│   │   ├── model_worker.py
│   │   ├── knowledge_base.py
│   │   ├── document.py
│   │   ├── document_chunk.py
│   │   ├── tool.py
│   │   ├── agent_run.py
│   │   ├── tool_execution.py
│   │   ├── model_inference.py
│   │   └── audit_log.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── user.py
│   │   ├── workspace.py
│   │   ├── chat.py
│   │   ├── agent.py
│   │   ├── model.py
│   │   ├── worker.py
│   │   ├── document.py
│   │   └── common.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   ├── chat_service.py
│   │   ├── agent_service.py
│   │   ├── model_router.py
│   │   ├── inference_service.py
│   │   ├── worker_service.py
│   │   ├── document_service.py
│   │   ├── rag_service.py
│   │   ├── tool_service.py
│   │   └── audit_service.py
│   │
│   └── utils/
│       ├── __init__.py
│       ├── hashing.py
│       └── helpers.py
│
├── migrations/
│   ├── versions/
│   ├── env.py
│   └── alembic.ini
│
├── tests/
│   ├── __init__.py
│   ├── test_health.py
│   ├── test_auth.py
│   ├── test_chat.py
│   ├── test_models.py
│   └── test_documents.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

The structure may evolve during development, but the architectural separation should remain.

---

# 5. Directory Responsibilities

## `app/main.py`

Application entry point.

Responsible for:

* Creating FastAPI application
* Registering routers
* Startup/shutdown handling
* Global middleware
* Exception handlers

Do not put business logic here.

---

## `app/api/`

Contains HTTP API routes.

Example:

```text
POST /api/auth/login
GET  /api/conversations
POST /api/chat
GET  /api/models
GET  /api/workers
POST /api/documents
```

Routes should:

1. Receive request
2. Validate request
3. Call service
4. Return response

Routes should not contain large business workflows.

---

## `app/core/`

Contains application-wide infrastructure.

Examples:

* Configuration
* Authentication/security
* Logging
* Exceptions
* Application constants

---

## `app/db/`

Contains database infrastructure.

Responsibilities:

* SQLAlchemy engine
* Sessions
* Base class
* Repository abstractions

Database connection logic should not be scattered across API files.

---

## `app/models/`

Contains SQLAlchemy database models.

These represent database tables and relationships.

Example:

```text
User
Workspace
Conversation
Message
Agent
Model
ModelWorker
Document
```

---

## `app/schemas/`

Contains Pydantic models.

These represent API data contracts.

Example:

```text
ChatRequest
ChatResponse
LoginRequest
LoginResponse
ModelResponse
WorkerResponse
DocumentResponse
```

SQLAlchemy models and Pydantic schemas should remain separate.

---

## `app/services/`

Contains business logic.

This is one of the most important directories.

Examples:

```text
chat_service.py
agent_service.py
model_router.py
rag_service.py
inference_service.py
worker_service.py
```

The service layer is responsible for coordinating system behavior.

---

## `app/utils/`

Contains small reusable utility functions.

Do not turn this into a dumping ground for business logic.

---

# 6. Core Backend Components

The backend will eventually contain the following logical components.

```text
                    FASTAPI BACKEND
                           │
       ┌───────────────────┼────────────────────┐
       │                   │                    │
       ▼                   ▼                    ▼
   API Layer          Service Layer        Database Layer
       │                   │                    │
       │          ┌────────┼────────┐           │
       │          ▼        ▼        ▼           │
       │       Agents     RAG     Models        │
       │                   │                    │
       │                   ▼                    │
       │             Model Router               │
       │                   │                    │
       └───────────────────┼────────────────────┘
                           │
                           ▼
                    Model Workers
```

---

# 7. Model Worker Architecture

Model workers are independent services running on machines inside the trusted network.

A worker can run:

* General LLM
* Vision-language model
* Coding model
* Specialized industrial model
* Embedding model

Example:

```text
Worker A
├── Host: Laptop / GPU Server
├── Model: General LLM
└── Capabilities:
    ├── text
    └── reasoning

Worker B
├── Host: Laptop / GPU Server
├── Model: Vision LLM
└── Capabilities:
    ├── image
    └── document analysis
```

---

# 8. Model Worker API Contract

Every worker should eventually expose a common API.

## Health

```http
GET /health
```

Example response:

```json
{
  "status": "online"
}
```

---

## Metadata

```http
GET /metadata
```

Example:

```json
{
  "worker_id": "worker-01",
  "model": "qwen-local",
  "model_type": "llm",
  "capabilities": [
    "text",
    "reasoning"
  ]
}
```

---

## Inference

```http
POST /generate
```

Example request:

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Explain this procedure."
    }
  ],
  "temperature": 0.2
}
```

Example response:

```json
{
  "response": "...",
  "model": "qwen-local",
  "worker_id": "worker-01"
}
```

The exact contract may evolve, but every worker should expose a consistent interface.

---

# 9. Model Router

The Model Router is responsible for deciding which worker/model should process an inference request.

Example:

```text
User Request
     │
     ▼
Agent
     │
     ▼
Model Router
     │
     ├── Requires text?
     │       └── Text Worker
     │
     ├── Requires vision?
     │       └── Vision Worker
     │
     └── Requires coding?
             └── Code Worker
```

The router should eventually consider:

* Required capability
* Model type
* Worker status
* Worker availability
* Model preference
* Hardware availability
* Latency

The first implementation may use simple capability-based routing.

---

# 10. Worker Registration

Workers should register themselves with the central backend.

Example:

```text
Worker starts
     │
     ▼
POST /api/workers/register
     │
     ▼
Backend stores worker metadata
     │
     ▼
Worker becomes available
```

Worker information should include:

* Worker ID
* Hostname
* IP
* Port
* Model
* Model type
* Capabilities
* Hardware information
* VRAM
* Status

---

# 11. Worker Heartbeats

Workers should periodically report health.

```text
Worker
   │
   │ heartbeat
   ▼
Backend
   │
   ▼
Update last_heartbeat
```

If the heartbeat becomes stale:

```text
last_heartbeat expired
        ↓
worker = offline/unhealthy
        ↓
router stops sending requests
```

This prevents routing requests to unavailable machines.

---

# 12. Chat Architecture

The basic chat workflow is:

```text
User
 │
 ▼
Frontend
 │
 ▼
POST /api/chat
 │
 ▼
FastAPI
 │
 ├── Validate request
 │
 ├── Load conversation
 │
 ├── Save user message
 │
 ├── Determine agent/model
 │
 ├── Retrieve context if required
 │
 ├── Model Router
 │
 ▼
Model Worker
 │
 ▼
Local LLM
 │
 ▼
Response
 │
 ▼
Backend
 │
 ├── Save assistant message
 │
 └── Create inference record
 │
 ▼
Frontend
```

---

# 13. RAG Architecture

RAG will allow the system to answer questions using confidential organizational documents.

Pipeline:

```text
Document Upload
      │
      ▼
Document Processing
      │
      ▼
Text Extraction
      │
      ▼
Chunking
      │
      ▼
Embedding Model
      │
      ▼
Vector Storage
      │
      ▼
PostgreSQL + pgvector
```

During a query:

```text
User Question
      │
      ▼
Embedding
      │
      ▼
Vector Similarity Search
      │
      ▼
Relevant Chunks
      │
      ▼
Context Construction
      │
      ▼
Model Worker
      │
      ▼
Local LLM
      │
      ▼
Grounded Response
```

No confidential document content should be sent to external AI APIs.

---

# 14. Agent Architecture

Agents provide higher-level task orchestration.

An agent may:

* Interpret a user request
* Select a model
* Search a knowledge base
* Call tools
* Perform multiple inference steps
* Produce an artifact
* Return a final response

Conceptual flow:

```text
User
 │
 ▼
Agent
 │
 ├── Think / Plan
 │
 ├── Retrieve Knowledge
 │
 ├── Select Model
 │
 ├── Call Tool
 │
 ├── Perform Inference
 │
 └── Produce Result
 │
 ▼
Response
```

Agent execution should be represented by an `agent_run`.

---

# 15. Tool Architecture

Tools are controlled capabilities available to agents.

Possible tools:

* Knowledge search
* Document search
* Calculator
* Code execution
* File processing
* Internal enterprise API
* Report generation

Tools should not be arbitrarily exposed to every agent.

Agent-tool relationships should be explicitly configured.

---

# 16. Authentication

Authentication will be implemented after the basic backend foundation.

Expected architecture:

```text
User
 │
 ▼
Login
 │
 ▼
Backend
 │
 ▼
Credential Verification
 │
 ▼
JWT
 │
 ▼
Authenticated API Requests
```

Passwords must never be stored in plaintext.

Only password hashes should be stored.

---

# 17. Authorization

Authorization will control access to:

* Workspaces
* Agents
* Knowledge bases
* Documents
* Models
* Tools
* System settings

Roles may include:

```text
Admin
Operator
Analyst
Viewer
```

Authorization should be enforced by backend services/routes rather than relying solely on frontend controls.

---

# 18. Audit Logging

Important system actions must be auditable.

Examples:

```text
LOGIN
LOGOUT
DOCUMENT_UPLOAD
DOCUMENT_DELETE
KNOWLEDGE_BASE_ACCESS
MODEL_REGISTER
MODEL_INFERENCE
AGENT_RUN
TOOL_EXECUTION
ARTIFACT_CREATED
```

Audit logs should contain enough information to answer:

* Who performed the action?
* What action occurred?
* What resource was affected?
* When did it occur?
* Was it successful?
* What was the source/request context?

Do not store sensitive secrets in audit logs.

---

# 19. Database Integration

The database will be maintained separately but must integrate with the backend through SQLAlchemy.

Major entities include:

```text
users
roles
user_roles

workspaces
workspace_members

agents

model_workers
models

conversations
messages

knowledge_bases
documents
document_chunks

tools
agent_tools
agent_knowledge_bases

agent_runs
tool_executions
model_inference_runs

artifacts
audit_logs
system_events
```

The exact schema is defined in the database design documentation.

The backend must not independently invent conflicting table definitions.

---

# 20. API Layer Principles

API endpoints should be:

* Versionable
* Consistent
* Validated
* Documented
* Authenticated where required
* Properly error-handled

Prefer a structure such as:

```text
/api/auth/*
/api/users/*
/api/workspaces/*
/api/chat/*
/api/agents/*
/api/models/*
/api/workers/*
/api/knowledge-bases/*
/api/documents/*
/api/tools/*
```

---

# 21. Error Handling

The backend should provide consistent errors.

Example:

```json
{
  "error": {
    "code": "MODEL_WORKER_UNAVAILABLE",
    "message": "No available model worker supports the requested capability."
  }
}
```

Avoid returning raw Python exceptions to the frontend.

Do not expose:

* Database credentials
* Stack traces
* Internal filesystem paths
* Secrets
* Internal infrastructure details

in normal production responses.

---

# 22. Configuration

Configuration must come from environment variables.

Example:

```env
DATABASE_URL=
ENVIRONMENT=development
DEBUG=true

JWT_SECRET=
JWT_ALGORITHM=

MODEL_WORKER_TIMEOUT=
MODEL_WORKER_HEARTBEAT_INTERVAL=

VECTOR_DIMENSION=
```

Secrets must never be committed to Git.

`.env.example` should contain placeholders only.

---

# 23. Logging

Application logs should provide useful operational information without leaking confidential data.

Log:

* Request lifecycle
* Errors
* Worker registration
* Worker availability
* Model routing decisions
* Agent execution status
* Document processing status

Do not log:

* Passwords
* JWT secrets
* API keys
* Complete confidential documents
* Sensitive user content unnecessarily

---

# 24. Testing Strategy

Testing should exist at multiple levels.

## Unit Tests

Test individual services:

```text
Model Router
RAG retrieval
Authentication
Agent logic
Document processing
```

## API Tests

Test:

```text
GET /health
POST /auth/login
POST /chat
GET /models
GET /workers
```

## Integration Tests

Test:

```text
FastAPI ↔ PostgreSQL
Backend ↔ Model Worker
Document → RAG → Model
```

The initial development stage should prioritize:

1. Health test
2. Database connectivity test
3. Model worker test
4. Chat API test

---

# 25. Development Phases

Implementation should happen incrementally.

## Phase 1: Backend Foundation

Implement:

* FastAPI
* Project structure
* Configuration
* PostgreSQL connection
* SQLAlchemy
* Alembic
* Health endpoints
* Basic tests

---

## Phase 2: Database Integration

Implement:

* SQLAlchemy models
* Relationships
* Repositories
* Migrations
* Seed data

Integrate the database schema prepared by the database team.

---

## Phase 3: Model Worker

Implement:

* Worker service
* `/health`
* `/metadata`
* `/generate`
* Local model integration

Start with ONE working model.

---

## Phase 4: Model Registry & Routing

Implement:

* Worker registration
* Worker heartbeat
* Model registry
* Capability discovery
* Basic model routing
* Inference tracking

---

## Phase 5: Chat

Implement:

* Conversations
* Messages
* Chat API
* Model invocation
* Message persistence

Target workflow:

```text
Frontend
   ↓
Backend
   ↓
Model Worker
   ↓
Local LLM
   ↓
Backend
   ↓
PostgreSQL
   ↓
Frontend
```

---

## Phase 6: RAG

Implement:

* Document upload
* Document processing
* Chunking
* Embeddings
* pgvector
* Retrieval
* Context injection

---

## Phase 7: Agents

Implement:

* Agent definitions
* Agent execution
* Model selection
* Knowledge retrieval
* Tool execution
* Agent run tracking

---

## Phase 8: Security

Implement:

* Authentication
* JWT
* Authorization
* Workspace isolation
* Input validation
* Audit logging
* Security middleware

---

## Phase 9: Production Hardening

Implement:

* Error handling
* Logging
* Monitoring
* Worker failure handling
* Timeouts
* Retry strategies
* Performance improvements
* Deployment configuration

---

# 26. MVP Critical Path

The minimum end-to-end functionality should be:

```text
                 USER
                   │
                   ▼
               FRONTEND
                   │
                   ▼
                FASTAPI
                   │
          ┌────────┴────────┐
          ▼                 ▼
      PostgreSQL       Model Router
                            │
                            ▼
                       Model Worker
                            │
                            ▼
                        Local LLM
                            │
                            ▼
                         Response
                            │
          ┌─────────────────┘
          ▼
      PostgreSQL
          │
          ▼
       FRONTEND
```

The first successful vertical slice should prove:

> A user can submit a question through the frontend, the central backend can route it to a locally hosted AI model, receive the response, persist the conversation, and return the answer to the user without relying on an external AI API.

This is the primary backend milestone.

---

# 27. Architectural Boundaries

## Frontend

Responsible for:

* User interface
* User interaction
* Client-side state
* Displaying results
* Calling backend APIs

The frontend should NOT contain:

* Database credentials
* AI model credentials
* Model orchestration logic
* Sensitive business logic

---

## Backend

Responsible for:

* Business logic
* API
* Authentication
* Authorization
* Agent orchestration
* RAG orchestration
* Model routing
* Tool management
* Database interaction
* Audit logging

---

## Database

Responsible for:

* Persistent application state
* Relationships
* Metadata
* Conversation history
* Document metadata
* Vector storage
* Audit records

---

## Model Workers

Responsible for:

* Loading local models
* Performing inference
* Reporting health
* Reporting capabilities
* Returning model responses

They should NOT contain application-wide business logic.

---

# 28. Security Principles

The backend must follow these principles:

### Data Sovereignty

Confidential organizational data should remain inside the organization's trusted infrastructure.

### No External AI Dependency

The core inference path should not require external commercial AI APIs.

### Least Privilege

Users, agents, and tools should only receive the permissions required for their tasks.

### Explicit Access

Knowledge bases, documents, tools, and workspaces should have controlled access.

### Auditability

Security-sensitive and important system actions should be traceable.

### Secret Protection

Secrets must be stored through environment configuration or an appropriate secret-management mechanism.

### Input Validation

All externally supplied data must be validated.

---

# 29. Performance Principles

The backend should:

* Use asynchronous operations where appropriate
* Avoid blocking the main event loop
* Reuse database connections
* Use connection pooling
* Apply timeouts to model workers
* Avoid unnecessarily sending large documents between services
* Retrieve only relevant RAG context
* Avoid loading models into the central backend

---

# 30. Distributed Inference Principle

The architecture should not assume that model inference happens on one particular machine.

The central backend should communicate with abstract model workers.

Today:

```text
Laptop A → Model Worker
Laptop B → Model Worker
Laptop C → Model Worker
```

Production:

```text
GPU Server A → Model Worker
GPU Server B → Model Worker
GPU Server C → Model Worker
```

The backend architecture should remain unchanged.

This allows the SIH prototype to demonstrate distributed local inference while remaining conceptually compatible with enterprise GPU infrastructure.

---

# 31. What NOT to Do

Do not:

* Put all backend code in `main.py`
* Hardcode database credentials
* Store plaintext passwords
* Put model weights in PostgreSQL
* Call external AI APIs in the core inference path
* Hardcode a single model throughout the application
* Put business logic in frontend components
* Mix SQLAlchemy models with API schemas
* Store entire documents unnecessarily in relational tables
* Create duplicate model-worker implementations for different models
* Initialize another Git repository inside `backend/`
* Modify the frontend without coordination
* Build all advanced features before the basic vertical slice works

---

# 32. First Implementation Target

The first backend implementation must ONLY establish:

```text
FastAPI
   │
   ├── /health
   │
   └── /health/db
           │
           ▼
       PostgreSQL
```

After this is verified, the next milestone is:

```text
FastAPI
   │
   ▼
Model Worker
   │
   ▼
Local Model
```

Then:

```text
Frontend
   │
   ▼
FastAPI
   │
   ├── PostgreSQL
   │
   └── Model Worker
          │
          ▼
        Local LLM
```

Only after this vertical slice is stable should we expand into RAG, agents, tools, and advanced orchestration.

---

# 33. Definition of a Successful Backend

The backend will be considered functionally successful when it can:

1. Authenticate a user.
2. Identify the user's workspace and permissions.
3. Create and retrieve conversations.
4. Accept user messages.
5. Select an appropriate local model worker.
6. Send inference requests to that worker.
7. Receive the local model response.
8. Persist messages and inference metadata.
9. Retrieve relevant private knowledge when required.
10. Execute controlled tools through agents.
11. Record important actions through audit logs.
12. Operate without depending on external AI inference services.

---

# 34. Final Architecture

The intended final architecture is:

```text
                         ┌──────────────┐
                         │    USER      │
                         └──────┬───────┘
                                │
                                ▼
                     ┌────────────────────┐
                     │     FRONTEND       │
                     │   Next.js / React  │
                     └─────────┬──────────┘
                               │
                               │ REST API
                               ▼
              ┌─────────────────────────────────┐
              │          FASTAPI BACKEND        │
              │                                 │
              │ ┌─────────┐   ┌──────────────┐ │
              │ │  Auth   │   │ API Layer    │ │
              │ └─────────┘   └──────┬───────┘ │
              │                      │         │
              │ ┌────────────────────▼───────┐ │
              │ │      Service Layer          │ │
              │ │                             │ │
              │ │ Agent │ RAG │ Router │ Tool │ │
              │ └──────────────┬──────────────┘ │
              │                │                │
              └────────────────┼────────────────┘
                               │
                ┌──────────────┴──────────────┐
                │                             │
                ▼                             ▼
       ┌─────────────────┐          ┌──────────────────┐
       │   PostgreSQL    │          │  MODEL WORKERS   │
       │                 │          │                  │
       │ App State       │          │ Worker A → LLM   │
       │ Conversations   │          │ Worker B → VLM   │
       │ Documents       │          │ Worker C → LLM   │
       │ Metadata        │          │ Worker D → ...   │
       │ pgvector        │          │                  │
       │ Audit Logs      │          │ Local Inference  │
       └─────────────────┘          └──────────────────┘
```

The central principle is:

> **Centralized orchestration. Distributed local inference. Persistent sovereign data.**

The backend should make the AI infrastructure modular, replaceable, observable, and independent of any single model or machine.
