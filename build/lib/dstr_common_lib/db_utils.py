def exec_sql_with_result(sql, cursor):
    cursor.execute(sql)
    return dictfetchall(cursor)


def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
    ]
