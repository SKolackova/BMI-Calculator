def main():
  hmotnost, vyska = otazka()
  print("Tvoje BMI je", hmotnost / (vyska * vyska))
  

def otazka():
  hmotnost = float(input("Zadej svoji váho v kilogramech: "))
  vyska = float(input("Zadej svoji výšku v metrech: "))
  return hmotnost, vyska

main()