


playerHands = [
['A', 'K', 'K', 'Q', 'Q'],
['A', 'Q', 'J', 'J', '9'],
['K', '9', '9', 'J', '8'],
]
# playerHands = [
# ['14', '6', '14', '6'],
# ['13', '9', '14', '7'],
# ]
# playerHands = [
# ['A', 'K', '8', '8', '6'],
# ['A', '3', 'Q', '5', '9', 'K', 'J'],
# ['A', '5', 'Q', '4', '7', '2', '3'],
# ['A', 'Q', 'J', 'J', '9'],
# ]


# playerHands = [
# ['A', 'K', '8', '8', '6'],
# ['A', '3', 'Q', '5', '9', 'K', 'J'],
# ['A', '5', 'Q', '4', '7', '2', '3'],
# ]


# playerHands = [
# ['A', '2', '3'],
# ['2', '3', 'A'],
# ['3', 'A', '2'],
# ]

# playerHands = [
# ['2', '4'],
# ['2', '4', '5', '9'],
# ]

# playerHands = [
# ['2', '4'],
# ['2', '4'],
# ]
# 2
# 3
# 5 A K K Q Q
# 5 A Q J J 9
# 5 K 9 9 J 8
# 3
# 5 A 2 3
# 7 2 3 A
# 7 3 A 2

original_hands = sorted(list(playerHands))



def getVal(card):
	if card.isdigit():
		return int(card)
	if card == 'A':
		return 14
	if card == 'J':
		return 11
	if card == 'Q':
		return 12
	if card == 'K':
		return 13
	return -1


#war
def war(playerHands, prevWinners, cardsLost):

	
	currwinners = []

	# we start from 3rd card
	for cardpos in xrange(2, 100, 2):
		maxCard = 0
		currwinners = []

		# only involved people who tied
		for i in prevWinners:
			if len(playerHands[i]) > cardpos+1:
				topCard = getVal(playerHands[i][cardpos])
				if topCard > maxCard:
					maxCard = topCard
					currwinners = [i]
				elif topCard == maxCard:
					currwinners.append(i)
		losers = set(prevWinners)-set(currwinners)
		for i in losers:
			cardsLost[i] += cardpos

		# for situation where everyone has less than 2 cards
		if currwinners == []:			
			return battle([hand[1:] for hand in playerHands])

		# end only if no winner or only 1 winner
		if len(currwinners)<=1:
			cardsLost[currwinners[0]] += cardpos
			break

		# play round again if not conclusive
		prevWinners = currwinners
	return cardsLost, currwinners



def battle(playerHands):
	maxCard = 0
	winners = []
	
	# for i in xrange(len(playerHands)):
	# 	if len(playerHands[i]) > 0:
	# 		topCard = getVal(playerHands[i][0])

	# 		if topCard > maxCard:
	# 			maxCard = topCard
	# 			winners = [i]	
	# 		elif topCard == maxCard:
	# 			winners.append(i)

	for i, player in enumerate(playerHands):
		if len(player) > 0:
			topCard = getVal(player[0])
			if topCard > maxCard:
				maxCard = topCard
				winners = [i]	

			elif topCard == maxCard:
				winners.append(i)			
	# everyone loses 1 card in a battle
	cardsLost = [1] * len(playerHands)


	if len(winners) > 1:
		cardsLost, winners = war(playerHands, winners, cardsLost)

	# print playerHands
	return cardsLost, winners

def playRounds(playerHands, original_hands):
	cardsLost, roundWinner = battle(playerHands)

	if (len(roundWinner)==1):
		winnerHand = playerHands[roundWinner[0]][cardsLost[roundWinner[0]]:]
		# all cards go to winner
		for i, lost in zip(xrange(len(playerHands)), cardsLost):
			winnerHand.extend(playerHands[i][0:lost])
			playerHands[i] = playerHands[i][lost:]

		playerHands[roundWinner[0]] = winnerHand
		# count empty hands, if everyone has empty hands, return index of winner
		# overallWinner should be equal to roundWinner
		emptyHands = 0
		overallWinner = -1
		# print playerHands
		for i, player in enumerate(playerHands):
			if len(player)==0:
				emptyHands += 1
			else:	
				overallWinner = i+1
		if emptyHands == len(playerHands)-1:
			return overallWinner

	# if cycle situation
	if original_hands == sorted(playerHands):
		return "No Winner"

	# keep playing if no winner and not cycle
	else: 
		return playRounds(playerHands, original_hands)



# def main():
# 	testcases = [[] for i in xrange(int(raw_input()))]
# 	for i in xrange(len(testcases)):
# 		playerHands = [[] for j in xrange(int(raw_input()))]
# 		for k in xrange(len(playerHands)):
# 				playerHands[k].extend(raw_input().split()[1:])

# 		testcases[i] = playerHands

# 	for i in xrange(len(testcases)):
# 		original_hands = sorted(list(testcases[i]))
# 		print playRounds(testcases[i], original_hands)


# if __name__ == "__main__":
#     main()


print playRounds(playerHands, original_hands)