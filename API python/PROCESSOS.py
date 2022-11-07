import psutil
from time import sleep

while True:

    p_list = []
    for proc in psutil.process_iter():
        proc_info = proc.as_dict(['name', 'cpu_percent'])
        if proc_info['cpu_percent'] > 0:
            p_list.append(proc_info)
            # print(proc_info)
            # sleep(2)

    sorted(
        p_list,
        key=lambda p: p['cpu_percent'],
        reverse=True
    )
print(p_list)