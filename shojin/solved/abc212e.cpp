#include <bits/stdc++.h>
#define ll long long int
#define MOD 998244353

ll modsum(std::vector<ll> &list, ll mod) {
    ll s = 0;
    for(auto l: list) {
        s += l;
        s %= mod;
    }

    return s;
}


int main(){
    int N, M, K;
    std::cin >> N >> M >> K;
    std::vector<std::pair<int, int>> broken_bridges(M);

    for(int i=0; i<M; i++) {
        int u, v;
        std::cin >> u >> v;
        broken_bridges.push_back({u, v});
    }

    std::vector<std::vector<ll>> dp(K+1);
    for(int i=0; i<K+1; i++) {
        std::vector<ll> d(N+1, 0);
        dp[i] = d;
    }

    dp[0][1] = 1;
    ll tmpsum = 0;

    for(int k=1; k<K+1; k++) {
        tmpsum = modsum(dp[k-1], MOD);
        for(int n=1; n<N+1; n++) {
            dp[k][n] = tmpsum - dp[k-1][n];
        }
        for(auto b: broken_bridges) {
            auto u = b.first;
            auto v = b.second;
            dp[k][u] -= dp[k-1][v];
            dp[k][u] %= MOD;
            dp[k][v] -= dp[k-1][u];
            dp[k][v] %= MOD;
        }
    }

    printf("%lld\n", (dp[K][1] % MOD + MOD) % MOD);
}
