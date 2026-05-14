import pygame

        for pellet in pellets:
            px, py = pellet
            distance = ((player.x - px) ** 2 + (player.y - py) ** 2) ** 0.5

            if distance < 14:
                player.score += 10
            else:
                remaining.append(pellet)

        pellets = remaining

        # Win condition
        if len(pellets) == 0:
            win = True

        # Ghost collision
        for ghost in ghosts:
            distance = ((player.x - ghost.x) ** 2 + (player.y - ghost.y) ** 2) ** 0.5

            if distance < TILE // 2:
                lose = True

    # Draw maze
    for row_index, row in enumerate(maze):
        for col_index, cell in enumerate(row):
            x = col_index * TILE
            y = row_index * TILE

            if cell == '#':
                pygame.draw.rect(screen, BLUE, (x, y, TILE, TILE))

    # Draw pellets
    for px, py in pellets:
        pygame.draw.circle(screen, WHITE, (px, py), 4)

    player.draw()

    for ghost in ghosts:
        ghost.draw()

    score_text = font.render(f"Score: {player.score}", True, WHITE)
    screen.blit(score_text, (10, HEIGHT - 40))

    if win:
        text = font.render("YOU WIN!", True, YELLOW)
        screen.blit(text, (WIDTH // 2 - 70, HEIGHT // 2))

    if lose:
        text = font.render("GAME OVER", True, RED)
        screen.blit(text, (WIDTH // 2 - 90, HEIGHT // 2))

    pygame.display.flip()

pygame.quit()
