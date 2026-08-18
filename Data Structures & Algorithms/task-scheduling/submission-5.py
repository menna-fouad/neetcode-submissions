class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0] * 26
        for task in tasks:
            counts[ord(task) - ord('A')] += 1
        
        max_freq = max(counts)
        max_count = 0
        for count in counts:
            max_count += 1 if count == max_freq else 0
        
        time = (max_freq - 1) * (n + 1) + max_count
        return max(time, len(tasks))
        