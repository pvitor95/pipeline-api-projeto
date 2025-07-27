import extrair_dados
from sqlalchemy import create_engine


df = extrair_dados.dadosDemograficos() # função obtem os metodos e atributos do pandas

# Selecionar paises da America para Analise

df = df[df['pais'].isin(["Argentina", "Bolivia", "Brazil","Chile", "Colombia","Ecuador","Guyana","Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela, RB"])]

print(df)

# Propriedades para conexão
usuario = 'XXXXX' # Substituir valores para conectar o banco
senha = 'XXXXXX'
host = 'XXXXXXXX'
porta = 'XXXXXX'
banco = 'XXXXXXX'


engine = create_engine(f'postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{banco}')

# Inserir DataFrame no banco

try:
    df.to_sql('dadosPaises', con=engine, if_exists='append', index=False)
    print("Dados inseridos com sucesso.")
except Exception as e:
    print("Erro ao inserir dados:", e)