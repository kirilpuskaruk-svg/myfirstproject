from ursina import * 
from ursina.color import orange
from ursina.prefabs.first_person_controller import FirstPersonController
app=Ursina() # підключаємо вікно ігри
player = FirstPersonController(
    model="sphere",
    color=color.orange,
    scale=(1,2,1),
    texture="brick",
    texture_scale=(1024,1024),
    position=(0,5,0),
    speed = 10,
    mouse_sensitivity = Vec2(40,40), # Чутливість мишки (X,Y)
    gravity = 0.2 ,
    jump_height = 10, # висота стрибка
    jump_duration = 10, # тривалість стрибка 
    collider = "box", # форма зіткнення
    height = 2, # висота камери 
    camera_pivot_y=0.5 # зміщення камери вгору/вниз
)
ground=Entity(model="plane",scale=50,texture="grass",texture_scale=(50,50),collider="box")
wall = Entity(model="cube",scale=(5,10,1),color=color.blue,collider="box",position=(4,1,25),texture="brick",texture_scale=(50,10))
wall = Entity(model="cube",scale=(5,10,1),color=color.orange,collider="box",position=(0,1,-25),texture="brick",texture_scale=(50,10))
wall = Entity(model="cube",scale=(3,10,45),color=color.yellow,collider="box",position=(-9,3,0),texture="brick",texture_scale=(20,10))
crosshair = Entity(
    model="quad",
    color=color.white,
    scale=0.020,
    rotation_z=45,
    parent=camera.ui
)
round=Entity(model="plane",scale=50,texture="grass",texture_scale=(50,50),collider="box")
wall = Entity(model="cube",scale=(4,10,1),color=color.red,collider="box",position=(3,1,-25),texture="brick",texture_scale=(5,10))
wall = Entity(model="cube",scale=(1,10,50),color=color.dark_gray,collider="box",position=(5,1,0),texture="brick",texture_scale=(5,10))
wall = Entity(model="cube",scale=(3,10,45),color=color.pink,collider="box",position=(-2,1,0),texture="brick",texture_scale=(5,10))


app.run()# запуск гри