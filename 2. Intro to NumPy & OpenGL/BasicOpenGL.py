import glfw
from OpenGL.GL import *

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

def render():
    smallTriangle()

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