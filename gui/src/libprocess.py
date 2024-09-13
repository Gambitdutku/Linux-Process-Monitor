import ctypes
import os

# Load the shared object
lib_path = os.path.join(os.path.dirname(__file__), '../../lib/libprocess_monitor.so')
lib = ctypes.CDLL(lib_path)

# Define functions
lib.getCpuUsage.restype = ctypes.c_float
lib.getDiskUsage.restype = None
lib.getNetworkUsage.restype = None
lib.getProcessByPid.argtypes = [ctypes.c_int]
lib.getProcessByPid.restype = None
lib.killProcess.argtypes = [ctypes.c_int]
lib.killProcess.restype = ctypes.c_int
lib.getMemoryUsage.argtypes = [ctypes.POINTER(ctypes.c_ulong), ctypes.POINTER(ctypes.c_ulong)]
lib.getMemoryUsage.restype = None
_mem_total = ctypes.c_ulong()
_mem_available = ctypes.c_ulong()



def fetch_cpu_usage():
    return lib.getCpuUsage()


def fetch_disk_usage():
    lib.getDiskUsage()

def fetch_network_usage():
    lib.getNetworkUsage()

def fetch_process_by_pid(pid):
    lib.getProcessByPid(pid)

def kill_process(pid):
    return lib.killProcess(pid)
def _fetch_memory_info():
    global _mem_total, _mem_available
    lib.getMemoryUsage(ctypes.byref(_mem_total), ctypes.byref(_mem_available))

def get_total_memory():
    _fetch_memory_info()
    return _mem_total.value / 1024  # covert to MB

def get_available_memory():
    _fetch_memory_info()
    return _mem_available.value / 1024  # covert to MB
