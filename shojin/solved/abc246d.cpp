#include <bits/stdc++.h>
#define ll long long int


int main(){
    ll N;
    std::cin >> N;
    if (N == 0) {
        std::cout << 0 << std::endl;
        return 0;
    }

    const auto f = [](ll x, ll y) {
        return x*x*x + x*x*y + x*y*y + y*y*y;
    };

    ll ans = 1000000000000000000;

    for (ll a=1; a<1000001; a++) {
        auto v = f(a, 0);
        if (v >= N) {
            ans = std::min(ans, v);
        }

        ll mi = a-1;
        ll ma = 1000001;
        while (ma - mi >= 2) {
            ll b = (ma + mi) / 2;
            auto v = f(a, b);
            if (v >= N) {
                ans = std::min(ans, v);
                ma = b;
            } else {
                mi = b;
            }
        }
    }

    std::cout << ans << std::endl;
}
