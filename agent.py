import json, anthropic
from tools import TOOLS
client = anthropic.Anthropic()  # needs ANTHROPIC_API_KEY env var
schema = json.load(open("schema.json"))

def run(goal):
    messages = [{"role": "user", "content": goal}]
    while True:
        r = client.messages.create(model="claude-sonnet-4-6", max_tokens=1000,
                                   tools=schema, messages=messages)
        messages.append({"role": "assistant", "content": r.content})
        if r.stop_reason != "tool_use":
            return "".join(b.text for b in r.content if b.type == "text")
        results = []
        for b in r.content:
            if b.type == "tool_use":
                out = TOOLS[b.name](**b.input)
                results.append({"type": "tool_result", "tool_use_id": b.id, "content": out})
        messages.append({"role": "user", "content": results})

if __name__ == "__main__":
    print(run(input("Goal: ")))
