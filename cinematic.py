x_0 = 0
y_0 = 0
v_0x = 35
v_0y = 75
g =  -9.8

t_max = ( v_0y + ( v_0y ** 2 + 2 * g * y_0 ) ** 0.5 ) / g
y_max = y_0 + v_0y * t_max/2 - 1 / 2 * g * (t_max/2)**2
x_max = x_0 + v_0x * t_max
x, y = 0, 0
t = 0


#Calculus of size event
width_event = x_max -x_0
height_event = y_max-y_0
#Decide who is limit

    
