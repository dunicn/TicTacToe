class TicTacToe:

    def __init__(self):
        self.user_input = "         "
        self.count = 0

    def replace_character_x(self, x, y):
        char_pos = self.coord_to_field(x, y)
        new_string = "X"
        self.user_input = self.user_input[:char_pos] + new_string + self.user_input[char_pos + 1:]

    def replace_character_o(self, x, y):
        char_pos = self.coord_to_field(x, y)
        new_string = "O"
        self.user_input = self.user_input[:char_pos] + new_string + self.user_input[char_pos + 1:]

    def coord_to_field(self, x, y):
        if x == 1 and y == 1:
            return 6
        elif x == 2 and y == 1:
            return 7
        elif x == 3 and y == 1:
            return 8
        elif x == 1 and y == 2:
            return 3
        elif x == 1 and y == 3:
            return 0
        elif x == 2 and y == 2:
            return 4
        elif x == 3 and y == 2:
            return 5
        elif x == 2 and y == 3:
            return 1
        elif x == 3 and y == 3:
            return 2

    def is_input_valid(self, x, y):
        x = int(x)
        y = int(y)

        if type(x) is not int and type(y) is not int:
            print("You should enter numbers!")
            return False
        elif 1 > x or x > 3 or 1 > y or y > 3:
            print("Coordinates should be from 1 to 3!")
            return False
        elif self.user_input[self.coord_to_field(x, y)] == "X" or self.user_input[self.coord_to_field(x, y)] == "O":
            print("This cell is occupied! Choose another one!")
            return False
        else:
            return True

    def user_move_x(self):
        self.print_field()

        print("Enter the coordinates: ")
        x, y = input().split()
        while not self.is_input_valid(x, y):
            print("Enter the coordinates: ")
            x, y = input().split()
        x = int(x)
        y = int(y)

        self.replace_character_x(x, y)
        self.print_field()

    def user_move_o(self):
        self.print_field()

        print("Enter the coordinates: ")
        x, y = input().split()
        while not self.is_input_valid(x, y):
            print("Enter the coordinates: ")
            x, y = input().split()
        x = int(x)
        y = int(y)

        self.replace_character_o(x, y)
        self.print_field()

    def print_field(self):

        print("---------")
        print("| {} {} {} |".format(self.user_input[0], self.user_input[1], self.user_input[2]))
        print("| {} {} {} |".format(self.user_input[3], self.user_input[4], self.user_input[5]))
        print("| {} {} {} |".format(self.user_input[6], self.user_input[7], self.user_input[8]))
        print("---------")

    def win_check(self):
        win_poss = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [6, 4, 2]]

        for win_line in win_poss:
            if self.user_input[win_line[0]] == self.user_input[win_line[1]] == \
                    self.user_input[win_line[2]] == "X":
                print("X wins")
                return "X wins"
            elif self.user_input[win_line[0]] == self.user_input[win_line[1]] == \
                    self.user_input[win_line[2]] == "O":
                print("O wins")
                return "O wins"
        if self.count == 9:
            print("Draw")
            return "Draw"

        self.count += 1

        return "Game not finished"

    def final_check(self):
        count = 1
        while self.win_check() == "Game not finished":
            if count % 2 != 0:
                self.user_move_x()
                count += 1
            else:
                self.user_move_o()
                count += 1


game = TicTacToe()

game.final_check()
