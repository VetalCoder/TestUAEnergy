from django.db import connection, ProgrammingError
from django.conf import settings
import collections


class TableDoesNotExists(Exception):
    pass


# data_csv -> dict {name: data (json)}
def create_table_with_data(table=settings.TABLE_NAME_FOR_VARIABLES, **data_csv):
    drop_table()

    with connection.cursor() as cursor:
        sql_row = f"""
            create table {table} (
                id serial not null primary key, 
                name varchar (50) not null,
                data json not null        
            );"""
        cursor.execute(sql_row, settings.TABLE_NAME_FOR_VARIABLES)

        if data_csv:
            sql_row = f"""
                insert into {table} (name, data)
                values 
                    {','.join('(%s, %s)' for _ in data_csv)}
                ;"""

            params = []
            for name, data in data_csv.items():
                params.append(name)
                params.append(data)

            cursor.execute(sql_row, params)


def drop_table(table=settings.TABLE_NAME_FOR_VARIABLES):
    with connection.cursor() as cursor:
        sql_row = f"drop table if exists {table};"
        cursor.execute(sql_row)


def get_data(table=settings.TABLE_NAME_FOR_VARIABLES, count=2):
    with connection.cursor() as cursor:
        sql_row = f"select name, data from {table} limit %s"

        try:
            cursor.execute(sql_row, [count])
        except ProgrammingError:
            raise TableDoesNotExists

        result_dict = collections.OrderedDict()
        for name, data in cursor.fetchall():
            result_dict[name] = data

        return result_dict
