import py5

def setup():
    py5.size(400, 400)
    

def draw():
    py5.background(255)    
    cx = py5.width / 2
    cy = py5.height / 2
    py5.ellipse(cx, cy, 100, 50)

    pass
    


py5.run_sketch()