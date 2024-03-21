
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        step = 1
        N = len(beginWord)
        queue = deque([(beginWord, step)])
        visited = set()
        all_comb_dict = defaultdict(list)

        for word in wordList:
            for i in range(N):
                all_comb_dict[word[:i] + "*" + word[i + 1:]].append(word)  # 每一个可能的组合里面都append进这个word

        while queue:
            current_word, step = queue.popleft()
            for i in range(N):
                intermediate_word = current_word[:i] + "*" + current_word[i + 1:]
                for word in all_comb_dict[intermediate_word]:
                    if word == endWord:
                        return step + 1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, step + 1))

        return 0

