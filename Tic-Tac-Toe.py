class Game(object):
    pass

    def Start_The_Game(self):
        input("Enter a character to start the game: ")

    def create_tictactoe_board(self):
        self.row1 = [{} ,{} ,{}] 
        self.row2 = [{} ,{} ,{}] 
        self.row3 = [{} ,{} ,{}] 
    
    def print_out_board(self):
        print("\nTic-Tac-Toe Board\n")
        print(self.row1)
        print(self.row2)
        print(self.row3)

    def X_collect_player_input_x(self):
        x = (input("\nWhere would you like to place an X? \n \n Row 1 = 1 \n Row 2 = 2 \n Row 3 = 3 \n\nInput: "))
        return int(x)
    
    def O_collect_player_input_x(self):
        x = (input("\nWhere would you like to place an O? \n \n Row 1 = 1 \n Row 2 = 2 \n Row 3 = 3 \n\nInput: "))
        return int(x)
    
    def X_collect_player_input_y(self):
        y = (input("\nWhere would you like to place an X? \n \n Column 1 = 1 \n Column 2 = 2 \n Column 3 = 3 \n\nInput: "))
        return int(y)
    
    def O_collect_player_input_y(self):
        y = (input("\nWhere would you like to place an O? \n \n Column 1 = 1 \n Column 2 = 2 \n Column 3 = 3 \n\nInput: "))
        return int(y)
    
    def X_User_Marking_Function(self,x,y):
        if x == 1 and self.row1[y-1] != "O":
            self.row1[y-1] = "X"
            return 0
        elif x == 2 and self.row2[y-1] != "O":
            self.row2[y-1] = "X"
            return 0
        elif x == 3 and self.row3[y-1] != "O":
            self.row3[y-1] = "X"
            return 0
        else:
          print(" \nCannot place an X on an occupied space")
          return 1
    
    def O_User_Marking_Function(self,x,y):
        if x == 1 and self.row1[y-1] != "X":
            self.row1[y-1] = "O"
            return 0
        elif x == 2 and self.row2[y-1] != "X":
            self.row2[y-1] = "O"
            return 0
        elif x == 3 and self.row3[y-1] != "X":
            self.row3[y-1] = "O"
            return 0
        else:
          print(" \nCannot place an O on an occupied space")
          return 1
          
  
    
    def X_Check_If_Game_Ended(self):
      self.column1 = [self.row1[0], self.row2[0], self.row3[0]]
      self.column2 = [self.row1[1], self.row2[1], self.row3[1]]
      self.column3 = [self.row1[2], self.row2[2], self.row3[2]]
      self.diagonal1 = [self.row1[0], self.row2[1], self.row3[2]]
      self.diagonal2 = [self.row1[2], self.row2[1], self.row3[0]]
      if ["X","X","X"] in (self.row1,self.row2, self.row3, self.column1, self.column2, self.column3, self.diagonal1, self.diagonal2):
            game = "Over"
            return game
            
    
    def O_Check_If_Game_Ended(self):
      self.column1 = [self.row1[0], self.row2[0], self.row3[0]]
      self.column2 = [self.row1[1], self.row2[1], self.row3[1]]
      self.column3 = [self.row1[2], self.row2[2], self.row3[2]]
      self.diagonal1 = [self.row1[0], self.row2[1], self.row3[2]]
      self.diagonal2 = [self.row1[2], self.row2[1], self.row3[0]]
      if ["O","O","O"] in (self.row1,self.row2, self.row3, self.column1, self.column2, self.column3, self.diagonal1, self.diagonal2):
            game = "Over"
            return game
            

instance_1 = Game()
instance_1.Start_The_Game()
instance_1.create_tictactoe_board()
instance_1.print_out_board()

w = 0
timer = 1
while w != "Over":
    if timer % 2 == 0:
        x = instance_1.O_collect_player_input_x()
        y = instance_1.O_collect_player_input_y()
        instance_1.O_User_Marking_Function(x, y)
        instance_1.print_out_board()
        instance_1.O_Check_If_Game_Ended()
        w = instance_1.O_Check_If_Game_Ended()
        z = instance_1.O_User_Marking_Function(x,y)
    else:
        x = instance_1.X_collect_player_input_x()
        y = instance_1.X_collect_player_input_y()
        instance_1.X_User_Marking_Function(x, y)
        instance_1.print_out_board()
        instance_1.X_Check_If_Game_Ended()
        w = instance_1.X_Check_If_Game_Ended()
        z = instance_1.X_User_Marking_Function(x,y)
    timer = timer + 1 + z

print("\nGame Over")