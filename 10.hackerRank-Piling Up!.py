# Enter your code here. Read input from STDIN. Print output to STDOUT

# 2
# 6
# 4 3 2 1 3 4
# 3
# 1 3 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

# int_count_case = int(input())

# for _ in range(int_count_case):
#     int_coun_num = int(input())
#     list_num = list(map(int, input().strip().split()))
#     int_comparison_num = list_num[0]
#     boolen_bigger = True
#     str_responce = "Yes"
#     for index in range(int_coun_num):
#         if boolen_bigger:
#             if list_num[index] <= int_comparison_num:
#                 int_comparison_num = list_num[index]
#             else:
#                 int_comparison_num = list_num[index]
#                 boolen_bigger = False
#         else:
#             if list_num[index] >= int_comparison_num:
#                 int_comparison_num = list_num[index]
#             else:
#                 str_responce = "No"
#                 break
#     print(str_responce)





# from collections import deque

# for _ in range(int(input())):
#     int_count_num = int(input())
#     deque_num = deque(map(int, input().strip().split()))
#     for index in reversed(sorted(deque_num)):
#         if deque_num[0] == index:
#             deque_num.popleft()
#         elif deque_num[-1] == index:
#             deque_num.pop()
#         else:
#             print("No")
#             break
#     else:
#         print("Yes")
