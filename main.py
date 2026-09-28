import sys
import pygame
import random

#Word List
word_list = ["SPACE","COMPUTER","MONEY","HOTEL","WORLD","PICTURE","HUMANS","LAZY","BOOK","ACCUSE","SLAVE","MEMES",
"PLAYGROUND","NUMBERS","DIAPERS","ANIMALS","SPIKY","CACTUS","POLICE","BEAUTY","FOOTBALL","BALL","ELECTRICITY",
"DICTIONARY","CARTOON","CORONA","TISSUE","PAPER","CURTAIN","KEY","BRIGHT","DARK","ACHIEVE","ACTOR","RECORD","BIOLOGY","DEPRESSION","EXAMINATION",
"BULLY","ROBOT","HOME","SCREEN","IMPRESSIVE","JOYFUL","PLAY","DESIGN","BATTERY","STATUE","BREAK","DINOSAUR",
"SHAKER","PRAY","FLOW","SOFT","HELP","CIRCLE","RACE","REACT","GOOD"]
#Word Hint
word_hint = {
    "SPACE":"IT IS SOMETHING WE ALL NEED SOMETIMES",
    "COMPUTER":"YOU ARE USING RIGHT NOW",
    "MONEY":"ITS A PIECE OF PAPER AND VERY VALUBLE",
    "HOTEL":"WE STAY HERE FOR A NIGHT OR TWO",
    "WORLD":"ITS VERY BIG AND WE ALL LIVE IN IT",
    "PICTURE":"ITS LIKE AN IMAGE",
    "HUMANS":"WHAT ARE WE?",
    "LAZY":"_ A _ Y",
    "BOOK":"IT HAS SEVERL PAGES",
    "ACCUSE":"SORT OF BLAMING",
    "SLAVE":"A SERVANT BUT HE IS TREATED IN A MUCH WORSE WAY",
    "MEMES":"A TYPE OF JOKE",
    "PLAYGROUND":"A PLACE WHERE WE PLAY",
    "NUMBERS":"THE MAIN THING IN MATHS",
    "DIAPERS":"WE WORE IT WHEN WE WERE BABIES",
    "ANIMALS":"_N_M_L_",
    "SPIKY":"SHARP AND POINTY",
    "CACTUS":"ITS LIKE A CACTUS",
    "POLICE":"ITS AN OCCUPATION WHICH FIGHTS CRIME",
    "BEAUTY":"_EA_T_",
    "FOOTBALL":"ITS A SPORT",
    "BALL":"IT HAS A SPHERE SHAPE",
    "ELECTRICITY":"WE NEED THIS TO RUN CERTAIN APPLIANCES",
    "DICTIONARY":"OXFORD __________",
    "CARTOON":"ITS AN ENTERTAINMENT",
    "CORONA":"IT BEGAN ON 2019 DECEMBER IN CHINA",
    "TISSUE":"WE USE IT TO WIPE",
    "PAPER":"ITS A PAPER",
    "CURTAIN":"SORRY I COUDNT FIND ANY HINT FOR THIS BUT WE JUST BOUGHT IT A FEW DAYS AGO FORM DUBAI",
    "KEY":"WE USE IT UNLOCK A DOOR",
    "BRIGHT":"ITS THE DEFENITION OF BRIGHT",
    "DARK":"OPPOSITE OF BRIGHT",
    "ACHIEVE":"AN ACT OF GETTING SOMETHING",
    "RECORD":"TO HOLD SOMETHING",
    "ACTOR":"A PERSON WHO ACTS AND PLAYS ROLES FOR A LIVING OR SOMETIMES FUN",
    "BIOLOGY":"ITS A SUBJECT",
    "DEPRESSION":"IMPRESSION BUT WITH A SLIGHT CHANGE IN ITS SPELLING",
    "EXAMINATION":"ITS SOMETHING MOST OF THE STUDENTS ARE AFRAID OF",
    "BULLY":"AN ACT OF HURTING SOMEONE",
    "ROBOT":"ITS A PART OF THE ARTIFICIAL INTELLIGENCE",
    "HOME":"SYNONYM OF HOUSE",
    "SCREEN":"YOU ARE LITERALLY LOOKING AT IT RIGHT NOW",
    "IMPRESSIVE":"_M_R_SS_V_",
    "JOYFUL":"SYNONYM OF FUN",
    "PLAY":"ITS SOMETHING WE KIDS LOVE TO DO",
    "DESIGN":"_E_I_N",
    "BATTERY":"WE PLUG IN OUR DEVICES TO INCREASE OUR _______?",
    "STATUE":"AN IDLE",
    "BREAK":"THE OPPOSITE OF MAKE",
    "DINASOUR":"THEY BECAME EXTINCT",
    "SHAKER":"SOMEONE WHO SHAKES",
    "PRAY":"AN ACT OF WORSHIP",
    "FLOW":"THE ANSWER IS LOW BUT WITH AN F",
    "SOFT":"OPPOSITE OF HARD",
    "HELP":"WE SAY THIS IN DESPERATE TIMES",
    "CIRCLE":"ITS CIRCULAR IN SHAPE",
    "RACE":"AN ACT TO FIND OUT WHO COMES FIRST OR SECOND OR THIRD OF FOURTH AND SO ON",
    "REACT":"WE DO THIS AFTER WE SEE OR HEAR ETC SOMETHING",
    "GOOD":"OPPOSITE OF BAD"
    }
#_________________
#Function for selecting random word from given Word List
def word_generator():
    temp_word=random.choice(word_list)
    return temp_word
#_______________

#Global Variable Declaration
game_active = False
winner_status = False
win=True
Word = word_generator()
moves_left = len(Word) +2
guessed_words = []
letter_list = []
#Printing Initial Word
#print("Initial Word= "+Word)

#Variable Declaration for alphabet UI creation
A = 65
Rows = 3
Cols = 5
Gap = 20
Size = 40
Boxes = []
Buttons = []

#Functionality building for creating whole alphabet UI
#_____________________________________________________
def alphabetUI(Word):
    # print(Word)
    for i in Word:
        letter_list.append(ord(i))
    count = len(letter_list)
    while count < 15:
        random_alpha = random.randint(65, 90)
        if random_alpha not in letter_list:
            letter_list.append(random_alpha)
            count = count + 1
    random.shuffle(letter_list)
    for row in range(Rows):
        for col in range(Cols):
            x = ((Gap * col) + Gap) + (Size * col) + 415
            y = ((Gap * row) + Gap) + (Size * row) + 200
            box = pygame.Rect(x, y, Size, Size)
            Boxes.append(box)
    for indx, box in enumerate(Boxes):
        letter = chr(letter_list[indx])
        button = [box, letter]
        Buttons.append(button)
#__________________________________________________

alphabetUI(Word)#called once for head start

#function for drawing alphabet UI Boxes
#_________________________
def draw_buttons(Buttons):
    for button, letter in Buttons:
        btn_font = pygame.font.Font(None, 40)
        btn_text = btn_font.render(letter, True, 'Black')
        btn_text_rect = btn_text.get_rect(center=(button.x + Size // 2, button.y + Size // 2))
        pygame.draw.rect(screen, 'Black', button, 2)
        screen.blit(btn_text, btn_text_rect)
#_______________________________

#background_for_word() function is used to create background for your input "_____"
def background_for_word():
    parent_surface = pygame.Surface((350, 350))
    parent_surface.fill('#F3E885')
    screen.blit(parent_surface, (400, 80))
    output_surface = pygame.Surface((300, 80))
    output_surface.fill('Teal')
    screen.blit(output_surface, (425, 100))
#____________________________

#displaying moves left
#_______________________________
def score_moves_left():
    score_font = pygame.font.Font(None, 40)
    score_txt = score_font.render('Moves Left: ' + f'{moves_left}', True, 'Black')
    screen.blit(score_txt, (0, 0))
#_______________________________

#display_guess() function display the guessed letter in UI
#______________________
def display_guess():
    display_word = ''
    for letter in Word:
        if letter in guessed_words:
            display_word += f"{letter}"
            if display_word==Word:
                global winner_status,game_active
                winner_status=True
                game_active=False
        else:
            display_word += "_ "
    letter_font = pygame.font.Font(None, 40)
    text = letter_font.render(display_word, True, 'Black')
    screen.blit(text, (450, 130))
#_____________________

#display_hint(Word) function display hints in UI
#_______________________________________________
def display_hint(Word):
    letter_font = pygame.font.Font(None, 25)
    text = letter_font.render(word_hint[Word], True, 'Black')
    screen.blit(text, (100, 200))
#_______________________________________________

#startScreen() function used to change indexing for character animation
#_________________________________________________
def startScreen():
    global sesame_surface, sesame_index
    sesame_index += 0.1 #ignore 0.1 here you can also use 1 here
    if sesame_index >= len(sesame_list): sesame_index = 0
    sesame_surface = sesame_list[int(sesame_index)]
#____________________________________________________

#Above this line all the functions are declared which contains logics(or functionality)

#Our game starts from here

pygame.init() #initializes few modules/works like a constructor
screen = pygame.display.set_mode((800, 500)) #Gaming screen width/hight initialization
pygame.display.set_caption('PlayWords')
clock = pygame.time.Clock() #control FPS(Frame Per Second)
#Won Screen Title
Won_font = pygame.font.Font('font/AlloyInk-nRLyO.ttf', 40)
Won_surface = Won_font.render('Game Won', True, 'Black')
Won_rect = Won_surface.get_rect(center=(400, 100))
#Lost Screen Title
Lost_font = pygame.font.Font('font/AlloyInk-nRLyO.ttf', 40)
Lost_title_surface = Lost_font.render('Game Lost', True, 'Black')
Lost_rect = Lost_title_surface.get_rect(center=(400, 100))
#Intro Screen Title
name_font = pygame.font.Font('font/AlloyInk-nRLyO.ttf', 40)
name_surface = Lost_font.render('Play Words', True, 'Black')
name_rect = name_surface.get_rect(center=(400, 100))

# Press Space To Start-> Text display
play_font = pygame.font.Font(None, 40)
play_surface = play_font.render('Press Space To Start', True, '#00827f')
play_rect = play_surface.get_rect(center=(410, 300))

#Moves_left->Text display
moves_left_font = pygame.font.Font(None, 40)
moves_left_txt = moves_left_font.render('Moves Left: ' + f'{moves_left}', True, 'Black')

# play Again
play_again_font = pygame.font.Font(None, 40)
play_again_txt = play_again_font.render('Press Space To Play Again', True, 'Black')
play_again_rect = play_again_txt.get_rect(center=(410, 350))

# character width/height initialization
x = 150
y = 180
# frame 1
sesame_1 = pygame.image.load('images/starting/1.png').convert_alpha()
sesame_1 = pygame.transform.scale(sesame_1, (x, y))
# frame 2
sesame_2 = pygame.image.load('images/starting/2.png').convert_alpha()
sesame_2 = pygame.transform.scale(sesame_2, (x, y))
# frame 3
sesame_3 = pygame.image.load('images/starting/3.png').convert_alpha()
sesame_3 = pygame.transform.scale(sesame_3, (x, y))
# frame 4
sesame_4 = pygame.image.load('images/starting/4.png').convert_alpha()
sesame_4 = pygame.transform.scale(sesame_4, (x, y))
# frame 5
sesame_5 = pygame.image.load('images/starting/5.png').convert_alpha()
sesame_5 = pygame.transform.scale(sesame_5, (x, y))
# frame 6
sesame_6 = pygame.image.load('images/starting/6.png').convert_alpha()
sesame_6 = pygame.transform.scale(sesame_6, (x, y))
# frame 7
sesame_7 = pygame.image.load('images/starting/7.png').convert_alpha()
sesame_7 = pygame.transform.scale(sesame_7, (x, y))
# frame 8
sesame_8 = pygame.image.load('images/starting/8.png').convert_alpha()
sesame_8 = pygame.transform.scale(sesame_8, (x, y))
# frame 9
sesame_9 = pygame.image.load('images/starting/9.png').convert_alpha()
sesame_9 = pygame.transform.scale(sesame_9, (x, y))
# frame 10
sesame_10 = pygame.image.load('images/starting/10.png').convert_alpha()
sesame_10 = pygame.transform.scale(sesame_10, (x, y))
# frame 11
sesame_11 = pygame.image.load('images/starting/11.png').convert_alpha()
sesame_11 = pygame.transform.scale(sesame_11, (x, y))
# frame 12
sesame_12 = pygame.image.load('images/starting/12.png').convert_alpha()
sesame_12 = pygame.transform.scale(sesame_12, (x, y))
# frame 13
sesame_13 = pygame.image.load('images/starting/13.png').convert_alpha()
sesame_13 = pygame.transform.scale(sesame_13, (x, y))
# frame 14
sesame_14 = pygame.image.load('images/starting/14.png').convert_alpha()
sesame_14 = pygame.transform.scale(sesame_14, (x, y))
# frame 15
sesame_15 = pygame.image.load('images/starting/15.png').convert_alpha()
sesame_15 = pygame.transform.scale(sesame_15, (x, y))
# frame 18
sesame_18 = pygame.image.load('images/starting/18.png').convert_alpha()
sesame_18 = pygame.transform.scale(sesame_18, (x, y))
# frame 20
sesame_20 = pygame.image.load('images/starting/20.png').convert_alpha()
sesame_20 = pygame.transform.scale(sesame_20, (x, y))
# frame 21
sesame_21 = pygame.image.load('images/starting/21.png').convert_alpha()
sesame_21 = pygame.transform.scale(sesame_21, (x, y))
# frame 23
sesame_23 = pygame.image.load('images/starting/23.png').convert_alpha()
sesame_23 = pygame.transform.scale(sesame_23, (x, y))
# frame 24
sesame_24 = pygame.image.load('images/starting/24.png').convert_alpha()
sesame_24 = pygame.transform.scale(sesame_24, (x, y))
# sesame_list
sesame_list = [sesame_1, sesame_2, sesame_3, sesame_4, sesame_5,
               sesame_6, sesame_7, sesame_8, sesame_9, sesame_10,
               sesame_11, sesame_12, sesame_13, sesame_14, sesame_15,
               sesame_18, sesame_20, sesame_20,
               sesame_21, sesame_23, sesame_24]
sesame_index = 0
sesame_surface = sesame_list[sesame_index]

sesame_rect = sesame_surface.get_rect(center=(400, 230))

#Infinite Loop Initiated gets terminated when we close it
while True:
    for event in pygame.event.get(): #event contain list for different operations
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_active = True
            winner_status=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked_pos = event.pos
            for button, letter in Buttons:
                if button.collidepoint(clicked_pos):
                    guessed_words.append(letter)
                    if letter not in Word:
                        moves_left -= 1
                    if moves_left == 0:
                        # In this section we reset the entire functionality so we can re-play with the new values and moves_left
                        Word=word_generator()
                        moves_left=len(Word)+2
                        guessed_words.clear()
                        Buttons.clear()
                        letter_list.clear()
                        Boxes.clear()
                        alphabetUI(Word)
                        win=False
                        game_active = False
    if game_active:
        win=True
        screen.fill('#FFF7B0')
        score_moves_left()
        background_for_word()
        draw_buttons(Buttons)
        display_guess()
        display_hint(Word)

    else:
        if win==False and winner_status==False:
            screen.fill("Red")
            screen.blit(Lost_title_surface, Lost_rect)
            screen.blit(play_again_txt, play_again_rect)
        elif winner_status==True:
            screen.fill("Blue")
            Word = word_generator()
            moves_left = len(Word) + 2
            guessed_words.clear()
            Buttons.clear()
            letter_list.clear()
            Boxes.clear()
            alphabetUI(Word)
            screen.blit(Won_surface, Won_rect)
            screen.blit(play_again_txt, play_again_rect)
        else:
            screen.fill('#FFF7B0')
            startScreen()
            screen.blit(sesame_surface, sesame_rect)
            screen.blit(name_surface, name_rect)
            screen.blit(play_surface, play_rect)
    pygame.display.update()
    clock.tick(80)
