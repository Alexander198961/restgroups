#!/bin/bash
ls -l /cgroup  | grep "^d" | awk '{print $9}'
