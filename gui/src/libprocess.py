import ctypes
import os

# Load the shared object
lib_path = os.path.join(os.path.dirname(__file__), '../../lib/libprocess_monitor.so')
lib = ctypes.CDLL(lib_path)

# Define functions
lib.getCpuUsage.restype = ctypes.c_float
lib.getMemoryUsage.restype = None
lib.getDiskUsage.restype = None
lib.getNetworkUsage.restype = None
lib.getProcessByPid.argtypes = [ctypes.c_int]
lib.getProcessByPid.restype = None
lib.killProcess.argtypes = [ctypes.c_int]
lib.killProcess.restype = ctypes.c_int

def fetch_cpu_usage():
    return lib.getCpuUsage()

def fetch_memory_usage():
    lib.getMemoryUsage()

def fetch_disk_usage():
    lib.getDiskUsage()

def fetch_network_usage():
    lib.getNetworkUsage()

def fetch_process_by_pid(pid):
    lib.getProcessByPid(pid)

def kill_process(pid):
    return lib.killProcess(pid)

