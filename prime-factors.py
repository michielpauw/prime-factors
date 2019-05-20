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


def sum_of_primes(expanded, upper_limit, next_prime):
    sum_of_primes = []
    current_prime = 2
    new_prime = True
    while current_prime <= expanded and current_prime <= upper_limit:
        if expanded % current_prime == 0:
            if new_prime:
                sum_of_primes.append(current_prime)
            expanded /= current_prime
            if next_prime.check_big_prime(expanded):
                sum_of_primes.append(expanded)
                return sum_of_primes
            new_prime = False
        else:
            new_prime = True
            current_prime = next_prime.get_next_prime()
            if not current_prime:
                return sum_of_primes
    return sum_of_primes


def factorize_first(n, upper_limit, next_prime):
    f = []
    sum_p = []
    f.append(n + 1)
    f.append(pow(n, 2) - n + 1)
    f.append(pow(n, 4) - pow(n, 3) + pow(n, 2) - n + 1)
    f.append(pow(n, 8) + pow(n, 7) - pow(n, 5) - pow(n, 4) - pow(n, 3) + n + 1)
    for factor in f:
        if factor > 1:
            sum_new = sum_of_primes(factor, upper_limit, next_prime)
            sum_p.extend(x for x in sum_new if x not in sum_p)
    return sum(list(sum_p))


def check_pattern(p_mod_15, amount_starters):
    if p_mod_15 == 1 and amount_starters != 15:
        return False
    if p_mod_15 == 2 and amount_starters != 1:
        return False
    if p_mod_15 == 3 and amount_starters != 1:
        return False
    if p_mod_15 == 4 and amount_starters != 3:
        return False
    if p_mod_15 == 5 and amount_starters != 1:
        return False
    if p_mod_15 == 6:
        print("CHECK 6: " + str(amount_starters))
        return True
    if p_mod_15 == 7 and amount_starters != 3:
        return False
    if p_mod_15 == 8 and amount_starters != 1:
        return False
    if p_mod_15 == 9:
        print("CHECK 9: " + str(amount_starters))
        return True
    if p_mod_15 == 10:
        print("CHECK 10: " + str(amount_starters))
        return True
    if p_mod_15 == 11 and amount_starters != 5:
        return False
    if p_mod_15 == 12:
        print("CHECK 12: " + str(amount_starters))
        return True
    if p_mod_15 == 13 and amount_starters != 3:
        return False
    if p_mod_15 == 14 and amount_starters != 1:
        return False
    return True


def get_starters(prime):
    n = 0
    starters = []
    amount_starters = 0
    while n < prime:
        n += 1
        if n % prime in starters:
            continue
        expanded = pow(n, 15) + 1
        if expanded % prime == 0:
            starters.append(n)
            amount_starters += 1
    if not check_pattern(prime % 15, amount_starters):
        print("FUCK")
        sys.exit(0)
    return amount_starters


def main():
    next_prime = NextPrime()
    print("DONE")
    total_starters = 0
    for p in next_prime.current_primes:
        total_starters += get_starters(p)
        print(total_starters)


if __name__ == "__main__":
    main()
