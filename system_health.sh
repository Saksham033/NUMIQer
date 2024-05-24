echo "------------------------"
display_info() {
    echo -e "\n$1:"
    $2
}
display_info "Uptime" "uptime"
display_info "CPU Information" "lscpu"
display_info "Memory Information" "free -h"
display_info "Disk Usage" "df -h"
display_info "Network Interfaces" "ip addr"
display_info "Open Ports" "ss -tuln"
display_info "Logged In Users" "who"


























#display_info "Running Processes" "ps aux"
