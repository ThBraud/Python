import sys
import math
import matplotlib.pyplot as plt

DRAW_NSTEPS = 10240

class Paint:
    def __init__(self, width=1000, height=1000):
        self.canvas = []
        for line in range(height):
            line_data = list()
            for col in range(width):
                line_data.append([255, 255, 255])
            self.canvas.append(line_data)

    def set_pixel(self, x, y, r=0, g=0, b=0):
        if x < 0 or y < 0:
            return
        if y >= len(self.canvas):
            return
        if x >= len(self.canvas[y]):
            return

        self.canvas[y][x] = [r, g, b]

    def show(self):
        plt.gca().invert_yaxis()
        plt.imshow(self.canvas)
        plt.show()
        sys.exit(0)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, autre):
        s =  (autre.x - self.x) ** 2
        s += (autre.y  - self.y) ** 2
        return math.sqrt(s)

    def draw(self, paint):
        paint.set_pixel(self.x, self.y)

class Ligne:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_length(self):
        return self.a.dist(self.b)

    def draw(self, paint):
        dx = (self.b.x - self.a.x) / DRAW_NSTEPS
        dy = (self.b.y - self.a.y) / DRAW_NSTEPS

        x = float(self.a.x)
        y = float(self.a.y)
        for step in range(DRAW_NSTEPS):
            paint.set_pixel(int(round(x, 0)), int(round(y, 0)))
            x += dx
            y += dy

paint = Paint()

#### Début du sujet
### Geometric objects here
class parallelogramme:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c 
        self.d_x = self.c.x +(self.b.x - self.a.x) 
        self.d_y = self.c.y +(self.b.y - self.a.y)
        self.d = Point(self.d_x,self.d_y)
        d =self.d

        self.ab = Ligne(a,b)
        self.ac = Ligne(a,c)
        self.bd = Ligne(b,d)
        self.dc = Ligne(d,c)
    
    def draw(self, paint):
        self.ab.draw(paint)
        self.ac.draw(paint)
        self.dc.draw(paint)
        self.bd.draw(paint)

a=Point(100, 250)
b=Point(400, 400)
c=Point(200, 250)
fido=parallelogramme(a,b,c)

fido.draw(paint)


class Rectangle(parallelogramme):
    def __init__(self,a,b,AC):
        ab = a.dist(b)
        delta_y = b.y -a.y
        delta_x =b.x -a.x
        c_x = a.x + (delta_y / ab) * AC 
        c_y = a.x - (delta_x/ ab) * AC
        c=Point(c_x,c_y)
        parallelogramme.__init__(self,a,b,c)
r=Rectangle(Point(100,100), Point (100,400), 500)
r.draw(paint)



class Carre (Rectangle):
     def __init__(self,a,b,AC):
        ab = a.dist(b)
        delta_y = b.y -a.y
        delta_x =b.x -a.x
        c_x = a.x + (delta_y / ab) * AC 
        c_y = a.x - (delta_x/ ab) * AC
        c=Point(c_x,c_y)
        Rectangle.__init__(self,a,b,AC)
c=Carre(Point(100,100), Point (100,200), 100)
c.draw(paint)

class Triangle (): 
    def __init__(self,a,b,c):
        self.ab = Ligne (a,b)
        self.ac = Ligne (a,c)
        self.bc = Ligne (b,c)
        
    def draw(self, paint):
        self.ab.draw(paint)
        self.ac.draw(paint)
        self.bc.draw(paint)


t=Triangle(Point(200,100),Point(100,200),Point (250,250))
t.draw(paint)



class TriangleRectangle (Triangle):
    def __init__ (self,a,b,angle):
        self.ab = Ligne (a,b)
        ab = a.dist(b)
        self.angle = 45
        bc = ab / math.cos(45)
        ac = bc * math.sin(45)
        delta_y = b.y -a.y
        delta_x =b.x -a.x
        c_x = a.x + (delta_y / ab) * ac
        c_y = a.x - (delta_x/ ab) * ac
        c=Point(c_x,c_y)
        Triangle.__init__(self,a,b,c)
        tr=TriangleRectangle(Point(400.100),Point (550,200))
        tr.draw(paint)

        
###     
paint.show()