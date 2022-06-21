import glfw
from OpenGL.GL import *
import numpy as np

def uniform_scale(M):
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    # draw cooridnate
    glBegin(GL_LINES)
    glColor3ub(255, 0, 0)
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([1.,0.]))
    glColor3ub(0, 255, 0)
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([0.,1.]))
    glEnd()

    # draw triangle - p'=Mp
    glBegin(GL_TRIANGLES)
    glColor3ub(255, 255, 255)
    glVertex2fv(M @ np.array([0.0,0.5]))
    glVertex2fv(M @ np.array([0.0,0.0]))
    glVertex2fv(M @ np.array([0.5,0.0]))
    glEnd()


def render(M):
    uniform_scale(M)

# def main():
#     if not glfw.init():
#         return

#     window = glfw.create_window(640, 640, "2D Trans", None, None)
#     if not window:
#         glfw.terminate()
#         return

#     glfw.make_context_current(window)

#     while not glfw.window_should_close(window):
#         glfw.poll_events()

#         M = np.array([
#             [2., 0.],
#             [0., 2.]
#         ])

#         render(M)

#         glfw.swap_buffers(window)
    
#     glfw.terminate()

# Animation

def main():
    if not glfw.init():
        return
    window = glfw.create_window(640,640,"2D Trans", None,None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)

    # set the number of screen refresh to wait before calling glfw.swap_buffer().
    # if your monitor refresh rate is 60Hz, the while loop is repeated every 1/60 sec
    glfw.swap_interval(1)

    while not glfw.window_should_close(window):
        glfw.poll_events()

        # get the current time, in seconds
        t = glfw.get_time()

        s = np.sin(t)
        M = np.array([
            [s , 0.],
            [0., s ]
        ])

        render(M)

        glfw.swap_buffers(window)
    glfw.terminate()

if __name__ == "__main__":
    main()