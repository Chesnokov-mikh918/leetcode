class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        def is_valid(segment: str) -> bool:
            if len(segment) > 1 and segment[0] == '0':
                return False
            if int(segment) > 255:
                return False
            return True

        def backtrack(start_pos, parts):
            if len(parts) == 4 and start_pos == len(s):
                result.append('.'.join(parts)) # поэкспериментируй с join
            if len(parts) == 4:
                return # то все, остановка, плохой вариант мы значит нашли
            remain_seg = 4 - len(parts)
            remain_char = len(s) - start_pos
            if remain_char < remain_seg or remain_char > remain_seg * 3:
                return

            for cur_len in (1, 2, 3):
                if start_pos + cur_len > len(s):
                    break
                if is_valid(s[start_pos:start_pos + cur_len]):
                    parts.append(s[start_pos:start_pos + cur_len])
                    backtrack(start_pos + cur_len, parts)
                    parts.pop()

        backtrack(0, [])
        return result