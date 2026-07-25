class DSU {
    vector<int> pars;
    vector<int> rank;
public:
    DSU(int n) {
        pars.resize(n, -1);
        rank.resize(n, 1);
    }

    int find(int n) {
        if (pars[n] == -1) return n;
        return find(pars[n]);
    }
 
    bool union_set(int u, int v) {
        int pu = find(u), pv = find(v);
        if (pu == pv) return false;

        if (rank[pu] > rank[pv]) {
            pars[pv] = pu;
            rank[pu] += rank[pv];
        } else {
            pars[pu] = pv;
            rank[pv] += rank[pu];
        }

        return true;
    }
};

class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        DSU dsu(n);
        int res = n;

        for (const auto& edge : edges) {
            if (dsu.union_set(edge[0], edge[1])) --res;
        }

        return res;
    }
};
