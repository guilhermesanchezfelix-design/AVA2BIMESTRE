# Guilherme Sanchez :Lógica Matemática
def calcular_imc(peso, altura):
    return peso / (altura ** 2)
# Guilherme Sanchez : Classificação de Dados
def classificar(valor_imc):
    if valor_imc < 25:
        return "Normal" 
    else:
        return "Acima do Peso"
# Lucas Eduardo : Especialista em Conteúdo
def gerar_mensagem(status):
    if status == "Normal":
        return "Parabéns, continue se esforçando 💪"
    else:
        return "Melhore sua alimentação, e procure fazer atividades fisícas 🫤"
# Raphaela Assis : Engenheiro de Programção {
peso = float(input("Digite o seu peso (kg) : "))
altura = float(input("Digite a sua altura (m) :"))
imc = calcular_imc(peso, altura)
status = classificar(imc)
mensagem = gerar_mensagem(status)
print(F"Imc: {imc:.2f}")
print(F"Classificação: {status}")
print(F"Recomendação: {mensagem}")






