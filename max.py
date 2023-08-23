'''x=[1,12,3,-8,5,6]
m=x[0]
for y in x[1:]:
    if m<y:
        m=y
print(m)'''

#-------------------prime no:
'''l1=[3,7,3,6,8,3,9]
c=0
for i in l1:
    f=0
    for j in range(2,i):
        if(i%j==0):
            f=1
            break
    if(f==0):
        c+=1
        print("prime no:",i)
print("total",c)            '''

#vowels
'''
n="RAJESH"
c=0
for i in n:
    if i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        c+=1
        print(i)
print(c)
'''
#duplicate 
n="RAAJEESH"
for i in n:
    if(n[i]==n[i+1])