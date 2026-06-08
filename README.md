# CLI AI Code Assistant

A command-line tool built in Python using the Google Gemini (`google-genai`) SDK to experiment with LLM function calling and automated tool execution. The application takes a natural language prompt, passes it to the model alongside a set of local tool definitions, and handles the execution loop based on the model's requests.

## How the System Works

The application coordinates an execution loop between the Gemini model and local system tools:

1. **Tool Registration:** Local Python functions are defined with explicit descriptions and parameters so the model understands their purpose.
2. **Payload Parsing:** If Gemini determines it needs a tool to answer a prompt, it returns a structured JSON request containing the function name and arguments.
3. **Local Dispatch:** A routing layer (`call_function.py`) maps the model's request to the actual Python function, executes the code, and catches the output.
4. **Context Loop:** The execution results are sent back to Gemini as context, allowing it to inspect the outcome, handle failures, and complete the task.

## Integrated System Tools

The assistant can interact with a sample project directory using four core capabilities:

* **Directory Mapping:** Indexes files and metadata within the workspace.
* **File Operations:** Reads and writes code blocks directly to project files.
* **Subprocess Runtime:** Executes test scripts locally and captures standard outputs or error messages to feed back into the model.

## Setup and Local Execution

### 1. Environment and Dependencies

Initialize a virtual environment and sync project dependencies using `uv`:

```bash
python -m venv .venv
source .venv/bin/activate
uv sync
```

### 2. Secrets Configuration

Create a `.env` file in the root directory and add your API key:

```bash
GEMINI_API_KEY=your_api_key_here
```

### 3. Run a Command

Execute the script using the verbose flag to observe the background tool calls:

```
uv run main.py "Run the calculator tests and fix any failures" --verbose
