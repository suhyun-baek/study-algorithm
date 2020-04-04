import sys

if __name__=="__main__":
    responce = 0
    int_list_count = int(sys.stdin.readline())
    list_time = list(map(int, sys.stdin.readline().split()))
    list_time = sorted(list_time, key=lambda list_time: list_time, reverse=False)
    # list_time.sort()
    int_time_sum = 0
    for int_time in list_time:
        int_time_sum += int_time
        responce += int_time_sum
    print(responce)



responce = 0
int_list_count = int(input())
list_time = list(map(int, input().split()))
# list_time = list_time.sorted()
list_time = sorted(list_time, key=lambda list_time: list_time, reverse=False)
int_time_sum = 0
for int_time in list_time:
    int_time_sum += int_time
    responce += int_time_sum
print(responce)

