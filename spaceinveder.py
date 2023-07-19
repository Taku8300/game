import pygame
import random
import time

# ゲームの初期化
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("敵をよけるゲーム")

# ゲームの要素の設定
player_image = pygame.Surface((30, 30))  # プレイヤー画像を作成
player_image.fill((255, 255, 0))  # プレイヤー画像を黄色に設定
player_width = 30
player_height = 30
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 1  # プレイヤーの速度を調整

enemy_width = 30
enemy_height = 30
enemy_x = random.randint(0, screen_width - enemy_width)
enemy_y = random.randint(50, 200)
enemy_speed = 1

# ゲームの状態
game_over = False
start_time = time.time()

# ランキングデータ
rankings = []

# ゲームループ
while not game_over:
    screen.fill((0, 0, 0))  # 画面を黒でクリア

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
            player_x += player_speed

        enemy_y += enemy_speed
        if enemy_y > screen_height:
            enemy_x = random.randint(0, screen_width - enemy_width)
            enemy_y = random.randint(50, 200)

        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
        if player_rect.colliderect(enemy_rect):
            game_over = True

        screen.blit(player_image, (player_x, player_y))
        pygame.draw.rect(screen, (255, 0, 0), enemy_rect)

    pygame.display.flip()

# タイム計測終了
end_time = time.time()
elapsed_time = end_time - start_time

# ランキングに記録追加
rankings.append(elapsed_time)

# ランキングをソート
rankings.sort()

# ランキングを表示
screen.fill((0, 0, 0))  # 画面を黒でクリア
font = pygame.font.Font(None, 30)
text = font.render("ランキング", True, (255, 255, 255))
screen.blit(text, (screen_width // 2 - text.get_width() // 2, 50))
for i, record in enumerate(rankings):
    text = font.render(f"{i+1}. {record:.2f}秒", True, (255, 255, 255))
    screen.blit(text, (screen_width // 2 - text.get_width() // 2, 100 + i * 30))
pygame.display.flip()

# 終了待機
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
