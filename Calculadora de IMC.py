def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "baixo peso"
    elif 18.5 <= imc < 25:
        return "Peso adequado"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidade grau I"
    elif 35 <= imc < 40:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"

def main():
    print("Calculadora de IMC")
    try:
        altura = float(input("Digite sua altura (em metros): "))
        peso = float(input("Digite seu peso (em kg): "))
        
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)

        print(f"\nSeu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao}")
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

if __name__ == "__main__":
    main()
