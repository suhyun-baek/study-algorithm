# S = list(input())

# isdigit : 특수문자에 숫자 까지 숫자로 확인 ½는 안됨
# isdecimal : 진짜 숫자인지만 확인
# isnumeric : ½ 도 숫자로 처리

# # Pass a tuple to the key field
# S.sort(key=lambda c: ( (c.isdigit() and int(c) % 2 == 0), (c.isdigit() and int(c) % 2 == 1), c.isupper(), c.islower(), c ) )
# print(*S, sep='')

list_str_input = list(input())
list_str_input.sort(key=lambda c: (c.isdigit())