# Makefile

# Compiler and flags
CXX = g++
CXXFLAGS = -fPIC -shared

# Source files
SRCS = src/process_info.cpp src/cpu_usage.cpp src/memory_usage.cpp src/disk_usage.cpp src/network_usage.cpp

# Output shared object file
TARGET = libprocess_monitor.so

# Default target
all: $(TARGET)

# Rule to create the shared object
$(TARGET): $(SRCS)
	$(CXX) $(CXXFLAGS) $(SRCS) -o $(TARGET)

# Clean up build files
clean:
	rm -f $(TARGET)

