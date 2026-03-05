import chromadb
from typing import Dict, List, Any

class ExperimentStore:
    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection("experiments")
        
    def add_experiment(self, experiment_data: Dict[str, Any]) -> str:
        # Add experiment to ChromaDB
        experiment_id = str(len(self.collection.get()))
        
        self.collection.add(
            documents=[str(experiment_data)],
            metadatas=[{
                "id": experiment_id,
                "task_type": experiment_data.get("task_type", "unknown"),
                "dataset_fingerprint": experiment_data.get("dataset_fingerprint", "unknown")
            }],
            ids=[experiment_id]
        )
        
        return experiment_id
    
    def query_experiments(self, query_text: str, limit: int = 5) -> List[Dict[str, Any]]:
        # Semantic search across experiments
        results = self.collection.query(
            query_texts=[query_text],
            n_results=limit
        )
        
        return results["documents"]