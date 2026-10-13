import json
from groq import Groq
from tools import TOOLS

client = Groq()  # reads GROQ_API_KEY from environment
schema = json.load(open("schema.json"))
tools = [{"type": "function", "function": {"name": s["name"], "description": s["description"], "parameters": s["input_schema"]}} for s in schema]

def run(goal):
    messages = [{"role": "user", "content": goal}]
    while True:
        r = client.chat.completions.create(model="llama-3.3-70b-versatile", messages=messages, tools=tools)
        m = r.choices[0].message
        if not m.tool_calls:
            return m.content
        messages.append({"role": "assistant", "content": m.content or "", "tool_calls": [
            {"id": t.id, "type": "function", "function": {"name": t.function.name, "arguments": t.function.arguments}} for t in m.tool_calls]})
        for t in m.tool_calls:
            args = json.loads(t.function.arguments or "{}")
            out = TOOLS[t.function.name](**args)
            print(f"[TOOL] {t.function.name}({args}) -> {out}")
            messages.append({"role": "tool", "tool_call_id": t.id, "content": out})

if __name__ == "__main__":
    print(run(input("Goal: ")))
