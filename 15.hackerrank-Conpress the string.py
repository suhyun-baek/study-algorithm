
# 11223333
# 이런 숫자들을 그룹화 해서
# (2, 3) (2, 2) (4, 3)
# 의형태로 출력

from itertools import groupby
S = list(input())
groups = []
for k, g in groupby(S):
    groups.append(list(g))
for g in groups:
    print((len(g), int(g[0])), end=' ')