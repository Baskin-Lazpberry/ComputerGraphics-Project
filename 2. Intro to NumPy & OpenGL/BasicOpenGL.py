import glfw
from OpenGL.GL import *
import numpy as np

def triangle():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glBegin(GL_TRIANGLES)
    glVertex2f(0.0, 1.0)
    glVertex2f(-1.0, -1.0)
    glVertex2f(1.0, -1.0)
    glEnd()

def smallTriangle():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glBegin(GL_TRIANGLES)
    glVertex2f(0.0, 0.5)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glEnd()

def primitiveTypes():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    #glBegin(GL_POINTS)
    #glBegin(GL_LINES)
    #glBegin(GL_LINE_STRIP)
    glBegin(GL_LINE_LOOP)

    glVertex2f(0.0, 0.5)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glEnd()

def rainbowTriangle():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.0, 1.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(-1.0, -1.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(1.0, -1.0)
    glEnd()

def redTriangle():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.0, 1.0)
    glVertex2f(-1.0, -1.0)
    glVertex2f(1.0, -1.0)
    glEnd()

def redTriangle_otherForm():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glBegin(GL_TRIANGLES)
    glColor3ub(255, 0, 0)
    glVertex2fv((0.0, 1.0))
    glVertex2fv([-1.0, -1.0])
    glVertex2fv(np.array([1.0, -1.0]))
    glEnd()

def render():
    redTriangle_otherForm()

def main():
    if not glfw.init():
        return

    window = glfw.create_window(640, 480, "Hello world", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glfw.poll_events()

        render()

        glfw.swap_buffers(window)
    
    glfw.terminate()

if __name__ == "__main__":
    main()