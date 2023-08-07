N = int(input())

# 1～Nまでを足して 1/N で割る
a = 0
type(a)
for i in range(1, N + 1):
    a = i + a
print(int( (a * 10000) / N ))