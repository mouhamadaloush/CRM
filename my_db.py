import psycopg2

conn = psycopg2.connect(database = "CRM", user="postgres", password="admin", host="localhost", port="5432")


#conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)


cur = conn.cursor()


cur.execute("CREATE TABLE")

print("Done")