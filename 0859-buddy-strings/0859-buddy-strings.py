class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        if s==goal:
            if s == goal and len(set(s)) < len(goal): return True
            else:
                return False
        else:
            listed = []
            for i in range(len(s)):
                if s[i]!=goal[i]:
                    listed.append(i)
                else:
                    pass
            if len(listed)==2:
                if s[listed[0]]==goal[listed[1]] and  s[listed[1]]==goal[listed[0]]:
                    return True 
                else:
                    return False
        