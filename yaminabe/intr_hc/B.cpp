#include <bits/stdc++.h>

int main() {
    int D;
    std::cin >> D;

    std::vector<short> c = {0};
    for(int i=0; i<26; i++) {
        short ci;
        std::cin >> ci;
        c.push_back(ci);
    }

    std::vector<std::vector<short>> s = {{}};
    for(int i=0; i<D; i++) {
        std::vector<short> si = {0};
        for(int j=0; j<26; j++) {
            short sij;
            std::cin >> sij;
            si.push_back(sij);
        }
        s.push_back(si);
    }

    std::vector<short> last(27, 0);

    int t;
    int satisfaction = 0;

    for(int d=1; d<=D; d++) {
        std::cin >> t;
        int score = s[d][t];
        last[t] = d;

        for(int i=1; i<=26; i++) {
            score -= (c[i] * (d - last[i]));
        }

        satisfaction += score;
        printf("%d\n", satisfaction);
    }


    return 0;
}
