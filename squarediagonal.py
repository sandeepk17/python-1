import math
s1=[]
s2=[]
s1.append(int(input()))
s1.append(int(input()))
tuple(s1)
s2.append(int(input()))
s2.append(int(input()))
tuple(s2)
length=math.sqrt(((s1[0]-s2[0])**2)+((s1[1]-s2[1])**2))
if(s1[1]==s2[1]):
    s3=[]
    s3.append(int(s1[0]))
    s3.append(int(s1[1]+length))
    s4=[]
    s4.append(int(s2[0]))
    s4.append(int(s2[1]+length))
elif(s1[0]==s2[0]):
    s3=[]
    s3.append(int(s1[0]+length))
    s3.append((int(s1[1])))
    s4=[]
    s4.appendint((s2[0]+length))
    s4.append(int(s2[1]))
print(tuple(s3))
print(tuple(s4))
diagonal=math.sqrt(length**2+length**2)
print(round(diagonal,2))
