class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        k = []
        s = 0 
        for i in range(len(logs)):
            # print(logs[i][1])
            # print("s",s)
            k.append([abs(s-logs[i][1]),i])
            s = logs[i][1]
        k.sort()
        print(k)
        h = k[len(k)-1][0]
        print(h)
        o = []
        for u in range(len(k)):
            o.append(k[u][0])
        print(o)
        counter = o.count(h)
        print(counter)
        if counter ==1:
            return logs[k[-1][1]][0]
        else:
            mins = 100000000000000
            while counter>=1:
                
                mins = min(mins,logs[k[-counter][1]][0])
                counter= counter -1
            return mins
