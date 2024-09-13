#include "../include/memory_usage.h"
#include <iostream>
#include <fstream>
#include <string>
#include <stdexcept>

extern "C" void getMemoryUsage(unsigned long* total, unsigned long* available) {
    // we're gonna use /proc/meminfo
    std::ifstream meminfo("/proc/meminfo");
    if (!meminfo.is_open()) {
        throw std::runtime_error("Failed to open /proc/meminfo");
    }

    std::string line;
    unsigned long memTotal = 0, memAvailable = 0;

    // Read through the file to find MemTotal and MemAvailable
    while (std::getline(meminfo, line)) {
        if (line.find("MemTotal:") == 0) {
            memTotal = std::stoul(line.substr(line.find_first_of("0123456789")));
        } else if (line.find("MemAvailable:") == 0) {
            memAvailable = std::stoul(line.substr(line.find_first_of("0123456789")));
        }
    }

    // Assign the values to the pointers passed in
    *total = memTotal;
    *available = memAvailable;
}

