from random import sample

list = sample(range(-100, 100), 30)
print(f"Generated list: {list}\n")

max_elem = (max(list), list.index(max(list)))

print(f"Max element: {max_elem[0]}\t\tindex:{max_elem[1]}\n")

for i in range(29):
  if list[i]<0 and list[i+1]<0:
    print("Numbers : " + str(list[i]) + " and " + str(list[i+1]))
