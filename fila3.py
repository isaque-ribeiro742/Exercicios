pedidos=[]
while True:
    comando=input("novo,preparar,encerrar : ")
    if comando=="encerrar":
        print(">> Espidiente encerrado!")
        print(f" atençao : {len(pedidos)} pedido(s) nao poderam ser entregues")
        break
    elif comando=="novo":
        lanche=input("qual e o pedido ? ")
        pedidos.append(lanche)
        print(f" {lanche} adicinada a fila de preparo ") 
    elif comando =="preparar":
        if len (pedidos)==0:
            print("nao a pedidos pendentes")
        else:        
            print(f"saindo pedido : {pedidos.pop(0)}!")     