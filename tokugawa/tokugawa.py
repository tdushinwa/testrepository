#! /usr/bin/python
# encoding: utf-8

from sys import argv
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class shogun(object):  # 将軍家各々のノード

    def __init__(self, name, parent, num):
        self.name = name
        self.parent = None
        self.num = num


class createFont():
    pass


def tree():  # Union-Findを使う
    parent = []


def glutPrint(x, y, font, text, r, g, b, a):
    glColor3f(1.0, 1.0, 1.0)
    glRasterPos2f(x, y)
    for ch in text:
        print(ch)
        glutBitmapCharacter(font, ord(ch))


class ogInit():  # openGLの初期化

    def init():
        glClearColor(0.0, 0.0, 0.0, 0.0)


class display():  # 描画

    def drawText():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        menu = u"おい"
        glutPrint(0.2, 0.2, GLUT_BITMAP_TIMES_ROMAN_24, menu, 1.0, 1.0, 1.0, 1.0)
        glFlush()

    def drawNord():
        glClear(GL_COLOR_BUFFER_BIT)

    def drawLine():
        glClear(GL_COLOR_BUFFER_BIT)

    def main():
        glutInit(argv)
        glutInitDisplayMode(GLUT_RGBA)
        glutInitWindowSize(640, 480)
        glutInitWindowPosition(100, 100)

        glutCreateWindow('tokugawa')
        ogInit.init()
        glutDisplayFunc(display.drawText)

        glutMainLoop()

if __name__ == '__main__':
    display.main()
