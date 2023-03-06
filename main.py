import psycopg2


def create(conn):
    # создание таблиц
    cur.execute("""
        CREATE TABLE IF NOT EXISTS client(
        id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        name VARCHAR(40) UNIQUE,
        last_name VARCHAR(40) UNIQUE,
        email VARCHAR(40) UNIQUE
        );
        """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS telephone(
        id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        number VARCHAR(40) UNIQUE NOT NULL,
        client integer NOT NULL REFERENCES client(id)
        );
        """)


def insert(conn, name, last_name, email, numb=None):
    # добавление клиента
    cur.execute("""
        INSERT INTO client (name, last_name, email)
        VALUES(%s,%s,%s);
        """, (name, last_name, email,))
    cur.execute("""
        SELECT id FROM client
        WHERE email = %s;
        """, (email,))
    id_client = cur.fetchone()
    if numb is not None:
        cur.execute("""
            INSERT INTO telephone (number, client)
            VALUES(%s, %s);
            """, (numb, id_client))


def add_tel(conn, email, numb):
    # добавление дополнительного номера тел.
    cur.execute("""
        SELECT id FROM client
        WHERE email = %s; 
        """, (email,))
    id_client = cur.fetchone()
    cur.execute("""
        INSERT INTO telephone (number, client)
        VALUES(%s, %s);
        """, (numb, id_client))


def update_client(conn, email):
    # изменение данных клиента
    cur.execute("""
        SELECT id FROM client
        WHERE email = %s; 
        """, (email,))
    id_client = cur.fetchone()
    name = input('Введите новое или актуальное имя клиента: ')
    last_name = input('Введите новую или актуальную фамилию клиента: ')
    email = input('Введите новую или актуальную эл. почту: ')
    numb = input('Введите новый или актуальный номер тел.: ')
    cur.execute("""
        UPDATE client
        SET name = %s, last_name = %s, email = %s
        WHERE id = %s;
        """, (name, last_name, email, id_client,))
    cur.execute("""
        SELECT number FROM telephone
        WHERE client = %s; 
        """, (id_client,))
    numbs_old = cur.fetchall()
    for n_old in numbs_old:
        delete_tel(conn, n_old)
    add_tel(conn, email, numb)


def delete_tel(conn, numb):
    # удаление номера тел.
    cur.execute("""
        SELECT id FROM telephone
        WHERE number = %s; 
        """, (numb,))
    id_numb = cur.fetchone()
    cur.execute("""
        DELETE FROM telephone
        WHERE id = %s;
        """, (id_numb,))


def delete_client(conn, email):
    # удаление клиента
    cur.execute("""
        SELECT id FROM client
        WHERE email = %s;
        """, (email,))
    id_client = cur.fetchone()
    cur.execute("""
        DELETE FROM telephone
        WHERE client = %s;
        """, (id_client,))
    cur.execute("""
        DELETE FROM client
        WHERE id = %s;
        """, (id_client,))


def search_client(conn, name=None, last_name=None, email=None, numb=None):
    # поиск клиета
    if name is not None:
        cur.execute("""
            SELECT name, last_name, email, t.number FROM client c
            JOIN telephone t ON t.client = c.id
            WHERE name = %s;
            """, (name,))

    elif last_name is not None:
        cur.execute("""
            SELECT name, last_name, email, t.number FROM client c
            JOIN telephone t ON t.client = c.id
            WHERE last_name = %s;
            """, (last_name,))
    elif email is not None:
        cur.execute("""
            SELECT name, last_name, email, t.number FROM client c
            JOIN telephone t ON t.client = c.id
            WHERE email = %s;
            """, (email,))
    elif numb is not None:
        cur.execute("""
            SELECT name, last_name, email, t.number FROM client c
            JOIN telephone t ON t.client = c.id
            WHERE t.number = %s;
            """, (numb,))
    info = cur.fetchone()
    print(info)


with psycopg2.connect(database="client", user="postgres", password="123456") as conn:
    with conn.cursor() as cur:
        # создание БД
        # create(conn)

        # добавление клиента
        # name = input('Введите имя клиента: ')
        # last_name = input ('Введите фамилию клиента: ')
        # email = input('Введите эл. почту: ')
        # numb = input('Введите номер тел.: ')
        # insert(conn, name, last_name, email, numb)

        # добавление номер тел. клиенту
        # email = input('Введите эл. почту клиента: ')
        # numb = input('Введите доп. номер тел.: ')
        # add_tel(conn, email, numb)

        # изменение данных по клиенту
        # email = input('Введите эл. почту: ')
        # update_client(conn, email)

        # удаление номера тел.
        # numb = input('Введите номер тел. для удаления: ')
        # delete_tel(conn, numb)

        # удаление клиента
        # email = input('Введите эл. почту удаляемого клиента: ')
        # delete_client(conn, email)

        # поиск клиента
        # search = int(input('Если хотите найти по имени нажмите 1, по фамилии 2, по email 3, по номеру тел. 4: '))
        # if search == 1:
        #     name = input('Введите имя клиента: ')
        #     search_client(conn, name=name)
        # elif search == 2:
        #     last_name = input('Введите фамилию клиента: ')
        #     search_client(conn, last_name=last_name)
        # elif search == 3:
        #     email = input('Введите email клиента: ')
        #     search_client(conn, email=email)
        # elif search == 4:
        #     numb = input('Введите номер тел. клиента: ')
        #     search_client(conn, numb=numb)
        conn.commit()  # фиксируем в БД
conn.close()
