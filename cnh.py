#cnh.py
from datetime import datetime
nome=input("Informe o nome do condutor:")
dt_nasc_str=input("Informe a data de nascimento do condutor:")
dt_nasc=datetime.strptime(dt_nasc_str, "%d/%m/%y").date()
dt_hoje=date.today()
if dt_hoje.year - dt_nasc.year >= 18:
    tc=input("Tem CNH(S/N)?")
    if tc=="S":
        print("Pode dirigir.")
    else:
        print("Não pode dirigir.")
else:
    print("Não pode dirigir por ser menor de idade")