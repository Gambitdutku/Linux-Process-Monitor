#include "../include/memory_usage.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <cstdint>

constexpr const char* meminfo_file = "/proc/meminfo";

extern "C" void getMemoryUsage(unsigned long* total, unsigned long* available) {
    std::ifstream ifs(meminfo_file);
    if (!ifs.good()) {
        throw std::runtime_error("Error: unable to open memory-info file.");
    }

    std::string line, label;
    std::uint64_t memTotal = 0, memAvailable = 0; 
    while (std::getline(ifs, line)) {
        std::stringstream ss{line};    
        ss >> label;

        if (label == "MemTotal:") {
            ss >> memTotal; // Read the value directly
        }
        if (label == "MemAvailable:") {
            ss >> memAvailable; // Read the value directly
        }
    }

    *total = memTotal;
    *available = memAvailable;
}

