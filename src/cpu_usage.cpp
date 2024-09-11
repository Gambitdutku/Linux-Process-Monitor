#include "../include/cpu_usage.h"
#include <iostream>
#include <fstream>
#include <string>
#include <thread>
#include <chrono>

// To calculate CPU usage
struct CpuData {
    unsigned long long idleTime, totalTime;
};

// gonna read from  /proc/stat
CpuData getCpuData() {
    std::ifstream statFile("/proc/stat");
    std::string cpu;
    unsigned long long user, nice, system, idle, iowait, irq, softirq;

    statFile >> cpu >> user >> nice >> system >> idle >> iowait >> irq >> softirq;
    statFile.close();

    unsigned long long totalTime = user + nice + system + idle + iowait + irq + softirq;
    CpuData data = {idle, totalTime};
    return data;
}

// Calculate from refferance
float calculateCpuUsage(const CpuData &prev, const CpuData &cur) {
    unsigned long long idleDiff = cur.idleTime - prev.idleTime;
    unsigned long long totalDiff = cur.totalTime - prev.totalTime;
    return 100.0f * (1.0f - (float)idleDiff / totalDiff);
}

extern "C" float getCpuUsage() {
    CpuData prevCpuData = getCpuData();
    std::this_thread::sleep_for(std::chrono::seconds(1));
    CpuData curCpuData = getCpuData();
    return calculateCpuUsage(prevCpuData, curCpuData);
}
