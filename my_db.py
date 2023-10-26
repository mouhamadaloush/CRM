import psycopg2

conn = psycopg2.connect(database = "CRM", user="postgres", password="admin", host="localhost", port="5432")


#conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
#"django-insecure-v_p!hgeb!31wnixjn1#pgm@m$wbng+wm#d%sidk)ttd-&6&oma"

cur = conn.cursor()


cur.execute("CREATE TABLE")

print("Done")