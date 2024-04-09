from queue import PriorityQueue

p = PriorityQueue();
p.put('z',200)
p.put('b',2)
p.put('a',1)
p.put('r',5)
p.put('m',4)
p.put('l',3)

x = 1
if x in p.queue:
    print(x);
else:
    print("not")

for x in p.queue:
    print(x)




