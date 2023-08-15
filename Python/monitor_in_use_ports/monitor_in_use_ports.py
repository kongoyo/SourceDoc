import psutil


def get_open_ports_with_pid_and_name():
    open_ports = []
    for conn in psutil.net_connections(kind="inet"):
        try:
            process = psutil.Process(conn.pid)
            process_name = process.name()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            process_name = "N/A"

        if process_name not in ["System Idle Process", "svchost.exe", "System"]:
            open_ports.append((conn.laddr.port, process_name, conn.pid))

    return open_ports


if __name__ == "__main__":
    open_ports = get_open_ports_with_pid_and_name()
    sorted_open_ports = sorted(open_ports, key=lambda x: x[0])  # 根據 port number 排序

    with open(
        r"D:\Downloads\SourceDoc\Python\monitor_in_use_ports\report.txt", "w"
    ) as report_file:
        report_file.write("Port".ljust(10) + "Process Name".ljust(30) + "PID\n")
        report_file.write("-" * (10 + 30 + len("PID") + 2) + "\n")

        for port, process_name, pid in sorted_open_ports:
            report_file.write(
                str(port).ljust(10) + process_name.ljust(30) + str(pid) + "\n"
            )

    print(
        "Report has been saved to 'D:\\Downloads\\SourceDoc\\Python\\monitor_in_use_ports\\report.txt'"
    )
