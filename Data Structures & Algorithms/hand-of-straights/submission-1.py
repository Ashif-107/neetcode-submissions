class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        freq = Counter(hand)
        hand.sort()
       
        for x in hand:
            if freq[x] == 0:
                continue
            
            for num in range(x, x+groupSize):
                if freq[num] == 0:
                    return False
                
                freq[num] -= 1
        
        return True