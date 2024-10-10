# Programm Bruttolohn v1

arb_std = int(input("Gib die Arbeitsstunden an: "))
std_satz = float(input("Gib den Stundensatz an: "))

bruttolohn = round(arb_std * std_satz, 2)

print("Zahlung:", bruttolohn)