#card_text="A-1 A-5 A-10 B-2 A-10 A-7 A-3"
card_text=input("Enter the space seperated card string")
team_a=11
team_b=11
card_lists=card_text.split(" ")

print(card_lists)

for card_list in card_lists:
    print(card_list[0])
    if card_list[0]=='A':
        team_a=team_a-1
    elif card_list[0]=='B':
        team_b=team_b-1

print("Team A - ",team_a," ; Team B - ",team_b)
if(team_a<7 or team_b<7):
    print("Game was terminated")