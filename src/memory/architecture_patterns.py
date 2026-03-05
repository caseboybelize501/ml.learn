from typing import Dict, List, Any

class ArchitecturePatternLibrary:
    def __init__(self):
        self.patterns = {}
        
    def add_pattern(self, task_type: str, dataset_size: str, vram_gb: int,
                   architecture_class: str, performance_metrics: Dict[str, float]):
        key = f"{task_type}_{dataset_size}_{vram_gb}gb"
        
        if key not in self.patterns:
            self.patterns[key] = []
            
        self.patterns[key].append({
            "architecture_class": architecture_class,
            "performance_metrics": performance_metrics
        })
    
    def get_patterns(self, task_type: str, dataset_size: str, vram_gb: int) -> List[Dict[str, Any]]:
        key = f"{task_type}_{dataset_size}_{vram_gb}gb"
        return self.patterns.get(key, [])