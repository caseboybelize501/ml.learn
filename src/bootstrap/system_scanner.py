import asyncio
from src.bootstrap.gpu_profiler import profile_gpus
from src.bootstrap.framework_scanner import scan_frameworks
from src.bootstrap.checkpoint_scanner import scan_checkpoints
from src.bootstrap.service_detector import detect_services
from src.bootstrap.experiment_registry import ExperimentRegistry
from src.bootstrap.system_profile import MLSystemProfile

async def run_system_scan():
    print("Running System Scan...")
    
    # Profile GPUs
    gpu_profile = await profile_gpus()
    
    # Scan installed frameworks
    framework_profile = scan_frameworks()
    
    # Scan existing checkpoints
    checkpoint_registry = scan_checkpoints()
    
    # Detect running services
    service_status = detect_services()
    
    # Create system profile
    system_profile = MLSystemProfile(
        gpu_profile=gpu_profile,
        framework_profile=framework_profile,
        checkpoint_registry=checkpoint_registry,
        service_status=service_status
    )
    
    print(f"System Profile Created: {system_profile.__dict__}")
    return system_profile