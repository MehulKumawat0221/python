
# Q1: Left-angled star triangle
n = 5
for i in range(1, n+1):
    print(' ' * (n - i) + '*' * i)

print()

# Q2: Hollow triangle
n = 5
for i in range(1, n+1):
    if i == 1:
        print(' ' * (n - i) + '*')
    elif i == n:
        print('*' * (2*n - 1))
    else:
        print(' ' * (n - i) + '*' + ' ' * (2*i - 3) + '*')

print()

# Q3: Right arrow star pattern
n = 5
for i in range(1, n+1):
    print('*' * i)
for i in range(n-1, 0, -1):
    print('*' * i)

print()

# Q4: Z star pattern
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == n-1-i:
            print('*', end='')
        else:
            print(' ', end='')
    print()

print()

# Q5: X star pattern
n = 5
for i in range(n):
    for j in range(n):
        if j == i or j == n-1-i:
            print('*', end='')
        else:
            print(' ', end='')
    print()

print()

# Q6: K pattern star
n = 5
for i in range(1, n+1):
    print('*' * i + '*' * (n - i))

print()

# Q7: Checkerboard pattern
n = 5
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print('*', end='')
        else:
            print(' ', end='')
    print()

print()

# Q8: Number V pattern
n = 5
for i in range(n):
    for j in range(n):
        if j == i or j == 2*(n-1)-i:
            print(i+1, end='')
        else:
            print(' ', end='')
    print()

print()

# Q9: Reverse number pyramid
n = 5
for i in range(n, 0, -1):
    print(' ' * (n - i), end='')
    for j in range(i, 0, -1):
        print(j, end='')
    print()

print()

# Q10: Number diamond
n = 5
for i in range(1, n+1):
    print(' ' * (n - i), end='')
    for j in range(1, i+1):
        print(j, end='')
    for j in range(i-1, 0, -1):
        print(j, end='')
    print()
for i in range(n-1, 0, -1):
    print(' ' * (n - i), end='')
    for j in range(1, i+1):
        print(j, end='')
    for j in range(i-1, 0, -1):
        print(j, end='')
    print()

print()

# Q11: Palindrome number triangle
n = 5
for i in range(1, n+1):
    print(' ' * (n - i), end='')
    for j in range(i, 0, -1):
        print(j, end='')
    for j in range(2, i+1):
        print(j, end='')
    print()

print()

# Q12: Square number matrix (row-wise)
n = 5
num = 1
for i in range(n):
    for j in range(n):
        print(num, end='\t')
        num += 1
    print()

print()

# Q13: Alphabet diamond
n = 5
for i in range(n):
    print(' ' * (n - i - 1), end='')
    for j in range(i+1):
        print(chr(65 + j), end='')
    for j in range(i-1, -1, -1):
        print(chr(65 + j), end='')
    print()
for i in range(n-2, -1, -1):
    print(' ' * (n - i - 1), end='')
    for j in range(i+1):
        print(chr(65 + j), end='')
    for j in range(i-1, -1, -1):
        print(chr(65 + j), end='')
    print()

print()

# Q14: Reversed alphabet pyramid
n = 5
for i in range(n):
    print(' ' * i, end='')
    for j in range(n-1, i-1, -1):
        print(chr(65 + j), end='')
    print()

print()

# Q15: Alphabet K pattern
n = 5
for i in range(n):
    print(chr(65 + i) * (i+1))

print()

# Q16: Wave number pattern
n = 5
for i in range(1, n+1):
    if i % 2 != 0:
        for j in range(1, n+1):
            print(j, end=' ')
    else:
        for j in range(n, 0, -1):
            print(j, end=' ')
    print()

print()

# Q17: Hollow diamond
n = 5
for i in range(1, n+1):
    print(' ' * (n - i), end='')
    if i == 1:
        print('*')
    else:
        print('*' + ' ' * (2*i - 3) + '*')
for i in range(n-1, 0, -1):
    print(' ' * (n - i), end='')
    if i == 1:
        print('*')
    else:
        print('*' + ' ' * (2*i - 3) + '*')

print()

# Q18: Multiplication table triangle
n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(i * j, end='\t')
    print()

print()

# Q19: Right-angled alphabet inverted triangle
n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end='')
    print()

print()

# Q20: Staircase number pattern
n = 5
for i in range(1, n+1):
    for j in range(1, n+1):
        if j <= i:
            print(j, end=' ')
        else:
            print(' ', end=' ')
    print()
