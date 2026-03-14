# 🧠 Adaptive General Intelligence (AGI)

A self-learning AI system built in Python that continuously learns, adapts, and retains knowledge from every interaction — growing smarter over time.

## What it does

Unlike static AI models, this AGI system **remembers and adapts**. Every conversation, every input, every correction — it learns from it and applies that knowledge in future interactions. The more you use it, the smarter it gets.

## Key Features

- 🧠 **Continuous learning** — learns from every interaction automatically
- 💾 **Persistent memory** — retains knowledge across sessions, never forgets
- 🔄 **Self-adapting** — adjusts its responses based on what it has learned
- 📚 **Knowledge base** — builds and expands its own knowledge over time
- ⚡ **Fast inference** — quick responses even as knowledge grows
- 🛠️ **Extensible** — easy to plug in new learning modules

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.11+ |
| AI / ML | Groq API (Llama 3.3) |
| Memory | JSON / Vector Store |
| Learning Engine | Custom Python modules |

## Getting Started

### Prerequisites
- Python 3.11+
- Groq API key (free at [console.groq.com](https://console.groq.com))

### Installation

**1. Clone the repo**
```bash
git clone https://github.com/a6hxin/agi.git
cd agi
```

**2. Install dependencies**
```bash
pip3 install -r requirements.txt
```

**3. Add your API key**
```bash
cp .env.example .env
# Add your GROQ_API_KEY inside .env
```

**4. Run the app**
```bash
python3 main.py
```

## How it learns

```
User Input
    ↓
AGI processes the input
    ↓
Checks existing knowledge base
    ↓
Generates response
    ↓
Stores new knowledge learned
    ↓
Adapts future responses based on memory
```

Every time you interact with it, the AGI extracts new knowledge and saves it — so the next conversation is always smarter than the last.

## Environment Variables

```
GROQ_API_KEY=your-groq-api-key-here
```

## Roadmap

- [ ] Web UI for interacting with the AGI
- [ ] Multi-modal learning (images, documents)
- [ ] Knowledge visualization dashboard
- [ ] Export / import knowledge base
- [ ] Multi-agent collaboration

## Contributing

Pull requests are welcome! If you have ideas for new learning strategies or memory systems, open an issue.

## License

MIT

