import psycopg2


def conecta_banco(dbname):
    try:
        conn = psycopg2.connect(database=dbname,
                                host="127.0.0.1",
                                user="postgres",
                                password="postgres",
                                port="5432")
        return conn
    except psycopg2.OperationalError as e:
        print(f"Postgres não está rodando ou o usuário está invalido -> {e}")



conn = conecta_banco("postgres")
conn.autocommit = True

cursor = conn.cursor()

try:
    print("Criado um banco chamado -> CRUDSI")
    cursor.execute("CREATE database crudsi")
except:
    pass

conn.close()
cursor.close()


conn = conecta_banco("crudsi")
cursor = conn.cursor()
print("Criando a tabela (sim, apenas)")
query = '''CREATE TABLE product(
product_id serial PRIMARY KEY,
product_name VARCHAR ( 50 ) NOT NULL,
product_description VARCHAR ( 200 ) NOT NULL,
product_price integer NOT NULL,
product_quantity integer NOT NULL
)'''
cursor.execute(query)