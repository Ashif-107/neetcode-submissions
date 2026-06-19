class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = sorted(zip(position,speed), reverse=True)

        fleets = []
        for pos, spd in cars:
            time = (target-pos) / spd

            if not fleets:
                fleets.append(time)
            if time > fleets[-1]:
                fleets.append(time)
            
        return len(fleets)