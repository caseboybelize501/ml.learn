import pynvml
from typing import Dict, List

class GPUProfile:
    def __init__(self, device_count: int, devices: List[Dict]):
        self.device_count = device_count
        self.devices = devices

async def profile_gpus() -> GPUProfile:
    try:
        pynvml.nvmlInit()
        device_count = pynvml.nvmlDeviceGetCount()
        devices = []
        
        for i in range(device_count):
            handle = pynvml.nvmlDeviceGetHandleByIndex(i)
            name = pynvml.nvmlDeviceGetName(handle)
            
            # Get memory info
            mem_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
            vram_total = mem_info.total // (1024**2)  # MB
            vram_free = mem_info.free // (1024**2)  # MB
            
            # Get compute capability
            try:
                cc = pynvml.nvmlDeviceGetCudaComputeCapability(handle)
                compute_capability = f"{cc[0]}.{cc[1]}"
            except:
                compute_capability = "Unknown"
            
            devices.append({
                "name": name,
                "vram_total": vram_total,
                "vram_free": vram_free,
                "compute_capability": compute_capability
            })
        
        return GPUProfile(device_count, devices)
    except Exception as e:
        print(f"Error profiling GPUs: {e}")
        return GPUProfile(0, [])