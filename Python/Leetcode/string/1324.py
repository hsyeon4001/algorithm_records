# 1324. Print Words Vertically
# 1) 내장함수 => 28 ms / 14 MB
class Solution:
    def printVertically(self, s: str) -> List[str]:
        l=list(s.split(" "))
        le=len(max(l,key=len))
        return (["".join(list(e)).rstrip() for e in zip(*list(map(lambda x:x.ljust(le," "), l)))])