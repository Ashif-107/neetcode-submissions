class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = sorted(zip(position,speed), reverse=True)

        fleets = 0
        lasttime = 0

        for pos, spd in cars:
            time = (target-pos) / spd
            if time > lasttime:
                fleets += 1
                lasttime = time
            
        return fleets