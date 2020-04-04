# Enter your code here. Read input from STDIN. Print output to STDOUT

int_n, int_m = map(int, input().strip().split())
list_input_num = list(map(int, input().strip().split()))
list_A = set(map(int, input().strip().split()))
list_B = set(map(int, input().strip().split()))

int_score = 0
for index in range(int_n):
    if list_input_num[index] in list_A:
        int_score += 1

    if list_input_num[index] in list_B:
        int_score -= 1
print(int_score)
