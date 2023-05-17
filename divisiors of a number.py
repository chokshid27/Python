def sum_of_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)

# Example 
num = 25
print("The sum of all divisors of", num, "is", sum_of_divisors(num))
