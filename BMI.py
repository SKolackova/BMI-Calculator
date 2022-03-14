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
  print('''Pro přehled tabulka s hodnotami:
BMI	            Hodnocení
méně než 18,5	Podváha
18,5 až 24,9	Normální hmotnost
25 až 29,9	    Nadváha
30 a více	    Obezita''')


def otazka():
  hmotnost = float(input("Zadej svoji váhu v kilogramech: "))
  vyska = float(input("Zadej svoji výšku v metrech. Použij tečku jako desetinou čárku: "))
  return hmotnost, vyska

main()