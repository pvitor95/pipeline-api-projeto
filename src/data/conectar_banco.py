from sqlalchemy import create_engine

def conectar_postgres(usuario, senha, host, porta, banco):
    """
    Retorna uma engine de conexão com o banco PostgreSQL.
    """
    try:
        engine = create_engine(f'postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{banco}')
        print("Conexão com PostgreSQL criada com sucesso!")
        return engine
    except Exception as e:
        print("Erro ao conectar ao PostgreSQL:", e)
        return None