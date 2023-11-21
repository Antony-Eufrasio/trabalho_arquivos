"""Você foi contratado, por um serviço de investigação para realizar a descoberta de informações sobre dados disponibilizados na Web.
Para isto, você deverá implementar em Python este programa, que deverá utilizar arquivo(s) de texto ou csv, para armazenar os dados referentes a análise.
Você deverá escolher um ou mais conjuntos de dados em formato textual, disponíveis, preferencialmente, no http://dados.gov.br, com no mínimo 500 linhas.
Seu programa deverá contar com um Menu Principal, para que o usuário possa informar as operações que deseja executar (ex. “1” - para relatório; “0” - para Sair).
Seu programa deverá conter, pelo menos, 06 funções de sua autoria, que deverão ser chamadas ao longo da execução. Estas funções deverão apresentar informações relevantes extraídas do arquivo e podem exibir os resultados no terminal ou em arquivos específicos.
Operações obrigatórias (que podem ser incluídas nas 06 funções):
Apresentar um relatório com o número de linhas do documento original, e os nomes das colunas, que descrevem os dados;
Criar um arquivo parcial, com nome informado pelo usuário, que armazenará os dados correspondentes a uma filtragem de dados. Para este arquivo, também deverá ser possível chamar a função de relatório anterior (retornar para o menu principal).
Criar arquivo de Resumo - Deverá apresentar dados agrupados, com totalizadores.
Apresentar dados estatísticos sobre o arquivo, pode ser gerado  , moda, desvio padrão, entre outros.
Realizar uma busca de dados no(s) arquivo(s)."""


def coluna(coluna):
    with open("planilhas/registroArma.csv", "r") as regArma:
        coluna1 = regArma.readline()
        return(coluna1)

def nome(linhas):
    with open("planilhas/registroArma.csv", "r") as regArma:
        cont = regArma.readlines()
        cont1 = 0
        #colunas = regArma.readline()
        
        for linha in cont:
            cont1 += 1
    print(f"O nummero de linhas é {cont1}")
    print(coluna)


def buscaNome(arma):
    with open("planilhas/registroArma.csv","r") as regArma , open("planilhas/nomeArma.csv","w") as nomeArma:
            for linha in regArma:
                colunas = linha.split(";")
                if (colunas[6].strip().lower() == arma.lower()):
                    nomeArma.write(colunas[6] + ";" + colunas[4] + ";" + colunas[2] + "\n")
            return(arma)
            nomeArma.close()
            regArma.close()

def requerimentosAno(ano):
    with open("planilhas/registro.csv","w") as registro , open("planilhas/registroArma.csv","r") as regArma:
        for linha in regArma:
            colunas = linha.split(";")
            if (int(colunas[0]) == ano):
                registro.write(colunas[0] + ";" + colunas[4] + ";" + colunas[6] + "\n")
        return(ano)
        

  
def buscaArma(arma): # ainda não está funcionando arrumar em breve
    with open ("planilhas/armas.csv","w") as buscArma, open("planilhas/registroArma.csv") as regArma:
        for linha in regArma:
            coluna = linha.split(";")
            if (coluna[5].strip()) == arma:
                buscArma.write(coluna[5] + ";" + coluna[1] + ";" + coluna[2] + ";" + coluna[6] + ";" + coluna[8] + "\n")
        return(arma)
        buscArma.close()
        regArma.close()


def armaEstado(estado):
    with open("planilhas/estado.csv","w") as buscEstado, open("planilhas/registroArma.csv") as regArma:
        for linha in regArma:
            coluna = linha.split(";")
            if coluna[2] == estado:
                buscEstado.write(coluna[0] + ";" + coluna[5] + ";" + coluna[1] + ";" + coluna[2] + ";" + coluna[6] + ";" + coluna[8] + "\n")
        return(estado)
        buscEstado.close()
        regArma.close()

opcao = 30
cont = 0
repetir = 2

while opcao != 0:
    if (cont >= 1) and (opcao != 29):
        repetir = int(input("Deseja repetir a operação? (informe 1 para SIM ou 2 para NÃO)"))
        
    if repetir == 2:
        print("\nInforme 0 para sair")
        print("Informe 1 para verificar o número de registros do arquivo registroArma.csv e quais suas colunas")
        print("Informe 2 para fazer uma busca por ano de todas as armas")
        print("Informe 3 para fazer uma busca pelo nome da arma")
        print("Informe 5 para fazer uma busca pelo tipo da arma")
        print("Informe 6 para fazer uma busca das armas de um determinado estado")
        opcao = int(input("Informe o número da operação que deseja: "))
    
    if (opcao > 6) or (opcao < 0):
        opcao = 29
        print("\n******************   Operação inválida!   ******************")

    if opcao == 1:
        nome("registroArma.csv")
        
    if opcao == 2:
        busca = int(input("Informe o Ano a ser pesquisado: "))
        if busca < 2013 or busca > 2023:
            print("Esse ano não está registrado no sistema!")
        requerimentosAno(busca)
        print(busca)

    if opcao == 3:
        busca = input("\nInforme o nome da arma a ser pesquisada: ")

        buscaNome(busca)

    if opcao == 5:
        busca = input("\nInforme o tipo da arma a ser pesquisada: ")

        buscaArma(busca)

    if opcao == 6:
        busca = input("\nInforme o estado a ser pesquisado: ")
        
        armaEstado(busca)
        print(busca)
        
    cont += 1

print("\nFim da execução")