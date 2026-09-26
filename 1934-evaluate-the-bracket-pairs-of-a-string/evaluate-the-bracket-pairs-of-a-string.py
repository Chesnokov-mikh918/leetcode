class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        ans_str = ""
        first = 0
        second = 0
        knowledge_map = {}
        for element in knowledge:
            knowledge_map[element[0]] = element[1]

        while first < len(s):
            if s[first] != "(":
                ans_str += s[first]
                first += 1
            else:
                while s[second] != ")":
                    second += 1
                key_word = s[first + 1:second]
                if key_word not in knowledge_map.keys():
                    ans_str += '?'
                else:
                    ans_str += knowledge_map[key_word]
                first = second + 1
                second += 1

        return ans_str
