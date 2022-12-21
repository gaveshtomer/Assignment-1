import math 
while(d<=345):
    r=math.radians(d)
    sine=round(math.sin(r),4)
    cosine=round(math.cos(r),4)
    print(d , sine , cosine)
d=d+15
