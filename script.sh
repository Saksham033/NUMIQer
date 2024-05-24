#!/bin/bash
 
# Function to get system health information
get_system_health() {
    echo "System Health Report"
    echo "---------------------"
    uptime
    top -bn1 | grep "Cpu(s)"
    free -m | awk '/Mem/{printf "RAM Usage: %d/%dMB (%.2f%%)\n", $3, $2, $3/$2*100}'
    df -h | awk '$NF=="/"{printf "Disk Usage: %d/%dGB (%s)\n", $3, $2, $5}'
    echo "Logged In Users: $(who | wc -l)"
    echo "Network Statistics:"
    netstat -i
}
 
# Output system health information
get_system_health
