import psycopg2

conn = psycopg2.connect(
    host='localhost',
    database='branas_ca_live',
    user='postgres',
    password='12345678')
