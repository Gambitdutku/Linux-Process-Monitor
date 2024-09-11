#include <iostream>
#include <fstream>
#include <string>
#include "../include/network_usage.h"

// Function to get network usage for all interfaces
extern "C" void getNetworkUsage() {
    std::ifstream file("/proc/net/dev");
    if (!file.is_open()) {
        std::cerr << "Unable to open file: /proc/net/dev" << std::endl;
        return;
    }

    std::string line;
    // Skip the first two lines which contain headers
    std::getline(file, line);
    std::getline(file, line);

    while (std::getline(file, line)) {
        std::cout << line << std::endl;
    }

    file.close();
}

