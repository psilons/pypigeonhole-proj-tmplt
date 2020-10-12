import psutil
import sys
import pathlib


def scan_cpu():
    print(f'cpu logicals: {psutil.cpu_count()}')
    print(f'cpu physicals: {psutil.cpu_count(logical=False)}')
    print(f'cpu freq: {psutil.cpu_freq()}')


if __name__ == '__main__':
    scan_cpu()
    p = pathlib.Path(sys.argv[1])
    settings = (p / "settings.txt").read_text()
    print(settings)
