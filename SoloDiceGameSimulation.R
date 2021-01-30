"
ECS 132: Probability and Statistical Modeling for Computer Science
By: Suryakiran Santhosh, Stephen Wong, Patrick Chan, and Curtis Stofer
University of California Davis Winter 2021
Homework #1 Problem 2 (Jill Solo Dice Game Simulation - Recursive)
"


pnk < - function(d, s, k){
    probability < - 0

    # if no turns left, you have zero probability of reaching the winning threshold
    if (k == 0){
        return(0)
    }

    # If d is negative, because your next roll is 1-s, you are guaranteed to win
    if (d <= 0){
        return(1)
    }

    # ex. k = 1, s = 6, d = 5. Rolling either 5 or 6 would result in a win
    # (6 - 5 + 1)/6 = 2/6.
    # ex. k = 1, s = 6, d = 1. Rolling 1,2,3,4,5, or 6 would result in a win
    # (6 - 1 + 1)/6 = 6/6

    # This is the reason for the +1
    if (k == 1 & 1 <= d & d <= s){  # If you only have 1 try, you need to roll a value equal or greater than d
        return((s-d+1)/s)
    }else if (k == 1 & d > s){
        # Impossible to reach value of d with rolls 1-s in one turn
        return(0)
    }

    for (r in 1: s){
        probability < - probability + pnk(d-r, s, k-1)
    }
    return(probability/s)
}


main < - function(){
    print(pnk(5, 6, 1))
    print(pnk(5, 100, 1))
    print(pnk(6, 6, 2))
}

main()
