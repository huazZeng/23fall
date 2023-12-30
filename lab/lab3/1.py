import random
a=[0,0,0,0,0,0,0]
for i in range(1,10000):
    a[random.randint(0,6)]+=1
print(a)