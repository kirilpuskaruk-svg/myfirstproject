import turtle

turtle.title("Сходинки")
turtle.bgcolor("white")

st = turtle.Turtle()
st.color("blue") 
st.pensize(3) 
st.speed(3) 
width = 40
height = 30
steps = 5

for i in range(steps):
    st.forward(width)
    st.left(90)
    st.forward(height) 
    st.right(90)
turtle.done()