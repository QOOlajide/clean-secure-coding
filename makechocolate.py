def make_chocolate(small, big, goal):
     max_bars = min(big, goal // 5)
     remianing = max(0, goal - (max_bars * 5))
     if small >= remianing:
        return remianing
     return -1
