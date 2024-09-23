import sys
import os
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from libprocess import fetch_cpu_usage, get_total_memory, get_available_memory, fetch_disk_usage, fetch_network_usage

# Set up the plotting style
style_name = 'dark_background'
style.use(style_name)

fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2)

# Data storage
cpu_data = []
memory_data = []
disk_read_data = []
disk_write_data = []
network_data = []
time_data = []

def main():
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()

def animate(i):
    global time_data, cpu_data, memory_data, disk_read_data, disk_write_data, network_data

    # Fetch current metrics
    current_memory_av = get_available_memory()  # Available memory in MB
    current_memory_tot = get_total_memory()  # Total memory in MB
    current_time = time.strftime('%H:%M:%S')
    current_cpu = fetch_cpu_usage()

    # Fetch disk usage data
    disk_usage = fetch_disk_usage()
    current_disk_read = disk_usage['reads_completed']  # Modify as needed
    current_disk_write = disk_usage['writes_completed']  # Modify as needed
    current_network = fetch_network_usage()  # Placeholder; replace with actual value

    # Calculate used memory
    current_memory = current_memory_tot - current_memory_av

    # Append current time and metrics to lists
    time_data.append(current_time)
    cpu_data.append(current_cpu)
    memory_data.append(current_memory)
    disk_read_data.append(current_disk_read)
    disk_write_data.append(current_disk_write)
    network_data.append(current_network)
    
    # Limit lists to the last 20 points
    time_data = time_data[-20:]
    cpu_data = cpu_data[-20:]
    memory_data = memory_data[-20:]
    disk_read_data = disk_read_data[-20:]
    disk_write_data = disk_write_data[-20:]
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
    ax2.set_title(f'Memory Usage (Total: {current_memory_tot:.2f} MB)')
    ax2.set_ylabel('MB')

    ax3.plot(time_data, disk_read_data, label="Disk Read", color="green", marker='o')
    ax3.set_title('Disk Read (Count)')
    ax3.set_ylabel('Reads')

    ax4.plot(time_data, disk_write_data, label="Disk Write", color="red", marker='o')
    ax4.set_title('Disk Write (Count)')
    ax4.set_ylabel('Writes')

    ax5.plot(time_data, network_data, label="Network Usage", color="blue", marker='o')
    ax5.set_title('Network Usage')
    ax5.set_ylabel('Data')

    # Rotate x-ticks for readability
    for ax in [ax1, ax2, ax3, ax4, ax5]:
        ax.tick_params(axis='x', rotation=45)
        ax.set_xlabel('Time')

    # Adjust layout to ensure no overlap
    fig.tight_layout()

if __name__ == '__main__':
    main()

