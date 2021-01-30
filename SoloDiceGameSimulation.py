"""
ECS 132: Probability and Statistical Modeling for Computer Science
By: Suryakiran Santhosh, Stephen Wong, Patrick Chan, and Curtis Stofer
University of California Davis Winter 2021
Homework #1 Problem 2 (Jill Solo Dice Game Simulation - Recursive)
"""


def pnk(d: int, s: int, k: int) -> float:
    probability = 0

    if k == 0:  # if no turns left, you have zero probability of hitting a number
        return 0

    if d <= 0:  # If d is negative, because your next roll is 1-s, you are guaranteed to win
        return 1

    # 0 or 1, e.g. p1,1, = 1"?
    # ex. k = 1, s = 6, d = 5. Rolling either 5 or 6 would result in a win
    # (6 - 5 + 1)/6 = 2/6.
    # ex. k = 1, s = 6, d = 1. Rolling 1,2,3,4,5, or 6 would result in a win
    # (6 - 1 + 1)/6 = 6/6
    if k == 1 and 1 <= d <= s:  # If you only have 1 try, you only have a change
        return (s-d+1)/s

    if k == 1 and d > s:  # Impossible to reach value of d with rolls 1-s in one turn
        return 0

    for r in range(1, s+1):
        probability += pnk(d-r, s, k-1)

    return(probability/s)


def main():
    print(pnk(1, 6, 1))  # Roll 1 dice once with sum of 1
    print(pnk(6, 6, 2))  # Roll a dice twice with sum of 6
    print(pnk(3, 100, 2))
    print(pnk(5, 6, 1))
    print(pnk(5, 100, 1))
    print(pnk(6, 6, 2))  # Textbook example of Table 2.1 on page 5


if __name__ == "__main__":
    main()
