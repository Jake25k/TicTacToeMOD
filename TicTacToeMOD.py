from random import *
from time import *
def main():
  
  #Intro
  intro_slur= randrange(1,4)
  if intro_slur == 1:
    showInformation("Welcome human, to the greatest showdown. I will play you in a game of Tic-Tac-Toe. May the best man or machine win.")
  if intro_slur == 2:
    showInformation("For once and for all I will prove machine is greater than man. Let us do battle in Tic-Tac-Toe!")
  if intro_slur == 3:
    showInformation("What is this? A competitor? You stand no chance in Tic-Tac-Toe versus me, human!")
    
  #Playing field
  pic=makeEmptyPicture(400, 400)
  show(pic)
  addRectFilled(pic, 125, 125, 10, 250, black)
  addRectFilled(pic, 250, 125, 10, 250, black)
  addRectFilled(pic, 50, 200, 270, 10, black)
  addRectFilled(pic, 50, 300, 270, 10, black)
  addText(pic, 90, 190, "0", black)  #slot 0
  addText(pic, 180, 190, "1", black)  #slot 1
  addText(pic, 270, 190, "2", black)  #slot 2
  addText(pic, 90, 260, "3", black)  #slot 3
  addText(pic, 180, 260, "4", black)  #slot 4
  addText(pic, 270, 260, "5", black)  #slot 5
  addText(pic, 90, 330, "6", black)  #slot 6
  addText(pic, 180, 330, "7", black)  #slot 7
  addText(pic, 270, 330, "8", black)  #slot 8
  
  #Game set up
  showInformation("The rules are simple: input a number between 0-8 to indicate which square you would like to occupy with your piece.")
  ans = requestString("Would you like to go first? (yes/no)")
  if ans == "yes" or ans == "Yes" or ans == "y":
    showInformation("Okay, good luck human.")
  if ans == "no" or ans == "No" or ans == "n":
    showInformation("HA! You might as well hand me the victory, human.")
  if ans != "yes" and ans != "no" and ans != "Yes" and ans != "No" and ans != "y" and ans != "n":
    showInformation("Okay, I am just going to go first...")
    ans = "no"
    
  addRectFilled(pic, 0, 0, 400, 400, white)
  addRectFilled(pic, 125, 125, 10, 250, black)
  addRectFilled(pic, 250, 125, 10, 250, black)
  addRectFilled(pic, 50, 200, 270, 10, black)
  addRectFilled(pic, 50, 300, 270, 10, black)
  repaint(pic)
  
  winningpoint=0
  activate_check=0
  moves_made = []
  moves_made_human = []
  moves_made_comp = []
  
  #Gameplay (If user wants to go first)
  while winningpoint==0:
    if ans == "yes" or ans == "Yes" or ans == "y":
      move= requestInteger("Please make your move:")
      while move > 8 or move < 0:
        move = requestInteger("That is not a proper move! Try again:")
      while activate_check > 1 and move in moves_made_human:
        move = requestInteger("You already made that move! Try again:")
      while activate_check > 1 and move in moves_made_comp:
        move = requestInteger("I already made that move! Try again:")
      
      moves_made.append(move)
      moves_made_human.append(move)
      
      if move == 0:
        addText(pic, 90, 190, "X", black)
        repaint(pic)
      if move == 1:
        addText(pic, 180, 190, "X", black)
        repaint(pic)
      if move == 2:
        addText(pic, 270, 190, "X", black)
        repaint(pic)
      if move == 3:
        addText(pic, 90, 260, "X", black)
        repaint(pic)
      if move == 4:
        addText(pic, 180, 260, "X", black)
        repaint(pic)
      if move == 5:
        addText(pic, 270, 260, "X", black)
        repaint(pic)
      if move == 6:
        addText(pic, 90, 330, "X", black)
        repaint(pic)
      if move == 7:
        addText(pic, 180, 330, "X", black)
        repaint(pic)
      if move == 8:
        addText(pic, 270, 330, "X", black)
        repaint(pic)
      
      #Winning criteria human
      if 0 in moves_made_human and 1 in moves_made_human and 2 in moves_made_human:
        showInformation("You win, human! How could this be?")
        winningpoint = 1
        break
      if 0 in moves_made_human and 3 in moves_made_human and 6 in moves_made_human:
        showInformation("You win, human! How could this be?")
        winningpoint = 1
        break
      if 0 in moves_made_human and 4 in moves_made_human and 8 in moves_made_human:
        showInformation("You win, human! How could this be?")
        winningpoint = 1
        break
      if 2 in moves_made_human and 4 in moves_made_human and 6 in moves_made_human:
        showInformation("You win, human! How could this be?")
        winningpoint = 1
        break
      if 2 in moves_made_human and 5 in moves_made_human and 8 in moves_made_human:
        showInformation("You win, human! How could this be?")
        winningpoint = 1
        break
      if 3 in moves_made_human and 4 in moves_made_human and 5 in moves_made_human:
        showInformation("You win, human! How could this be?")
        winningpoint = 1
        break
      if 6 in moves_made_human and 7 in moves_made_human and 8 in moves_made_human:
        showInformation("You win, human! How could this be?")
        winningpoint = 1
        break
      elif 1 in moves_made_human and 4 in moves_made_human and 7 in moves_made_human:
        showInformation("You win, human! How could this be?")
        winningpoint = 1
        break
      if 0 in moves_made and 1 in moves_made and 2 in moves_made and 3 in moves_made and 4 in moves_made and 5 in moves_made and 6 in moves_made and 7 in moves_made and 8 in moves_made:
        break
      
    
      #computer move
    
      showInformation("Interesting move. Let me think...")
      sleep(.9)
      comp_1 = randrange(0,9)
      while comp_1 in moves_made:
        comp_1 = randrange(0,9)
      if comp_1 == 0:
        addText(pic, 90, 190, "O", black)
        repaint(pic)
      if comp_1 == 1:
        addText(pic, 180, 190, "O", black)
        repaint(pic)
      if comp_1 == 2:
        addText(pic, 270, 190, "O", black)
        repaint(pic)
      if comp_1 == 3:
        addText(pic, 90, 260, "O", black)
        repaint(pic)
      if comp_1 == 4:
        addText(pic, 180, 260, "O", black)
        repaint(pic)
      if comp_1 == 5:
        addText(pic, 270, 260, "O", black)
        repaint(pic)
      if comp_1 == 6:
        addText(pic, 90, 330, "O", black)
        repaint(pic)
      if comp_1 == 7:
        addText(pic, 180, 330, "O", black)
        repaint(pic)
      if comp_1 == 8:
        addText(pic, 270, 330, "O", black)
        repaint(pic)
      showInformation("A-ha! A far superior move, human.")
      moves_made.append(comp_1)
      moves_made_comp.append(comp_1)
    
   
      #Winning criteria comp
      if 0 in moves_made_comp and 1 in moves_made_comp and 2 in moves_made_comp:
        showInformation("I am victorious! I am not suprised.")
        winningpoint = 1
        break
      if 0 in moves_made_comp and 3 in moves_made_comp and 6 in moves_made_comp:
        showInformation("I am victorious! I am not suprised.")
        winningpoint = 1
        break
      if 0 in moves_made_comp and 4 in moves_made_comp and 8 in moves_made_comp:
        showInformation("I am victorious! I am not suprised.")
        winningpoint = 1
        break
      if 2 in moves_made_comp and 4 in moves_made_comp and 6 in moves_made_comp:
        showInformation("I am victorious! I am not suprised.")
        winningpoint = 1
        break
      if 2 in moves_made_comp and 5 in moves_made_comp and 8 in moves_made_comp:
        showInformation("I am victorious! I am not suprised.")
        winningpoint = 1
        break
      if 3 in moves_made_comp and 4 in moves_made_comp and 5 in moves_made_comp:
        showInformation("I am victorious! I am not suprised.")
        winningpoint = 1
        break
      if 6 in moves_made_comp and 7 in moves_made_comp and 8 in moves_made_comp:
        showInformation("I am victorious! I am not suprised.")
        winningpoint = 1
        break
      if 1 in moves_made_comp and 4 in moves_made_comp and 7 in moves_made_comp:
        showInformation("I am victorious! I am not suprised.")
        winningpoint = 1
        break
      if 0 in moves_made and 1 in moves_made and 2 in moves_made and 3 in moves_made and 4 in moves_made and 5 in moves_made and 6 in moves_made and 7 in moves_made and 8 in moves_made:
        break
      activate_check= 500
    
    #If user does not want to go first
    if ans == "no" or ans == "No" or ans == "n":
      comp_1 = randrange(0,9)
      if activate_check == 500:
        showInformation("Interesting move. Let me think...")
        sleep(.9)
      while comp_1 in moves_made:
        comp_1 = randrange(0,9)
      if comp_1 == 0:
        addText(pic, 90, 190, "O", black)
        repaint(pic)
      if comp_1 == 1:
        addText(pic, 180, 190, "O", black)
        repaint(pic)
      if comp_1 == 2:
        addText(pic, 270, 190, "O", black)
        repaint(pic)
      if comp_1 == 3:
        addText(pic, 90, 260, "O", black)
        repaint(pic)
      if comp_1 == 4:
        addText(pic, 180, 260, "O", black)
        repaint(pic)
      if comp_1 == 5:
        addText(pic, 270, 260, "O", black)
        repaint(pic)
      if comp_1 == 6:
        addText(pic, 90, 330, "O", black)
        repaint(pic)
      if comp_1 == 7:
        addText(pic, 180, 330, "O", black)
        repaint(pic)
      if comp_1 == 8:
        addText(pic, 270, 330, "O", black)
        repaint(pic)
      if activate_check == 0:
        showInformation("A perfect first choice for me!")
      if activate_check == 500:
        showInformation("A-ha! A far superior move, human.")
      moves_made.append(comp_1)
      moves_made_comp.append(comp_1)
      
   
      #Winning criteria comp
      if 0 in moves_made_comp and 1 in moves_made_comp and 2 in moves_made_comp:
        showInformation("I am victorious! I am not suprised.")
        winningpoint = 1
        break
      if 0 in moves_made_comp and 3 in moves_made_comp and 6 in moves_made_comp:
        showInformation("I am victorious! I am not suprised.")
        winningpoint = 1
        break
      if 0 in moves_made_comp and 4 in moves_made_comp and 8 in moves_made_comp:
        showInformation("I am victorious! I am not suprised.")
        winningpoint = 1
        break
      if 2 in moves_made_comp and 4 in moves_made_comp and 6 in moves_made_comp:
        showInformation("I am victorious! I am not suprised.")
        winningpoint = 1
        break
      if 2 in moves_made_comp and 5 in moves_made_comp and 8 in moves_made_comp:
        showInformation("I am victorious! I am not suprised.")
        winningpoint = 1
        break
      if 3 in moves_made_comp and 4 in moves_made_comp and 5 in moves_made_comp:
        showInformation("I am victorious! I am not suprised.")
        winningpoint = 1
        break
      if 6 in moves_made_comp and 7 in moves_made_comp and 8 in moves_made_comp:
        showInformation("I am victorious! I am not suprised.")
        winningpoint = 1
        break
      if 1 in moves_made_comp and 4 in moves_made_comp and 7 in moves_made_comp:
        showInformation("I am victorious! I am not suprised.")
        winningpoint = 1
        break
      if 0 in moves_made and 1 in moves_made and 2 in moves_made and 3 in moves_made and 4 in moves_made and 5 in moves_made and 6 in moves_made and 7 in moves_made and 8 in moves_made:
        break
      #Human move
      move= requestInteger("Please make your move:")
      while move > 8 or move < 0:
        move = requestInteger("That is not a proper move! Try again:")
      while activate_check > 1 and move in moves_made_human:
        move = requestInteger("You already made that move! Try again:")
      while move in moves_made_comp:
        move = requestInteger("I already made that move! Try again:")
      
      moves_made.append(move)
      moves_made_human.append(move)
      
      if move == 0:
        addText(pic, 90, 190, "X", black)
        repaint(pic)
      if move == 1:
        addText(pic, 180, 190, "X", black)
        repaint(pic)
      if move == 2:
        addText(pic, 270, 190, "X", black)
        repaint(pic)
      if move == 3:
        addText(pic, 90, 260, "X", black)
        repaint(pic)
      if move == 4:
        addText(pic, 180, 260, "X", black)
        repaint(pic)
      if move == 5:
        addText(pic, 270, 260, "X", black)
        repaint(pic)
      if move == 6:
        addText(pic, 90, 330, "X", black)
        repaint(pic)
      if move == 7:
        addText(pic, 180, 330, "X", black)
        repaint(pic)
      if move == 8:
        addText(pic, 270, 330, "X", black)
        repaint(pic)
      
      #Winning criteria human
      if 0 in moves_made_human and 1 in moves_made_human and 2 in moves_made_human:
        showInformation("You win, human! How could this be?")
        winningpoint = 1
        break
      if 0 in moves_made_human and 3 in moves_made_human and 6 in moves_made_human:
        showInformation("You win, human! How could this be?")
        winningpoint = 1
        break
      if 0 in moves_made_human and 4 in moves_made_human and 8 in moves_made_human:
        showInformation("You win, human! How could this be?")
        winningpoint = 1
        break
      if 2 in moves_made_human and 4 in moves_made_human and 6 in moves_made_human:
        showInformation("You win, human! How could this be?")
        winningpoint = 1
        break
      if 2 in moves_made_human and 5 in moves_made_human and 8 in moves_made_human:
        showInformation("You win, human! How could this be?")
        winningpoint = 1
        break
      if 3 in moves_made_human and 4 in moves_made_human and 5 in moves_made_human:
        showInformation("You win, human! How could this be?")
        winningpoint = 1
        break
      if 6 in moves_made_human and 7 in moves_made_human and 8 in moves_made_human:
        showInformation("You win, human! How could this be?")
        winningpoint = 1
        break
      if 1 in moves_made_human and 4 in moves_made_human and 7 in moves_made_human:
        showInformation("You win, human! How could this be?")
        winningpoint = 1
        break
      
      activate_check = 500
      if 0 in moves_made and 1 in moves_made and 2 in moves_made and 3 in moves_made and 4 in moves_made and 5 in moves_made and 6 in moves_made and 7 in moves_made and 8 in moves_made:
        break
  if winningpoint == 0:
    showInformation("A tie! How unlikely...")
       