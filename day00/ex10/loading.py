from time import time, sleep


def ft_progress(lst):
    start = time()
    now = 0
    prev_time = 0
    for i in range(len(lst)):
        p = int(i / len(lst) * 100)
        e = int(p * 0.5)
        t = time()
        print(f'ETA: {(now - prev_time) * (len(lst) - i):4.2f}s', end=' ')
        print(f'[{p:3}%]', end='')
        print(' [' + '=' * e + '>' + ' ' * (49 - e) + ']', end='')
        print(f' {i}/{len(lst)} {t - start:.2f}s')
        prev_time = time()
        yield i
        now = time()
    print("ETA: 0.00s [100%]" + ' [' + '=' * 50 + ']', end=' ')
    print(f'{len(lst)}/{len(lst)} {t - start:.2f}s')


listy = range(100)
ret = 0

for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.01)

print(ret)
