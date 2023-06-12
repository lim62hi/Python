def sortirovka (*args,kluch):
    spisok=[]
    chet=[]
    nechet=[]
    for i in args:
        for p in i:
            if p not in spisok:
                spisok.append(p)
    if kluch == True:
        spisok.sort()         
    return(spisok)
x=[8,9,10,10,44,4,5]
y=[1,2,4,4,44,6,7,6]
z=[1,2,3,4,5]
f=sortirovka(x,y,z,kluch=True)
print(f)
