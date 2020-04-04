import sys


def fn_get_meet_max_count(list_meeting):
    responce = 0
    int_end_time = 0
    for list_time  in list_meeting:
        if int_end_time <= list_time[0]:
            int_end_time = list_time[1]
            responce +=1
    return responce


if __name__=="__main__":
    int_list_count = int(sys.stdin.readline())
    list_meeting = []
    for int_index in range(int_list_count):
        int_start_time, int_end_time = map(int, sys.stdin.readline().split())
        list_meeting.append([int_start_time, int_end_time])
    list_meeting = sorted(list_meeting, key=lambda list_meeting: (list_meeting[1],list_meeting[0]), reverse=False)
    print(fn_get_meet_max_count(list_meeting))


# import sys 
# N = int(sys.stdin.readline()) 
# time = [[0]*2 for _ in range(N)] 

# for i in range(N): 
#     s, e = map(int, sys.stdin.readline().split()) 
#     time[i][0] = s 
#     time[i][1] = e 
# time.sort(key = lambda x: (x[1], x[0])) 
# cnt = 1 
# end_time = time[0][1] 
# for i in range(1, N): 
#     if time[i][0] >= end_time: 
#         cnt += 1 
#         end_time = time[i][1] 
# print(cnt)
