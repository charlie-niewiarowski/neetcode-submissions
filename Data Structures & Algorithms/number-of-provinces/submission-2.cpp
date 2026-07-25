class DSU {
private:
    vector<int> pars, rank;
    int components;
public:
    DSU(int n) {
        pars.resize(n);
        rank.assign(n, 1);
        components = n;
        for (int i = 0; i < n; ++i) pars[i] = i;
    }
    
    int find(int node) {
        if (pars[node] != node) {
            pars[node] = find(pars[node]);
        }
        return pars[node];
    }

    bool unionSet(int u, int v) {
        int pu = find(u), pv = find(v);
        if (pu == pv) return false;

        if (rank[pu] > rank[pv]) {
            pars[pv] = pu;
            rank[pu] += rank[pv];
        } else {
            pars[pu] = pv;
            rank[pv] += rank[pu];
        }

        --components;
        return true;
    }

    int numComponents() {
        return components;
    }
};

class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        DSU dsu(n);

        for (int r = 0; r < n; ++r) {
            for (int c = 0; c < r; ++c) {
                if (isConnected[r][c]) dsu.unionSet(r, c);
            }
        }

        return dsu.numComponents();
    }
};