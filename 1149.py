Number = list(map(int, input().split()))

A = Number[0]
N = Number[-1]

total = [A]

for i in range(1,N):
    A += 1
    total.append(A)
    #print(A)

#print(total)
result = sum(total)
print(result)
