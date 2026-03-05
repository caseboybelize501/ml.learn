import json
from typing import Dict, List, Any
from src.bootstrap.system_profile import MLSystemProfile

class ArchitectureAgent:
    def __init__(self, system_profile: MLSystemProfile):
        self.system_profile = system_profile
        
    def design_architectures(self, task_type: str, data_profile: Dict,
                           hardware_constraints: Dict) -> Dict[str, Any]:
        # Get available VRAM
        vram_total = sum([dev["vram_total"] for dev in self.system_profile.gpu_profile.devices])
        usable_vram = int(vram_total * 0.85)  # 15% safety margin
        
        # Determine architecture candidates based on task and hardware
        candidates = []
        
        if task_type == "image_classification":
            candidates = self._design_image_classification_architectures(usable_vram)
        elif task_type == "text_classification":
            candidates = self._design_text_classification_architectures(usable_vram)
        elif task_type == "regression":
            candidates = self._design_regression_architectures(usable_vram)
        
        return {
            "candidates": candidates,
            "hardware_constraints": hardware_constraints
        }
    
    def _design_image_classification_architectures(self, usable_vram: int) -> List[Dict]:
        # Placeholder for architecture design logic
        return [
            {
                "name": "EfficientNet-B0",
                "architecture_description": "MobileNet-based CNN with efficient attention",
                "estimated_params_M": 5.3,
                "estimated_vram_gb": 1.2,
                "rationale": "Good balance of accuracy and efficiency for small VRAM",
                "memory_pattern_used": "image_classification_small_vram",
                "expected_eval_strengths": ["accuracy", "latency"],
                "expected_eval_weaknesses": ["robustness"]
            },
            {
                "name": "ResNet-18",
                "architecture_description": "Standard ResNet with batch normalization",
                "estimated_params_M": 11.7,
                "estimated_vram_gb": 2.5,
                "rationale": "Well-established architecture for image classification",
                "memory_pattern_used": "image_classification_medium_vram",
                "expected_eval_strengths": ["accuracy", "calibration"],
                "expected_eval_weaknesses": ["throughput"]
            }
        ]
    
    def _design_text_classification_architectures(self, usable_vram: int) -> List[Dict]:
        return [
            {
                "name": "DistilBERT",
                "architecture_description": "Lightweight BERT variant with 40% fewer parameters",
                "estimated_params_M": 67.5,
                "estimated_vram_gb": 1.8,
                "rationale": "Efficient transformer for text classification",
                "memory_pattern_used": "text_classification_small_vram",
                "expected_eval_strengths": ["accuracy", "calibration"],
                "expected_eval_weaknesses": ["latency"]
            }
        ]
    
    def _design_regression_architectures(self, usable_vram: int) -> List[Dict]:
        return [
            {
                "name": "MLP-3L",
                "architecture_description": "Three-layer feedforward neural network",
                "estimated_params_M": 0.5,
                "estimated_vram_gb": 0.2,
                "rationale": "Simple architecture for regression tasks",
                "memory_pattern_used": "regression_small_vram",
                "expected_eval_strengths": ["accuracy", "latency"],
                "expected_eval_weaknesses": ["robustness"]
            }
        ]