from collections import Counter
print()

## Part 2 Example
# camel_cards = [ "32T3K 765",
#                 "T55J5 684",
#                 "KK677 28",
#                 "KTJJT 220",
#                 "QQQJA 483"]

with open('Input7.txt', 'r') as file:
    camel_cards = file.read().splitlines()

camel_cards = [x.split() for x in camel_cards]

my_dict = { "J" : "M",
            "A" : "A",
            "K" : "B",
            "Q" : "C",
            "T" : "D",
            "9" : "E",
            "8" : "F",
            "7" : "G",
            "6" : "H",
            "5" : "I",
            "4" : "J",
            "3" : "K",
            "2" : "L",
            }

hand_type_dict = {'five_of_a_kind'  : [],
                  'four_of_a_kind'  : [],
                  'full_house'      : [],
                  'three_of_a_kind' : [],
                  'two_pair'        : [],
                  'one_pair'        : [],
                  'high_card'       : []
                  }

rank = len(camel_cards)

for hand, bet in camel_cards:
    
    for key, value in my_dict.items():
        hand = hand.replace(key, value)

    # print(f"Hand: {hand} || Bet: {bet} || Count: {Counter(hand)}")

    value_counter = Counter(hand)
    hand_counts = value_counter.values()

    if 'M' in hand:
        if (5 in hand_counts) or (4 in hand_counts) or ((3 in hand_counts) and (2 in hand_counts)):
            hand_type_dict['five_of_a_kind'].append((hand, bet))
        elif (3 in hand_counts) and (2 not in hand_counts):
            hand_type_dict['four_of_a_kind'].append((hand, bet))
        elif Counter(hand_counts)[2] == 2:
            if value_counter['M']==2:
                hand_type_dict['four_of_a_kind'].append((hand, bet))
            elif value_counter['M']==1:
                hand_type_dict['full_house'].append((hand, bet))
        elif Counter(hand_counts)[2] == 1:
            hand_type_dict['three_of_a_kind'].append((hand, bet))
        else:
            hand_type_dict['one_pair'].append((hand, bet))

    else:
        if 5 in hand_counts:
            hand_type_dict['five_of_a_kind'].append((hand, bet))
        elif 4 in hand_counts:
            hand_type_dict['four_of_a_kind'].append((hand, bet))
        elif (3 in hand_counts) and (2 in hand_counts):
            hand_type_dict['full_house'].append((hand, bet))
        elif (3 in hand_counts) and (2 not in hand_counts):
            hand_type_dict['three_of_a_kind'].append((hand, bet))
        elif Counter(hand_counts)[2] == 2:
            hand_type_dict['two_pair'].append((hand, bet))
        elif Counter(hand_counts)[2] == 1:
            hand_type_dict['one_pair'].append((hand, bet))
        else:
            hand_type_dict['high_card'].append((hand, bet))


for k, v in hand_type_dict.items():
    v.sort(key=lambda a: a[0])


total_winnings = 0
for h_type in ['five_of_a_kind', 'four_of_a_kind', 'full_house', 'three_of_a_kind', 'two_pair', 'one_pair', 'high_card']:
    for v in hand_type_dict[h_type]:
        
        total_winnings += int(v[1]) * rank
        rank -= 1

print(f"Answer: {total_winnings}")
print()





    