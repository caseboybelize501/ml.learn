import os
import hashlib
from pathlib import Path
from typing import List, Dict

class Checkpoint:
    def __init__(self, path: str, hash_value: str, architecture: str, metrics: Dict):
        self.path = path
        self.hash = hash_value
        self.architecture = architecture
        self.metrics = metrics

class CheckpointRegistry:
    def __init__(self, checkpoints: List[Checkpoint]):
        self.checkpoints = checkpoints

def scan_checkpoints() -> CheckpointRegistry:
    checkpoint_paths = [
        "./checkpoints",
        "~/models",
        "/models",
        "~/.cache"
    ]
    
    checkpoints = []
    
    for path in checkpoint_paths:
        try:
            full_path = Path(path).expanduser()
            if full_path.exists():
                for file in full_path.rglob("*.pt"):
                    if file.is_file():
                        # Calculate hash
                        with open(file, 'rb') as f:
                            file_hash = hashlib.sha256(f.read()).hexdigest()
                        
                        # Parse architecture and metrics (simplified)
                        architecture = "unknown"
                        metrics = {}
                        
                        checkpoints.append(Checkpoint(
                            path=str(file),
                            hash_value=file_hash,
                            architecture=architecture,
                            metrics=metrics
                        ))
        except Exception as e:
            print(f"Error scanning {path}: {e}")
    
    return CheckpointRegistry(checkpoints)