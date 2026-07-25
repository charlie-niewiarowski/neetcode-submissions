class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {char: idx for idx, char in enumerate(order)}

        for i in range(len(words) - 1):
            w1, w2, = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            for j in range(minLen):
                print(w1[j], w2[j])
                if w1[j] != w2[j]:
                    if order_map[w1[j]] > order_map[w2[j]]:
                        return False
                    break
            else:
                if len(w1) > len(w2):
                    return False

        return True
            
