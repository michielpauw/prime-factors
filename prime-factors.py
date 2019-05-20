#!/usr/bin/python3.x


class NextPrime:
    def __init__(self):
        self.current_primes = [2]
        self.last_prime = 2
        self.index = 0
        self.create_primes()

    def create_primes(self):
        while self.last_prime < 100000000:
            print(self.last_prime)
            self.get_next_prime()

    def get_next_prime(self):
        self.index += 1
        if self.index == 1:
            return 2
        if len(self.current_primes) >= self.index:
            self.last_prime = self.current_primes[self.index - 1]
            return self.last_prime
        current_number = self.last_prime
        is_prime = False
        while not is_prime:
            current_number += 1 if self.last_prime == 2 else 2
            is_prime = self.check_prime(current_number)
        self.current_primes.append(current_number)
        self.last_prime = current_number
        self.index += 1
        return current_number

    def reset_index(self):
        self.index = 0
        self.last_prime = 2

    def check_prime(self, n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for prime in self.current_primes:
            if n % prime == 0:
                return False
            if prime * prime > n:
                break
        return True

    def check_big_prime(self, n):
        if not self.check_prime(n):
            return False
        while True:
            next_prime = self.get_next_prime()
            if n % next_prime == 0:
                return False
            if next_prime * next_prime > n:
                return True


def sum_of_primes(expanded, upper_limit, next_prime):
    sum_of_primes = 0
    current_prime = 2
    new_prime = True
    while current_prime <= expanded and current_prime <= upper_limit:
        if expanded % current_prime == 0:
            if new_prime:
                sum_of_primes += current_prime
            expanded /= current_prime
            if next_prime.check_big_prime(expanded):
                return sum_of_primes + expanded
            new_prime = False
        else:
            new_prime = True
            current_prime = next_prime.get_next_prime()
    return sum_of_primes


def factorize_first(n, upper_limit, next_prime):
    f = []
    sum_p = 0
    f.append(n + 1)
    f.append(pow(n, 2) - n + 1)
    f.append(pow(n, 4) - pow(n, 3) + pow(n, 2) - n + 1)
    f.append(pow(n, 8) + pow(n, 7) - pow(n, 5) - pow(n, 4) - pow(n, 3) + n + 1)
    for factor in f:
        if factor > 1:
            print(factor)
            sum_p += sum_of_primes(factor, upper_limit, next_prime)
    return sum_p


def main():
    next_prime = NextPrime()
    print("DONE")
    print(len(next_prime.current_primes))
    total_sum = 0
    upper_limit = pow(10, 8)
    max_n = pow(10, 11)
    for n in range(1, max_n):
        sum_p = factorize_first(n, upper_limit, next_prime)
        total_sum += sum_p
        next_prime.reset_index()
        print(str(n) + ": " + str(sum_p) + " - " + str(total_sum))


if __name__ == "__main__":
    main()
