def hello(name):
    print('hello', name)

def pack(a, b, c):
    return [a, b, c]


def eat_lunch(my_lst):
  if len(my_lst) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(my_lst)):
      if i == 0:
        print(f"First I eat {my_lst[0]}")
      else:
        print(f"Next I eat {my_lst[i]}")

hello("Adam")
print(pack("b","b","c"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(['a sandwich', 'an apple', 'chips'])
