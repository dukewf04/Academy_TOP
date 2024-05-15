import random
from board import *
from config import *
from connect import *

def main():
    grid = new_grid()

    draw_grid(grid)
    pg.display.update()

    pick_random = random.randint(PLAYER, AI_PLAYER)

    game_over = False
    while not game_over:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    sys.exit()
            elif event.type == pg.QUIT:
                sys.exit()

            if event.type == pg.MOUSEMOTION:
                pg.draw.rect(screen, WHITE, (0, 0, width, DISC_SIZE))
                position_x = event.pos[0]  # Нулевая позиция
                if pick_random == PLAYER:
                    pg.draw.circle(screen, RED, (position_x, int(DISC_SIZE/2)), DISC_RADIUS)
            pg.display.update()
            if event.type == pg.MOUSEBUTTONDOWN:
                pg.draw.rect(screen, WHITE, (0, 0, width, DISC_SIZE))
                if pick_random == PLAYER:
                    position_x = event.pos[0]
                    column = int(math.floor(position_x/DISC_SIZE))

                    if is_valid_position(grid, column):
                        row = get_next_open_row(grid, column)
                        grid[row][column] = PLAYER_PIECE

                        if search_win_move(grid, PLAYER_PIECE):
                            label = my_font.render("Player WIN!", 1, RED)
                            screen.blit(label, (40, 10))
                            game_over = True

                        pick_random += 1
                        pick_random %= 2

                        draw_grid(grid)

        if pick_random == AI_PLAYER and not game_over:
            column, minimax_score = minimax(grid, 5, -math.inf, math.inf, True)

            if is_valid_position(grid, column):
                row = get_next_open_row(grid, column)
                grid[row][column] = AI_PLAYER_PIECE

                if search_win_move(grid, AI_PLAYER_PIECE):
                    label = my_font.render("AI WIN!", 1, RED)
                    screen.blit(label, (40, 10))
                    game_over = True
                draw_grid(grid)
                pick_random += 1
                pick_random %= 2

        if game_over:
            pg.time.wait(2500)

if __name__ == "__main__":
    main()
    pg.quit()