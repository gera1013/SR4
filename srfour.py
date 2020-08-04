from gl import Render, color
from obj import ObjFile 

r = Render(800, 1000)

r.glLoadObj('lowpolytree.obj', (400, 400, 0), (150, 150, 200))

r.glZBuffer()
r.glFinish()