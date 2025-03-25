import mouse
import time
import random

print("a1")
time.sleep(3)
a1=mouse.get_position()
print(a1)

print("a2")
time.sleep(3)
a2=mouse.get_position()
print(a2)

print("a3")
time.sleep(3)
a3=mouse.get_position()
print(a3)

print("a4")
time.sleep(3)
a4=mouse.get_position()
print(a4)

print("continue")
time.sleep(3)
cont=mouse.get_position()
print(cont)

print("starting")
time.sleep(3)
while True:
    an=random.randint(1,4)
    if an==1:
        mouse.drag(a1[0],a1[1],a1[0],a1[1])
        mouse.click()
    elif an==2:
        mouse.drag(a2[0],a2[1],a2[0],a2[1])
        mouse.click()
    elif an==3:
        mouse.drag(a3[0],a3[1],a3[0],a3[1])
        mouse.click()
    else:
        mouse.drag(a4[0],a4[1],a4[0],a4[1])
        mouse.click()

    mouse.drag(cont[0],cont[1],cont[0],cont[1])
    mouse.click()

#mouse.drag(0,0,)