import py5

mode = 0

def key_pressed():
    global mode
    if py5.key >= '0' and py5.key <= '9':
        mode = int(py5.key) - int('0')
        print(mode)

def setup():
    py5.size(500, 500)  

def draw():
    global mode
    print(mode)
    if mode == 0:
        py5.circle(py5.mouse_x, py5.mouse_y, 10)
    elif mode == 1:
        py5.rect(py5.mouse_x, py5.mouse_y, 10, 100)
    

py5.run_sketch()  
