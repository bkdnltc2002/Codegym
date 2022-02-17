def game21():
    import random as rd
    while True:
        current_number = 0
        turn = rd.randint(0,1)
        if turn==0:
            current_player = 'human'
        elif turn==1:
            current_player='computer'
        while int(current_number) < 21:
            print('Điểm hiện tại: '+str(current_number))
            if current_player =='human':
                while True:
                    player_choice = int(input('Nhập điểm thêm: '))
                    if player_choice > 0 and player_choice <4:
                        break
                current_number += player_choice
                if current_number >=21:
                    print(str(current_number) + ' You lost')
                else:
                    current_player = 'computer'
            else:
                current_player ='computer'
                computer_choice = rd.randint(1,3)
                print('Điểm máy thêm: '+str(computer_choice))
                current_number += computer_choice
                if current_number >=21:
                    print(str(current_number)+' You win')
                else:
                    current_player='human'
        play_again = str(input('Play again?'))
        if play_again[0] == 'y':
            continue
        else:
            break
if __name__ == '__main__':
    game21()