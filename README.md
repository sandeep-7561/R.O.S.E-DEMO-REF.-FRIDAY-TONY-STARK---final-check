# R.O.S.E-DEMO-REF.-FRIDAY-TONY-STARK---final-check
hey, im sandeep and today i will start to create my own assistance.



Project Structure----------------------------------
rose/
│
├── app.py                # Entry Point
├── config.py             # Config
├── .env
│
├── brain/
│   ├── llm.py            # Ollama
│   ├── prompt.py         # System Prompt
│   └── chat.py           # Chat Logic
│
├── mcp/
│   ├── client.py         # MCP Client
│   └── manager.py
│
├── memory/
│   ├── short_term.py
│   ├── long_term.py
│   └── database.py
│
├── servers/
│   ├── notes/
│   ├── weather/
│   ├── browser/
│   └── filesystem/
│
├── planner/
│   └── planner.py
│
└── ui/
    └── terminal.py



MODULE 1: create AI Brain.

User
   │
   ▼
Friday
   │
   ▼
Qwen (Ollama)
   │
   ▼
Answer


MODULE 2: MCP Integration

User
   │
   ▼
Brain
   │
Need Tool?
   │
   ▼
MCP Client
   │
   ▼
FastMCP Server


Module 3: Memory

Short Memory
Long Memory
Semantic Search
SQLite
Vector DB


Module 4: Planner

Task Planning
Goal Planning
Reflection


Module 5: Voice

Speech To Text
Text To Speech
Wake Word


Module 6: Vision

Camera
Screenshot
OCR
Image Understanding


Module 7: Automation
Mouse
Keyboard
VS Code
Browser
Windows

FINAL RESULT:
                YOU
                 │
                 ▼
           Friday Assistant
                 │
     ┌───────────┴───────────┐
     ▼                       ▼
   Brain                 Memory
     │                       │
     └───────────┬───────────┘
                 ▼
              Planner
                 │
        ┌────────┴────────┐
        ▼                 ▼
    MCP Client         Voice
        │                 │
        ▼                 ▼
     MCP Servers       Vision
        │
        ▼
   Weather / Notes / Browser / SQL / VS Code

----------------------------------------------------------------- 
FRIDAY/
│
├── app.py                 ← Entry point
├── config.py              ← Settings
├── .env                   ← Secrets
│
├── brain/
│   ├── __init__.py
│   ├── llm.py             ← Ollama se baat
│   ├── chat.py            ← Chat flow
│   ├── controller.py      ← Decision maker (Boss)
│   └── prompt.py          ← System prompt
│
├── mcp/
│   ├── client.py
│   └── manager.py
│
├── memory/
│
├── planner/
│
├── voice/
│
├── vision/
│
├── automation/
│
└── servers/




now we create brain folder and flow of brain folder:

User
      │
      ▼
ask_llm()
      │
      ▼
SYSTEM_PROMPT add hota hai
      │
      ▼
User Message add hota hai
      │
      ▼
Ollama
      │
      ▼
Qwen3 Sochta hai
      │
      ▼
Response
      │
      ▼
Sirf Content return