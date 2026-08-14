with open("logs.txt","r",encoding="utf-8")as aqTexto,open("erros_filtrados.txt.","w")as aqErro:
    qtERROR=0
    qtWARNING=0
    qtINFO=0
    for linha in aqTexto:
        if "ERROR" in linha:
            aqErro.write(linha)
            qtERROR+=1
        elif "WARNING" in linha:
            qtWARNING+=1
        elif "INFO" in linha:
            qtINFO
    print(f"linhas de error: {qtERROR}")
    print(f"linhas de warning: {qtWARNING}")
    print(f"linhas de info: {qtINFO}")

