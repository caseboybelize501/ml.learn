import asyncio
from fastapi import FastAPI
from src.bootstrap.system_scanner import run_system_scan
from src.planner.ml_planner import plan_experiment
from src.agents.data_agent import DataAgent
from src.agents.architecture_agent import ArchitectureAgent
from src.agents.train_agent import TrainAgent
from src.agents.eval_agent import EvalAgent
from src.agents.hyper_agent import HyperAgent
from src.agents.learn_agent import LearnAgent

app = FastAPI(title="Autonomous ML Jarvis", version="0.1.0")

@app.on_event("startup")
async def startup_event():
    print("Starting System Scan...")
    system_profile = await run_system_scan()
    print(f"System Profile: {system_profile}")

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "gpu_detected": True,
        "frameworks_loaded": True,
        "checkpoints_indexed": True,
        "experiments_cached": True,
        "consecutive_eval_passes": 0,
        "meta_accuracy": 0.0
    }

@app.post("/api/experiment/start")
async def start_experiment(request: dict):
    # Placeholder for experiment pipeline
    return {"status": "experiment started", "details": request}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)