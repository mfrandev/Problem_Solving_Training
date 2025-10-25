class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        # figuring out neg and pos was the hard part of this problem
        neg = set() # r-c
        pos = set() # r+c
        res = []
        board = [['.'] * n for i in range(n)]
        def bt(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 
            for c in range(n):
                if c in col or r+c in pos or r-c in neg:
                    continue
                col.add(c)
                pos.add(r+c)
                neg.add(r-c)
                board[r][c]="Q"
                bt(r+1)
                col.remove(c)
                neg.remove(r-c)
                pos.remove(r+c)
                board[r][c]="."
            return 
        bt(0)
        return res