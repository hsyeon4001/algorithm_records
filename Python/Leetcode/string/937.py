# 937. Reorder Data in Log Files
# lambda key => 72 ms / 13.8 MB 
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dig, let = [], []
        for log in logs:
            chk = log.split(" ")
            if chk[1].isdigit():
                dig.append(log)
            else:
                let.append(log)
        let.sort(key = lambda x : (x.split(" ")[1:], x.split(" ")[0]))

        return let + dig