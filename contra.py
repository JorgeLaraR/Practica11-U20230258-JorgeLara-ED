import random

def contra(longitud):
  caracteres = "arriba7"
  contras = ""
  
  for _ in range(longitud):
    contras += caracteres[random.randint(0, len(caracteres) - 1)]
  return contras