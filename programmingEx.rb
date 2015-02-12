# playerHands = [
# ['A', 'K', '8', '8', '6'],
# ['A', '3', 'Q', '5', '9', 'K', 'J'],
# ['A', '5', 'Q', '4', '7', '2', '3'],
# ]
# playerHands = [
# ['14', '6', '14', '6'],
# ['13', '9', '14', '7'],
# ]

playerHands = [
['A', 'K', 'K', 'Q', 'Q'],
['A', 'Q', 'J', 'J', '9'],
['K', '9', '9', 'J', '8'],
]
# playerHands = [
# ['A', 'K', '8', '8', '6'],
# ['A', '3', 'Q', '5', '9', 'K', 'J'],
# ['A', '5', 'Q', '4', '7', '2', '3'],
# ['A', 'Q', 'J', 'J', '9'],
# ]

# playerHands = [
# ['A', '2', '3'],
# ['2', '3', 'A'],
# ['3', 'A', '2'],
# ]

# playerHands = [
# ['2', '4'],
# ['2', '4'],
# ]


# playerHands = [
# ['2', '4'],
# ['2', '4', '5', '9'],
# ]

original_hands = Array.new(playerHands).sort

def isdigit?(lookAhead)
  lookAhead =~ /[0-9]/
end

def getVal(card)
	if isdigit? card
		return card.to_i
	end
	case card
	when 'J'
		return 11
	when 'Q'
		return 12
	when 'K'
		return 13
	when 'A'
		return 14
	end
	return -1
end

def war(playerHands, prevWinners, cardsLost)
	currwinners = []

	(2...100).step(2) do |cardpos|
		maxCard = 0
		currwinners = []

		prevWinners.each do |i|
			if playerHands[i].count > cardpos+1
				topCard = getVal playerHands[i][cardpos]
				if topCard > maxCard
					maxCard = topCard
					currwinners = [i]
				elsif topCard == maxCard
					currwinners << i
				end
			end
		end
		losers = prevWinners.uniq - currwinners.uniq
		losers.each do |i| 
			cardsLost[i] += cardpos
		end
		if currwinners.empty?			
			return battle playerHands.collect{ |hand| hand[1..-1] } 
		end
		
		if currwinners.count<=1
			cardsLost[currwinners.first] += cardpos
			break
		end
		prevWinners = currwinners
	end
	
	return cardsLost, currwinners
end


def battle(playerHands) 
	maxCard = 0
	winners = []
	
	playerHands.each_with_index do |player, i|
		if not player.empty?
			topCard = getVal(player.first)
			if topCard > maxCard
				maxCard = topCard
				winners = [i]
				
			elsif topCard == maxCard
				winners << i
			end
		end
	end
	# everyone loses 1 card in battle 
	cardsLost = Array.new(playerHands.count, 1)
	
	if winners.count > 1
		cardsLost, winners = war playerHands, winners, cardsLost
	end
	
	return cardsLost, winners

end

def playRounds(playerHands, original_hands)
	cardsLost, roundWinner = battle playerHands

	if roundWinner.count == 1
		# print playerHands
		winnerHand = playerHands[roundWinner.first][cardsLost[roundWinner.first]..-1]
		# print playerHands
		# all cards go to winner
		# print playerHands
		((0...playerHands.count).zip(cardsLost)).each do |i, lost|
			winnerHand += playerHands[i][0...lost]
			playerHands[i] = playerHands[i][lost..-1] == nil ? [] : playerHands[i][lost..-1]
		end 
		playerHands[roundWinner.first] = winnerHand
		# count empty hands, if everyone has empty hands, return index of winner
		# overallWinner should be equal to roundWinner
		emptyHands = 0
		overallWinner = -1
		# print playerHands

		playerHands.each_with_index do |player, i|
			if player.empty?
				emptyHands +=1
			else
				overallWinner = i+1
			end
		end

		if emptyHands == playerHands.count-1
			return overallWinner
		end

	end

	# if cycle situation
	if original_hands == playerHands.sort
		return "No Winner"
	# keep playing if no winner and not cycle
	else
		return playRounds(playerHands, original_hands)
	end
end


puts playRounds(playerHands, original_hands)