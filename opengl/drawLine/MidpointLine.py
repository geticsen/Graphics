from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
width,height=300,300

def drawPoint(x,y):
    # 只绘制端点
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(x / width, y / height, 0)

def LineMP():
    x1, y1, x2, y2 = 0, 0, 100, 100
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glOrtho(0.0, 1.0, 0.0, 1.0, -1.0, 1.0)
    # 设置点大小
    glPointSize(1)
    glBegin(GL_POINTS)
    if x1 < x2 and y1 < y2:
        a = y1-y2
        b = x2-x1
        x ,y = x1,y1
        d = 2 * a+b
        da1 = 2 * a
        da2 = 2 * (a+b)
        drawPoint(x,y)
        for i in range(x,x2):
            if d < 0:
                x += 1
                y += 1
                d += da2
            else:
                x += 1
                d += da1
            drawPoint(x, y)
    elif x1>x2 and y1>y2:
        a = y2 - y1
        b = x1 - x2
        x ,y = x2,y2
        d = 2 * a + b
        da1 = 2 * a
        da2 = 2 * (a + b)
        drawPoint(x, y)
        for i in range(x, x2):
            if d < 0:
                x+=1
                y+=1
                d += da2
            else:
                x+=1
                d += da1
                drawPoint(x, y)
    elif x1>x2 and y1<y2:
        a = -y2
        b = x1 - x2
        x ,y = 0,0
        d = 2 * a + b
        da1 = 2 * a
        da2 = 2 * (a + b)
        drawPoint(x1-x, y+y1)
        for i in range(x, b):
            if d < 0:
                x+=1
                y+=1
                d += da2
            else:
                x+=1
                d += da1
                drawPoint(x1 - x, y + y1)
    elif x1<x2 and y1>y2:
        a = -y1
        b = x2 - x1
        x ,y = 0,0
        d = 2 * a + b
        da1 = 2 * a
        da2 = 2 * (a + b)
        drawPoint(x2 - x, y + y2)
        for i in range(x, b):
            if d < 0:
             x+=1
             y+=1
             d=d+da2
            else:
             x+=1
             d += da1
             drawPoint(x2 - x, y + y2)
    glEnd()
    glFlush()
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowSize(width,height)
    glutCreateWindow("LineMP")
    glutDisplayFunc(LineMP)
    #glutIdleFunc(LineMP)
    glutMainLoop()
main()