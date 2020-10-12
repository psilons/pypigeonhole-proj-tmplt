import psutil


def scan_cpu():
    print(f'cpu logicals: {psutil.cpu_count()}')
    print(f'cpu physicals: {psutil.cpu_count(logical=False)}')
    print(f'cpu freq: {psutil.cpu_freq()}')
