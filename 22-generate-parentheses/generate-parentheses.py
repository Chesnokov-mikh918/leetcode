class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        cur = []

        def backtrack(open_cnt: int, close_cnt: int) -> None:
            if len(cur) == 2 * n:
                res.append("".join(cur))
                return
            if open_cnt < n:
                cur.append("(")
                backtrack(open_cnt + 1, close_cnt)
                cur.pop()
            if close_cnt < open_cnt:
                cur.append(")")
                backtrack(open_cnt, close_cnt + 1)
                cur.pop()

        backtrack(0, 0)
        return res