from typing import TypeVar, Generic, List, Callable

T = TypeVar('T')
class SegmentTree(Generic[T]):
    @staticmethod
    def log2(x) -> int:
        ans = -1
        while x != 0:
            x >>= 1
            ans += 1

        return ans


    def __init__(
        self,
        init_data: List[T],
        e: T,
        op: Callable[[T, T], T]
    ) -> None:
        n = len(init_data)
        self.n_leaves = 2 ** (self.log2(n-1) + 1)
        self.tree = [e for _ in range(2*self.n_leaves - 1)]
        self.op = op
        self.e = e
        self.lazy = [e for _ in range(2*self.n_leaves - 1)]

        for i, elm in enumerate(init_data):
            self.tree[self.n_leaves + i - 1] = elm
            self.lazy[self.n_leaves + i - 1] = elm

        for i in range(self.n_leaves-2, -1, -1):
            l = self.tree[2*i+1]
            r = self.tree[2*i+2]
            self.tree[i] = self.op(l, r)


    def update(self, ql: int, qr: int, val: T) -> None:
        self._update(ql, qr, val, 0, 0, self.n_leaves)


    def _update(self, ql: int, qr: int, val: T, index: int, l: int, r: int) -> None:
        self.lazy_eval(index)
        if ql <= l and r <= qr:
            self.lazy[index] = self.op(self.lazy[index], val)
            self.lazy_eval(index)
        elif ql < r and l < qr:
            self._update(ql, qr, val, 2*index+1, l, (l+r) // 2)
            self._update(ql, qr, val, 2*index+2, (l+r) // 2, r)
            self.tree[index] = self.op(self.tree[2*index+1], self.tree[2*index+2])


    def lazy_eval(self, index: int) -> None:
        if self.lazy[index] == self.e:
            return

        if index < self.n_leaves - 1:
            self.lazy[2*index + 1] = self.op(self.lazy[index], self.lazy[2*index + 1])
            self.lazy[2*index + 2] = self.op(self.lazy[index], self.lazy[2*index + 2])

        self.tree[index] = self.op(self.lazy[index], self.tree[index])
        self.lazy[index] = self.e


    def query(self, ql: int, qr: int) -> T:
        return self._query(ql, qr, 0, 0, self.n_leaves)


    def _query(self, ql: int, qr: int, index: int, l: int, r: int) -> T:
        self.lazy_eval(index)
        if r <= ql or qr <= l:
            return self.e
        elif ql <= l and r <= qr:
            return self.tree[index]
        else:
            vl = self._query(ql, qr, 2*index + 1, l, (l+r)//2)
            vr = self._query(ql, qr, 2*index + 2, (l+r)//2, r)
            return self.op(vl, vr)
