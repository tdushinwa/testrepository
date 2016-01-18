#! /usr/bin/python
# encoding: utf-8
# とりあえず2D図形を書く練習

from sys import argv
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


# 将来的には汎用性を高めるため
# 各ノードのサイズ・座標を入れれば描画するという関数を作る
# class argument():

#     def __init__(self, size, x, y):
#         self.size = size
#         self.x = x
#         self.y = y


class openGLInit():

    def initGL():
        # 背景色を初期化
        glClearColor(1.0, 1.0, 1.0, 1.0)

    def resize(w, h):
        glViewport(0, 0, w, h)
        glLoadIdentity()
        glOrtho(-w / 480.0, w / 480.0, -h / 480.0, h / 480.0, -1.0, 1.0)


class display():

    # sizeは大きさの比率, XYは座標
    def drawIndividual():
        import math
        size = 0.7
        X, Y = 0, 0
        glClear(GL_COLOR_BUFFER_BIT)

        glColor3d(0, 0, 0)
        # 四角形の部分
        glBegin(GL_QUADS)

        # 本体
        glVertex2d((X + -0.7) * size, (Y + 0.7) * size)
        glVertex2d((X + 0.7) * size, (Y + 0.7) * size)

        glVertex2d((X + 0.7) * size, (Y + -0.7) * size)
        glVertex2d((X + -0.7) * size, (Y + -0.7) * size)

        # 親への鍵
        glVertex2d((X + -0.1) * size, (Y + 0.7) * size)
        glVertex2d((X + -0.1) * size, (Y + 0.9) * size)

        glVertex2d((X + 0.1) * size, (Y + 0.9) * size)
        glVertex2d((X + 0.1) * size, (Y + 0.7) * size)

        glEnd()

        # 親への鍵の凸部分(三角形)
        glBegin(GL_TRIANGLES)
        glVertex2d((X + -0.1) * size, (Y + 0.9) * size)
        glVertex2d((X + 0.1) * size, (Y + 0.9) * size)
        glVertex2d((X + 0) * size, (Y + 1.0) * size)
        glEnd()

        # 婚姻関係の鍵(半円)
        glBegin(GL_TRIANGLE_FAN)
        glVertex2d((X + -0.7) * size, (Y + 0) * size)  # 中心点
        n = 100  # 円の精度
        r = 0.15  # 半径
        for i in range(n + 1):
            y = (i / n) * r * 2 - r
            x = math.sqrt(r ** 2 - y ** 2)
            glVertex2d((-x + -0.7) * size, y * size)
        glEnd()
        glFlush()  # 描画

    def main():
        glutInit(argv)
        glutInitDisplayMode(GLUT_RGBA)
        glutInitWindowSize(640, 480)
        glutInitWindowPosition(100, 100)

        glutCreateWindow('WHIteBasE draw test')
        openGLInit.initGL()
        glutDisplayFunc(display.drawIndividual)
        glutReshapeFunc(openGLInit.resize)

        glutMainLoop()

if __name__ == '__main__':
    display.main()
