class DSU {
private:
    vector<int> rank;

public:
    vector<int> pars;

    DSU(int size) {
        pars.resize(size);
        for (int i = 0; i < size; ++i) pars[i] = i;
        rank.resize(size, 1);
    }

    int find(int n) {
        if (pars[n] == n) return n;
        return pars[n] = find(pars[n]);
    }

    bool union_find(int n1, int n2) {
        int p1 = find(n1), p2 = find(n2);
        if (p1 == p2) return false;

        if (rank[p1] < rank[p2]) {
            pars[p1] = p2;
            rank[p2] += rank[p1];
        } else {
            pars[p2] = p1;
            rank[p1] += rank[p2];
        }

        return true;
    }
};

class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        DSU dsu(n);

        for (const auto& vec : edges) {
            dsu.union_find(vec[0], vec[1]);
        }
        
        int res = 0;
        for (int i = 0; i < n; ++i) {
            if (dsu.pars[i] == i) ++res;
        }

        return res;
    }
};
