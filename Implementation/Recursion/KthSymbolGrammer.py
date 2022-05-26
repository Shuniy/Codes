class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k == 1:
            return 0

        if n <= 1 and k <= 1:
            return 0

        result = 0
        mid = 2**(n - 1) // 2
        if k <= mid:
            result = self.kthGrammar(n - 1, k)
        else:
            result = 1 if not self.kthGrammar(n - 1, k - mid) else 0

        return result
