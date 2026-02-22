<div align="center">

# 🧠 Fikra Nano 1B

### *"The Intel Inside for Edge AI"*

**A 1B parameter reasoning model that runs 100% offline on your CPU.**

[![PyPI](https://img.shields.io/pypi/v/fikra?color=blue)](https://pypi.org/project/fikra/)
[![Downloads](https://static.pepy.tech/badge/fikra/month)](https://pepy.tech/project/fikra)
[![License](https://img.shields.io/badge/License-Apache%202.0-green.svg)](LICENSE)
[![HuggingFace](https://img.shields.io/badge/🤗-Model-yellow)](https://huggingface.co/lacesseapp/Fikra-1B-Nano-v0.2-GGUF)
[![Made in Kenya](https://img.shields.io/badge/Made%20in-Kenya%20🇰🇪-red)](https://lacesse.co.ke)

[Install](#-installation) • [Quickstart](#-quickstart) • [Examples](#-examples) • [Benchmarks](#-benchmarks) • [Roadmap](#-roadmap)

<img src="assets/demo.gif" width="600" alt="Fikra Demo">

</div>

---

## 🎯 What is Fikra Nano 1B?

Fikra Nano is a **1 billion parameter language model** fine-tuned for **mathematical reasoning** and **instruction following**. Unlike cloud-based AI:

- ✅ **100% Offline** - No internet needed after installation
- ✅ **$0 Forever** - No API costs, no subscriptions
- ✅ **CPU Only** - No GPU required
- ✅ **700MB** - Fits on any device (laptop, phone, Raspberry Pi)
- ✅ **Private** - Your data never leaves your machine
- ✅ **Apache 2.0** - Use commercially, embed in products

Built by [James Miano](https://linkedin.com/in/jamesmiano) / [Lacesse Ventures](https://lacesse.co.ke) 🇰🇪

---

## 📊 Performance

| Model | Size | Internet | Cost/1M tokens | Latency | Math (GSM8K) |
|-------|------|----------|----------------|---------|--------------|
| **Fikra Nano** | 700MB | ❌ No | **$0** | 50-200ms | **68%*** |
| GPT-3.5 Turbo | API | ✅ Required | $0.50-$2 | 500-2000ms | 57% |
| Claude Haiku | API | ✅ Required | $0.25 | 300-1000ms | 88% |
| Llama 3.2 1B | 1.2GB | ❌ No | $0 | 100-300ms | 42% |

*Estimated on GSM8K subset (official benchmark coming soon)

---

## 🚀 Installation
```bash
pip install fikra
```

That's it. The model downloads automatically on first use (~700MB).

---

## ⚡ Quickstart
```python
from fikra import Fikra

# Initialize (downloads model on first run)
brain = Fikra()

# Ask anything
answer = brain.reason("If I have 3 apples and eat one, how many are left?")
print(answer)
# Output: "You have 2 apples."
```

### More Examples

**Math Reasoning:**
```python
brain.reason("A train travels 60 km in 30 minutes. What's its speed in km/h?")
# Output: "The train's speed is 120 km/h."
```

**Code Help:**
```python
brain.reason("Write a Python function to reverse a string")
# Output: "def reverse_string(s):\n    return s[::-1]"
```

**General Knowledge:**
```python
brain.reason("Explain photosynthesis in one sentence")
# Output: "Photosynthesis is the process where plants use sunlight to convert CO2 and water into glucose and oxygen."
```

---

## 💡 Use Cases

<table>
<tr>
<td width="50%">

### 🏢 **Enterprise**
- Offline customer service bots
- Internal knowledge assistants
- Data processing pipelines
- Compliance-safe AI (GDPR, HIPAA)

</td>
<td width="50%">

### 📱 **Mobile & Edge**
- iOS/Android apps
- Raspberry Pi projects
- Smart home devices
- Offline translators

</td>
</tr>
<tr>
<td>

### 🎓 **Education**
- Homework helpers
- Math tutors
- Coding assistants
- Research tools

</td>
<td>

### 🌍 **Offline Environments**
- Rural areas with no internet
- Airplanes, ships, remote locations
- Military/government secure systems
- Privacy-first applications

</td>
</tr>
</table>

---

## 🛠️ Advanced Usage

### Custom Parameters
```python
brain = Fikra()

# Adjust creativity
answer = brain.reason(
    "Write a poem about the ocean",
    temperature=0.9,      # Higher = more creative (0.0-1.0)
    max_tokens=200        # Response length
)
```

### Batch Processing
```python
questions = [
    "What is 15 * 23?",
    "Explain gravity",
    "Write a haiku about code"
]

for q in questions:
    print(f"Q: {q}")
    print(f"A: {brain.reason(q)}\n")
```

### Chat Interface
```python
print("Fikra Chat (type 'exit' to quit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = brain.reason(user_input)
    print(f"Fikra: {response}\n")
```

---

## 🔧 Manual Usage (llama.cpp)

If you prefer using `llama.cpp` directly:
```bash
# Download the GGUF file from HuggingFace
wget https://huggingface.co/lacesseapp/Fikra-1B-Nano-v0.2-GGUF/resolve/main/fikra-1b-nano-v0.2-q4_k_m.gguf

# Run inference
./llama-cli -m fikra-1b-nano-v0.2-q4_k_m.gguf \
  -n 128 \
  -p "User: Why is the sky blue?\nAssistant:"
```


## 🗺️ Roadmap

- [x] Fikra Nano 1B (GGUF quantized)
- [ ] **Fikra 7B Instruct** (Q2 2026) - 7B param version
- [ ] **Fikra API** (Q2 2026) - Cloud API at $2/1M tokens
- [ ] **Fikra Chat** - ChatGPT alternative UI
- [ ] **Fikra Code** - AI coding assistant
- [ ] **Fikra 7B Ternary** - Even smaller, faster model
- [ ] iOS/Android SDKs
- [ ] Fine-tuning toolkit

---

## 🏗️ Technical Details

**Architecture:**
- Base: Falcon 1B
- Fine-tuning: GSM8K (math) + Dolly 15k (instructions)
- Quantization: Q4_K_M (4-bit)
- Context: 2048 tokens
- Format: GGUF (optimized for CPU)

**Training:**
- Developed by: [Lacesse Ventures](https://lacesse.co.ke)
- Location: Nairobi, Kenya 🇰🇪
- Training data: Open source datasets + proprietary Kenyan knowledge
- Compute: Consumer GPUs (A4000, RTX 3090)

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Ways to contribute:**
- 🐛 Report bugs or suggest features
- 📝 Improve documentation
- 🧪 Add benchmarks or tests
- 🌍 Translate to other languages
- ⭐ Star the repo to show support!

---

## 📜 License

Apache 2.0 - Free for commercial use.

You can:
- ✅ Use in commercial products
- ✅ Modify and distribute
- ✅ Embed in proprietary software
- ✅ Sell applications built with Fikra

See [LICENSE](LICENSE) for details.

---

## 🌟 Related Projects

Built by the same team:

- **[Lacesse Duka](https://lacesse.co.ke)** - E-commerce platform for African merchants (60-second online shops)
- **Fikra 7B** (coming Q2 2026) - More powerful reasoning model

---

## 💬 Community

- 🐦 **Twitter**: [@LacesseApp](https://twitter.com/LacesseApp) (updates & announcements)
- 💼 **LinkedIn**: [James Miano](https://linkedin.com/in/jamesmiano) (founder updates)
- 🐛 **Issues**: [GitHub Issues](https://github.com/dawn-pixellate/fikra-nano-1b/issues)
- 📧 **Email**: info@lacesse.co.ke

---

## 🙏 Acknowledgments

- Hugging Face for model hosting
- llama.cpp team for GGUF format
- GSM8K & Dolly datasets
- Open source AI community

---

## 📊 Stats

![GitHub stars](https://img.shields.io/github/stars/yourusername/fikra?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/fikra?style=social)
![PyPI downloads](https://static.pepy.tech/badge/fikra)

---

<div align="center">

**Built with ❤️ in Kenya 🇰🇪**

If Fikra helped you, **⭐ star this repo** and share it with others!

[⬆ Back to Top](#-fikra-nano-1b)

</div>
