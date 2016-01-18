#! /usr/bin/python
# encoding: utf-8

import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


window = 0
X_AXIS = 0.0
Y_AXIS = 0.0
Z_AXIS = 0.0


class OpenGLInit():

    def initGL(w, h):
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0)

        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, float(w) / float(h), 0.1, 100.0)

        glMatrixMode(GL_MODELVIEW)


class MainWindow():

    def draw():
        global X_AXIS, Y_AXIS, Z_AXIS
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glLoadIdentity()
        glTranslatef(0.0, 0.0, -6.0)

        glRotate(X_AXIS, 1.0, 0.0, 0.0)
        glRotate(Y_AXIS, 0.0, 1.0, 0.0)
        glRotate(Z_AXIS, 0.0, 0.0, 1.0)

        # Draw Cube
        glBegin(GL_QUADS)

        glColor(1.0, 0.0, 0.0)
        glVertex3f(1.0, 1.0, -1.0)
        glVertex3f(-1.0, 1.0, -1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f(1.0, 1.0, 1.0)

        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(1.0, -1.0, 1.0)
        glVertex3f(-1.0, -1.0, 1.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(1.0, -1.0, -1.0)

        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(1.0, 1.0, 1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f(-1.0, -1.0, 1.0)
        glVertex3f(1.0, -1.0, 1.0)

        glColor3f(1.0, 1.0, 0.0)
        glVertex3f(1.0, -1.0, -1.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(-1.0, 1.0, -1.0)
        glVertex3f(1.0, 1.0, -1.0)

        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f(-1.0, 1.0, -1.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(-1.0, -1.0, 1.0)

        glColor3f(1.0, 0.0, 1.0)
        glVertex3f(1.0, 1.0, -1.0)
        glVertex3f(1.0, 1.0, 1.0)
        glVertex3f(1.0, -1.0, 1.0)
        glVertex3f(1.0, -1.0, -1.0)

        glEnd()
        glFlush()

        X_AXIS -= 0.30
        Y_AXIS -= 0.30
        glutSwapBuffers()

    def main():
        global window
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(640, 480)
        glutInitWindowPosition(200, 200)

        window = glutCreateWindow('PyOpenGL Cube Test')
        OpenGLInit.initGL(640, 480)
        glutDisplayFunc(MainWindow.draw)
        glutIdleFunc(MainWindow.draw)
        glutMainLoop()

if __name__ == '__main__':
    MainWindow.main()
