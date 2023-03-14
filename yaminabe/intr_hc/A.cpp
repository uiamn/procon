#include <bits/stdc++.h>

int D = 365;
std::random_device rnd;
std::mt19937 mt(rnd());
std::uniform_int_distribution<short> rand26(1, 26);
std::uniform_int_distribution<short> rand365(1, D);
std::uniform_int_distribution<short> rand2(0, 1);

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

std::vector<short> initial_solution(
    std::vector<std::vector<short>> &s
) {
    // 貪欲法による初期解の探索を行ふ
    // 各日について最も s が大きいものを取ってくる
    std::vector<short> t = {0};

    for(int d=1; d<s.size(); d++) {
        auto sd = s[d];

        short maxarg = -1;
        int max_s = -1;
        for(short contest_type=1; contest_type<=26; contest_type++) {
            if(max_s < sd[contest_type]) {
                maxarg = contest_type;
                max_s = sd[contest_type];
            }
        }

        t.push_back(maxarg);
    }

    return t;
}

std::pair<short, short> generate_query(
    std::vector<short> &c,
    std::vector<std::vector<short>> &s,
    std::vector<short> &t,
    std::unordered_map<short, std::vector<short>> &td
) {
    // スコアが伸びるクエリを探す
    // std::vector<std::pair<short, short>> candidate_queries = {};
    auto diffmax = -5000;
    auto diffmaxquery = std::make_pair<short, short>(-1, -1);

    auto candidate_thre = 30000;

    for(int d=1; d<=D; d++) for(int ct=1; ct<=26; ct++) {
        auto candpair = std::make_pair<short, short>(d, ct);
        auto diff = diff_score(c, s, td, t[d], candpair);
        if(diffmax < diff) {
            diffmax = diff;
            diffmaxquery = candpair;
        }
        // if (diff > candidate_thre) candidate_queries.push_back(candpair);
    }

    // if(diffmax == -1 || candidate_queries.size() == 0) {
    //     return std::make_pair(rand365(mt), rand26(mt));
    // } else if (rand2(mt)) {
    //     return diffmaxquery;
    // } else {
    //     std::uniform_int_distribution<short> rand(0, (short)candidate_queries.size() - 1);
    //     return candidate_queries[rand(mt)];
    // }

    if (diffmax > -5000) {
        return diffmaxquery;
    } else {
        return std::make_pair(rand365(mt), rand26(mt));
    }
}


int main() {
    auto begin = std::chrono::system_clock::now();

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

    auto t = initial_solution(s);
    int score = calc_score(c, s, t);

    std::unordered_map<short, std::vector<short>> td;  // コンテストタイプとそれが開催される日付の一覧を対応付ける hashmap
    for(int i=1; i<=26; i++) {
        td[i] = {0};
    }

    for(int i=1; i<=D; i++) {
        auto ti = t[i];
        td[ti].push_back(i);
    }

    for(int i=1; i<=26; i++) {
        td[i].push_back(D+1);
    }

    while(std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::system_clock::now() - begin).count() < 1990) {
        auto q = generate_query(c, s, t, td);
        // auto diff_s = diff_score(c, s, td, t[q.first], q);
        // if(diff_s > 0) apply_query(t, td, t[q.first], q);
        apply_query(t, td, t[q.first], q);
    }

    for(int i=1; i<t.size(); i++) {
        printf("%d\n", t[i]);
    }

    return 0;
}
