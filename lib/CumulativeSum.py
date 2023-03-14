class CumulativeSum2D:
    def __init__(self, n: int, m: int, A):
        """
            A は n+1 個の長さ m+1 のリストからなるリスト
            つまり初期化の式が A = [[0 for _ in range(m+1)] for _ in range(n+1)]
            更に A[0][*] = A[*][0] = 0 を満たす必要がある
        """
        self.n = n
        self.m = m
        self.A = A
        self.S = [[0 for _ in range(m+1)] for _ in range(n+1)]
        self._calcCumulativSum()

    def _calcCumulativSum(self):
        for i in range(1, self.n+1):
            for j in range(1, self.m+1):
                self.S[i][j] = self.S[i-1][j] + self.S[i][j-1] - self.S[i-1][j-1] + self.A[i][j]

    def get(self, a, b, c, d):
        """
            A[a][b] + A[a][b+1] + ... + A[a][d] + A[a+1] + ... + A[c][b] + ... + A[c][d] を求める
            a, b が左上， c, d が右上のイメージ．
        """
        return self.S[c][d] - self.S[a-1][d] - self.S[c][b-1] + self.S[a-1][b-1]
