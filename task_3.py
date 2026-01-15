import time
M = int(input())
N = int(input())

start_time = time.time()
for i in range(M):
    print(i)
    time.sleep(1)
    for k in range(N):
        print(k)
        time.sleep(1)
end_time = time.time()
time_all = end_time - start_time
print(time_all)
