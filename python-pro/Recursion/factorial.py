def factorial(n):
    assert 0 <= n == int(n), 'the number must be positive'
    if n in[0, 1]:
        return 1
    else:
        return n * factorial(n - 1)
# factorial 5!=1x2x3x4x5=120

print(factorial(4))
