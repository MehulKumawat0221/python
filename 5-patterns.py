
# Pattern 1
# 1
# 12
# 123
# 1234
# 12345
for i in range(1, 6):
    print("".join(str(x) for x in range(1, i+1)))

# Pattern 2
# 1
# 22
# 333
# 4444
# 55555
for i in range(1, 6):
    print(str(i) * i)

# Pattern 3
# 1
# 23
# 345
# 4567
# 56789
for i in range(1, 6):
    print("".join(str(x) for x in range(i, i + i)))

# Pattern 4
# 1
# 12
# 123
# 1234
# 12345
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Pattern 5
# A
# AB
# ABC
# ABCD
# ABCDE
for i in range(1, 6):
    print("".join(chr(65 + j) for j in range(i)))

# Pattern 6
# A
# BB
# CCC
# DDDD
# EEEEE
for i in range(1, 6):
    print(chr(64 + i) * i)

# Pattern 7
# E
# D E
# C D E
# B C D E
# A B C D E
for i in range(5, 0, -1):
    print(" ".join(chr(64 + j) for j in range(i, 6)))

# Pattern 8
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
num = 1
for i in range(1, 6):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# Pattern 9
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
num = 1
for i in range(1, 6):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# Pattern 10
# 1
# 12
# 123
# 1234
# 12345
for i in range(1, 6):
    print("".join(str(x) for x in range(1, i+1)))