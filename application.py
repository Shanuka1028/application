def is_prime(number):
    """Check if a given number is prime."""
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def print_primes_up_to(limit):
    """Print all prime numbers up to a given limit."""
    for num in range(2, limit + 1):
        if is_prime(num):
            print(num, end=' ')

if __name__ == "__main__":
    # Example: Print prime numbers up to 20
    print_primes_up_to(20)
