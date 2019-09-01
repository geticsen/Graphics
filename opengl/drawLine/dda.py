from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class DrawLine:
    width = 300
    height = 400
    point_size = 5
    x0 , x1 , y0 , y1 = 0 , 0 , 0 , 0

    def __init__(self,width,height,point_size):
        self.height = height
        self.width = width
        self.point_size = point_size

    def DDA(self,x0,y0,x1,y1):
        self.x0,self.y0,self.x1,self.y1 = x0,y0,x1,y1
        glutInit()
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
        glutInitWindowSize(self.width, self.height)
        glutCreateWindow("DAA")
        glutDisplayFunc(self.DAAImplement)
        glutMainLoop()
    def DAAImplement(self):
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClear(GL_COLOR_BUFFER_BIT)
        glOrtho(0.0, 1.0, 0.0, 1.0, -1.0, 1.0)
        # 设置点大小
        glPointSize(self.point_size)
        glBegin(GL_POINTS)
        if self.x0 > self.x1:
            self.x0, self.x1 = self.x1, self.x0
            self.y0, self.y1 = self.y1, self.y0
        # 图形初始化
        delta_x = self.x1 - self.x0
        delta_y = self.y1 - self.y0
        d = 0
        if delta_x == 0:
            k = 999999999
        else:
            k = delta_y / delta_x
        x = round(x0)
        y = round(y0)
        # DDA算法
        if k > -1 and k < 1:
            # X 最大位移
            while True:
                if x > self.x1:
                    break
                self.drawPoint(x, y, )
                x = x + 1
                y = y + k
        elif k >= 1:
            # Y 最大位移
            while True:
                if y > self.y1:
                    break
                self.drawPoint(x, y, )
                y = y + 1
                x = x + 1 / k
        else:
            while True:
                if y < self.y1:
                    break
                self.drawPoint(x, y,)
                y = y - 1
                x = x - 1 / k
        glEnd()
        glFlush()
    def drawPoint(self,x,y):
        # 只绘制端点
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(x/self.width, y/self.height, 0)




# 将一行的字符串分割并转化为数字
width, height= map(int, input("输入画布的宽高: ").split(' '))
x0, y0, x1, y1= map(int, input("输入直线的两点坐标: ").split(' '))
drawLine = DrawLine(width, height, 1)
drawLine.DDA(x0, y0, x1, y1)
print("111111111111")