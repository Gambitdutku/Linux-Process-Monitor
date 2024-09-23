#ifndef DISK_USAGE_H
#define DISK_USAGE_H

#include <cstdint>  // For uint64_t

extern "C" {
    void getDiskUsage(
        uint64_t* reads_completed, 
        uint64_t* sectors_read, 
        uint64_t* writes_completed, 
        uint64_t* sectors_written
    );
}

#endif

