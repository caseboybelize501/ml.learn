import torch
import jax
import sklearn
import tensorflow
import xgboost
import lightgbm
import catboost
from typing import Dict

class FrameworkProfile:
    def __init__(self, frameworks: Dict):
        self.frameworks = frameworks

def scan_frameworks() -> FrameworkProfile:
    frameworks = {}
    
    try:
        frameworks["torch"] = {
            "version": torch.__version__,
            "cuda_available": torch.cuda.is_available(),
            "cuda_version": torch.version.cuda if torch.cuda.is_available() else None,
            "cudnn_version": torch.backends.cudnn.version() if torch.cuda.is_available() else None
        }
    except Exception as e:
        print(f"Error scanning PyTorch: {e}")
    
    try:
        frameworks["jax"] = {
            "version": jax.__version__,
            "backend": jax.default_backend()
        }
    except Exception as e:
        print(f"Error scanning JAX: {e}")
    
    try:
        frameworks["sklearn"] = {"version": sklearn.__version__}
    except Exception as e:
        print(f"Error scanning scikit-learn: {e}")
    
    try:
        frameworks["tensorflow"] = {"version": tensorflow.__version__}
    except Exception as e:
        print(f"Error scanning TensorFlow: {e}")
    
    try:
        frameworks["xgboost"] = {"version": xgboost.__version__}
    except Exception as e:
        print(f"Error scanning XGBoost: {e}")
    
    try:
        frameworks["lightgbm"] = {"version": lightgbm.__version__}
    except Exception as e:
        print(f"Error scanning LightGBM: {e}")
    
    try:
        frameworks["catboost"] = {"version": catboost.__version__}
    except Exception as e:
        print(f"Error scanning CatBoost: {e}")
    
    return FrameworkProfile(frameworks)