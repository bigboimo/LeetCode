class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seatsTaken = set()
        seats.sort()
        students.sort()
        res = 0
        print(seats, students)

        for i in range(len(seats)): 
            res += abs(seats[i] - students[i])
            seatsTaken.add(seats[i])
        
        return res