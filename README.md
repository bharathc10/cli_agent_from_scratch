# Autonomous AI Agent Layer (CLI Execution Engine)

An engineering prototype of a standalone command-line AI Agent capable of autonomous file system exploration, code modification, and dynamic runtime validation.

Using the Google Gemini (google-genai) SDK, the system creates a deterministic execution loop around an LLM reasoning engine by routing function-calling payloads to local Python system tools.

==================================================
CORE ENGINEERING ARCHITECTURE
==================================================

The engine bridges the gap between non-deterministic model outputs and deterministic system execution through an event-driven loop:

1. System Ingestion
   - The runtime initializes through a CLI wrapper.
   - System prompts, behavioral guardrails, and JSON function schemas are injected into model context.

2. Dynamic Tool Resolution
   - Model outputs are interpreted as structured tool-call requests rather than plain text.

3. Local Tool Dispatcher
   - call_function.py receives tool execution requests.
   - Parameters are validated.
   - The corresponding Python routine is executed.
   - Standard output and error streams are captured.

4. Context Hydration
   - Execution results are returned to the model.
   - The model evaluates outcomes.
   - The model debugs failures.
   - The cycle repeats until the objective is completed.

==================================================
SYSTEM TOOLING CAPABILITIES
==================================================

The agent operates within a sandboxed module structure and exposes several deterministic tools:

Directory Enumeration
- Recursively scans workspace directories.
- Generates metadata describing files and folders.

Stream Serialization
- Reads file contents.
- Writes new files.
- Updates existing files programmatically.

Subprocess Execution Layer
- Executes Python scripts and tests.
- Captures stdout.
- Captures stderr.
- Returns execution traces to the model.

==================================================
TECHNICAL ARCHITECTURE
==================================================

.
├── main.py
│   CLI runtime wrapper and agent execution loop
│
├── call_function.py
│   Deterministic router that maps tool schemas to implementations
│
├── prompts.py
│   System instructions and behavioral constraints
│
├── functions/
│   ├── get_files_info.py
│   ├── get_file_content.py
│   ├── write_file.py
│   └── run_python_file.py
│
└── calculator/
    Target project containing source code and tests

==================================================
DEPLOYMENT AND LOCAL EXECUTION
==================================================

1. Create Virtual Environment

python -m venv .venv
source .venv/bin/activate

2. Install Dependencies

uv sync

3. Configure Environment Variables

Create a .env file:

GEMINI_API_KEY=your_production_api_key_here

4. Run the Agent

uv run main.py "Run the calculator tests and fix any failures" --verbose
