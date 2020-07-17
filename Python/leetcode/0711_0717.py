# 1493(array)
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        arr = []
        for i, v in enumerate(nums):
            if v == 0:
                arr.append(i)
        answer = 0
        if len(arr) == 0 or len(arr) == 1:
            return len(nums) - 1
        for i, v in enumerate(arr):
            left = -1 if i == 0 else arr[i-1]
            right = len(nums) if i == len(arr)-1 else arr[i+1]
            answer = max(answer, right-left-2)

        return answer

# 1418(hash table)
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        table_dict, order_table = {}, []
        display_table = [[]]

        for order in orders:
            if order[2] not in display_table[0]:
                display_table[0].append(order[2])
                
            if order[1] in table_dict:
                if order[2] in table_dict[order[1]]:
                    table_dict[order[1]][order[2]] += 1
                else:
                    table_dict[order[1]][order[2]] = 1
            else:
                table_dict[order[1]] = {order[2]: 1}

        display_table[0].sort()
        d = display_table.pop()

        for table, order in table_dict.items():
            for menu in d:
                if menu in order:
                    order_table.append(str(order[menu]))
                else:
                    order_table.append('0')
            order_table.insert(0, int(table))
            display_table.append(order_table)
            order_table = []
        display_table.sort()
        
        for display in display_table:
            display[0] = str(display[0])

        display_table.insert(0, d)
        display_table[0].insert(0, 'Table')
        
        return display_table

# 1461(string)
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        max_s = int('1' * k, 2)
        nums = set()
        for i in range(len(s)-k+1):
            num = s[i:i+k]
            nums.add(num)
        if len(nums)-1 == max_s:
            return True
        else:
            return False