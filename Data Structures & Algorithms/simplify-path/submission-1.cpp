/*
iterate over the string
if we see a slash(es) that means the current directory name has concluded it
so push it to a stack
if we see a period do nothing
if we see two periods pop from the stack if it's non empty
after done iterating, build a slash separated string from the stack's entries
*/

class Solution {
public:
    string simplifyPath(string path) {
        vector<string> stk;
        size_t i{}, n{path.size()};
        string inode{""};

        while (i < n) {
            while (i < n && path[i] == '/') {
                ++i;
            }

            while (i < n && path[i] != '/') {
                inode += path[i++];
            }

            if (inode == "..") {
                if (!stk.empty()) {
                    stk.pop_back();
                }
            } else if (inode != "." && !inode.empty()) {
                stk.push_back(inode);
            }

            inode = "";
        }

        string result = "/";
        for (int i = 0; i < stk.size(); ++i) {
            if (i > 0) result += "/";
            result += stk[i];
        }

        return result;
    }
};