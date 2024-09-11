#include "../include/disk_usage.h"
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

extern "C" void getDiskUsage() {
    std::ifstream diskstats("/proc/diskstats");
    std::string line;

    // get disks from /proc/diskstats
    while (std::getline(diskstats, line)) {

        if (line.find("sd") != std::string::npos || line.find("nvme") != std::string::npos) {
            std::istringstream iss(line);
            std::string device;
            unsigned long reads_completed, reads_merged, sectors_read, time_reading;
            unsigned long writes_completed, writes_merged, sectors_written, time_writing;
            unsigned long in_progress_io, io_ticks, time_in_queue;

            // let's read data
            iss >> device >> reads_completed >> reads_merged >> sectors_read >> time_reading
                >> writes_completed >> writes_merged >> sectors_written >> time_writing
                >> in_progress_io >> io_ticks >> time_in_queue;

            // giving out output
            std::cout << "Disk: " << device << std::endl;
            std::cout << "Reads Completed: " << reads_completed << std::endl;
            std::cout << "Sectors Read: " << sectors_read << std::endl;
            std::cout << "Writes Completed: " << writes_completed << std::endl;
            std::cout << "Sectors Written: " << sectors_written << std::endl;
            std::cout << "Time Reading (ms): " << time_reading << std::endl;
            std::cout << "Time Writing (ms): " << time_writing << std::endl;
            std::cout << "In Progress I/O: " << in_progress_io << std::endl;
            std::cout << "I/O Ticks (ms): " << io_ticks << std::endl;
            std::cout << "Time in Queue (ms): " << time_in_queue << std::endl;
        }
    }
}
