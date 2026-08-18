class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0] * 26
        for task in tasks:
            counts[ord(task) - ord('A')] += 1
        
        counts.sort()
        maxf = counts[25]
        idle = (maxf - 1) * n

        for i in range(24, -1, -1):
            idle -= min(maxf - 1, counts[i])
        
        return max(0, idle) + len(tasks)
        