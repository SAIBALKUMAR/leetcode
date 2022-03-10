class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        roomvisited=set()
        keys=[0]
        while len(keys)>0:
            i=keys.pop(0)
            roomvisited.add(i)
            for j in rooms[i]:
                if j not in roomvisited:
                    keys.append(j)
            
        
        return len(roomvisited)==len(rooms)
        