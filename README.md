# YOLOV8-on-jetson-nano-

## Installation Steps

1. **Install Jetpack 4.6 on Jetson Nano**  
   Ensure Jetpack 4.6 (L4T 32.6.1) is installed on the Jetson Nano.

2. **Update and Install Dependencies**  
   Open a terminal and run the following commands:
   ```bash
   sudo apt update
   sudo apt install -y python3.8 python3.8-venv python3.8-dev python3-pip \
   libopenmpi-dev libomp-dev libopenblas-dev libblas-dev libeigen3-dev libcublas-dev
   ```
