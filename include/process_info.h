#ifndef PROCESS_INFO_H
#define PROCESS_INFO_H

extern "C" void getProcessByPid(int pid);

extern "C" float getProcessCpuUsage(int pid);

extern "C" void getProcessMemoryUsage(int pid);

extern "C" void getProcessDiskUsage(int pid);

extern "C" int killProcess(int pid);

#endif // PROCESS_INFO_H

