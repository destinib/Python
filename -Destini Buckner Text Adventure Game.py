# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 08:34:12 2018

@author: Destini B
"""

"""
        
    |   \/   |     /   \     |           ||  |  |  | |   _  \      /   \     |  |     |  |     
    |  \  /  |    /  ^  \    `---|  |----`|  |__|  | |  |_)  |    /  ^  \    |  |     |  |     
    |  |\/|  |   /  /_\  \       |  |     |   __   | |   _  <    /  /_\  \   |  |     |  |     
    |  |  |  |  /  _____  \      |  |     |  |  |  | |  |_)  |  /  _____  \  |  `----.|  `----.
    |__|  |__| /__/     \__\     |__|     |__|  |__| |______/  /__/     \__\ |_______||_______|
                                                                                               



DocString

A  Introduction:
    Mathball is an educational game to help students apply and enhance their
    algebraic skills to assist their team in winning the baseball championship
    game.The game consists of four stages, which challenge their knowledge and 
    progressively gets harder as the student advances to the next stage. The 
    student will need to bring their mathematical knowledge and skills to win 
    the game. 
    
    Stage 1: Batting  - Simplyfing Equations
    Stage 2: 1st Base - Solving Inequalities
    Stage 3: 2nd Base - Solving Word Problems
    Stage 4: 3rd Base - Solving Systems of Equations
    
B  Known Bugs and/or Errors:
    Global names and invalid loop

      
"""
from sys import exit
import random
import math

##############################################################################
#Start of the Game:
#The start function is the introduction to the game and asks for global inputs
##############################################################################

def start():
    global name_1
    global name_2
    global runs
    
    print(f"""
            \   \  /  \  /   / |   ____||  |      /      | /  __  \  |   \/   | |   ____|
             \   \/    \/   /  |  |__   |  |     |  ,----'|  |  |  | |  \  /  | |  |__   
              \            /   |   __|  |  |     |  |     |  |  |  | |  |\/|  | |   __|  
               \    /\    /    |  |____ |  `----.|  `----.|  `--'  | |  |  |  | |  |____ 
                \__/  \__/     |_______||_______| \______| \______/  |__|  |__| |_______|
                                                                                         
        """)
    
    print(f"""
          Are you ready to play some baseball??? Help your team win the 
          championship game by using your mathematical skills to score the 
          winning run. The game consists of four stages, which get harder as 
          you complete each stage. In each stage you will be asked a question.
          Your goal is to answer the questions correctly to advance the runner 
          around the bases to score the winning run. In a baseball game once 
          you have 3 outs it ends the inning. Therefore, you will have three 
          outs as well in this game. You will face different circumstances at 
          different stages, so be careful when answering. 
          Good Luck! PLAY BALL!!!
          """)

    input("<Please press enter, input your name, and press enter to continue>")
    name_1 = input("> ")
    name_1 = name_1.upper()
    
    while name_1 == (""):
        print("Invalid Response... Please input your name to continue>")
        name_1 = input("> ")
        name_1 = name_1.upper()
         
    input("<Please press enter, input your team's name, and press enter to continue>")
    name_2 = input("> ")
    name_2 = name_2.upper()
    
    while name_2 == (""):
         print("Invalid Response... Please input your team's name to continue>")
         name_2 = input("> ")
         name_2 = name_2.upper() 
    
    batting()
       

##############################################################################
#Stage 1: Batting
#The batting function is the first stage in the game
#In this function the while loop is limited to three chances to answer correctly before the player loses the game
##############################################################################
    
def batting():
       
        runs = random.randint(2,11)
        
        print(f"""
              {name_1}: The score is {runs} to {runs - 2}. The {name_2} are
              down by 2 runs with the bases loaded. You're up at the plate
              with no outs. Like at any at bat, you have three strikes before 
              you strike out. If you strike out you lose the game, 
              so answer wisely!
              BATTER UP!!!
             """)
       
        strike_list = ["Use the distributive property to simplify the answer for the expression \n 4(x + 5)",
                       "Use the order of operations (PEMDAS) to solve the expression\n 5 + 2(7 -3)^2 - 3 * 4", 
                       "Simplify the expression \n 9c-2(3c + 4)"]
        
        strikes = 3
        
        while strikes > 0:
            s = random.choice(strike_list)
            input("<Press enter for your question>\n")
            print(s)
            print(" ")
            
            if s == strike_list[0]:
                answer_1 = input(f"""Please choose the correct answer from the following choices\n
                                  A. x
                                  B. 4x + 20
                                  C. 20x
                                  D. 4x + 5 \n
                                  Answer:
                                  """)
                answer_1 = answer_1.lower()
                
                if "4x + 20" in answer_1 or "B" in answer_1 or "b" in answer_1:
                    print("""WHAT A HIT! Advance to first base!\n""")
                    input("<Press enter to continue>\n")
                    first_base()
                    break
                
                else:
                    print(f"""STRIKE!!! That's incorrect! Be careful not to strike out!""")
                    
                    strikes -=1
                
            elif s == strike_list[1]:
                 print("Please choose the correct answer from the following choices \n")
                 answer_2 = input(f"""
                                  A. 20 
                                  B. 132
                                  C. 57
                                  D. 25 \n
                                  Answer:
                                  """)
                 answer_2 = answer_2.lower()
                 
                 if "25" in answer_2 or "D" in answer_2 or "d" in answer_2:
                     print("""Awesome! Take your base!""")
                     input("<Press enter to continue > \n")
                     first_base()
                     break
                 
                 else:
                    print(f"""STRIKE!!! That's incorrect! Be careful not to strike out!""")
                    
                    strikes -=1
                    
            elif s  == strike_list[2]:
                    answer_3 =input(f"""Please choose the correct answer from the following choices\n
                                  A. 3c - 8 
                                  B. 3c + 8
                                  C. 15c + 6 
                                  D. 15c - 6 \n
                                  Answer:
                                  """)
                    answer_3 = answer_3.lower()
                    
                    if "3c - 8" in answer_3 or "A" in answer_3 or "a" in answer_3:
                        print("""You might be the next Babe Ruth or Hank Aaron! \n Take your base!""")
                        input("<Press enter to continue> \n")
                        first_base()
                        break
                    
                    else: 
                      print(f"""STRIKE!!! That's incorrect! Be careful not to strike out!""")
                     
                    strikes -=1
            
        else: 
            strikes == 0
            fail_1()

##############################################################################            
#Stage 2: First Base
#The first base function is the second stage in the game
#In this function the while loop is limited to three chances to answer correctly before the player loses the game            
##############################################################################

def first_base():
        
        print(f"""
              {name_1}, you are doing great! You've made it to first base and 
              scored a run for the {name_2}! There are no outs, so 
              you have three chances to advance to second base. If you don't 
              advance to second base, then you lose the game.
              Keep up the good work!
             """)
       
        base_one_list = ["""Solve the inequality \n x + 5 <= 20""", 
                      """Solve the inequality \n -3y < 27""",
                      """Solve the inequality \n  16 > 4y > 8"""]
        first = 3
        
        while first > 0:
            fb = random.choice(base_one_list)
            input("<Press enter for your question>\n")
            print(fb)
            print(" ")
            
            if fb == base_one_list[0]:
                answer_4 = input(f"""Please choose the correct answer from the following choices\n
                                  A. x => 25 
                                  B. x => 15
                                  C. x <= 25
                                  D. x <= 15 \n
                                  Answer:
                                  """)
                answer_4 = answer_4.lower()
                
                if "x <= 15" in answer_4 or "D" in answer_4 or "d" in answer_4:
                    print("""WHAT A STEAL! You're on second base!\n""")
                    input("<Press enter to continue>\n")
                    second_base()
                    break
                
                else:
                    print("""YOU'RE OUT!!! That's incorrect! Don't lose the game for your team!""")
                    
                    first -=1
 
                
            elif fb == base_one_list[1]:
                 answer_5 = input(f"""Please choose the correct answer from the following choices\n
                                  A. y > -9
                                  B. y <  9
                                  C. y >  9
                                  D. y < -9 \n
                                  Answer:
                                 """)
                 answer_5 = answer_5.lower()
                 
                 if "y > -9" in answer_5 or "A" in answer_5 or "a" in answer_5:
                     print("""You're as fast as lightning!The catcher didn't stand a chance throwing you out at second base!""")
                     input("<Press enter to continue > \n")
                     second_base()
                     break
                 
                 else:
                    print(""" That's an incorrect answer! Wow they really hosed you down!!! You're Out!""")
                    
                    first -=1
                  
            elif fb  == base_one_list[2]:
                    answer_6 =input(f"""Please choose the correct answer from the following choices\n
                                  A. 64 > y > 48
                                  B. 64 < y < 48
                                  C. 4 > y > 2
                                  D. 4 < y < 2 \n
                                  Answer:
                                  """)
                    answer_6 = answer_6.lower()
                    
                    if "4 > y > 2" in answer_6 or "C" in answer_6 or "c" in answer_6:
                        print(f"""Did you see the lead you had? You're a pro! Second base is all yours!""")
                        input("<Press enter to continue> \n")
                        second_base()
                        break
                    
                    else: 
                      print("""Incorrect answer! Oh no the pitcher picked you off! You're out!""")
                     
                    first -=1
            
        else:
            first == 0
            fail_2()
                
##############################################################################                
#Stage 3: Second Base
#The second base function is the third stage in the game
#In this function the while loop is limited to two chances to answer correctly before the player loses the game
##############################################################################    

def second_base():
        print(f""" 
             So you've made it to second base! You're AMAZING! There is one out 
             because your teammate was thrown out by bunting the ball 
             to advance you to second base. You're halfway to home plate, 
             so don't get out now. 
             """)
        
        base_two_list = ["""Ben has to drive to a meeting in San Francisco. It takes him 30 minutes to drive from Oakland to San Francicso. He is driving at 70 miles per hour. What is the total distance of Ben's trip?""",
                         """Stacy brought a pair of running pants for $15. She also  purchased a pair of running shoes that were 3 times the price of the running pants. How much were the running shoes?""", 
                         """The sum of two consecutive numbers is 49. If the equation is: x + x+1 = 49, then what are the two numbers?"""]
        second = 2
      
        while second > 0:
            sb = random.choice(base_two_list)
            input("<Press enter for your question>\n")
            print(sb)
            print(" ")
            
            if sb == base_two_list[0]:
                print("What is the total distance of Ben's Trip? \n Hint: Use the distance equation (d=r*t) \n Don't forget to convert the time")
                answer_7 = input (f"""Please choose the correct answer from the following choices\n
                                  A. 210 miles
                                  B. 35 miles
                                  C. 2100 miles
                                  D. 15 miles \n
                                  Answer:
                                  """)
                answer_7 = answer_7.lower()

                
                if "35" in answer_7 or " B" in answer_7 or "35 miles" in answer_7 or "b" in answer_7:
                    print(""" OMG you just broke up that double play! You Rock! Third base is yours!\n""")
                    input("<Press enter to continue>\n")
                    third_base()
                    break
                
                else:
                    print("""Incorrect Answer! It was close play, but unfortunately you're out!""")
                    second -=1

                
            elif sb == base_two_list[1]:
                 print("Hint: Use the equation 3x = y, where x = running pants and y = running shoes")
                 answer_8 = input(f"""Please choose the correct answer from the following choices\n
                                  A. 5 dollars
                                  B. 15 dollars
                                  C. 45 dollars
                                  D. 30 dollars \n
                                  Answer:
                                  """)
                 answer_8 = answer_8.lower()
                 
                 if "45" in answer_8 or "C" in answer_8 or "c" in answer_8: 
                        print(f"""Awesome steal! Take your base! \n""")
                        input("<Press enter to continue> \n")
                        third_base()
                        break
                 
                 else:
                    print("""Incorrect answer! It was very close, but the third basement got you with that tag! You're out!""")
                    second -=1
                    
            elif sb == base_two_list[2]:
                    print("Solve for x in the equation and pick the two consecutive numbers...\n")
                    answer_9 = input(f"""Please choose the correct answer from the following choices\n
                                  A. 24 and 25
                                  B. 25 and 26
                                  C. 46 and 47
                                  D. Cannot be solved \n
                                  Answer:
                                  """)
                    answer_9 = answer_9.lower()
                    
                    if "24 and 25" in answer_9 or "A" in answer_9 or "a" in answer_9: 
                        print(f"""Wow the short stop really bobbled the ball! That's great for the {name_2}!\n Take your base""")
                        input("<Press enter to continue> \n")
                        third_base()
                        break
                    
                    else: 
                      print("""Incorrect answer! You were soooooo close, but YOU'RE OUT!!!""")
                      second -=1
                    
                
        else:
            second == 0
            fail_2()
    
##############################################################################                
#Stage 4: Third Base
#The third base function is the fourth stage in the game
#In this function the while loop is limited to one chance to answer correctly before the player loses the game
##############################################################################

def third_base():
        print(f""" 
             You're in the last stretch. A double play was turned as you 
             advanced to third base; therefore, there are two outs. However, 
             you are one base away from winning the championship game!
             Don't make a silly mistake and lose the game, so answer wisely!
             """)
        
        base_three_list = ["""Solve this system of equations for x and y \n 2x + y = 5 and y = x + 8""",
                      """Solve this system of equations for x and y \n 3x + y = 9 and 2x - y = -4""", 
                      """Solve this system of equations for x and y \n 3y + 2x = 6 and 5y - 2x = 10"""]
        third = 1
        
        while third > 0:
            tb = random.choice(base_three_list)
            input("<Press enter for your question>\n")
            print(tb)
            print(" ")
            
            if tb == str(base_three_list[0]):
                print("What are the values for x and y?\n")
                answer_10 = input(f"""Please choose the correct answer from the following choices (Answers provided as coordinate format)\n
                                  A. (21,13)
                                  B. (13,21)
                                  C. (-1, 7) 
                                  D. (7 ,-1) \n
                                  Answer:
                                  """)
                answer_10 = answer_10.lower()
                
                if "(-1, 7)" in answer_10 or "C" in answer_10 or "c" in answer_10:
                    print("""OH BABY! You did it! We won! \n""")
                    input("<Press enter to continue>\n")
                    home_plate()
                    break
                
                else:
                    print("""That's incorrect! Awww man we just lost the game \n """)
                    third -=1
                
            elif tb == str(base_three_list[1]):
                 print("What are the values for x and y? \n")
                 answer_11 = input(f"""Please choose the correct answer from the following choices (Answers provided as coordinate format)\n
                                  A. (1 ,6)
                                  B. (6 ,1)
                                  C. (-1,2) 
                                  D. (2,-1) \n
                                  Answer:
                                  """) 
                 answer_11 = answer_11.lower()
                 
                 if "(1,6)" in answer_11 or "A" in answer_11 or "a" in answer_11:
                     print("""What a slide into home plate! You just won the game for us!!!\n""")
                     input("<Press enter to continue > \n")
                     home_plate()
                     break
                 
                 else:
                    print(""" Incorrect Answer! YOU'REEEEEEEEE OUT OF HERE!""")
                    third -=1
                    
            elif tb == str(base_three_list[2]):
                    print("What are the values for x and y? \n Hint: Use the method of elimination to solve the problem \n")
                    answer_12 = input(f"""Please choose the correct answer from the following choices (Answers provided as coordinate format)\n
                                  A. (6 ,-2)
                                  B. (-2, 6)
                                  C. (2 , 0) 
                                  D. (0 , 2) \n
                                  Answer:
                                  """) 
                    answer_12 = answer_12.lower()
                                       
                    if "(0,2)" in answer_12 or "D" in answer_12 or "d" in answer_12:
                        print(f"""What a play! You totally siked them out with that steal. \n We are the CHAMPIONS!!!""")
                        input("<Press enter to continue> \n")
                        home_plate()
                        break
                    
                    else: 
                      print("""Unfornately that's not the right answer and You're Out!""")
                      third -=1
                    
        else:
            third == 0
            fail_2()
                
            
###############################################################################
#End of the Game: Winner
#The home plate function to symbolize the game has been won
############################################################################### 
                
def home_plate():
  
   print(f"""
   
         /      ||  |  |  |     /   \     |   \/   | |   _  \  |  |  /  __  \  |  \ |  | 
        |  ,----'|  |__|  |    /  ^  \    |  \  /  | |  |_)  | |  | |  |  |  | |   \|  | 
        |  |     |   __   |   /  /_\  \   |  |\/|  | |   ___/  |  | |  |  |  | |  . `  | 
        |  `----.|  |  |  |  /  _____  \  |  |  |  | |  |      |  | |  `--'  | |  |\   | 
         \______||__|  |__| /__/     \__\ |__|  |__| | _|      |__|  \______/  |__| \__| 
                                                                                         
         """)
    
   print(f"""
          {name_1}
          Wow you are incredible! You and the {name_2} came from behind and 
          won the championship game!!! That is AWESOME! It's time to 
          celebrate!!!
          """)
    
   play = input(f"""Would you like to play again?
          1. Yes
          2. No \n
          Answer:
          """)
   play = play.lower()
  
   if "1" in play or "yes" in play :
        print("Great Let's Play Again!")
        input("< Press enter to start> \n")
        start()

   else:
        print("Thanks for playing! Good Bye!")
        input("< Press enter to exit> \n")
        exit()
 
##############################################################################                                           
#End of the game: Loser
#The first fail function used for the batting section 
##############################################################################
                
def fail_1():
    print("""Strike Three!!! You're Out!!! Time for more practice on your algebra!
          """)
    play= input(f"""Would you like to play again?
          1. Yes
          2. No \n
          Answer:
          """)
    play = play.lower()
    
    if "1" in play or "yes" in play :
        print("Great Let's Play Again!")
        input("<Press enter to start>")
        start()
        
    else:
        print("Thanks for playing! Good Bye!")
        input("< Press enter to exit> \n")
        exit()

##############################################################################     
# End of the game: Loser
#The second fail function created for the base stages because of the different verbage   
##############################################################################

def fail_2():
     print("""That makes three outs!!! Time for more practice on your algebra!
          """)
     play= input(f"""Would you like to play again?
          1. Yes
          2. No \n
          Answer: 
              """)
     play= play.lower()
     
     if "1" in play or "yes" in play:
        print("Great Let's Play Again!")
        input("<Press enter to start> \n")
        start()
        
     else:
        print("Thanks for playing! Good Bye!")
        input("<Press enter to exit> \n")
        exit()
        
start()
    