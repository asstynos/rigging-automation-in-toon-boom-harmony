import time


def time_sleep(time_int):
    for i in range(time_int):
        time.sleep(1)
        print(f'{i+1}/{time_int} time')
