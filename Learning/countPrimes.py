class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        arr = []
        # if n <= 1:
        #     return count
        if n <= 2:
            return len(arr)

        elif self.isPrime(n):
            # count = count + 1
            arr.append(n)

        return len(arr)  + self.countPrimes(n - 1)


    def isPrime(self, num):
        valid = False
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return valid

        valid = True
        return valid


a = Solution()
print(a.countPrimes(4))
print(a.countPrimes(2))
print(a.countPrimes(10))
# print(a.countPrimes(992))
# print(a.countPrimes(50))

# print(isPrime(5))
# print(isPrime(4))
# print(isPrime(1))
# print(countPrimes(10))
# print(countPrimes(100))
# print(countPrimes(4))
# print('Prime:', n, 'Count:', count)
