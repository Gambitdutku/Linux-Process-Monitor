import ctypes
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Load the shared object file
lib = ctypes.CDLL('./lib/libprocess_monitor.so')

# Define argument and return types for functions from the .so file
lib.getCpuUsage.restype = ctypes.c_double
lib.getMemoryUsage.restype = ctypes.c_double
lib.getDiskUsage.restype = ctypes.c_double
lib.getNetworkUsage.restype = ctypes.c_double
lib.getProcessByPid.argtypes = [ctypes.c_int]
lib.getProcessByPid.restype = ctypes.c_char_p

class SystemMonitorApp:
    def __init__(self):
        self.time_data = []
        self.cpu_data = []
        self.memory_data = []
        self.disk_data = []
        self.network_data = []

        # Set up the plot
        self.fig, (self.cpu_ax, self.memory_ax, self.disk_ax, self.network_ax) = plt.subplots(4, 1, figsize=(10, 8))
        self.fig.suptitle('System Resource Usage')

        # Initialize the plots
        self.cpu_line, = self.cpu_ax.plot([], [], label='CPU Usage')
        self.memory_line, = self.memory_ax.plot([], [], label='Memory Usage')
        self.disk_line, = self.disk_ax.plot([], [], label='Disk Usage')
        self.network_line, = self.network_ax.plot([], [], label='Network Usage')

        self.cpu_ax.legend()
        self.memory_ax.legend()
        self.disk_ax.legend()
        self.network_ax.legend()

        # Set axis labels
        self.cpu_ax.set_ylabel('CPU Usage (%)')
        self.memory_ax.set_ylabel('Memory Usage (MB)')
        self.disk_ax.set_ylabel('Disk Usage (%)')
        self.network_ax.set_ylabel('Network Usage (MB/s)')

        # Set x-axis labels
        self.cpu_ax.set_xlabel('Time')
        self.memory_ax.set_xlabel('Time')
        self.disk_ax.set_xlabel('Time')
        self.network_ax.set_xlabel('Time')

        self.anim = FuncAnimation(self.fig, self.update_chart, interval=1000)

        plt.show()

    def update_chart(self, frame):
        current_time = time.strftime('%H:%M:%S')
        self.time_data.append(current_time)

        # Fetch real data from the shared object library
        cpu_usage = lib.getCpuUsage()
        memory_usage = lib.getMemoryUsage()
        disk_usage = lib.getDiskUsage()
        network_usage = lib.getNetworkUsage()

        self.cpu_data.append(cpu_usage)
        self.memory_data.append(memory_usage)
        self.disk_data.append(disk_usage)
        self.network_data.append(network_usage)

        # Update the plots with real data
        self.update_plot(self.cpu_line, self.cpu_data, 'CPU Usage (%)', self.cpu_ax)
        self.update_plot(self.memory_line, self.memory_data, 'Memory Usage (MB)', self.memory_ax)
        self.update_plot(self.disk_line, self.disk_data, 'Disk Usage (%)', self.disk_ax)
        self.update_plot(self.network_line, self.network_data, 'Network Usage (MB/s)', self.network_ax)

    def update_plot(self, line, data, ylabel, ax):
        line.set_data(range(len(data)), data)
        ax.relim()
        ax.autoscale_view()

if __name__ == "__main__":
    app = SystemMonitorApp()

