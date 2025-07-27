# Script para acessar os dados na API, extrair e transformar em um DF

def dadosDemograficos():
    import pandas as pd
    import requests as r
    import xmltodict as xl

    
    paginasAPI = [x for x in range(1,346)] #Lista de Paginas
    listaPaginas = []
    
    for y in paginasAPI:
        response = r.get(f'https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?data=2000:2025&page={y}')
        resposta = xl.parse(response.content) # Converte XML para dicionario

        # Verificando se a existencia da chave 'wb:data'
        if 'wb:data' in resposta and 'wb:data' in resposta['wb:data']:
            resposta = resposta['wb:data']['wb:data']

            #Processar cada item da resposta
            for x in resposta:
                if isinstance(x, dict):  # Verifica se x é dicionario
                    resultado = {
                        'pais': x['wb:country']['#text'], # País
                        'codigoPais': x['wb:country']['@id'], # ID País
                        'ano': x['wb:date'], # Ano
                        'populacao': x['wb:value'] # População
                    }
                    listaPaginas.append(resultado) # Adiciona o resultado à uma lista

    df = pd.DataFrame(listaPaginas)
    return df # Retorna o dataframe

