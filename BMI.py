def main():
  hmotnost, vyska = otazka()
  BMI = hmotnost / (vyska * vyska)
  if BMI <= 18.5:
    print("Tvoje BMI je", BMI, ". Máš podváhu." )
  elif BMI > 18.5 and BMI < 24.5:
    print("Tvoje BMI je", BMI,". Máš normální hmotnost.")

  
  print("Tvoje BMI je", BMI )
  print('''BMI	Hodnocení
méně než 18,5	Podváha
18,5 až 24,9	Normální hmotnost
25 až 29,9	Nadváha
30 a více	Obezita''')
  

def otazka():
  hmotnost = float(input("Zadej svoji váho v kilogramech: "))
  vyska = float(input("Zadej svoji výšku v metrech: "))
  return hmotnost, vyska

main()