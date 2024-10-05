from copy import deepcopy
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(req_skills)
        skill_index = {skill: i for i, skill in enumerate(req_skills)}

        dp = {0:[]}
        for i, person in enumerate(people):
            people_skills = 0

            for skill in person:
                people_skills |= 1 << skill_index[skill]

            for pre_skills,team in list(dp.items()):
                updated_skills = people_skills | pre_skills
                
                if updated_skills == pre_skills:
                    continue
                
                if (updated_skills not in dp) or len(dp[updated_skills]) > len(team) + 1:
                    dp[updated_skills] = team + [i]
        return dp[(1<<n)-1]
                    
                    
             
                

        