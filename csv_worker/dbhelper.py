from django.db import connection
from django.conf import settings


# data_csv -> dict {name: data (json)}
def create_table_with_data(table=settings.TABLE_NAME_FOR_VARIABLES, **data_csv):
    drop_table()

    with connection.cursor() as cursor:
        sql_raw = f"""
            create table {table} (
                id serial not null primary key, 
                name varchar (50) not null,
                data json not null        
            );"""
        cursor.execute(sql_raw, settings.TABLE_NAME_FOR_VARIABLES)

        if data_csv:
            sql_raw = f"""
                insert into {table} (name, data)
                values 
                    {','.join('(%s, %s)' for _ in data_csv)}
                ;"""

            params = []
            for name, data in data_csv.items():
                params.append(name)
                params.append(data)

            cursor.execute(sql_raw, params)


def drop_table(table=settings.TABLE_NAME_FOR_VARIABLES):
    with connection.cursor() as cursor:
        sql_raw = f"drop table if exists {table};"
        cursor.execute(sql_raw)


