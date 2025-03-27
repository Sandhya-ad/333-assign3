#!/usr/bin/env python3
import subprocess
import signal

# Target executable
program = "./weak"

# Find the minimum buffer size that causes overflow
def find_buffer_size():
    print("Finding minimum buffer size that causes segfault...")
    
    # Try increasing buffer sizes until we get a crash
    for size in range(1, 100):
        print(f"Trying buffer size: {size}", end="\r")
        
        # Test if this buffer size causes a crash
        input_data = b"A" * size
        proc = subprocess.Popen(
            [program], 
            stdin=subprocess.PIPE, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE
        )
        proc.communicate(input_data)
        
        # Check if it crashed
        if proc.returncode == -signal.SIGSEGV:
            return size
    
    return None

# Main function
if __name__ == "__main__":
    buffer_size = find_buffer_size()
    if buffer_size:
        print(f"\nFound minimum buffer size: {buffer_size}")
    else:
        print("\nCould not find buffer size that causes segfault")