class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 10**9 + 7
        dp = {}

        def count(goal_left, traversed_songs):
            if (goal_left == 0 and traversed_songs == n):
                return 1
            if (goal_left == 0 or traversed_songs > n):
                return 0
            if (goal_left,traversed_songs) in dp:
                return dp[(goal_left,traversed_songs)]
            
            res = (n - traversed_songs) * count(goal_left -1 , traversed_songs+1)

            if traversed_songs > k:
                res += (traversed_songs - k) * count(goal_left -1 , traversed_songs)

            dp[(goal_left, traversed_songs)] = res % mod
            return dp[(goal_left, traversed_songs)] 
        return count(goal,0)

            
