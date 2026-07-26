class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white_count = 0
        for i in range(0, k):
            if (blocks[i] == 'W'):
                white_count += 1
        
        min_changes = white_count
        for i in range(k, len(blocks)):
            if (blocks[i - k] == 'W' and blocks[i] == 'B'):
                white_count -= 1
            if (blocks[i - k] == 'B' and blocks[i] == 'W'):
                white_count += 1
            min_changes = min(min_changes, white_count)
        return min_changes

