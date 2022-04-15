from collections import defaultdict

class Solver(object):

    def process(self, line: str) -> str:
        """
        TODO Implement correct solution logic
        """

        card_order_dict = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13, "A":14}

        hand_list = line.split(" ")
        hand_list.pop(0)

        card_values = []
        ranked_hands = {}
        unsorted_dict = {}

        for hand in hand_list:
            value_counts = defaultdict(lambda:0)
            suit_set = set()
            for i in range(len(hand)):
                if i % 2 == 0:
                    card_values.append(hand[i])
                    value_counts[hand[i]] += 1
                if i % 2 == 1:
                    suit_set.add(hand[i])

            rank_values = [card_order_dict[i] for i in card_values]
            value_range = max(rank_values) - min(rank_values)        

            hand_value = 1
            if 2 in value_counts.values():
                hand_value = 2   
            if sorted(value_counts.values()) == [1, 2, 2]:
                hand_value = 3  
            if set(value_counts.values()) == set([3, 1]):
                hand_value = 4       
            if len(set(value_counts.values())) == 1 and (value_range == 4):
                hand_value = 5
            if len(suit_set) == 1:
                hand_value = 6    
            if sorted(value_counts.values()) == [2, 3]:
                hand_value = 7    
            if sorted(value_counts.values()) == [1, 4]:
                hand_value = 8
            if (len(suit_set) == 1 and len(set(value_counts.values())) == 1 and value_range == 4):
                hand_value = 9    

            outputString = "".join(hand)
            unsorted_dict[outputString] = hand_value
            card_values = []
            rank_values = []
        ranked_hands = dict(sorted(unsorted_dict.items(), key=lambda x:x[1]))

        result = ""
        for ranked_hand in ranked_hands.keys():
            result += (ranked_hand + " ")
        result = result.rstrip()
        print(result)

    print("Ranking of example hands:")
    process(process, "five-card-draw 7h4s4h8c9h Tc5h6dAc5c Kd9sAs3cQs Ah9d6s2cKh 4c8h2h6c9c")

    print("Ranking of hands, test set 1:")
    process(process, "five-card-draw 4s5hTsQh9h Qc8d7cTcJd 5s5d7s4dQd 3cKs4cKdJs 2hAhKh4hKc 7h6h7d2cJc As6d5cQsAc")
    
    print("Ranking of hands, test set 2:")
    process(process, "five-card-draw 7h4s4h8c9h Tc5h6dAc5c Kd9sAs3cQs Ah9d6s2cKh 4c8h2h6c9c")

    print("Ranking of hands, test set 3:")
    process(process, "five-card-draw 5s3s4c2h9d 8dKsTc6c2c 4h6s8hJd5d 5c3cQdTd9s AhQhKcQc2d KhJs9c5h9h 8c3d7h7dTs")