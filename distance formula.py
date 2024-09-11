y1 = 0
x2 = 0
y2 = 0

xdif = 0
ydif = 0
dist = 0
mult = 0





def distance_formula(x1, y1, x2, y2):

    xdif = x2 - x1
    
    ydif = y2 - y1
    
    mult = xdif * xdif + ydif * ydif
    
    dist = math.sqrt(mult)
    
    print("The distance is", dist)
    
distance_formula(0, 0, 6, 8) 

