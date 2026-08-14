fila=[]
while True:
    comando=input("adicionar,atender,sair : ")
    if comando== "sair":
        print(">> Espidiente encerrado!")
        print(f"pacientes que ficaram aguardando : {fila}")
        break
    elif comando=="adicionar":
        nome=input("nome do paciente :")
        fila.append(nome)
        print(f"{nome} entrou na fila .")
    elif comando=="atender":
        print(f"chamado para o consultorio : {fila.pop(0)}")       