# Time: O(logN)
def reverse_integer(num):
    sign = -1 if num < 0 else 1
    num *= sign
    reverse_num = 0
    while num > 0:
        digit = num % 10
        num = num // 10
        reverse_num = reverse_num * 10 + digit
    # Check if the reversed number is within the 32-bit signed integer range
    if not -2147483648 <= sign * reverse_num <= 2147483647:
        return 0

    return sign * reverse_num


print(reverse_integer(123))
print(reverse_integer(-123))

# Time: O(N); Space: O(N)


def reverse_integer(num):
    sign = -1 if num < 0 else 1
    num *= sign
    reverse_num = int(str(num)[::-1])
    # Check if the reversed number is within the 32-bit signed integer range
    if not -2147483648 <= sign * reverse_num <= 2147483647:
        return 0
    return sign * reverse_num


print(reverse_integer(-123))
print(reverse_integer(123))
