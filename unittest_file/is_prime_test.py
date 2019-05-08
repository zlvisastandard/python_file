def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n % 2 ==0:
            return False
    return True

res = is_prime(681)
print(res)