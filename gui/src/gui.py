import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from libprocess import fetch_cpu_usage, _fetch_memory_info, fetch_disk_usage, fetch_network_usage, fetch_process_by_pid, get_total_memory, get_available_memory
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time
style_name = 'dark_background'
style.use(style_name)

fig,ax1 = plt.subplots()


fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2)

cpu_data = []
memory_data = []
disk_data = []
network_data = []
time_data = []  

# Fetch CPU usage from your function (replace this with the real function call)
def fetch_cpu_usage():
    from libprocess import fetch_cpu_usage
    return fetch_cpu_usage()  
def fetch_memory_usage():
    from libprocess import fetch_memory_usage
    return fetch_memory_usage()  
#from libprocess import fetch_cpu_usage, fetch_memory_usage, fetch_disk_usage, fetch_network_usage, fetch_process_by_pid
def get_total_memory():
    from libprocess import get_total_memory
    return get_total_memory()  
def get_total_memory():
    from libprocess import get_available_memory
    return get_available_memory()  

def fetch_disk_usage():
    from libprocess import fetch_disk_usage
    return fetch_disk_usage()  
def fetch_network_usage():
    from libprocess import fetch_network_usage
    return fetch_network_usage()  

def main():
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()

def animate(i):
    global time_data, cpu_data, memory_data, disk_data, network_data
    current_memory_av = get_available_memory()
    current_memory_tot = get_total_memory()
    print(current_memory_av)
    print(current_memory_tot)
    # Fetch current time and metrics
    current_time = time.strftime('%H:%M:%S')
    current_cpu = fetch_cpu_usage()
    current_memory = current_memory_av
    current_disk = fetch_disk_usage()  # Use disk usage for both read and write plots
    current_network = fetch_network_usage()

    # Append current time and metrics to lists
    time_data.append(current_time)
    cpu_data.append(current_cpu)
    memory_data.append(current_memory)
    disk_data.append(current_disk)
    network_data.append(current_network)
    
    # Limit lists to the last 20 points
    time_data = time_data[-20:]
    cpu_data = cpu_data[-20:]
    memory_data = memory_data[-20:]
    disk_data = disk_data[-20:]
    network_data = network_data[-20:]

    # Clear each subplot before plotting new data
    ax1.clear()
    ax2.clear()
    ax3.clear()
    ax4.clear()
    ax5.clear()
    ax6.clear()

    # Plot data on each subplot
    ax1.plot(time_data, cpu_data, label="CPU Usage", color="cyan", marker='o')
    ax1.set_title('CPU Usage')
    ax1.set_ylabel('%')

    ax2.plot(time_data, memory_data, label="Memory Usage", color="magenta", marker='o')
    ax2.set_title('Memory Usage')
    ax2.set_ylabel('%')

    ax3.plot(time_data, disk_data, label="Disk Usage", color="yellow", marker='o')
    ax3.set_title('Disk Usage')
    ax3.set_ylabel('%')

    ax4.plot(time_data, network_data, label="Network Usage", color="blue", marker='o')
    ax4.set_title('Network Usage')
    ax4.set_ylabel('%')

    # Using the same disk data for both read and write plots
    ax5.plot(time_data, disk_data, label="Disk Read", color="green", marker='o')
    ax5.set_title('Disk Read')
    ax5.set_ylabel('MB/s')

    ax6.plot(time_data, disk_data, label="Disk Write", color="red", marker='o')
    ax6.set_title('Disk Write')
    ax6.set_ylabel('MB/s')

    # Rotate x-ticks for readability
    for ax in [ax1, ax2, ax3, ax4, ax5, ax6]:
        ax.tick_params(axis='x', rotation=45)
        ax.set_xlabel('Time')

    # Adjust layout to ensure no overlap
    fig.tight_layout()

if __name__ == '__main__':
    main()
