s = input()
n = int(input())
p = input()

final = [s]
p = p.split()
for i in range(0, n):
    final.append("a" * int(p[i]))

print(" ".join(final))
