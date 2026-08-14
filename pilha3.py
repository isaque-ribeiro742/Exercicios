pilha_mesa=[]
pilha_suap=[]
for i in range(4):
    aluno=input(f"digite o nome do aluno {i+1} : ")
    pilha_mesa.append(aluno)
print(f"\n estadado atual da pilha na mesa : {pilha_mesa}\n")  
print('inicializando a transferencia (inverçao) para o suap ' )  
for j in range (len(pilha_mesa)):
    tranferencia =pilha_mesa.pop()
    pilha_suap.append(tranferencia)
    print(f">>Transfirindo: {tranferencia}\n")
print('transferencia concluida!')
print(f"pilha_mesa{pilha_mesa}")
print(f"pilha pronta para o suap :{pilha_suap}")        