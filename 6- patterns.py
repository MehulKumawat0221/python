
# Pattern 1
# *
# **
# ***
# ****
# *****
for i in range(1, 6):
    print("*" * i)

# Pattern 2
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
for i in range(1, 6):
    print("*" * i)
for i in range(4, 0, -1):
    print("*" * i)

# Pattern 3
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
for i in range(1, 6):
    print(" ".join(str(x) for x in range(1, i + 1)))

# Pattern 4
# A
# AB
# ABC
# ABCD
# ABCDE
for i in range(1, 6):
    print("".join(chr(65 + j) for j in range(i)))

# Pattern 5
# A
# BB
# CCC
# DDDD
# EEEEE
for i in range(1, 6):
    print(chr(64 + i) * i)

# Pattern 6
# *
# ***
# *****
# *******
# *********
for i in range(1, 10, 2):
    print("*" * i)

# Pattern 7
# *
# ***
# *****
# ***
# *
for i in range(1, 6, 2):
    print("*" * i)
for i in range(3, 0, -2):
    print("*" * i)

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
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
for i in range(5, 0, -1):
    print(" ".join(str(x) for x in range(1, i+1)))

# Pattern 10
# *
# ***
# *****
# ***
# *
for i in range(1, 6, 2):
    print("*" * i)
for i in range(3, 0, -2):
    print("*" * i)