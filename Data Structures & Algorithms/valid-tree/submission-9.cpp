class DSU {
private:
    vector<int> rank;
public:
    vector<int> pars;

    DSU(int n) {
        pars.resize(n);
        for (int i{}; i < n; ++i) pars[i] = i;
        rank.resize(n, 1);
    }

    int find(int n) {
        if (pars[n] == n) return n;
        return pars[n] = find(pars[n]);
    }

    bool union_find(int n1, int n2) {
        int p1 = find(n1), p2 = find(n2);
        if (p1 == p2) return false; // cycle

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
    bool validTree(int n, vector<vector<int>>& edges) {
        int num_edges = edges.size();
        if (num_edges != n - 1) return false;

        DSU dsu(n);
        for (auto& e : edges) {
            if (!dsu.union_find(e[0], e[1])) return false;
        }

        int num_components = 0;
        for (int i{}; i < n; ++i) {
            if (dsu.pars[i] == i) ++num_components;
        }

        return num_components == 1;
    }
};
