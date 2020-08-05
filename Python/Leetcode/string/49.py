# 49. Group Anagrams
# 1) dict => 100 ms / 16.6 MB
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        result = []
        for string in strs:
            s_word = "".join(sorted(string))
            if s_word in words:
                words[s_word].append(string)
            else:
                words[s_word] = [string]
        
        for word in words.values():
            word.sort()
            result.append(word)
            
        return result

# 2) collections.defaultdict => 96ms / 17.3 MB
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        import collections
        anagrams = collections.defaultdict(list)
        
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
            
        return anagrams.values()