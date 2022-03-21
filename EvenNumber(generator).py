def evennumber(n):
    i=1
    while n:
        yield 2*i
        i+=1
        n-=1
it= evennumber(10)
even_list=[]
while True:
    try:
        even_list.append(next(it))
    except StopIteration:
        break

print(even_list)
