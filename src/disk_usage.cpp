#include "../include/disk_usage.h"
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

extern "C" void getDiskUsage(
    unsigned long* reads_completed, 
    unsigned long* sectors_read, 
    unsigned long* writes_completed, 
    unsigned long* sectors_written) {
    
    std::ifstream diskstats("/proc/diskstats");
    std::string line;

    // Initialize output variables to 0
    *reads_completed = 0;
    *sectors_read = 0;
    *writes_completed = 0;
    *sectors_written = 0;

    // Get disks from /proc/diskstats
    while (std::getline(diskstats, line)) {
        if (line.find("sd") != std::string::npos || line.find("nvme") != std::string::npos) {
            std::istringstream iss(line);
            std::string device;
            unsigned long r_completed, r_merged, s_read, t_reading;
            unsigned long w_completed, w_merged, s_written, t_writing;
            unsigned long in_progress_io, io_ticks, time_in_queue;

            // Read data
            iss >> device >> r_completed >> r_merged >> s_read >> t_reading
                >> w_completed >> w_merged >> s_written >> t_writing
                >> in_progress_io >> io_ticks >> time_in_queue;

            // Aggregate results
            *reads_completed += r_completed;
            *sectors_read += s_read;
            *writes_completed += w_completed;
            *sectors_written += s_written;
        }
    }
}

