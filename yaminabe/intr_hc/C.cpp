#include <bits/stdc++.h>

int calc_score(
    std::vector<short> &c,
    std::vector<std::vector<short>> &s,
    std::vector<short> &t
) {
    std::vector<short> last(27, 0);
    int D = t.size() - 1;
    int satisfaction = 0;


    for(int d=1; d<=D; d++) {
        short td = t[d];
        int score = s[d][td];
        last[td] = d;

        for(int i=1; i<=26; i++) {
            score -= (c[i] * (d - last[i]));
        }

        satisfaction += score;
    }

    return satisfaction;
}

int diff_score(
    std::vector<short> &c,
    std::vector<std::vector<short>> &s,
    std::unordered_map<short, std::vector<short>> &td,
    short org_contest, // 元々 d 日目に開催される予定だったコンテスト
    std::pair<short, short> &query  // (d, t) d 日目に開催されるコンテストを t に変更する
) {
    // query を適用したときの最終的な score の差分を計算する
    int dni_index = std::lower_bound(td[org_contest].begin(), td[org_contest].end(), query.first) - td[org_contest].begin();
    int dmj_index = std::lower_bound(td[query.second].begin(), td[query.second].end(), query.first) - td[query.second].begin() - 1;

    int delta_f = 0;
    // delta_f += c[org_contest] * (td[org_contest][dni_index+1] - td[org_contest][dni_index]) * (td[org_contest][dni_index] - td[org_contest][dni_index-1]);
    delta_f += c[org_contest] * (td[org_contest][dni_index+1] - query.first) * (query.first - td[org_contest][dni_index-1]);
    delta_f += c[query.second] * (td[query.second][dmj_index+1] - query.first) * (td[query.second][dmj_index] - query.first);

    int delta_score = s[query.first][query.second] - s[query.first][org_contest] - delta_f;
    return delta_score;
}

void apply_query(
    std::vector<short> &t,
    std::unordered_map<short, std::vector<short>> &td,
    short org_contest, // 元々 d 日目に開催される予定だったコンテスト
    std::pair<short, short> &query  // (d, t) d 日目に開催されるコンテストを t に変更する
) {
    int dmj_index = std::lower_bound(td[query.second].begin(), td[query.second].end(), query.first) - td[query.second].begin() - 1;

    td[org_contest].erase(std::lower_bound(td[org_contest].begin(), td[org_contest].end(), query.first));
    td[query.second].insert(std::lower_bound(td[query.second].begin(), td[query.second].end(), query.first), query.first);
    t[query.first] = query.second;
}

int main() {
    int D;
    std::cin >> D;

    std::vector<short> c = {0};
    for(int i=0; i<26; i++) {
        short ci;
        std::cin >> ci;
        c.push_back(ci);
    }

    std::vector<std::vector<short>> s = {{}};  // s[i][j] = i 日目にコンテスト j を開催したときの満足度
    for(int i=0; i<D; i++) {
        std::vector<short> si = {0};
        for(int j=0; j<26; j++) {
            short sij;
            std::cin >> sij;
            si.push_back(sij);
        }
        s.push_back(si);
    }

    std::vector<short> t = {0};
    std::unordered_map<short, std::vector<short>> td;  // コンテストタイプとそれが開催される日付の一覧を対応付ける hashmap
    for(int i=1; i<=26; i++) {
        td[i] = {0};
    }

    for(int i=1; i<=D; i++) {
        short ti;
        std::cin >> ti;
        t.push_back(ti);
        td[ti].push_back(i);
    }

    for(int i=1; i<=26; i++) {
        td[i].push_back(D+1);
    }

    int M;
    std::cin >> M;

    std::vector<std::pair<short, short>> queries;

    for(int i=0; i<M; i++) {
        short di, qi;
        std::cin >> di >> qi;
        queries.push_back(std::make_pair(di, qi));
    }

    int score = calc_score(c, s, t);

    for(auto q: queries) {
        score += diff_score(c, s, td, t[q.first], q);
        printf("%d\n", score);
        apply_query(t, td, t[q.first], q);
    }

    return 0;
}
