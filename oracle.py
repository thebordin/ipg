import oracledb
#cx_Oracle.init_oracle_client(lib_dir="/instantclient_21_10")
# Configurações de conexão
host = 'bdi.ipg.pt'
port = '1521'
service_name = ''
username = 'bdi_dai_1707750'
password = 'bdi'

# Cria a string de conexão
dsn = oracledb.makedsn(host, port)
connection = oracledb.connect(user=username, password=password, dsn=dsn)

try:
    # Cria um cursor
    cursor = connection.cursor()

    # Executa uma consulta SQL
    cursor.execute('SELECT * FROM nome_da_tabela')

    # Recupera os resultados da consulta
    for row in cursor:
        print(row)

finally:
    # Fecha o cursor e a conexão
    cursor.close()
    connection.close()