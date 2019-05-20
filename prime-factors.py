#!/usr/bin/python3.x

import sys


class NextPrime:
    def __init__(self):
        self.current_primes = [2]
        self.last_prime = 2
        self.index = 0
        self.create_primes()
        self.starters = [0, 15, 1, 1, 3, 1, 0, 3, 1, 0, 0, 5, 0, 3, 1]

    def create_primes(self):
        while self.last_prime < 100000000:
            self.append_next_prime()

    def append_next_prime(self):
        current_number = self.last_prime
        is_prime = False
        while not is_prime:
            current_number += 1 if self.last_prime == 2 else 2
            is_prime = self.check_prime(current_number)
        self.current_primes.append(current_number)
        self.last_prime = current_number
        return current_number

    def get_next_prime(self):
        self.index += 1
        if self.index >= len(self.current_primes):
            return None
        self.last_prime = self.current_primes[self.index - 1]
        return self.last_prime

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
        if n in self.current_primes:
            return True
        else:
            return False


def check_starters(p, next_prime, target):
    amount_starters = next_prime.starters[p % 15]
    added_so_far = 0
    amount_all = 0
    max_contribution = target // p + 1
    for n in range(1, target % p + 1):
        expanded = pow(n, 15) + 1
        if expanded % p == 0:
            added_so_far += 1
            multiplicativity = ((target - n) // p) + 1
            amount_all += multiplicativity * p
    multiplicativity = ((target - p) // p) + 1
    amount_all += multiplicativity * p * (amount_starters - added_so_far)
    return amount_all


def main():
    next_prime = NextPrime()
    print("DONE")
    result = 0
    target = pow(10, 11)
    i = 0
    for p in next_prime.current_primes:
        if next_prime.starters[p % 15] == 1:
            contribution = (((target - (p - 1)) // p) + 1) * p
        else:
            contribution = check_starters(p, next_prime, target)
        result += contribution
        i += 1
        if i % 100000 == 0:
            print("Iteration: " + str(i) + "Latest: " + str(contribution) + " Added: " + str(result))
    print(result)


if __name__ == "__main__":
    main()
