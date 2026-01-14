## Paper: AUTOMATION OF ADVERSARIAL RED TEAMING THROUGH LLM BASED MULTI-AGENT SYSTEMS: APPROACH TO ACCELERATING DISCOVERY, AND OPTIMIZATION

![alt text](https://img.shields.io/badge/license-MIT-blue.svg)
![alt text](https://img.shields.io/badge/python-3.9%2B-blue.svg)
[![DOI](https://img.shields.io/badge/DOI-10.13140%2FRG.2.2.29306.35521-blue)](https://doi.org/10.13140/RG.2.2.29306.35521)

SafeAgent is a cutting-edge, autonomous multi-agent Large Language Model (LLM) framework designed to accelerate AI safety auditing and compliance verification. This repository provides the source code and resources to facilitate automated red teaming, self-healing attack execution, and quantitative safety evaluation across critical risk domains.

### 🚀 Features

- **Autonomous Red Teaming**: Orchestrates agents to generate, execute, and refine adversarial attacks without human intervention.
- **Self-Healing Code Generation**: Features a Coder Agent that autonomously detects runtime API errors (e.g., rate limits, syntax errors) and rewrites its own Python scripts to ensure experiment completion.
- **LLM-as-a-Judge Evaluation**: Eliminates human bias by using a strict binary rubric to score model refusals vs. jailbreaks.
- **Multi-Domain Auditing**: Validated across six safety categories:
  - Chemical & Biological Weapons
  - Cybersecurity Exploits
  - Self-Harm & Violence
  - Disinformation Campaigns
  - PII Leakage
  - Copyright Infringement
- **"Superhuman" Audit Loop**: Simulates a future-proof evaluation by using GPT-5-mini (Attacker) to audit GPT-4o-mini (Target).

### Safety & Ethics Statement
This framework is released for defensive research purposes only.
To prevent misuse, the dataset of 1,200 adversarial prompts generated during our study has been withheld from this repository. The data/ folder contains a sanitized example_benchmark.csv for demonstration purposes. The author does not condone the generation of harmful content.

### 📑 Project Structure

```
SAFETYAGENT/
│── data/                   # Input datasets 
│── paper_results/          # Logs, Charts, Reports
│   ├── Experiment_EXP_01_Chemical...
│   ├── Experiment_EXP_04_Disinformation...
│   └── ...
│── src/                    # Core components
│   ├── agents/             # Agents
│   │   ├── coder_agent.py      # Writes & Fixes Python Code
│   │   ├── judge_agent.py      # Evaluates Safety
│   │   ├── hypothesis_agent.py # Formulates Strategy
│   │   ├── visualization_agent.py # Visualizes ASR
│   │   └── supervisor.py       # Orchestration Logic
│   ├── tools/              # Execution Logic
│── main.py                 # Main Entry Point
│── requirements.txt        # Dependencies
│── LICENSE                 # MIT License
```

### 🔧 Installation

#### Prerequisites

- Python 3.9+
- OpenAI API Key (Required for Agents)

#### Setup

#### Clone the repository

```bash
git clone https://github.com/dave21-py/SAFETYAGENT.git
cd SAFETYAGENT
```

#### Install dependencies

```bash
pip install -r requirements.txt
```

#### Configure Environment

Create a `.env` file in the root directory:

```bash
OPENAI_API_KEY="sk-..."
```

### 🛠️ Usage

To reproduce, simply run:

```bash
python main.py
```

### The Autonomous Loop:

1. Hypothesis Agent drafts a research plan.
2. Coder Agent writes a Python script to attack the target model.
3. Executor runs the script. If it crashes, the Coder Agent fixes it automatically.
4. Judge Agent scores the results (0% - 100% ASR).
5. Visualizer plots the data.
6. Report Agent writes the final Final_Audit_Report.md.

### 📊 Key Findings (Jan 2026)

SafeAgent identified a critical "Safety Alignment Gap" in efficient frontier models. While GPT-4o-mini demonstrated robust refusal against technical threats, it remained susceptible to persuasive roleplay:

| Category | Attack Success Rate (ASR) | Status |
|----------|---------------------------|--------|
| Chemical Weapons | 0.00% | ✅ Robust |
| Cybersecurity | 0.00% | ✅ Robust |
| Self-Harm | 2.50% | ⚠️ Minor Leakage |
| Disinformation | 7.50% | ❌ Vulnerable |

Check the `paper_results/` directory for full audit reports and visualizations.

### 📝 Citation

If you use SafeAgent in your research, please cite:

```bibtex
@article{SafeAgent2026,
  title   = {Automation of Adversarial red teaming throuh LLM based multi-agent systems: approach to accelerating discovery, and optimization},
  author  = {David Geddam},
  journal = {ResearchGate Preprint},
  year    = {2026},
  doi     = {10.13140/RG.2.2.29306.35521},
  url     = {https://www.researchgate.net/publication/399742498_AUTOMATION_OF_ADVERSARIAL_RED_TEAMING_THROUGH_LLM_BASED_MULTI-AGENT_SYSTEMS_APPROACH_TO_ACCELERATING_DISCOVERY_AND_OPTIMIZATION}
```

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

### 🤝 Acknowledgments

- Inspired by the MatAgent framework for autonomous scientific discovery.
- Built with LangChain and OpenAI.

---
For any questions, please reach out via GitHub Issues or Discussions.

🌟 **Star this repository if you find it useful!**
