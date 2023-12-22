def is_prime(number):
    """Check if a given number is prime."""
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def is_palindrome(number):
    """Check if a given number is a palindrome."""
    num_str = str(number)
    return num_str == num_str[::-1]

def print_primes_and_palindromes_up_to(limit):
    """Print prime numbers and palindromic numbers up to a given limit."""
    print("Prime numbers:")
    for num in range(2, limit + 1):
        if is_prime(num):
            print(num, end=' ')

    print("\nPalindromic numbers:")
    for num in range(1, limit + 1):
        if is_palindrome(num):
            print(num, end=' ')

if __name__ == "__main__":
    # Example: Print prime numbers and palindromic numbers up to 30
    print_primes_and_palindromes_up_to(30)

