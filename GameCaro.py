player_name = []


def tic_tac_toe(player1, player2):
    """
    Hàm bắt đầu trò chơi

    """
    player_name.append(player1)
    player_name.append(player2)
    board = [str(i) for i in range(1, 10)]
    welcome_message()
    display_board(board)
    print("#" * 100)
    turn = 0
    rounds = 0  # Sau 9 vòng, nếu isWin vẫn false thì game hòa
    while True:  # Vòng lặp game

        print("It's player " + player_name[turn] + " turn")  # Thông báo người chơi hiện tại

        while True:  # Xác thực dữ liệu đầu vào
            inp = str(input("Enter your choice from 1 to 9: "))
            is_digit_boolean = inp.isdigit()
            if len(inp) > 1 or len(inp) <= 0 or not is_digit_boolean or inp == '0':  # Xử lý dữ liệu sai
                print("Invalid input please enter again!")
                continue
            if board[int(inp) - 1] == 'o' or board[int(inp) - 1] == 'x':
                print("This cell is already chosen! Please pick another cell")  # Xữ lý dữ liệu đã được nhập
                continue
            break

        chess = 'o' if turn == 1 else 'x'  # id Thay đổi kí hiệu dựa vào id người chơi
        board[int(inp) - 1] = chess  # Đặt dấu
        display_board(board)

        if is_win(board):
            print("The winner is player " + player_name[turn])
            return

        rounds += 1  # Tăng số vòng để xác định trạng thái game
        if rounds == 9:
            print("It's a draw!")
            return

        turn = 1 if turn == 0 else 0  # Thay đổi id người chơi


def display_board(board):
    """
    Hàm in bảng caro

    """
    # Xuất bảng caro
    print("{} | {} | {} ".format(board[0], board[1], board[2]))
    print("---------")
    print("{} | {} | {} ".format(board[3], board[4], board[5]))
    print("---------")
    print("{} | {} | {} ".format(board[6], board[7], board[8]))
    print("---------")


def is_win(board):
    """
    Hàm kiểm tra điều kiện thắng

    """
    # Xét hàng dọc
    for i in range(3):
        if board[0 + i] == board[3 + i] == board[6 + i]:
            return True

    # Xét hàng ngang
    if board[0] == board[1] == board[2]:
        return True
    elif board[3] == board[4] == board[5]:
        return True
    elif board[6] == board[7] == board[8]:
        return True

    # Xét hàng chéo
    if board[0] == board[4] == board[8]:
        return True
    elif board[2] == board[4] == board[6]:
        return True

    return False


def welcome_message():
    """
    Hàm hướng dẫn chơi game

    """
    # Print welcome messages
    print("Welcome to TICTACTOE")
    print("There are two players, you have to enter the number in the board in order to choose that board")
    print("Player 1 will be 'x' and player 2 will be 'o'")
    print('The winner will be the first one to have chosen cells that are align horizontally, vertically or diagonally')
    print("#" * 100)

tic_tac_toe('Human','PC')