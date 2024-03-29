# -*- coding: UTF-8 -*-
import easygui
import pygame,sys,random
import pickle



global points1
global obstacles
global speed


def main_menu () :
    pygame.init ()
    pygame.mixer.music.load('start.mp3')
    pygame.mixer.music.play()
  
    menu=easygui.buttonbox("                                GAME MENU",
                    choices=["  Start game  ","  Load save  ","  Game control  " ,"  Exit game  "])
  
    
    if(menu=="  Start game  "):
        game(0)
    elif (menu=="  Exit game  "):
        exit()
    elif (menu=="  Game control  "):
        print ("\a")
        control = easygui.msgbox(title = "Control ",msg = " |Turn left| - [ A ] \n |Turn right| - [ D ] \n |Boost| - [ W ] \n |Retard| - [ S ] ")
        main_menu ()
    elif (menu=="  Game settings  "):
        settings=easygui.msgbox("COMING SOON")
    elif (menu=="  Load save  "):
        f = open('data', 'rb')
        points1 = pickle.load(f)
        print ("\a")
        f.close()
        game(points1)
 



def game(count_points):
    skier_images = ["players_left.png","players_right.png","player_front.png"]

    
    class SkierClass(pygame.sprite.Sprite):
        def __init__(self):
             pygame.sprite.Sprite.__init__(self)            #init-Инициализирует игру и создает объект экрана
             self.image = pygame.image.load("player_front.png")   #загрузка изображения лыжника в положении "вперед"
             self.rect=self.image.get_rect()
             self.rect.center=[320,100]      #определяет координаты центра
             self.angle=0                #угол равен 0
        def turn(self,direction):   #функция поворота направо принимает
            self.angle=self.angle+direction  #угол равен,угол+направление движения
            if self.angle < -2: self.angle = -2 # если угол меньше -2,то угол равен 2
            if self.angle > 2: self.angle = 2  #усли угол больше 2,то угол равен 2
            center = self.rect.center   #оординаты центра
            self.image = pygame.image.load(skier_images[self.angle])   #загрузка лыжника взависимости от угла
            self.rect = self.image.get_rect()
            self.rect.center=center
            speed = [self.angle, 6 - abs(self.angle)* 1]
            return speed
        def move(self,speed):                               
            self.rect.centerx = self.rect.centerx + speed[0]     #centerx-перемещает центр по оси x
            if self.rect.centerx < 20: self.rect.centerx = 20
            if self.rect.centerx > 620: self.rect.centerx = 620
    class  ObstacleClass(pygame.sprite.Sprite):              #Sprite-Спрайт для группировки
        def __init__(self, image_file, location, type):      #image — сохранение и загрузка изображений
            pygame.sprite.Sprite.__init__(self)
            self.image_file = image_file
            self.image = pygame.image.load(image_file)
            self.rect = self.image.get_rect()          # Rect – прямоугольные области, имеющие координаты, длину и ширину.
            self.rect.center = location                # get_rect() применяется без аргументов, для его верхнего левого угла устанавливаются координаты(0, 0)
            self.type = type
            self.passed = False
        def update(self):
            self.rect.centery -= speed[1]
            if self.rect.centery < -32:
                self.kill()
    def create_map():             #cоздание карты
        locations = []
        for i in range (10):
            row = random.randint(0,9)
            col = random.randint(0,9)
            location = [col * 64 + 20, row * 64 + 20 + 740]    #определяет положение припятствий
            if not (location in locations):
                locations.append(location)
                type = random.choice(["tree", "flag", "rock" , "boost" , "slow" , "coin" ])       #cлучайное появление деревьев или флажков
                if type == "tree": img = "tree.jpg"     #если появилось дерево,загрузка нужного изображения
                elif type == "flag": img = "flag.png"
                elif type == "rock": img = "rock.png"
                elif type == "boost" : img = "boost.png"
                elif type == "slow" : img = "slow.png"
                elif type == "coin" : img = "coin.png"
                obstacle =  ObstacleClass(img, location, type)
                obstacles.add(obstacle)
    def animate():
        screen.fill([255, 255, 255])
        obstacles.draw(screen)
        screen.blit(skier.image, skier.rect)
        screen.blit(score_text, [10, 10])
        pygame.display.flip()
    pygame.init()
    pygame.mixer.music.load('Test.mp3')
    pygame.mixer.music.play()
    screen = pygame.display.set_mode([640,640])    #display — управление окном или экраном
    clock = pygame.time.Clock()             #time — управление таймерами
    skier = SkierClass()
    speed = [0, 6]
    obstacles = pygame.sprite.Group()         #Group-Группа объектов
    map_position = 0
    points = count_points
    coins = int (0)
    create_map()
    font = pygame.font.Font(None, 50)       #font — создание и отображение шрифтов TrueType
    running = True
    while running:

        clock.tick(60)
        for event in pygame.event.get():    #event — управление событиями и очередью событий
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a: #key — управление клавиатурой
                    speed = skier.turn(-2)  
                    
                elif event.key == pygame.K_d:
                    speed = skier.turn(2)

                elif event.key == pygame.K_w :
                     speed = [0 , 9]

                elif event.key == pygame.K_s :
                    speed = [0 , 3 ] 

                elif event.key == pygame.K_w and event.key == pygame.K_a :
                    speed = [ 0 , 6 ] and skier.turn (-2)

                elif event.key == pygame.K_w and event.key == pygame.K_d :
                    speed = [ 0 , 6 ] and skier.turn (2)

                elif event.key == pygame.K_s and event.key == pygame.K_a :
                    speed = [ 0 , 3 ] and skier.turn (-2)

                elif event.key == pygame.K_s and event.key == pygame.K_d :
                    speed = [ 0 , 3 ] and skier.turn (2)




        skier.move(speed)
        map_position += speed[1]
        
        if map_position >=640:
            create_map()
            map_position = 0
        hit = pygame.sprite.spritecollide(skier, obstacles, False)
        if hit:
            if hit[0].type == "tree" and  not hit[0].passed:
                points = points - 150
                if coins > 0 : coins = coins - 1
                skier.image = pygame.image.load("boom.png")
                animate()
                pygame.time.delay(1000)
                skier.image = pygame.image.load("player_front.png")
                skier.angle = 0
                speed = [0, 6]
                hit[0].passed = True
            elif hit[0].type == "rock" and not hit [0].passed:
                points = points - 300
                if coins > 0 : coins = coins - 1
                skier.image = pygame.image.load("boom.png")
                animate()
                pygame.time.delay(1000)
                skier.image = pygame.image.load("player_front.png")
                skier.angle = 0
                speed = [0, 6]
                hit[0].passed = True
            elif hit[0].type == "flag" and not hit [0].passed:
                points +=200
                hit[0].kill()

            elif hit[0].type == "boost" and not hit [0].passed :
                speed = [0 , 15]
                hit[0].kill ()

            elif hit[0].type == "slow" and not hit [0].passed :
                speed = [0 , 1]
                hit[0].kill()

            elif hit[0].type == "coin" and not hit [0].passed :
                coins = coins + 1
                hit[0].kill()
                if coins == 10 :
                    points = points + 500
                    coins = 0

                
        obstacles.update()
        score_text = font.render("Score: " +str(points)  +"                     Coins : "  + str (coins), 1, (0, 0, 0))
        animate()
        points1=points
        f = open('data', 'wb')
        pickle.dump(points1,f)
        f.close()
    pygame.quit()

main_menu ()
    
