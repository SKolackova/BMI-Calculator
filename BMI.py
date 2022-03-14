def main():
  hmotnost, vyska = otazka()
  BMI = hmotnost / (vyska * vyska)
  if BMI <= 18.5:
    print("Tvoje BMI je", BMI, ". Máš podváhu." )
  elif BMI > 18.5 and BMI <= 24.5:
    print("Tvoje BMI je", BMI,". Máš normální hmotnost.")
  elif BMI >= 25 and BMI <= 29.9:
    print("Tvoje BMI je", BMI, ". Máš nadváhu." )
  elif BMI > 30:
    print("Tvoje BMI je", BMI, ". Máš nadváhu." )
    

def otazka():
  hmotnost = float(input("Zadej svoji váho v kilogramech: "))
  vyska = float(input("Zadej svoji výšku v metrech: "))
  return hmotnost, vyska

main()