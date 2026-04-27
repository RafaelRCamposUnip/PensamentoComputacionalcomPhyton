#Somando dois números
def somar (valor1,valor2):
    return valor1+valor2
def main():
    num1=int(input("Informe um número inteiro:"))
    num2=int(input("Informe outro número inteiro:"))
    print(f"A soma desses números é {somar(num1,num2)}")
if __name__=="__main__":
    main()