# AI Code Assistant (Boot.dev Course Project)

This project is a small AI-powered code assistant built as part of the **Boot.dev AI Code Assistant course**.

It takes a prompt from the command line, sends it to Google Gemini, and allows the model to call predefined Python tools. When Gemini decides to use a tool, the application executes the corresponding Python function and returns the result to the model.

---

## Tech Stack

* Python
* Google Gemini (`google-genai`)
* Tool-based function execution

---

## Features

The assistant can:

* List files in the project
* Read file contents
* Write to files
* Run Python files (for example, tests)

These tools allow the model to inspect, modify, and validate a small sample project programmatically.

---

## Project Structure

.
├── main.py
├── call_function.py
├── prompts.py
├── functions/
│   ├── get_files_info.py
│   ├── get_file_content.py
│   ├── write_file.py
│   └── run_python_file.py
└── calculator/

* **main.py** – CLI entrypoint and Gemini request/response handling
* **call_function.py** – Maps Gemini tool calls to real Python functions
* **prompts.py** – System prompt used to guide the model
* **functions/** – Tool implementations
* **calculator/** – Sample project used by the assistant (source files and tests)

---

## How It Works

1. A prompt is passed in via the command line.
2. The prompt, system instructions, and tool definitions are sent to Gemini.
3. Gemini may respond with a tool (function) call.
4. The application executes the requested Python function.
5. The result is returned to Gemini so it can continue reasoning.

---

## Setup

### 1. Create and activate a virtual environment

python -m venv .venv
source .venv/bin/activate  (macOS/Linux)
.venv\Scripts\activate     (Windows)

### 2. Install dependencies

uv sync

### 3. Set the Gemini API key
Create a .env file in the project root and add:

GEMINI_API_KEY=your_api_key_here

Make sure the .env file is loaded before running the app (for example, using python-dotenv or your runtime’s environment loading).

---

## Running the Assistant

uv run main.py "your prompt here" --verbose

### Example

uv run main.py "Run the calculator tests and fix any failures" --verbose

---

## Acknowledgements

This project was built while following the **AI Code Assistant course on Boot.dev**.

Big thanks to **Boot.dev** for the lessons, structure, and inspiration behind this assistant.
