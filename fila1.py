fila=[]
while True:
    ps=input("digite o nome do paciente ou encerrar quando acabar as vagas : ")
    if ps =="encerrar":
        print("acabou o agendamento")
        break
    else:
        fila.append(ps)
while True:
    chamada=input("digite 1 quando for pra chama o paciente : ")
    if len (fila)==0:
        print("acabou os pacientes")
        break
    if chamada=="1":
        print(f"o paciente {fila.pop(0)} sendo chamado ")        