class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solution=defaultdict(list) 
        for sol in strs:
            sorS="".join(sorted(sol))
            solution[sorS].append(sol)
        return list(solution.values())