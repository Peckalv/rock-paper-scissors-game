human_turn='Rock'
computer_turn='Paper'

if human_turn==computer_turn:
    print('Draw!')
elif human_turn=='Rock' and computer_turn=='Scissors':
    print('human wins!')
elif human_turn=='Paper' and computer_turn=='Rock':
    print('human wins!')
elif human_turn=='Scissors' and computer_turn=='Paper':
    print('human wins!')
else:
    print('computer wins!')
