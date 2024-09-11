#include <signal.h>
#include <unistd.h>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include "../include/process_info.h"


// Function to get process details by PID
extern "C" void getProcessByPid(int pid) {
    std::ostringstream path_stream;
    path_stream << "/proc/" << pid << "/status";
    std::string path = path_stream.str();

    std::ifstream file(path);
    if (!file.is_open()) {
        std::cerr << "Unable to open file: " << path << std::endl;
        return;
    }

    std::string line;
    while (std::getline(file, line)) {
        std::cout << line << std::endl;
    }

    file.close();
}

// Function to get CPU usage of a specific process by PID
extern "C" float getProcessCpuUsage(int pid) {
    std::cout << "CPU usage for PID " << pid << " is not yet implemented." << std::endl;
    return 0.0f; // Dummy return
}

// Function to get memory usage of a specific process by PID
extern "C" void getProcessMemoryUsage(int pid) {
    std::cout << "Memory usage for PID " << pid << " is not yet implemented." << std::endl;
}

// Function to get disk usage of a specific process by PID
extern "C" void getProcessDiskUsage(int pid) {
    std::cout << "Disk usage for PID " << pid << " is not yet implemented." << std::endl;
}

// Function to kill process by PID
extern "C" int killProcess(int pid) {
    if (kill(pid, SIGKILL) == 0) {
        return 0; // Success
    } else {
        return -1; // Failure
    }
}

