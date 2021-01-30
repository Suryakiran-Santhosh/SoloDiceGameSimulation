# SoloDiceGameSimulation
Recursive Implementation of Probability Calculation Problem


In the context of Problem 1--Dice_Game_Simulation Repo--now suppose the game consists of only one player (still to be referred to as Jill). Let N denote the number of turns it takes to win. We will be interested in P(N = k). You will find code to find the exact value of this probability (not a simulation). Also, we will now generalize from an ordinary die to an s-sided one.

The call form will be:

    pnk(d,s,k)
    where d is as above and s is the number of sides on the die, all equally likely.

Your code will be recursive, exploiting the following relation. Let pd,k = P(N = k) for a winning threshold of d. (The quantity s is fixed here, so it doesn't appear as a subscript.) Then

    pd,k = (1/s) Σr=1,...,s pd-r,k-1

The basic idea is that if Jill's first turn yields r dots, then she now is shooting for a total of d-r, and has k-1 turns left to meet her original goal of k.
A key point will be that some of the pd,k will be 0 or 1, e.g. p1,1 = 1.
