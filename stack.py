import collections
stack=collections.deque()
print("select the options")
print("\n1-push the element \n2-pop the element \n3-display \n0-exit")
n=int(input("enter the size of stack"))
while  True:
  option=int(input("enter the option:"))
  if option==1:
    if n==len(stack):
      print("stack is full")
    else:
      stack.append(input("enter the value for push:"))
  elif option==2:
    if  not stack:
      print("stack is empty!")
    else:
      stack.pop()
  elif option==3:
    print(stack)
  elif option==0:
    break
  else:
    print("your choice was wrong plz enter the correct choice")
