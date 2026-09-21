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