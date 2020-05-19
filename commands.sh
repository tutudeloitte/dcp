#!/bin/bash



# Extend a filesystem after resizing EBS
# After increasing the size of EBS, SSH into the T2 instance

# List all partitions
lsblk

# From command above, identify which partition to increase, and replace /dev/xvda1 with the name
sudo growpart /dev/xvda 1
