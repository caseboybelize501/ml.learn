import subprocess
import httpx
from typing import Dict, List

class ServiceStatus:
    def __init__(self, mlflow: bool, ray: bool, optuna: bool, inference_servers: List[str]):
        self.mlflow = mlflow
        self.ray = ray
        self.optuna = optuna
        self.inference_servers = inference_servers

async def detect_services() -> ServiceStatus:
    services = {
        "mlflow": False,
        "ray": False,
        "optuna": False,
        "inference_servers": []
    }
    
    # Check MLflow server
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("http://localhost:5000")
            if response.status_code == 200:
                services["mlflow"] = True
    except Exception:
        pass
    
    # Check Ray cluster
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("http://localhost:8265")
            if response.status_code == 200:
                services["ray"] = True
    except Exception:
        pass
    
    # Check Optuna storage
    try:
        # Try to connect to SQLite or PostgreSQL
        import sqlite3
        conn = sqlite3.connect("optuna.db")
        conn.close()
        services["optuna"] = True
    except Exception:
        pass
    
    # Check inference servers
    inference_ports = [11434, 8000, 1234, 8080]
    for port in inference_ports:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"http://localhost:{port}")
                if response.status_code == 200:
                    services["inference_servers"].append(str(port))
        except Exception:
            pass
    
    return ServiceStatus(
        mlflow=services["mlflow"],
        ray=services["ray"],
        optuna=services["optuna"],
        inference_servers=services["inference_servers"]
    )