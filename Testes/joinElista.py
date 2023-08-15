x,y=map(int,input().split())
lista=[]
for a in range(1,y):
    for i in range(len(lista)<x):
        i=a
        lista.append(i)
        if len(lista)==x:
            lista1 = " ".join(lista)
            print(lista1)
            del lista[::]
    i=a+1