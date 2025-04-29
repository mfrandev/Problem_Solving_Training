"""
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
    - Will need some way to approach the circular thing.

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
    - "cost[i]" gas is needed to move from i to i + 1 

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.
    - We know that len(gas) == len(cost) ( == n )
    - Solution may not exist.
    - Start off assuming that clockwise traversal is necessary. If can prove a simpler solution with counterclockwise traversal, good, but be careful.

Observation 1: We have an obvious mapping between gas and cost
Observation 2: Absolutely nothing said about needing to start at index 0. 
Observation 3: Our return value represents the index at which we start traversing when we can make a full loop. 
Observation 4: If we run out of gas, that's totally fine as long as we've not looped through the array once already.
Observation 5: If at any point the amount of gas in our tank + the amount of gas at the current station is insufficient to reach the next stop, then we have to pick a new starting position.
Observation 6: In other words, our invariant is curr_gas + gas[i] >= cost[i]

Q1: Is there a way we can avoid doing repeated work?
A1: Yes! Clever observation shows that if sum(cost) > sum(gas), then no solution exists. Additionally, since the solution is unique, we can apply inductive reasoning. 
Ex: Gas: [1,2,3,4,5], Cost: [3,4,5,1,2] Since we see that i = 4 is a good position, and i = 3 is a good position, we know that i = 3 is the solution, and not i = 4 by induction, because solution is unique.

"""


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        # If this doesn't return, we know a solution is guaranteed to exist
        if sum(gas) < sum(cost):
                return -1

        gas_in_tank = 0
        start = 0
        
        for i in range(n):
            if gas_in_tank + gas[i] < cost[i]:
                start = i + 1
                gas_in_tank = 0
            else:
                gas_in_tank = gas_in_tank + gas[i] - cost[i]

        return start
             
