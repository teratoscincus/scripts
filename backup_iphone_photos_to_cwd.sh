#!/bin/bash

# Back up photos, etc, from an iPhone on a Linux machine
# Copies to the current working directory from where this script is called.
#
# Requirements:
#   ifuse

# Pair iPhone
idevicepair pair

# Mount iPhone and copy content
sudo mkdir -p /mnt/iphone
sudo ifuse -o allow_other /mnt/iphone
cp -rt "$PWD" /mnt/iphone/DCIM

# Clean up
idevicepair unpair
sudo umount /mnt/iphone
sudo rm -rf /mnt/iphone
