Team, we are building the frontend for the SIH 2026 project inside the existing repository:

`https://github.com/brevankumargoud/SIH_2026`

IMPORTANT:
Do NOT create another Git repository.
Do NOT clone/create a second project inside this repository.
Do NOT delete or replace existing repository files.
Do NOT create separate Next.js/Vite projects for each person.

We are maintaining ONE frontend application in ONE shared repository.

The repository currently contains the project-level README and `docs/`. The frontend should be created as a dedicated application directory so that backend and frontend can coexist cleanly.

==================================================

1. FRONTEND TECHNOLOGY STACK
   ==================================================

Use the following stack:

### Next.js

Use the latest stable Next.js version available in our environment, with the App Router.

WHY:

* React-based framework
* Routing is built in
* Good structure for a production web application
* Easy frontend/backend API integration
* Supports layouts, loading states, error states, etc.

### TypeScript

Use TypeScript instead of plain JavaScript.

WHY:

* Prevents many common frontend bugs
* Gives us type safety
* Makes API integration easier
* Makes a shared project easier to maintain

### Tailwind CSS

Use Tailwind CSS for styling.

WHY:

* Fast UI development
* Consistent design
* Easy responsive layouts
* Avoids creating hundreds of scattered CSS files

### shadcn/ui

Use shadcn/ui components where appropriate.

WHY:

* Gives us accessible, reusable UI primitives
* We can customize them to match our design
* Better than everyone creating their own Button, Dialog, Dropdown, etc.

### Lucide Icons

Use Lucide React for icons.

WHY:

* Consistent icon set
* Clean modern appearance
* Avoid random icon libraries being mixed together

### TanStack Query

Use TanStack Query for server/API state once API integration begins.

WHY:

* Handles API fetching
* Loading/error states
* Caching
* Refetching
* Keeps API logic cleaner

For purely local UI state, use React state/context where appropriate.

### Zod

Use Zod for validating important client-side data structures and API responses where useful.

WHY:

* Gives us runtime validation
* Keeps frontend data contracts safer

==================================================
2. REPOSITORY STRUCTURE
=======================

Create the frontend ONLY inside:

`frontend/`

The repository should eventually look approximately like this:

SIH_2026/
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── features/
│   ├── hooks/
│   ├── lib/
│   ├── services/
│   ├── types/
│   ├── public/
│   ├── styles/
│   ├── package.json
│   ├── tsconfig.json
│   ├── next.config.ts
│   ├── postcss.config.mjs
│   ├── eslint.config.mjs
│   └── README.md
│
├── docs/
│
├── README.md
│
└── [backend will be added separately]

The backend team will NOT work inside `frontend/`.

==================================================
3. NEXT.JS APP STRUCTURE
========================

Inside `frontend/app/` use the App Router.

Recommended structure:

frontend/
└── app/
├── layout.tsx
├── page.tsx
├── globals.css
│
├── login/
│   └── page.tsx
│
├── dashboard/
│   └── page.tsx
│
├── chat/
│   └── page.tsx
│
├── agents/
│   └── page.tsx
│
├── knowledge/
│   └── page.tsx
│
├── models/
│   └── page.tsx
│
└── settings/
└── page.tsx

Do NOT put everything into one giant `page.tsx`.

Each route gets its own page.

==================================================
4. COMPONENT STRUCTURE
======================

Use:

frontend/components/

for reusable UI components.

Example:

components/
├── ui/
│   ├── Button.tsx
│   ├── Input.tsx
│   ├── Dialog.tsx
│   ├── Dropdown.tsx
│   └── ...
│
├── layout/
│   ├── Sidebar.tsx
│   ├── Header.tsx
│   └── PageContainer.tsx
│
├── chat/
│   ├── ChatInput.tsx
│   ├── MessageBubble.tsx
│   ├── ChatHistory.tsx
│   └── ModelIndicator.tsx
│
├── agents/
│   ├── AgentCard.tsx
│   ├── AgentList.tsx
│   └── AgentEditor.tsx
│
├── knowledge/
│   ├── DocumentCard.tsx
│   ├── UploadZone.tsx
│   └── KnowledgeBaseCard.tsx
│
└── models/
├── ModelCard.tsx
├── WorkerStatus.tsx
└── ModelStatusBadge.tsx

The exact components can evolve, but follow this principle:

Reusable component → `components/`

Page-specific composition → route's `page.tsx`

==================================================
5. FEATURE-BASED ORGANIZATION
=============================

For larger functionality, use:

frontend/features/

Example:

features/
├── auth/
├── chat/
├── agents/
├── knowledge/
├── models/
└── settings/

A feature can contain:

features/chat/
├── components/
├── hooks/
├── api.ts
├── types.ts
└── utils.ts

This keeps complex functionality grouped together instead of scattering related files throughout the project.

==================================================
6. API / BACKEND COMMUNICATION
==============================

DO NOT write fetch calls randomly inside every component.

Create:

frontend/services/

Example:

services/
├── api-client.ts
├── auth-service.ts
├── chat-service.ts
├── agent-service.ts
├── document-service.ts
└── model-service.ts

Example responsibility:

`chat-service.ts`

should handle communication with backend chat endpoints.

Components should call the service rather than directly constructing HTTP requests everywhere.

Example flow:

Chat UI
↓
chat-service
↓
FastAPI backend
↓
response

==================================================
7. SHARED TYPES
===============

Create:

frontend/types/

Example:

types/
├── auth.ts
├── chat.ts
├── agent.ts
├── model.ts
├── document.ts
└── common.ts

Example:

```ts
export interface Message {
  id: string;
  conversationId: string;
  role: "user" | "assistant" | "system" | "tool";
  content: string;
  createdAt: string;
}
```

The frontend should have clear types for the data it receives from the backend.

Once the backend API contracts are finalized, update these types accordingly.

==================================================
8. UTILITY / CONFIGURATION CODE
===============================

Use:

frontend/lib/

for shared utilities and configuration.

Example:

lib/
├── api.ts
├── utils.ts
├── constants.ts
└── env.ts

Do NOT put random business logic here.

==================================================
9. HOOKS
========

Use:

frontend/hooks/

for reusable React hooks.

Examples:

hooks/
├── useAuth.ts
├── useChat.ts
├── useCurrentUser.ts
└── useModelStatus.ts

Do not create a hook for every tiny piece of state.

==================================================
10. PUBLIC ASSETS
=================

All static assets go inside:

frontend/public/

Example:

public/
├── logo.svg
├── icons/
└── images/

Do NOT keep random images in the project root.

==================================================
11. ENVIRONMENT VARIABLES
=========================

Use environment variables for backend URLs and configuration.

Example:

`.env.local`

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

IMPORTANT:

Do NOT commit `.env.local`.

Make sure it is included in `.gitignore`.

Never hardcode backend URLs throughout the application.

==================================================
12. FRONTEND PAGES WE NEED
==========================

Our initial application should have these major areas:

### Authentication

* Login
* Logout state
* Authentication-aware routing

### Dashboard

* Overview
* System status
* Recent conversations
* Active models/workers
* Knowledge base overview

### Chat

* Conversation list
* Chat messages
* Message input
* Model/agent information
* Loading state
* Error state
* New conversation

### Agents

* Agent list
* Agent details
* Create/edit agent
* Agent status

### Knowledge

* Knowledge bases
* Document upload
* Document list
* Processing status
* Search/retrieval interface

### Models

* Available models
* Model capabilities
* Worker status
* Online/offline/busy state

### Settings

* Profile
* Workspace
* System configuration where needed

These pages should be built progressively, not all as giant finished pages on day one.

==================================================
13. DESIGN RULES
================

The entire application must feel like ONE product.

Do NOT let each teammate invent a different visual language.

We need shared:

* Typography
* Spacing
* Border radius
* Shadows
* Buttons
* Inputs
* Cards
* Modals
* Icons
* Status badges
* Colors
* Responsive behavior

Create a small design system before building many pages.

For example:

Primary button
Secondary button
Danger button
Input
Card
Badge
Modal
Tabs
Dropdown
Toast
Loading state

Use these consistently.

==================================================
14. TEAM WORKFLOW
=================

Because four people are working on the frontend, do NOT let everyone work directly on `main`.

Each developer should create a feature branch.

Examples:

`frontend/login`

`frontend/dashboard`

`frontend/chat`

`frontend/knowledge`

or use your preferred naming convention.

Workflow:

main
↓
feature branch
↓
development
↓
commit
↓
Pull Request
↓
review
↓
merge

Do NOT push experimental work directly into `main`.

==================================================
15. IMPORTANT GIT RULES
=======================

Before starting work:

```bash
git checkout main
git pull origin main
```

Then create your feature branch.

Before pushing:

```bash
git status
git diff
```

Make sure you are only committing your intended files.

DO NOT commit:

* `.env`
* `.env.local`
* `node_modules/`
* build output
* personal IDE files
* temporary files
* API keys
* passwords
* machine-specific configuration

==================================================
16. VERY IMPORTANT: DO NOT RECREATE THE REPOSITORY
==================================================

You have already cloned:

`SIH_2026`

That is the project repository.

Do NOT do this:

```text
SIH_2026/
    another-project/
        another-next-app/
```

Do NOT create:

```text
frontend/frontend/
```

Do NOT initialize another Git repository inside `frontend/`.

There should be ONE `.git` directory at the repository root.

Correct:

```text
SIH_2026/
├── .git/
├── frontend/
├── docs/
└── README.md
```

Wrong:

```text
SIH_2026/
├── .git/
├── frontend/
│   ├── .git/       ❌
│   └── ...
└── ...
```

==================================================
17. DO NOT MODIFY BACKEND FILES
===============================

The backend team will work in its own directory.

Expected final repository:

SIH_2026/
│
├── frontend/
│
├── backend/
│
├── docs/
│
└── README.md

Frontend developers should normally modify only:

`frontend/`

and relevant project documentation when necessary.

==================================================
18. FRONTEND-BACKEND CONTRACT
=============================

The frontend should NOT invent backend endpoints arbitrarily.

As the backend team creates APIs, we will agree on endpoint contracts.

Example:

```text
POST /api/auth/login
GET  /api/conversations
GET  /api/conversations/{id}/messages
POST /api/chat
GET  /api/models
GET  /api/model-workers
POST /api/documents
```

Once the backend team confirms an endpoint, implement the corresponding frontend service.

Use mock data temporarily when necessary, but clearly isolate it so it can be replaced by real API calls later.

==================================================
19. MOCK DATA RULE
==================

During UI development, you may use mock data.

But:

* Keep mock data in a clearly identified location.
* Do not mix fake data directly into production services.
* Make it obvious what will later be replaced by an API call.

Example:

`features/chat/mock-data.ts`

Once the backend endpoint exists:

mock data → real API.

==================================================
20. DEVELOPMENT PRIORITY
========================

Build in this order:

1. Shared design system
2. Application shell
3. Login
4. Dashboard
5. Chat UI
6. Agents
7. Knowledge base
8. Models/workers
9. Settings
10. Backend integration
11. Loading/error/empty states
12. Responsive polish

Do NOT spend the entire SIH day polishing one page while the rest of the application doesn't exist.

==================================================
21. DEFINITION OF DONE FOR A FEATURE

A frontend feature is not considered complete merely because "the page looks good".

It should have:

* Proper route
* Reusable components where appropriate
* Responsive layout
* Loading state
* Empty state
* Error state
* Sensible accessibility
* No hardcoded secrets
* No unnecessary duplicated components
* Clean TypeScript
* No console errors
* Tested locally

==================================================
22. MOST IMPORTANT TEAM RULE

We are building ONE application.

Before creating a new:

* component
* utility
* hook
* API service
* design pattern

check whether something equivalent already exists.

DO NOT create:

`Button.tsx`
`Button2.tsx`
`CustomButton.tsx`
`NewButton.tsx`

just because another developer created a button differently.

Reuse or improve the existing component.

The goal is not four separate beautiful pages.

The goal is ONE coherent enterprise AI workbench.

==================================================

FINAL TARGET

The repository should evolve into:

SIH_2026/
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── features/
│   ├── hooks/
│   ├── services/
│   ├── lib/
│   ├── types/
│   ├── public/
│   ├── styles/
│   ├── package.json
│   └── README.md
│
├── backend/
│   └── [backend team]
│
├── docs/
│
└── README.md

Frontend = presentation and user interaction.

Backend = business logic, orchestration, APIs.

Database = persistent system state.

Model workers = local AI inference.

Keep those boundaries clean throughout development.
