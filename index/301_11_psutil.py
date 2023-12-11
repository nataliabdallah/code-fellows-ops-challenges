#!/usr/bin/env python3

# Script Name:                  Challenge 11 Psutil
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      12/11/2023
# Sources:                      https://chat.openai.com/, https://github.com/codefellows/seattle-ops-301d10
# Purpose:                      Ops Challenge: Psutil

# Overview

# Python is known for its versatile and diverse selection of libraries. Libraries are installable toolkits that add new functions to the language on your system. Today you will use Psutil to fetch system information.

# Objectives

# Install Psutil.

# Create a Python script that fetches this information using Psutil:

# Time spent by normal processes executing in user mode
# Time spent by processes executing in kernel mode
# Time when system was idle
# Time spent by priority processes executing in user mode
# Time spent waiting for I/O to complete.
# Time spent for servicing hardware interrupts
# Time spent for servicing software interrupts
# Time spent by other operating systems running in a virtualized environment
# Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel

import psutil

def wait_for_enter():
    input("Press Enter to continue...")

def get_system_info():
    # Time spent by normal processes executing in user mode
    user_time = psutil.cpu_times().user
    print(f"Command: user_time = psutil.cpu_times().user")
    print(f"Time spent by normal processes executing in user mode: {user_time} seconds")
    wait_for_enter()

    # Time spent by processes executing in kernel mode
    kernel_time = psutil.cpu_times().system
    print(f"Command: kernel_time = psutil.cpu_times().system")
    print(f"Time spent by processes executing in kernel mode: {kernel_time} seconds")
    wait_for_enter()

    # Time when system was idle
    idle_time = psutil.cpu_times().idle
    print(f"Command: idle_time = psutil.cpu_times().idle")
    print(f"Time when the system was idle: {idle_time} seconds")
    wait_for_enter()

    # Time spent by priority processes executing in user mode
    priority_user_time = psutil.cpu_times().nice
    print(f"Command: priority_user_time = psutil.cpu_times().nice")
    print(f"Time spent by priority processes executing in user mode: {priority_user_time} seconds")
    wait_for_enter()

    # Time spent waiting for I/O to complete
    io_wait_time = psutil.cpu_times().iowait
    print(f"Command: io_wait_time = psutil.cpu_times().iowait")
    print(f"Time spent waiting for I/O to complete: {io_wait_time} seconds")
    wait_for_enter()

    # Time spent for servicing hardware interrupts
    hardware_interrupt_time = psutil.cpu_times().irq
    print(f"Command: hardware_interrupt_time = psutil.cpu_times().irq")
    print(f"Time spent for servicing hardware interrupts: {hardware_interrupt_time} seconds")
    wait_for_enter()

    # Time spent for servicing software interrupts
    software_interrupt_time = psutil.cpu_times().softirq
    print(f"Command: software_interrupt_time = psutil.cpu_times().softirq")
    print(f"Time spent for servicing software interrupts: {software_interrupt_time} seconds")
    wait_for_enter()

    # Time spent by other operating systems running in a virtualized environment
    steal_time = psutil.cpu_times().steal
    print(f"Command: steal_time = psutil.cpu_times().steal")
    print(f"Time spent by other operating systems running in a virtualized environment: {steal_time} seconds")
    wait_for_enter()

    # Time spent running a virtual CPU for guest operating systems
    guest_time = psutil.cpu_times().guest
    print(f"Command: guest_time = psutil.cpu_times().guest")
    print(f"Time spent running a virtual CPU for guest operating systems: {guest_time} seconds")

if __name__ == "__main__":
    get_system_info()
