#include "../include/memory_usage.h"
#include <iostream>
#include <fstream>
#include <string>

// We're gonna use /proc/meminfo
extern "C" void getMemoryUsage() {
    std::ifstream meminfo("/proc/meminfo");
    std::string line;
    unsigned long memTotal = 0, memAvailable = 0;

    while (std::getline(meminfo, line)) {
        if (line.find("MemTotal:") == 0) {
            memTotal = std::stoul(line.substr(line.find_first_of("0123456789")));
        } else if (line.find("MemAvailable:") == 0) {
            memAvailable = std::stoul(line.substr(line.find_first_of("0123456789")));
        }
    }

    unsigned long memUsed = memTotal - memAvailable;
    std::cout << "Total Memory: " << memTotal / 1024 << " MB\n";
    std::cout << "Used Memory: " << memUsed / 1024 << " MB\n";
}
