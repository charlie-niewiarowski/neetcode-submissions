struct TrieNode {
    TrieNode() {
        children.assign(26, nullptr);
        end = false;
    }

    vector<TrieNode*> children;
    bool end;
};

class PrefixTree {
public:
    PrefixTree() {
        root = new TrieNode();
    }
    
    void insert(string word) {
        TrieNode *curr{root};

        for (const char ch : word) {
            int idx{ch - 'a'};

            if (curr->children[idx] == nullptr) {
                curr->children[idx] = new TrieNode();
            }

            curr = curr->children[idx];
        }

        curr->end = true;
    }
    
    bool search(string word) {
        TrieNode *curr{root};

        for (const char ch : word) {
            int idx{ch - 'a'};
            if (curr->children[idx] == nullptr) return false;
            curr = curr->children[idx];
        }

        return curr->end;
    }
    
    bool startsWith(string prefix) {
        TrieNode *curr{root};

        for (const char ch : prefix) {
            int idx{ch - 'a'};
            if (curr->children[idx] == nullptr) return false;
            curr = curr->children[idx];
        }   

        return true;
    }
private:
    TrieNode *root;
};
