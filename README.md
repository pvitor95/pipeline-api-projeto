🌍 Pipeline de Análise Populacional Global (2000–2025)
Este projeto tem como objetivo construir um pipeline de dados completo, desde a extração de informações populacionais globais via API, até a visualização dos dados em um dashboard interativo. O foco está na comparação do crescimento populacional por continente entre os anos de 2000 e 2025.

🎯 Objetivo
Criar um pipeline automatizado que:

Extrai dados populacionais de uma API oficial de censo.

Armazena os dados em um banco de dados PostgreSQL estruturado.

Analisa e visualiza o crescimento populacional por continente.

Orquestra o fluxo de dados para garantir consistência e reprodutibilidade.

🧱 Estrutura do Pipeline
📡 Coleta de Dados

Integração com uma API pública de dados populacionais (como World Bank, UN Data, etc.).

Extração dos dados de 2000 a 2025.

🛢️ Armazenamento

Modelagem e criação das tabelas em um banco de dados PostgreSQL.

Inserção dos dados normalizados via scripts Python (usando psycopg2 ou SQLAlchemy).

📊 Visualização (Dashboard)

Criação de visualizações com Power BI, Metabase, ou Streamlit.

Dashboards com indicadores de crescimento, gráficos por continente e linha do tempo.
