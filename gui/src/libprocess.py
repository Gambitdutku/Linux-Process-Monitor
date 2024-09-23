import ctypes
import os

# Load the shared object
lib_path = os.path.join(os.path.dirname(__file__), '../../lib/libprocess_monitor.so')
lib = ctypes.CDLL(lib_path)

# Define function signatures
lib.getCpuUsage.restype = ctypes.c_float
lib.getDiskUsage.argtypes = [
    ctypes.POINTER(ctypes.c_ulong),  # reads_completed
    ctypes.POINTER(ctypes.c_ulong),  # sectors_read
    ctypes.POINTER(ctypes.c_ulong),  # writes_completed
    ctypes.POINTER(ctypes.c_ulong)   # sectors_written
]
lib.getDiskUsage.restype = None
lib.getNetworkUsage.restype = None
lib.getProcessByPid.argtypes = [ctypes.c_int]
lib.getProcessByPid.restype = None
lib.killProcess.argtypes = [ctypes.c_int]
lib.killProcess.restype = ctypes.c_int
lib.getMemoryUsage.argtypes = [ctypes.POINTER(ctypes.c_ulong), ctypes.POINTER(ctypes.c_ulong)]
lib.getMemoryUsage.restype = None

# Global memory variables
_mem_total = ctypes.c_ulong()
_mem_available = ctypes.c_ulong()

def fetch_cpu_usage():
    """Fetch CPU usage from the shared library."""
    return lib.getCpuUsage()

def fetch_disk_usage():
    """Fetch disk usage from the shared library."""
    reads_completed = ctypes.c_ulong()
    sectors_read = ctypes.c_ulong()
    writes_completed = ctypes.c_ulong()
    sectors_written = ctypes.c_ulong()

    # Call the C++ function
    lib.getDiskUsage(ctypes.byref(reads_completed), ctypes.byref(sectors_read),
                     ctypes.byref(writes_completed), ctypes.byref(sectors_written))

    # Return the results
    return {
        "reads_completed": reads_completed.value,
        "sectors_read": sectors_read.value,
        "writes_completed": writes_completed.value,
        "sectors_written": sectors_written.value,
    }

def fetch_network_usage():
    """Fetch network usage from the shared library."""
    lib.getNetworkUsage()
    # Consider returning a meaningful value if applicable

def fetch_process_by_pid(pid):
    """Fetch process information by PID."""
    lib.getProcessByPid(pid)

def kill_process(pid):
    """Kill a process by its PID."""
    return lib.killProcess(pid)

def _fetch_memory_info():
    """Fetch memory information from the shared library."""
    global _mem_total, _mem_available
    try:
        lib.getMemoryUsage(ctypes.byref(_mem_total), ctypes.byref(_mem_available))
    except Exception as e:
        print(f"Error fetching memory info: {e}")

def get_total_memory():
    """Get total memory in MB."""
    _fetch_memory_info()
    return _mem_total.value / 1024  # Convert to MB

def get_available_memory():
    """Get available memory in MB."""
    _fetch_memory_info()
    return _mem_available.value / 1024  # Convert to MB

