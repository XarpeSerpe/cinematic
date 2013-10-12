import math
x_0 = 0.0 #m
y_0 = 0.0 #m
v_0x = 20.0 #m/s
v_0y = 30.0 #m/s
g =  -9.8 #m/s^2
m = 10.0 #kg
x = 0.0
y = 0.0
v_x = 0.0
v_y = 0.0
v = math.sqrt(v_x*v_x+v_y*v_y)
#Tiempo mAximo de vuelo
t_max = ( v_0y + ( v_0y ** 2 + 2 * g * y_0 ) ** 0.5 ) / g
#Altura mAxima en el vuelo
y_max = y_0 + v_0y * t_max/2 - 1 / 2 * g * (t_max/2)**2
#Distancia mAxima recorrida durante el vuelo
x_max = x_0 + v_0x * t_max

#Calculus of size event
width_event = x_max -x_0
height_event = y_max-y_0
#Decide who is limit


    
