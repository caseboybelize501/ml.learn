# Autonomous ML Experiment Jarvis

A self-learning autonomous machine learning experimentation system that designs, runs, evaluates, and iterates experiments with 10-stage validation cycles.

## Features

- **System Scan**: Complete infrastructure inventory (GPUs, frameworks, checkpoints)
- **Deduplication**: Model checkpoint, package, and experiment deduplication
- **10-Stage Evaluation**: Accuracy, calibration, robustness, fairness, latency, throughput, memory footprint, adversarial, distribution shift, regression
- **Adaptive Hyperparameter Optimization**: Memory-warm Optuna search with adaptive mutation
- **4-Layer Self-Learning Memory**: Experiment results, hyperparameter effectiveness, architecture patterns, meta-learning
- **Production Ready**: 7 consecutive passing cycles required for production status

## Architecture


Voice/Chat → Planner LLM → Agent Controller
    ↓
Data Agent → Architecture Agent → Train Agent → Eval Agent
    ↓
Hyper Agent → Learn Agent


## System Requirements

- Python 3.10+
- Docker (for training sandboxes)
- GPU with CUDA support (optional but recommended)

## Installation

bash
pip install -r requirements.txt


## Quick Start

bash
python src/main.py


## API Endpoints

- `GET /health` - System health check
- `POST /api/experiment/start` - Start new experiment
- `GET /api/system/profile` - Get system profile
- `GET /api/memory/experiments` - Browse experiment memory
- `GET /api/memory/hyperparams` - Query hyperparameter graph

## Memory Layers

1. **Experiment Results Memory**: Store and query past experiment results
2. **Hyperparameter Effectiveness Graph**: Neo4j graph of hyperparam → metric relationships
3. **Architecture Pattern Library**: Known-good architectures per task + hardware combo
4. **Meta-Learning Index**: Search strategy classifier based on hardware/dataset combinations

## License

MIT