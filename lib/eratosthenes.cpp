#include <bits/stdc++.h>

template <class T = int>
std::vector<bool> primes(T n, std::vector<T> &ps) {
    // &ps に n 未満の素数一覧を格納し， さらに素数テーブルを return する．
    std::vector<bool> table(n, true);
    table[0] = false;
    table[1] = false;
    ps.clear();
    for (T i=2; i*i < n; i++) {
        if(table[i]) {
            for(T j = i*i; j<n; j+=i) table[j] = false;
            ps.push_back(i);
        }
    }

    return table;
}


int main() {
    int max = 10000000;
    std::vector<int> ps;
    auto pt = primes(max, ps);

    for(int i=0; i<10; i++) std::cout << i << " " << ps[i] << " " << pt[i] << std::endl;

    return 0;
}
