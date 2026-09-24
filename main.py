import pygame
import sys
import random

pygame.init() #initializes few modules/works like a constructor
screen = pygame.display.set_mode((800, 500)) #Gaming screen width/hight initialization
pygame.display.set_caption('PlayWords')
clock = pygame.time.Clock()

#Word List
word_list = ["SPACE","COMPUTER","MONEY","HOTEL","WORLD","PICTURE","HUMANS","LAZY","BOOK","ACCUSE","SLAVE","MEMES",
"PLAYGROUND","NUMBERS","DIAPERS","ANIMALS","SPIKY","CACTUS","POLICE","BEAUTY","FOOTBALL","BALL","ELECTRICITY",
"DICTIONARY","CARTOON","CORONA","TISSUE","PAPER","CURTAIN","KEY","BRIGHT","DARK","ACHIEVE","ACTOR","RECORD","BIOLOGY","DEPRESSION","EXAMINATION",
"BULLY","ROBOT","HOME","SCREEN","IMPRESSIVE","JOYFUL","PLAY","DESIGN","BATTERY","STATUE","BREAK","DINOSAUR",
"SHAKER","PRAY","FLOW","SOFT","HELP","CIRCLE","RACE","REACT","GOOD"]
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
Buttons = []

def phase_one_handle_events():
    """
    Phase 1:
    Read and process all user input.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_active = True
                winner_status = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked_pos = event.pos
            for button, letter in Buttons:
                if button.collidepoint(clicked_pos):
                    guessed_words.append(letter)
                    if letter not in Word:
                        moves_left -= 1
                    if moves_left == 0:
                        # Dummy reset function
                        reset_game_after_loss()
def reset_game_after_loss():
    """
    Dummy function.
    The real reset logic will be added in Phase 2.
    """
    pass
def phase_two_update_game():
    """
    Phase 2:
    Update the game state after input.
    """
    pass
def phase_three_draw_screen():
    """
    Phase 3:
    Draw the correct screen based on the current game state.
    """
    pass
# Main game loop
while True:
    # Phase 1: Handle keyboard, mouse, and window events
    phase_one_handle_events()
    # Phase 2: Update the game state
    phase_two_update_game()
    # Phase 3: Draw the correct screen
    phase_three_draw_screen()
    # Refresh the display
    pygame.display.update()
    # Control the frame rate
    clock.tick(80)