import pygame
import random
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


#정육면체를 구성하는 요소에 대해 알아보자.
#정육면체는 이름처럼 여섯개의 면으로 구성되어있다.
#면은 꼭짓점과 변으로 구성되어있으므로 먼저 꼭짓점과 변을 정의해주자.


#정육면체는 총 8개의 꼭짓점으로 구성되어있다.
vertices = ((1, -1, -1), (1, 1, -1),
            (-1, 1, -1), (-1,-1,-1),
            (1, -1, 1), (1, 1, 1),
            (-1, -1, 1), (-1, 1, 1))

edges = ((0,1), (0,3), (0,4),
         (2,1), (2,3), (2,7),
         (6,3), (6,4), (6,7),
         (5,1), (5,4), (5,7))



surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

#R,G,B순서로 색을 나타낸다. 부동소수 형 (3f라던지..)는 0.0~1.0 사잇값으로
#색을 표현할 수 있다.
colors = (
        (1,0,0),
        (0,1,0),
        (0,0,1),
        (1,1,0),
        (1,0,1),
        (0,1,1),
        (1,0,0),
        (0,1,0),
        (0,0,1),
        (1,1,0),
        (1,0,1),
        (0,1,1)

    )

def drawCube():
    #glBegin 함수는 점이나 선을 정의할 때 필요한 함수다. 끝낼때는 glEnd()함수를
    #사용한다.
    #점 : GL_POINTS
    #선 : GL_LINES
    #삼각형을 그릴 때는 GL_TRIANGLES
    #사각형을 그릴 때는 GL_QUADS
    #다각형을 그릴 때는 GL_POLYGON을 사용한다.
    #
    glBegin(GL_QUADS)
    x = 0
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x+=1
            #
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
        
    glEnd()

    
    #OpenGL에게 직선을 그릴 것이라고 알려준다.
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def myOpenGL():
    pygame.init()
    #지금 이 display는 튜플형이야. 바꿀 수 없는 자료형.
    #자세한건 파이썬의 array, dictionary, tuple의 차이를 알아보길.
    
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)


    
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    
    glTranslatef(random.randrange(-5,5),random.randrange(-5,5), -40)

    x = glGetDoublev(GL_MODELVIEW_MATRIX)
    print(x)

    objectPassed = False

    while not objectPassed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #방향키가 눌려져 있는지 확인하는 조건문이야.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-1,0,0)
                    x = glGetDoublev(GL_MODELVIEW_MATRIX)
                    print(x)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(1,0,0)
                    x = glGetDoublev(GL_MODELVIEW_MATRIX)
                    print(x)
                if event.key == pygame.K_UP:
                    glTranslatef(0,1,0)
                    x = glGetDoublev(GL_MODELVIEW_MATRIX)
                    print(x)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0,-1,0)
                    x = glGetDoublev(GL_MODELVIEW_MATRIX)
                    print(x)

##            #MOUSEBUTTONDOWN은 마우스 스크롤이 움직이고 있다는 뜻이다.
##            if event.type == pygame.MOUSEBUTTONDOWN:
##                if event.button == 4:
##                    glTranslatef(0,0,1)
##                if event.button == 5:
##                    glTranslatef(0,0,-1)

                    
        x = glGetDoublev(GL_MODELVIEW_MATRIX)
        print(x)

        camera_x = x[3][0]
        camera_y = x[3][1]
        camera_z = x[3][2]

        if camera_z < 0:
            objectPassed = True
        

        glRotate(1, 3, 1, 1)

        

        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glTranslatef(0,0,0.001)
        
        drawCube()
        pygame.display.flip()
        pygame.time.wait(10)

while True:
    myOpenGL()
