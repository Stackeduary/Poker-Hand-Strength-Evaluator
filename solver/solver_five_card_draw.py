from collections import defaultdict
from itertools import combinations

class Solver(object):

    def process(self, line: str) -> str:
        """
        TODO Implement correct solution logic
        """

        # to calculate individual card values
        card_order_dict = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

        # The next nine functions evaluate whether a hand is a straight flush, full house, etc.

        def check_straight_flush(hand):
            if check_flush(hand) and check_straight(hand):
                return True
            else:
                return False

        def check_four_of_a_kind(hand):
            values = [i[0] for i in hand]
            value_counts = defaultdict(lambda:0)
            for v in values: 
                value_counts[v] += 1
            if sorted(value_counts.values()) == [1,4]:
                return True
            return False

        def check_full_house(hand):
            values = [i[0] for i in hand]
            value_counts = defaultdict(lambda:0)
            for v in values: 
                value_counts[v] += 1
            if sorted(value_counts.values()) == [2,3]:
                return True
            return False

        def check_flush(hand):
            suits = [i[1] for i in hand]
            if len(set(suits)) == 1:
                return True
            else:
                return False

        def check_straight(hand):
            values = [i[0] for i in hand]
            value_counts = defaultdict(lambda:0)
            for v in values:
                value_counts[v] += 1
            rank_values = [card_order_dict[i] for i in values]
            value_range = max(rank_values) - min(rank_values)
            # value_range = rank_values #max(rank_values) - min(rank_values)
            if len(set(value_counts.values())) == 1 and value_range == 4:
                return True
            else: 
                # check straight with low ace
                if set(values) == set(["A", "2", "3", "4", "5"]):
                    return True
                return False

        def check_three_of_a_kind(hand):
            values = [i[0] for i in hand]
            value_counts = defaultdict(lambda:0)
            for v in values:
                value_counts[v] += 1
            if set(value_counts.values()) == set([3, 1]):
                return True
            else:
                return False

        def check_two_pair(hand):
            values = [i[0] for i in hand]
            value_counts = defaultdict(lambda:0)
            for v in values:
                value_counts[v] += 1
            if sorted(value_counts.values()) == [1, 2, ]:
                return True
            else:
                return False

        def check_pair(hand):
            values = [i[0] for i in hand]
            value_counts = defaultdict(lambda:0)
            for v in values:
                value_counts[v] += 1
            if 2 in value_counts.values():
                return True
            else:
                return False

        def check_hand(hand):
            if check_straight_flush(hand):
                return 9
            if check_four_of_a_kind(hand):
                return 8
            if check_full_house(hand):
                return 7
            if check_flush(hand):
                return 6
            if check_straight(hand):
                return 5
            if check_three_of_a_kind(hand):
                return 4
            if check_two_pair(hand):
                return 3
            if check_pair(hand):
                return 2
            return 1 # one point for high card is the default case when no other hand values apply

        # convert a hand in list form back to string form after its value has been calculated
        def stringify_result(hand_list):
            result = ""
            for suited_card in hand_list:
                result += (suited_card + " ")
                result = result.rstrip()
            return result

        # split the input string into a list of strings
        input_list = line.split(" ")
        hand_list = []
        high_card = 0

        # split the hand string into a list of individual cards and append that list to a list of hands
        for i in range(1, len(input_list)):
            hand = [i + j for i, j in zip(input_list[i][::2], input_list[i][1::2])]
            hand_list.append(hand)        
        total_value = 0  
        best_hand_dict = {}

        # for each hand in the hand_list, get and record its hand_value from the check_hand() function, its high card value and the total point value of the hand
        for j in range(len(hand_list)):
            hand = hand_list[j]
            hand_value = check_hand(hand)
            for card in range(len(hand)):
                total_value += card_order_dict[hand[card][0]]
                if card_order_dict[hand[card][0]] > high_card:
                    high_card = card_order_dict[hand[card][0]]

            # store the hand as a key and its value is a tuple containing its hand value, high card value and total hand value
            best_hand_dict[stringify_result(hand)] = hand_value, high_card, total_value
            total_value = 0 
            high_card = 0

        # create a new dictionary that sorts the hands based on the hand value, high card and total card value; this will allow breaking ties based on the value of the hand, then by high card, then by total card value in that order
        sorted_dict = dict(sorted(best_hand_dict.items(), key = lambda x:x[1]))

        # return the result in string representation
        result = ""
        for key in sorted_dict.keys():
            result += key + " "
        return result.rstrip()