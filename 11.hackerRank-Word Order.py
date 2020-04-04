# 4
# bcdef
# abcdefg
# bcde
# bcdef
# 중에서 각 단어가 몇번 나왔는지 츨력 
# OrderedDict의 경우 순서를 지키며 배열 출력


from collections import OrderedDict

int_input_count = int(input())
colletion_word = OrderedDict()

for _ in range(int_input_count):
    str_word = str(input())
    colletion_word[str_word] = colletion_word.get(str_word, 0) + 1

print(len(colletion_word))
print(*[colletion_word[str_word] for str_word in colletion_word], sep=" ")
