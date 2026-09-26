class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        first = 0
        second = 0
        knowledge_map = {}
        for element in knowledge:
            knowledge_map[element[0]] = element[1]

        parts = []
        while first < len(s):
            if s[first] != "(":
                parts.append(s[first])
                first += 1
            else:
                while s[second] != ")":
                    second += 1
                key_word = s[first + 1:second]
                if key_word not in knowledge_map.keys():
                    parts.append('?')
                else:
                    parts.append(knowledge_map[key_word])
                first = second + 1
                second += 1

        return "".join(parts)
