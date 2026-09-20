<div align="center">

<!-- Optional: add a banner image here once generated, e.g.
<img src="BANNER_URL" alt="CS50 AI" width="100%"/>
-->

# 🧠 CS50 AI: Artificial Intelligence with Python

### *Twelve projects. One goal — teaching machines to think.*

**Complete solutions to Harvard University's CS50 AI, covering search, knowledge, uncertainty, optimization, machine learning, neural networks, and language.**

[![Course](https://img.shields.io/badge/Harvard-CS50%20AI-A51C30?style=for-the-badge&logo=harvard&logoColor=white)](https://cs50.harvard.edu/ai/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](./LICENSE) <!-- TODO: add a LICENSE file, or remove this badge -->
[![Status](https://img.shields.io/badge/Projects-12%20%2F%2012-success?style=for-the-badge)](#-projects-at-a-glance)

[Overview](#-overview) · [Projects](#-projects-at-a-glance) · [Highlights](#-highlighted-projects) · [Concepts](#-concept--project-map) · [Getting Started](#-getting-started) · [Structure](#-repository-structure) · [Certificate](#-certificate) · [Honesty](#-academic-honesty)

---

![Stars](https://img.shields.io/badge/%E2%AD%90-If%20this%20helped%2C%20star%20it-FFD700?style=flat-square)

</div>

---

## 📖 Overview

This repository contains my complete solutions to all **12 projects** of [CS50's Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/) — Harvard's flagship course on the foundations of modern AI.

Every project implements a core AI concept **from first principles**: graph search and adversarial game trees, logical inference engines, probabilistic reasoning, constraint solvers, reinforcement learning agents, convolutional networks, and the attention mechanism behind Transformers.

> [!TIP]
> **Best result:** a convolutional neural network reaching **98.93% test accuracy** on 43-class German traffic sign recognition (GTSRB).

| | |
|:---|:---|
| 🧩 **Projects completed** | **12 / 12** |
| 🐍 **Language** | Python 3 |
| 📚 **Libraries** | TensorFlow, Keras, scikit-learn, NumPy, OpenCV, NLTK |
| 🏆 **Best result** | 98.93% test accuracy on 43-class traffic sign recognition |
| 🎓 **Certificate** | Awarded 2026 |

---

## 🗂️ Projects at a Glance

| Week | Pillar | Project | Key Techniques |
|:----:|:-------|:--------|:---------------|
| 0 | 🔍 Search | **Degrees** | Breadth-first search on an actor/movie graph |
| 0 | 🔍 Search | **Tic-Tac-Toe** | Minimax, optimal adversarial play |
| 1 | 🧠 Knowledge | **Knights** | Propositional logic, model checking |
| 1 | 🧠 Knowledge | **Minesweeper** | Logical inference, knowledge-base updates |
| 2 | 🎲 Uncertainty | **PageRank** | Markov chains, sampling and iterative ranking |
| 2 | 🎲 Uncertainty | **Heredity** | Bayesian networks, joint probability distributions |
| 3 | ⚙️ Optimization | **Crossword** | Constraint satisfaction, AC-3, backtracking |
| 4 | 🤖 Learning | **Shopping** | k-nearest neighbors, scikit-learn |
| 4 | 🤖 Learning | **Nim** | Q-learning, epsilon-greedy exploration |
| 5 | 🖼️ Neural Networks | **Traffic** | Convolutional neural networks |
| 6 | 💬 Language | **Parser** | Context-free grammars, NLTK |
| 6 | 💬 Language | **Attention** | Scaled dot-product and multi-head attention |

---

## 🌟 Highlighted Projects

### 🚦 Traffic Sign Classifier

A convolutional neural network that classifies German traffic signs ([GTSRB](https://benchmark.ini.rub.de/)) into **43 categories** — from speed limits to pedestrian crossings.

| | |
|:---|:---|
| **Dataset** | 50,000+ labeled images |
| **Test accuracy** | 🏆 **98.93%** |
| **Stack** | TensorFlow · Keras · OpenCV · NumPy |

**Architecture**

```
Input (30×30×3) → Conv2D → MaxPool → Conv2D → MaxPool → Flatten → Dense(512) → Dropout → Softmax(43)
```

**Approach**

- Normalize and resize all images; augment with random shifts to improve generalization.
- Stack two convolution + pooling blocks to learn hierarchical spatial features (edges → shapes → sign symbols).
- A wide `Dense(512)` layer followed by **Dropout** combats overfitting on the large label space.
- Softmax outputs a probability distribution across all 43 sign classes.

<details>
<summary>🔧 <b>How it runs</b></summary>

```bash
cd traffic
python traffic.py gtsrb model.h5     # load data, train, save model, evaluate
```

The script accepts the dataset directory and an output filename for the trained `.h5` model, printing train/validation/test accuracy at each epoch.
</details>

---

### ✒️ Crossword Solver

Generates solutions to arbitrary crossword puzzles by modeling the grid as a **constraint satisfaction problem (CSP)** — each slot is a variable, each word that fits is a domain value, and overlapping letters are binary constraints.

- **Techniques:** node and arc consistency (**AC-3**), backtracking search with the **MRV** (minimum remaining values) heuristic, forward checking
- **Result:** solves all provided test puzzles in **fewer than 10 backtrack calls**
- **Stack:** Python (pure standard library)

**Pipeline**

```
Grid → extract variables → enforce node consistency → enforce arc consistency (AC-3)
     → backtracking search (MRV + degree heuristic) → rendered solution image
```

<details>
<summary>🔧 <b>How it runs</b></summary>

```bash
cd crossword
python generate.py data/structure1.txt data/words1.txt output.png
```

Pass a structure file (the grid layout) and a vocabulary file; the solver writes the completed puzzle as an image.
</details>

---

### ⚡ Attention Mechanism

A from-scratch implementation of the core building block behind modern Transformers such as **GPT** and **BERT**.

- **Components implemented:**
  - `softmax` — numerically stable probability normalization
  - `scaled_dot_product_attention` — `softmax(QKᵀ / √d_k)·V` with query, key, and value projections
  - `MultiHeadAttention` — parallel attention heads, each learning a different representation subspace, concatenated and projected back
- **Stack:** TensorFlow · NumPy

<details>
<summary>📐 <b>Why scaling matters</b></summary>

Dot products between high-dimensional vectors grow with dimension `d_k`, pushing softmax into saturation and shrinking gradients. Dividing by `√d_k` keeps the attention logits in a well-behaved range — the small detail that makes deep Transformers trainable.
</details>

---

### 🎮 Nim AI

A reinforcement learning agent that learns to play the game of Nim **optimally through pure self-play** — no game tree, no minimax, just experience.

- **Technique:** **Q-learning** — a `Q(s, a)` table updated after every move with reward `+1` for wins and `-1` for losses
- **Exploration:** **epsilon-greedy** policy (random moves early, exploitation later)
- **Result:** effectively **unbeatable after 10,000 self-play training games**
- **Stack:** Python (pure standard library)

<details>
<summary>🔧 <b>How it runs</b></summary>

```bash
cd nim
python play.py        # trains the agent, then lets you play against it
```
</details>

---

## 🗺️ Concept → Project Map

How the course's core ideas map onto the code in this repository:

| AI Concept | Where You'll Find It | One-Line Essence |
|:-----------|:---------------------|:-----------------|
| Breadth-First Search | `degrees/` | Explore a graph layer by layer to find the shortest connection path |
| Minimax & Alpha-Beta | `tictactoe/` | Assume a perfect opponent and pick moves that maximize your worst case |
| Propositional Logic | `knights/` | Encode "knights tell truth, knaves lie" as sentences and enumerate models |
| Knowledge-Based Inference | `minesweeper/` | Derive certain mines from subsets of known sentences |
| Markov Chains | `pagerank/` | Rank pages via random surfing or a fixed-point iterative solution |
| Bayesian Networks | `heredity/` | Compute joint probabilities over genes with conditional independence |
| Constraint Satisfaction | `crossword/` | Prune inconsistent domains with AC-3, then backtrack to a solution |
| Supervised Learning | `shopping/` | k-NN classifies purchase intent from behavioral features |
| Reinforcement Learning | `nim/` | Learn a value function from rewards, with no teacher |
| Deep Learning / CNNs | `traffic/` | Convolutions turn pixels into hierarchical visual features |
| Context-Free Grammars | `parser/` | Parse natural language into noun-phrase / verb-phrase trees |
| Transformers | `attention/` | Attend to every token simultaneously via queries, keys, and values |

---

## 🛠️ Tech Stack

| Category | Tools |
|:---------|:------|
| **Language** | Python |
| **Machine learning** | TensorFlow, Keras, scikit-learn |
| **Scientific computing** | NumPy |
| **Computer vision** | OpenCV |
| **NLP** | NLTK |
| **Concepts** | BFS · Minimax · Propositional Logic · Bayesian Networks · Constraint Satisfaction · k-NN · CNNs · Q-Learning · Context-Free Grammars · Transformers |

---

## 🚀 Getting Started

### Prerequisites

- Python **3.9** or newer
- `pip` (a virtual environment is recommended)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/<your-repo>.git   # TODO: replace with your repo URL
cd <your-repo>

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install tensorflow numpy opencv-python scikit-learn nltk
```

### Running a Project

Each project folder includes its own `README.md` with full instructions. The general pattern is:

```bash
cd <project-name>
python <main-file>.py
```

**Examples**

```bash
# Traffic sign classifier — dataset dir + output model path
cd traffic
python traffic.py gtsrb model.h5

# Crossword solver — structure + words + output image
cd crossword
python generate.py data/structure1.txt data/words1.txt output.png

# Nim — train via self-play, then challenge the agent
cd nim
python play.py
```

<details>
<summary>💡 <b>Tips</b></summary>

- **TensorFlow CPU vs GPU:** the `traffic` project trains much faster on a GPU; on CPU, reduce epochs if you just want a quick sanity check.
- **NLTK data:** the `parser` project may need `python -c "import nltk; nltk.download('punkt')"` on first run.
- **Reproducibility:** neural-network results vary slightly per run due to random initialization; the 98.93% figure reflects a full training run.
</details>

---

## 📁 Repository Structure

```
.
├── degrees/        # BFS actor connection finder
├── tictactoe/      # Unbeatable Minimax player
├── knights/        # Propositional logic puzzle solver
├── minesweeper/    # Logical inference agent
├── pagerank/       # Page ranking via sampling and iteration
├── heredity/       # Bayesian network for gene probabilities
├── crossword/      # CSP crossword generator
├── shopping/       # k-NN purchase intent predictor
├── nim/            # Q-learning game agent
├── traffic/        # CNN traffic sign classifier (98.93%)
├── parser/         # CFG sentence parser (NLTK)
└── attention/      # Transformer attention mechanism
```

Each folder contains the project source, its own `README.md`, and (where applicable) the required CS50 distribution data files.

---

## 🎓 Certificate

**CS50's Introduction to Artificial Intelligence with Python**
Harvard University · Completed **2026**

<!-- TODO: replace with the URL of your verified certificate
![Certificate](CERTIFICATE_URL_TODO)
-->

---

## 🤝 Academic Honesty

This repository is a record of **my own learning**, published to document how each algorithm was understood and built.

If you are currently taking CS50 AI, please follow the course's [Academic Honesty policy](https://cs50.harvard.edu/ai/honesty/): **do not copy** this code. Use it only as inspiration after you have submitted your own work — the real value of this course is in the struggle, not the solution.

---

<div align="center">

### ⭐ Built while learning how machines think.

**If this repository helped you, consider giving it a star — it means a lot.**

[![Star this repo](https://img.shields.io/badge/%E2%AD%90_Star-This%20Repository-FFD700?style=for-the-badge&logo=github&logoColor=white)](https://github.com/<your-username>/<your-repo>) <!-- TODO: replace with your repo URL -->

Made with 🧠 and ☕ · **12 projects · 6 pillars · 1 journey**

</div>
