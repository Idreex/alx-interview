#!/usr/bin/python3

def isWinner(x, nums):
    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def playGame(n):
        primes = [i for i in range(2, n + 1) if isPrime(i)]
        turn = 0  # 0 for Maria, 1 for Ben
        while primes:
            if turn == 0:
                chosen = primes[0]
            else:
                chosen = 0
                for prime in primes:
                    if (n // prime) % 2 == 1:
                        chosen = prime
                        break
                if chosen == 0:
                    chosen = primes[-1]

            primes = [p for p in primes if p % chosen != 0]
            turn = 1 - turn

        return turn  # 0 for Maria, 1 for Ben

    scores = [0, 0]  # Maria's score, Ben's score
    for n in nums:
        winner = playGame(n)
        scores[winner] += 1

    if scores[0] > scores[1]:
        return "Maria"
    elif scores[1] > scores[0]:
        return "Ben"
    else:
        return None
    
   
