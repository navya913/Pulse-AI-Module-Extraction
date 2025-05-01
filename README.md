# Pulse-AI Module Extraction Agent

## 🚀 Overview
**Pulse-AI** is an intelligent agent built to extract structured information from product documentation. By crawling URLs, it identifies product modules, submodules, and generates clean, well-structured JSON outputs—empowering teams to understand documentation hierarchies instantly.

---

## 🧠 Features
- 🔗 **URL Processing**: Accepts one or multiple documentation URLs as input
- 🕸️ **Intelligent Crawling**: Recursively processes internal links with edge-case handling
- 🧽 **Content Extraction**: Strips away boilerplate, navigation, and noise
- 🏗️ **Hierarchy Inference**: Detects modules/submodules from content structure
- ✍️ **Description Generation**: Summarizes relevant content into module descriptions
- 📦 **Structured Output**: Outputs results as clean JSON for downstream use

---

## 🛠️ Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/navya913/Pulse-AI-Module-Extraction.git
cd pulse
pip install -r requirements.txt

⚙️ Usage
📟 Command Line Interface
bash
python module_extractor.py --urls https://help.instagram.com https://help.example.com
🧾 Output Format

{
    "module": "Account Settings",
    "Description": "Includes features for managing account preferences and privacy.",
    "submodules": {
        "Change Username": "Explains how to update your account handle.",
        "Privacy Settings": "Details options for controlling account visibility."
    }
}
🧪 Testing & Benchmarking
Successfully tested on:

Instagram Help

Neo Space Support

WordPress Documentation

Zluri Help

Chargebee Docs

🧬 Technical Architecture
🔧 Key Components
URL Crawler – Smart link traversal with rate-limiting

Content Parser – Extracts and cleans DOM content using NLP

Hierarchy Detector – Infers structure from headers and sectioning

Description Generator – Uses extractive summarization for clarity

📦 Dependencies
beautifulsoup4 – HTML parsing

requests – Web requests

nltk – Natural language processing

streamlit – Optional UI

