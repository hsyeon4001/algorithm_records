import turtle as t

# 사각나선
def spiral(sp_len):
    if sp_len <= 5:
        return
    t.forward(sp_len)
    t.right(90)
    spiral(sp_len - 5)

t.speed(0)
spiral(200)
t.hideturtle()
t.done()

#시에르핀스키 삼각형
def tri(tri_len):
    if tri_len <= 10:
        for i in range(0, 3):
            t.forward(tri_len)
            t.left(120)
        return
    new_len = tri_len / 2
    tri(new_len)
    t.forward(new_len)
    tri(new_len)
    t.backward(new_len)
    t.left(60)
    t.forward(new_len)
    t.right(60)
    tri(new_len)
    t.left(60)
    t.backward(new_len)
    t.right(60)

t.speed(0)
tri(160)
t.hideturtle()
t.done()

# 나무
def tree(br_len):
    if br_len <= 5:
        return
    new_len = br_len * 0.7
    t.forward(br_len)
    t.right(20)
    tree(new_len)
    t.left(40)
    tree(new_len)
    t.right(20)
    t.backward(br_len)

t.speed(0)
t.left(90)
tree(70)
t.hideturtle()
t.done()

# 눈꽃
def snow_line(snow_len):
    if snow_len <= 10:
        t.forward(snow_len)
        return
    new_len = snow_len / 3
    snow_line(new_len)
    t.left(60)
    snow_line(new_len)
    t.right(120)
    snow_line(new_len)
    t.left(60)
    snow_line(new_len)

t.speed(0)
snow_line(150)
t.right(120)
snow_line(150)
t.right(120)
snow_line(150)
t.hideturtle()
t.done()