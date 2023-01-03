class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        row = len(accounts[0])
        col = len(accounts)
        wealth = 0
        for i in range(col):
            richest=0
            for j in range(row):
                richest += accounts[i][j]
                wealth = max(richest, wealth)

        return wealth