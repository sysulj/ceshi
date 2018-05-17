"""
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

"""


"""
素数，指在一个大于1的自然数中，除了1和此整数自身外，不能被其他自然数整除的数。
一个比较常见的求素数的办法是埃拉托斯特尼筛法(the Sieve of Eratosthenes) :
从2开始依次往后面数，如果当前数字是素数，那么就将所有其倍数的数从表中删除或者标记，然后最终得到所有的素数
"""
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n, i):
                    primes[j] = False

        return sum(primes)

"""
优化一下代码
"""

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        primes = [1] * n
        primes[0] = primes[1] = 0
        for i in range(2,int(n**0.5)+1):
            if primes[i] == 1:
                primes[i*i:n:i] = [0]*len(primes[i*i:n:i])
        return sum(primes)