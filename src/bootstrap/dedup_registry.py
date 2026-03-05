import hashlib
from typing import Dict, List

class DedupRegistry:
    def __init__(self):
        self.checkpoint_hashes = set()
        self.framework_versions = set()
        self.experiment_configs = set()
        
    def add_checkpoint(self, hash_value: str):
        self.checkpoint_hashes.add(hash_value)
        
    def is_checkpoint_duplicate(self, hash_value: str) -> bool:
        return hash_value in self.checkpoint_hashes
    
    def add_framework_version(self, version_string: str):
        self.framework_versions.add(version_string)
        
    def is_framework_duplicate(self, version_string: str) -> bool:
        return version_string in self.framework_versions
    
    def add_experiment_config(self, config_hash: str):
        self.experiment_configs.add(config_hash)
        
    def is_experiment_duplicate(self, config_hash: str) -> bool:
        return config_hash in self.experiment_configs

# Global registry instance
dedup_registry = DedupRegistry()