def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
print("1. is_prime funksiyasi:")
print(is_prime(4))  # False
print(is_prime(7))  # True
print()



def digit_sum(k):
    return sum(int(digit) for digit in str(k))
print("2. digit_sum funksiyasi:")
print(digit_sum(24))   # 6
print(digit_sum(502))  # 7
print()



def powers_of_two(n):
    power = 1
    result = []
    while power * 2 <= n:
        power *= 2
        result.append(power)
    return result
print("3. 2 ning darajalari:")
print(*powers_of_two(10))  # 2 4 8
