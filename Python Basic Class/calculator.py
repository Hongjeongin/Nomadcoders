def calculator(num1, num2, operator):
  return_result = ""
  result = 0

  try:
    num1 = float(num1)
  except:
    return "(Error) - Please enter a number num1!!!"

  try:
    num2 = float(num2)
  except:
    return "(Error) - Please enter a number num2!!!"

  if operator == "+":
    result = num1 + num2
  elif operator == "-":
    result = num1 - num2
  elif operator == "*":
    result = num1 * num2
  elif num2 == 0:
    return_result = "Can't use num2 zero on division!!!"
  elif operator == "/":
    return_result = f"Result: {num1 / num2}"
  else:
    return_result = "(Error) - Please enter an operation in [+, -, *, /, exit]!!!"

  if return_result != "":
    return return_result

  if result % 1 != 0:
    return_result = f"Result: {result}"
  else:
    return_result = f"Result: {int(result)}"

  return return_result


while (True):
  num1 = input("Choose a number(first number):\n")
  num2 = input("Choose another number(second number):\n")

  print("Choose an operation:")
  print("\tOptions are: + , - , * or /.")
  print("\tWrtie 'exit' to finish.")

  operator = input()
  if operator == "exit":
    break

  result = calculator(num1, num2, operator)
  print(result)
