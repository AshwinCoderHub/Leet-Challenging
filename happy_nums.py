def is_happy_number(n):
    seen_numbers = set()
    while n != 1 and n not in seen_numbers:
        seen_numbers.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

# Example u
n = 19
print(is_happy_number(n))