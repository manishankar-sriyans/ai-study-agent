# ai-study-agent

# AI Study Agent

An agentic AI that takes a goal, picks tools, runs them, observes results, and repeats until the goal is done.

## Architecture
User goal → LLM (Claude) → decides tool call → tools.py executes → result returned to LLM → loop until final answer

## Tools
- `calculator`: evaluates math expressions
- `save_note`: saves a study note to notes.txt
- `read_notes`: reads all saved notes

## Files
- `agent.py`: agent loop
- `tools.py`: tool functions
- `schema.json`: tool schema

## Run
```
pip install -r requirements.txt
export ANTHROPIC_API_KEY=your_key
python agent.py
```

## Demo Output

Goal: `Calculate 25*4+10, then save the result as a note, then read my notes`

```
[TOOL] calculator({'expression': '25*4+10'}) -> 110
[TOOL] save_note({'text': 'Result of 25*4+10 = 110'}) -> saved
[TOOL] read_notes({}) -> Result of 25*4+10 = 110

Result: 110
Saved note: "Result of 25*4+10 = 110"
```
