def switcher(number):
  
  # Use dicionário (do Módulo 3) para armazenar switch cases
  # Se não for encontrado, o get() será o valor padrão
  return {
    '0':"Entered 0",
    '1':"Entered 1",
    '2':"Entered 2",
    '3':"Entered 3",
    '4':"Entered 4",
    '5':"Entered 5",
    '6':"Entered 6",
    '7':"Entered 7",
    '8':"Entered 8",
    '9':"Entered 9",
  }.get(number,"Invalid number!")    

# input() lê uma entrado do usuário de stdin
number = input("Dial a number")
if int(number) == 0:
  print('Entered 0')
elif int(number) == 1:
  print("Entered 1")
elif int(number) == 2:
  print("Entered 2")
elif int(number) == 3:
  print("Entered 3")  
elif int(number) == 4:
  print("Entered 4")
elif int(number) == 5:
  print("Entered 5")
elif int(number) == 6:
  print("Entered 6")
elif int(number) == 7:
  print("Entered 7")
elif int(number) == 8:
  print("Entered 8")  
elif int(number) == 9:
  print("Entered 9")
else:
  print("Invalid number!")

number = input("Dial a number")
switcher(number)

