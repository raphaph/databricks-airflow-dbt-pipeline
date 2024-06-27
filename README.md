## Dbt Databricks + Airflow 

O projeto consistente em construir uma pipeline de dados conectando o dbt com o databricks e orquestrando as execuções com o Airflow, as configurações e ambiente de dados do databricks não estará presente nesse repositório.

**Notes Airflow**  

O arquivo de configuração do Airflow esta setado para ambiente de produção com o Executor Celery e banco de dados Postgres, as informações contidas são padrões, lembre-se de configurar senhas e usuários fortes e proteger o ambiente.

Caso deseje ambiente de desenvolvimento a principio, por padrão o comando <code>airflow standalone</code> já configura o arquivo e utiliza recursos simples como SQLite e Executor Sequentials, não recomendados para produção.

O arquivo de configuração do airflow.cfg geralmente é armazenado em /home/user/airflow.

A pasta de dag's pode ser modificada a localização, portando deve ser atualizada a variável da localização no airflow.cfg.

**Notes dbt**
O arquivo profiles.yaml geralmente é armazenado em /home/user/.dbt.

No repositório está disponivel o requirements.txt com todos os pacotes instalados no projeto, se necessário futuramente incluo toda instalação aqui

**Principais libs/pkg**
- python3.8+
- dbt-core
- dbt-databricks
- apache-airflow
- postgresql
- postgresql-contrib
- psycopg2-binary
- redis-server
