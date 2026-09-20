<div align="center">

# 🧠 CS50 AI: Artificial Intelligence with Python

**Complete solutions to Harvard University's CS50 AI, covering search, logic, probability, optimization, machine learning, neural networks, and language.**

[![Harvard CS50 AI](https://img.shields.io/badge/Harvard-CS50%20AI-A51C30?style=for-the-badge&logo=harvard&logoColor=white)](https://cs50.harvard.edu/ai/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)

[Overview](#overview) · [Projects](#projects) · [Highlights](#highlighted-projects) · [Getting Started](#getting-started) · [Structure](#repository-structure) · [Certificate](#certificate)

</div>

---

## Overview

This repository contains my solutions to all **12 projects** of [CS50's Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/). Each project implements a core AI concept from first principles, from graph search and logical inference to convolutional networks and attention mechanisms.

| | |
|---|---|
| **Projects completed** | 12 / 12 |
| **Language** | Python 3 |
| **Libraries** | TensorFlow, Keras, scikit-learn, NumPy, OpenCV, NLTK |
| **Best result** | 98.93% test accuracy on 43-class traffic sign recognition |

---

## Projects

| Week | Topic | Project | Key Techniques |
|:----:|-------|---------|----------------|
| 0 | Search | **Degrees** | Breadth-first search on an actor/movie graph |
| 0 | Search | **Tic-Tac-Toe** | Minimax, optimal adversarial play |
| 1 | Knowledge | **Knights** | Propositional logic, model checking |
| 1 | Knowledge | **Minesweeper** | Logical inference, knowledge base updates |
| 2 | Uncertainty | **PageRank** | Markov chains, sampling and iterative ranking |
| 2 | Uncertainty | **Heredity** | Bayesian networks, joint probability |
| 3 | Optimization | **Crossword** | Constraint satisfaction, AC-3, backtracking |
| 4 | Learning | **Shopping** | k-nearest neighbors, scikit-learn |
| 4 | Learning | **Nim** | Q-learning, epsilon-greedy exploration |
| 5 | Neural Networks | **Traffic** | Convolutional neural networks |
| 6 | Language | **Parser** | Context-free grammars, NLTK |
| 6 | Language | **Attention** | Scaled dot-product and multi-head attention |

---

## Highlighted Projects

### Traffic Sign Classifier

A convolutional neural network that classifies German traffic signs (GTSRB) into 43 categories.

| | |
|---|---|
| **Dataset** | 50,000+ labeled images |
| **Test accuracy** | **98.93%** |
| **Stack** | TensorFlow, Keras, OpenCV, NumPy |

**Architecture**

```
Input → Conv2D → MaxPool → Conv2D → MaxPool → Flatten → Dense(512) → Dropout → Softmax(43)
```

### Crossword Solver

Generates solutions to arbitrary crossword puzzles by modeling the grid as a constraint satisfaction problem.

- **Techniques:** node and arc consistency (AC-3), backtracking search, MRV heuristic
- **Result:** solves all provided test puzzles in fewer than 10 backtrack calls
- **Stack:** Python

### Attention Mechanism

Implements the core building block behind modern Transformers such as GPT and BERT.

- **Components:** `softmax`, `scaled_dot_product_attention`, `MultiHeadAttention`
- **Stack:** TensorFlow, NumPy

### Nim AI

A reinforcement learning agent that learns to play Nim optimally through self-play.

- **Technique:** Q-learning with an epsilon-greedy policy
- **Result:** unbeatable after 10,000 self-play training games
- **Stack:** Python

---

## Tech Stack

| Category | Tools |
|----------|-------|
| **Language** | Python |
| **Machine learning** | TensorFlow, Keras, scikit-learn |
| **Scientific computing** | NumPy |
| **Computer vision** | OpenCV |
| **NLP** | NLTK |
| **Concepts** | BFS, Minimax, Propositional Logic, Bayesian Networks, Constraint Satisfaction, k-NN, CNNs, Q-Learning, Context-Free Grammars, Transformers |

---

## Getting Started

### Prerequisites

- Python 3.9 or newer
- `pip` (and optionally a virtual environment)

### Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

# (Optional) create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Install dependencies
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
# Traffic sign classifier
cd traffic
python traffic.py gtsrb model.h5

# Crossword solver
cd crossword
python generate.py data/structure1.txt data/words1.txt output.png

# Nim (train, then play)
cd nim
python play.py
```

---

## Repository Structure

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

---

## Certificate

**CS50's Introduction to Artificial Intelligence with Python**
Harvard University · Completed 2026

---

## Academic Honesty

This repository is a record of my own learning. If you are currently taking CS50 AI, please follow the course's [Academic Honesty policy](https://cs50.harvard.edu/ai/honesty/) and use this code for reference only.

---

<div align="center">

**Built while learning how machines think.**

If you found this useful, consider giving it a star.

</div>
