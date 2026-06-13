

# Q1: Right-angled star triangle
n = 5
for i in range(1, n+1):
    print('*' * i)

print()

# Q2: Inverted right-angled star triangle
n = 5
for i in range(n, 0, -1):
    print('*' * i)

print()

# Q3: Star pyramid (centered)
n = 5
for i in range(1, n+1):
    print(' ' * (n - i) + '*' * (2*i - 1))

print()

# Q4: Inverted star pyramid
n = 5
for i in range(n, 0, -1):
    print(' ' * (n - i) + '*' * (2*i - 1))

print()

# Q5: Diamond star pattern
n = 5
for i in range(1, n+1):
    print(' ' * (n - i) + '*' * (2*i - 1))
for i in range(n-1, 0, -1):
    print(' ' * (n - i) + '*' * (2*i - 1))

print()

# Q6: Hollow square star pattern
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print('*', end='')
        else:
            print(' ', end='')
    print()

print()

# Q7: Right-angled number triangle
n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end='')
    print()

print()

# Q8: Floyd's triangle
n = 5
num = 1
for i in range(1, n+1):
    for j in range(i):
        print(num, end=' ')
        num += 1
    print()

print()

# Q9: Number pyramid
n = 5
for i in range(1, n+1):
    print(' ' * (n - i), end='')
    for j in range(1, i+1):
        print(j, end='')
    for j in range(i-1, 0, -1):
        print(j, end='')
    print()

print()

# Q10: Pascal's triangle
n = 5
for i in range(n):
    val = 1
    print(' ' * (n - i), end='')
    for j in range(i+1):
        print(val, end=' ')
        val = val * (i - j) // (j + 1)
    print()

print()

# Q11: Alphabet right triangle
n = 5
for i in range(n):
    for j in range(i+1):
        print(chr(65 + j), end='')
    print()

print()

# Q12: Alphabet pyramid
n = 5
for i in range(n):
    print(' ' * (n - i - 1), end='')
    for j in range(i+1):
        print(chr(65 + j), end='')
    for j in range(i-1, -1, -1):
        print(chr(65 + j), end='')
    print()

print()

# Q13: Repeating alphabet triangle
n = 5
for i in range(n):
    for j in range(i+1):
        print(chr(65 + i), end='')
    print()

print()

# Q14: Reversed alphabet right triangle
n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end='')
    print()

print()

# Q15: Butterfly pattern
n = 5
for i in range(1, n+1):
    print('*' * i + ' ' * (2*(n-i)) + '*' * i)
for i in range(n, 0, -1):
    print('*' * i + ' ' * (2*(n-i)) + '*' * i)

print()

# Q16: Sandglass star pattern
n = 5
for i in range(n, 0, -1):
    print(' ' * (n - i) + '*' * (2*i - 1))
for i in range(2, n+1):
    print(' ' * (n - i) + '*' * (2*i - 1))

print()

# Q17: Right-angled number triangle (same number per row)
n = 5
for i in range(1, n+1):
    for j in range(i):
        print(i, end='')
    print()

print()

# Q18: Binary (0/1) triangle
n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        if (i + j) % 2 == 0:
            print(1, end='')
        else:
            print(0, end='')
    print()

print()

# Q19: Cross / Plus pattern
n = 7
mid = n // 2
for i in range(n):
    for j in range(n):
        if i == mid or j == mid:
            print('*', end='')
        else:
            print(' ', end='')
    print()

print()

# Q20: Spiral number matrix
n = 4
matrix = [[0]*n for _ in range(n)]
top, bottom, left, right = 0, n-1, 0, n-1
num = 1
while top <= bottom and left <= right:
    for i in range(left, right+1):
        matrix[top][i] = num
        num += 1
    top += 1
    for i in range(top, bottom+1):
        matrix[i][right] = num
        num += 1
    right -= 1
    for i in range(right, left-1, -1):
        matrix[bottom][i] = num
        num += 1
    bottom -= 1
    for i in range(bottom, top-1, -1):
        matrix[i][left] = num
        num += 1
    left += 1
for row in matrix:
    print(row)
