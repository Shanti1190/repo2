#age.py
try:
  age=int(input("enter your age:"));
  if age>=18:
    print("You are eligible");
  else:
    print("You are not eligible");
except ValueError:
  print(Enter a valid age");
