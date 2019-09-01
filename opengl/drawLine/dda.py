from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def drawFunc():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glOrtho(0.0, 1.0, 0.0, 1.0, -1.0, 1.0)

    # 设置点大小
    glPointSize(5)
    # 只绘制端点
    glBegin(GL_POINTS)
    # 第一个点
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.25, 0.25, 0)
    # 第二个点
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.75, 0.25, 0)
    # 第三个点
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.75, 0.75, 0)
    # 第四个点
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.25, 0.75, 0)
    glEnd()

    glFlush()


if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowSize(400, 400)
    glutCreateWindow(b"First")
    glutDisplayFunc(drawFunc)
    glutMainLoop()