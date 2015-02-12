# IDA-Hackertrail

Solution to the Hackertrail contest hosted by IDA. 
The solution was initially coded in python (a language that I was familar with). 
The ruby script was then written (a direct conversion from the python script) as an exercise to pick up ruby.

### Problem

War is a very popular game among kids. The rules are simple. The deck of cards is divided between players. In each round all players set out one card and the oldest card wins (color doesn't matter). The winner of the round takes all the cards and puts them on the bottom of his pot. If two or more players have the same cards then the "war" begins. In this case owners of the oldest cards set out two more cards and put them on their cards. The winner is the player whose top card is the oldest one. If there still is more than one victor then the war remains. The winner is the player who at the end collects all of his opponents' cards.

In the case that during a war a player is left with no more cards, the player with the most number of cards on hand wins.

Everyone that has ever played War knows that it may last very long and its score is foregone at the beginning. Save players' time and write a program that determines the winner.

Examplary round
Before the round:
player 1: A K 8 8 6
player 2: A 3 Q 5 9 K J
player 3: A 5 Q 4 7 2 3

After the round:
player 1: 8 6
player 2: K J A K 8 A 3 Q 5 9 A 5 Q 4 7
player 3: 2 3

Input
First line of the input contains number of tests t (t≤20). Each test consists of number of players n (2≤n≤8) and n more lines. At the beginning of each line there is an integer m (m<99) being the number of cards the current player has. Then, separated by spaces follow m characters ('A', 'K', 'Q', 'J') or numbers in range from 2 to 10describing the kind of each card.

Output
For each test print the index of the winner (starting from 1).

If there is no winner in the test, output should display No Winner.

Example
Input:
2
3
5 A K K Q Q
5 A Q J J 9
5 K 9 9 J 8
3
5 A K 8 8 6
7 A 3 Q 5 9 K J
7 A 5 Q 4 7 2 3

Output:
1
2
