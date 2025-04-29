"""
Fact 1: Lemonades cost $5.
Fact 2: One lemonade per-customer.
Fact 3: We accept 5, 10, and 20 bills.
Fact 4: We must return the correct amount of change to customer.
Fact 5: We start with no change.

Return Value: Bool. True means we can give change to all customers. Otherwise false.

Approach: The only greedy choice here is whether or not we give a 10 dollar bill whenever someone pays with a 20. The answer is: if possible, yes we give a 10 bill back, since 20 is the only denomination for which we can give 10 bills in change. We want to save our 5s if someone pays in 10s, so give 10s whenever possible.

"""

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = tens = twenties = 0
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                tens += 1
                fives -= 1
            else:
                if tens > 0:
                    tens -= 1
                    fives -= 1
                else:
                    fives -= 3
            if fives < 0 or tens < 0:
                return False
        return True
