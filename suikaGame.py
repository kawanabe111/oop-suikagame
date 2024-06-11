import pygame #ライブラリのインポート
import pymunk
import math
import random

disp_size = (800, 800) #画面サイズ
FPS = 100 #フレームレート

#色の定義
BLACK = (0, 0, 0)
WHEAT = (245, 222, 179)
WHITE = (255, 255, 255)
color_01 = (255,   0,   0)
color_02 = (255, 100, 100)
color_03 = (100,   0, 150)
color_04 = (255, 150,   0)
color_05 = (255, 100,   0)
color_06 = (255,   0,   0)
color_07 = (255, 255, 150)
color_08 = (255, 200, 200)
color_09 = (255, 200,   0)
color_10 = (100, 200,  50)
color_11 = (  0, 150,   0)

#Ballの半径を定義
radius_01 = 10
radius_02 = 15
radius_03 = 20
radius_04 = 25
radius_05 = 30
radius_06 = 35
radius_07 = 40
radius_08 = 45
radius_09 = 50
radius_10 = 55
radius_11 = 60


#pygame初期化
def initialize_pygame(disp_size):
    pygame.init()
    display = pygame.display.set_mode(disp_size)
    clock = pygame.time.Clock()
    return display, clock

#pymunk初期化
def initialize_pymunk(gravity=(0, -1000)):
    space = pymunk.Space()
    space.gravity = gravity
    return space

#初期化実行
display, clock = initialize_pygame(disp_size)
space = initialize_pymunk()

#座標変換用メソッド(pygameの原点は左上でpymunkの原点は左下)
def convert_cordinates(point):
    return point[0], disp_size[1] - point[1]

def draw_title():
    font = pygame.font.SysFont(None, 60)
    title_text = font.render("SUIKA GAME", True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(disp_size[1] / 2, disp_size[1] / 2))
    display.blit(title_text, title_rect)


class Ball(object):
    def __init__(self, x, y, color, radius, mass, collision_type):
        self.color = color #色
        self.body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)#物理的性質の定義
        self.body.position = x, y #座標
        self.body.mass = mass #質量
        self.shape = pymunk.Circle(self.body, radius) #形状の指定
        self.shape.collision_type = collision_type #衝突時の物体識別
        self.shape.density = 1 #密度
        self.shape.elasticity = 0.5 #弾性
        self.shape.friction = 0.5 #摩擦係数
        space.add(self.body, self.shape) #spaceという物理空間に
    def draw(self):
        pygame.draw.circle(
            display,
            self.color,
            convert_cordinates(self.body.position),
            self.shape.radius
        )

def game():
    running = True
    while running: #タイトル画面
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False

        # 画面のクリア
        display.fill(WHEAT)

        # タイトルを描画
        draw_title()

        # 画面の更新
        pygame.display.flip()

    # Ball
    balls = []

    # Game Start
    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                return
            if(event.type == pygame.MOUSEBUTTONDOWN):
                x, y = convert_cordinates(event.pos)
                balls.append(
                    Ball(x, y, BLACK, 50, 50,0)
                )
        # Fiil background
        display.fill(WHEAT)

        # Draw Ball
        for ball in balls:
            ball.draw()

        # Display Update
        pygame.display.update()
        clock.tick(FPS)
        space.step(1/FPS)


game()
pygame.quit()