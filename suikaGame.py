import pygame #ライブラリのインポート
import pymunk
import math
import random

disp_size = (800, 800) #画面サイズ
FPS = 100 #フレームレート

#色の定義
BLACK = (0, 0, 0)
BG = (255, 255, 220)
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
radius_07 = 50
radius_08 = 55
radius_09 = 60
radius_10 = 65
radius_11 = 75


#pygame初期化
def init_pygame(disp_size):
    pygame.init()
    display = pygame.display.set_mode(disp_size)
    clock = pygame.time.Clock()
    return display, clock

#pymunk初期化
def init_pymunk(gravity=(0, -1000)):
    space = pymunk.Space()
    space.gravity = gravity
    return space

#初期化実行
display, clock = init_pygame(disp_size)
space = init_pymunk()

#座標変換用メソッド(pygameの原点は左上でpymunkの原点は左下)
def coordinate_trans(point):
    return point[0], disp_size[1] - point[1]

#進化の輪を描画するために角度回転したときの座標を算出する
def cordinate_rotate(point, d):
    rad = math.radians(d)
    rotated_x = point[0] * math.cos(rad) - point[1] * math.sin(rad)
    rotated_y = point[0] * math.sin(rad) + point[1] * math.cos(rad)
    return rotated_x, rotated_y

def draw_title():
    #フォントの設定
    font = pygame.font.SysFont(None, 60)

    #タイトルテキストの作成
    title_text = font.render("SUIKA GAME", True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(disp_size[0] / 2, disp_size[1] / 2))

    #説明テキストの作成
    sub_font = pygame.font.SysFont(None, 40)
    sub_text = sub_font.render("push space key", True, (255, 255, 255))
    sub_rect = sub_text.get_rect(center=(disp_size[0] / 2, disp_size[1] / 2 + 60))

    #テキストの表示
    display.blit(title_text, title_rect)
    display.blit(sub_text, sub_rect)

def draw_gameover():
    font = pygame.font.SysFont(None, 60)
    game_over_text = font.render("Game Over", True, BLACK)
    game_over_rect = game_over_text.get_rect(
        midbottom=(disp_size[0]/2, disp_size[1]/2)
    )
    display.blit(game_over_text, game_over_rect)
def draw_score(tlx, cx, handler):
        font = pygame.font.SysFont(None, 60)
        

        # Draw Score Text
        score_text = font.render("Score: {:,}".format(handler.data["score"]), True, BLACK)
        score_rect = (500, 170)
        display.blit(score_text, score_rect)
class Ball(object):
    def __init__(self, x, y, color, radius, mass, collision_type):
        self.color = color #色
        self.body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)#物理的性質の定義
        self.body.position = x, y #座標
        self.body.mass = mass #質量
        self.shape = pymunk.Circle(self.body, radius) #形状の指定
        self.shape.collision_type = collision_type #衝突時の物体識別
        self.shape.density = 1 #密度
        self.shape.elasticity = 0.1 #弾性
        self.shape.friction = 0.5 #摩擦係数
        space.add(self.body, self.shape) #spaceという物理空間に追加
    def draw(self):
        pygame.draw.circle(
            display,
            self.color,
            coordinate_trans(self.body.position),
            self.shape.radius
        )
#Ballのサブクラス，コンストラクタで半径と色を変えるだけ
class Ball01(Ball): 
    def __init__(self, x, y):
        super().__init__(x, y, color_01, radius_01, 10, 1)
        pass

class Ball02(Ball):
    def __init__(self, x, y):
        super().__init__(x, y, color_02, radius_02, 15, 2)
        pass

class Ball03(Ball):
    def __init__(self, x, y):
        super().__init__(x, y, color_03, radius_03, 20, 3)
        pass

class Ball04(Ball):
    def __init__(self, x, y):
        super().__init__(x, y, color_04, radius_04, 25, 4)
        pass

class Ball05(Ball):
    def __init__(self, x, y):
        super().__init__(x, y, color_05, radius_05, 30, 5)
        pass

class Ball06(Ball):
    def __init__(self, x, y):
        super().__init__(x, y, color_06, radius_06, 35, 6)
        pass

class Ball07(Ball):
    def __init__(self, x, y):
        super().__init__(x, y, color_07, radius_07, 40, 7)
        pass

class Ball08(Ball):
    def __init__(self, x, y):
        super().__init__(x, y, color_08, radius_08, 45, 8)
        pass

class Ball09(Ball):
    def __init__(self, x, y):
        super().__init__(x, y, color_09, radius_09, 50, 9)
        pass

class Ball10(Ball):
    def __init__(self, x, y):
        super().__init__(x, y, color_10, radius_10, 55, 10)
        pass

class Ball11(Ball):
    def __init__(self, x, y):
        super().__init__(x, y, color_11, radius_11, 60, 11)
        pass

def collide(arbiter,space,data):
    a,b = arbiter.shapes
    a_ct = a.collision_type
    b_ct = b.collision_type
    #ボール同士の衝突処理を実装しない場合を判定
    if(a_ct != b_ct):
        #もし異なるBall同士の衝突の場合
        return
    # if(a_ct == 11 or b_ct == 11):
    #     #Ball11同士の衝突の場合
    #     return
    #衝突した座標を算出
    a_x,a_y = a.body.position
    b_x,b_y = b.body.position
    x = (a_x + b_x) / 2
    y = (a_y + b_y) / 2
    #削除するBallを求める
    balls_to_remove = []
    for ball in data["balls"]:
        if(ball.shape == a or ball.shape == b):
            balls_to_remove.append(ball)
            #Ballを削除する
    for ball in balls_to_remove:
        space.remove(ball.shape,ball.body)
        data["balls"].remove(ball)
        #Ballの作成とスコアの更新
    if(a_ct == 1 and b_ct == 1):
        #もしBall01同士の衝突ならBall02を作成かつスコアを1更新
        data["balls"].append(Ball02(x,y))
        data["score"] += 1
    elif(a_ct == 2 and b_ct == 2):
        #もしBall02同士の衝突ならBall03を作成かつスコアを3更新
        data["balls"].append(Ball03(x,y))
        data["score"] += 3
    elif(a_ct == 3 and b_ct == 3):
        #もしBall03同士の衝突ならBall04を作成かつスコアを6更新
        data["balls"].append(Ball04(x,y))
        data["score"] += 6
    elif(a_ct == 4 and b_ct == 4):
        #もしBall04同士の衝突ならBall05を作成かつスコアを10更新
        data["balls"].append(Ball05(x,y))
        data["score"] += 10
    elif(a_ct == 5 and b_ct == 5):
            #もしBall05同士の衝突ならBall05を作成かつスコアを15更新
        data["balls"].append(Ball06(x,y))
        data["score"] += 15
    elif(a_ct == 6 and b_ct == 6):
            #もしBall06同士の衝突ならBall05を作成かつスコアを21更新
        data["balls"].append(Ball07(x,y))
        data["score"] += 21
    elif(a_ct == 7 and b_ct == 7):
        #もしBall07同士の衝突ならBall05を作成かつスコアを28更新
        data["balls"].append(Ball08(x,y))
        data["score"] += 28
    elif(a_ct == 8 and b_ct == 8):
        #もしBall08同士の衝突ならBall05を作成かつスコアを36更新
        data["balls"].append(Ball09(x,y))
        data["score"] += 36
    elif(a_ct == 9 and b_ct == 9):
            #もしBall09同士の衝突ならBall10を作成かつスコアを45更新
        data["balls"].append(Ball10(x,y))
        data["score"] += 45
    elif(a_ct == 10 and b_ct == 10):
            #もしBall10同士の衝突ならBall11を作成かつスコアを55更新
        data["balls"].append(Ball11(x,y))
        data["score"] += 55
    elif(a_ct == 11 and b_ct == 11):
            #もしBall11同士の衝突ならスコア更新だけ
        # data["balls"].append(Ball11(x,y))
        data["score"] += 70
    pass

def collision_handler(space, balls, collide):
    handler = space.add_default_collision_handler()
    handler.data["balls"] = balls
    handler.data["score"] = 0
    handler.post_solve = collide
    return handler
         
class RingBall(object):
    def __init__(self, x, y, color, radius):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
    def draw(self):
        pygame.draw.circle(
            display,
            self.color,
            coordinate_trans((self.x, self.y)),
            self.radius
        )

class CurrentBall(RingBall):
    def __init__(self, x, y, color, radius, start, stop):
        super().__init__(x, y, color, radius)
        self.dist = 2
        self.start = start
        self.stop = stop
    def move_ball(self):
        mouse_x, _ = pygame.mouse.get_pos()
        if mouse_x < self.start:
            self.x = self.start
        elif mouse_x > self.stop:
            self.x = self.stop
        else:
            self.x = mouse_x
    def get_ball(self):
        if(self.radius == radius_01):
            ball = Ball01(self.x, self.y)
        elif(self.radius == radius_02):
            ball = Ball02(self.x, self.y)
        elif(self.radius == radius_03):
            ball = Ball03(self.x, self.y)
        elif(self.radius == radius_04):
            ball = Ball04(self.x, self.y)
        elif(self.radius == radius_05):
            ball = Ball05(self.x, self.y)
        return ball

class Field():
    def __init__(self, tlx, tly, brx, bry):
        self.tlx = tlx  #左上のx座標
        self.tly = tly  #左上のy座標
        self.brx = brx  #右下のx座標
        self.bry = bry  #右下のy座標
        
        self.field_width = int(brx - tlx)  #フィールドの幅
        self.step = 7  #点線の間隔
        self.line_width = 3  #線の幅
        
        #右線の開始点と終了点
        self.rl_start, self.rl_stop = (brx, tly), (brx, bry)
        
        #下線の開始点と終了点
        self.bl_start, self.bl_stop = (tlx, bry), (brx, bry)
        
        #左線の開始点と終了点
        self.ll_start, self.ll_stop = (tlx, tly), (tlx, bry)
        
        #pymunkを使って境界線を作成(描画じゃなくて物理的な判定みたいな感じ)
        self.create_line(self.rl_start, self.rl_stop)  # 右の境界線
        self.create_line(self.bl_start, self.bl_stop)  # 下の境界線
        self.create_line(self.ll_start, self.ll_stop)  # 左の境界線

    #上部の点線を描画するメソッド
    def draw(self):
        for i in range(0, self.field_width, self.step):
            if(i % (self.step * 2) == 0):
                pygame.draw.line(
                    display, 
                    BLACK,  
                    coordinate_trans((self.tlx+i, self.tly)),  #開始点
                    coordinate_trans((self.tlx+i+self.step, self.tly)),  #終了点
                    self.line_width  #線の幅設定
                )
        #右の境界線を描画
        pygame.draw.line(
            display,
            BLACK,
            coordinate_trans(self.rl_start),
            coordinate_trans(self.rl_stop),
            self.line_width
        )
        #下の境界線を描画
        pygame.draw.line(
            display,
            BLACK,
            coordinate_trans(self.bl_start),
            coordinate_trans(self.bl_stop),
            self.line_width
        )
        #左の境界線を描画
        pygame.draw.line(
            display,
            BLACK,
            coordinate_trans(self.ll_start),
            coordinate_trans(self.ll_stop),
            self.line_width
        )

    def create_line(self, start, stop):
        body = pymunk.Body(body_type=pymunk.Body.STATIC)  
        shape = pymunk.Segment(body, start, stop, self.line_width)
        shape.elasticity = 0.75  #弾性
        shape.friction = 0.9  #摩擦
        space.add(shape, body)  #スペースに追加

class NextBall(RingBall):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.create_ball()
    def create_ball(self):
        r = random.randint(1, 5)
        if(r == 1):
            self.color = color_01
            self.radius = radius_01
        elif(r == 2):
            self.color = color_02
            self.radius = radius_02
        elif(r == 3):
            self.color = color_03
            self.radius = radius_03
        elif(r == 4):
            self.color = color_04
            self.radius = radius_04
        elif(r == 5):
            self.color = color_05
            self.radius = radius_05

#ゲームオーバーかを確認する
def is_game_over(balls, y):
    for ball in balls:
        ball_top = ball.body.position[1] + ball.shape.radius #各ボールのy方向座標
        if(ball_top >= y):
            return True
    return False

#ゲーム実行メソッド(main)
def game():
    running = True
    while running: #タイトル画面
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
            

        #バックグラウンドの色を設定
        display.fill(color_11)

        #タイトルを描画
        draw_title()

        #画面の更新
        pygame.display.flip()

    #フィールドの定数
    tlx, tly = 250, 450 #左上のxと左上のy
    brx, bry = 550, 100
    field = Field(tlx, tly, brx, bry) #フィールドのインスタンス

    #フィールド上にあるBallを納める
    balls = []

    #同じball衝突の処理
    handler = collision_handler(space, balls, collide) 
    #進化の輪の変数
    cx, cy = 170, 600 #輪の位置
    ring_of_balls = [
        RingBall(cx, cy, color_01, radius_01),
        RingBall(cx, cy, color_02, radius_01),
        RingBall(cx, cy, color_03, radius_01),
        RingBall(cx, cy, color_04, radius_01),
        RingBall(cx, cy, color_05, radius_01),
        RingBall(cx, cy, color_06, radius_01),
        RingBall(cx, cy, color_07, radius_01),
        RingBall(cx, cy, color_08, radius_01),
        RingBall(cx, cy, color_09, radius_01),
        RingBall(cx, cy, color_10, radius_01),
        RingBall(cx, cy, color_11, radius_01),
    ]
    for i, ball in enumerate(ring_of_balls):
        d = -30 + (-30) * i
        x, y = cordinate_rotate((0, 100), d)
        ball.x += x
        ball.y += y
        pass

    #currentBallの宣言
    current_ball = CurrentBall(
        tlx + (brx - tlx) / 2,  # フィールド中央
        tly + radius_06,        # フィールド上端からボール6半径分上
        color_01,
        radius_01,
        tlx + radius_06,        # フィールド左端からボール6半径分内側
        brx - radius_06         # フィールド右端からボール6半径分内側
    )
    next_ball = NextBall(cx, cx)  # サンプルボールの上方に表示

    #ゲームオーバーフラグ
    GAMEOVERFLAG = False
    CHECKGAMEOVER = pygame.USEREVENT + 1

    #ゲーム開始
    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
            # マウスボタンが押されたときの処理
                if event.button == 1:  # 左クリック
                # Drop Current Circle
                    balls.append(current_ball.get_ball())
                # Update Current Circle
                    current_ball.color = next_ball.color
                    current_ball.radius = next_ball.radius
                # Update Next Circle
                    next_ball.create_ball()
                pygame.time.set_timer(CHECKGAMEOVER, 1000)#1秒後にチェックゲームオーバーイベントをよぶ
            if(event.type==CHECKGAMEOVER):
                GAMEOVERFLAG = is_game_over(balls, tly)
                # print(GAMEOVERFLAG)

        #背景の色
        display.fill(BG)
        #枠を描画
        field.draw()
        #進化の輪描画
        for ball in ring_of_balls:
            ball.draw()
        
        #フィールドのBallを描画
        for ball in balls:
            ball.draw()

        current_ball.draw()
        current_ball.move_ball()
      
        #ネクストボール更新
        next_ball.draw()
        if(GAMEOVERFLAG):
            draw_gameover()
            pygame.display.update()
            for ball in balls:
                space.remove(ball.shape, ball.body)
            balls.clear()
            pygame.time.wait(2000)
            game()
        draw_score(tlx, cx, handler)

        #画面更新
        pygame.display.update()
        clock.tick(FPS)
        space.step(1/FPS)

game()
pygame.quit()