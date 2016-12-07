# coding: utf-8
from logging import INFO, basicConfig, error, info
from os import system as sys
from os import environ

import psycopg2
import simplejson as json


def fetch_and_save_data_to_file(db_cursor, file_options, sql_opt):
    file_options['samplefile'] = 'sample_' + file_options['filename']
    with open(file_options['filename'], 'w') as mainfile,\
         open(file_options['samplefile'], 'w') as samplefile:
        info('File: %s', file_options['filename'])
        i = 0
        samples = []
        for row in db_cursor.fetchmany(sql_opt['limit']):
            mainfile.write(json.dumps(row[0], mainfile))
            mainfile.write('\n')
            if i < sql_opt['limit']:
                i += 1
                samples.append(row[0])

        info('File: %s', file_options['samplefile'])
        for sample in samples:
            samplefile.write(json.dumps(sample, samplefile))
            samplefile.write('\n')
    info('Closing conection...')


def serialize_sql_opt(table='saude', term='dengue', limit=10):
    sql_opt = {}
    sql_opt['table'] = table
    sql_opt['term'] = term
    sql_opt['limit'] = limit
    return sql_opt


def data_retrieval(table='saude', term='dengue', limit=10):
    basicConfig(format='%(levelname)s %(message)s', level=INFO)
    sql_opt = serialize_sql_opt(table, term, limit)
    USER = environ.get('DB_USER', 'YOUR_USER_NAME')
    PASSWORD = environ.get('DB_PASSWORD', 'YOUR_PASSWORD')
    if not USER or not PASSWORD:
        error('no USER or PASSWORD for connection found')
        sys.exit(1)

    HOST = environ.get('DB_HOST', 'HOST_NAME')
    DATABASE = environ.get('DB_NAME', 'DATABASE_NAME')
    if not HOST or not DATABASE:
        error('no HOST or DATABASE for connection found')
        sys.exit(1)

    info('Connecting to database...')
    conn = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD,
                            host=HOST)
    cur = conn.cursor()

    sql = ("SELECT json "             # complete json
           "FROM {table} "            # view or table
           "WHERE lower(text) "       # tweet text
           "like '%{term}%' "         # term in the tweet like dengue
           "limit {limit};")          # limit number of tweets
    sql = sql.format(table=sql_opt['table'],
                     term=sql_opt['term'],
                     limit=sql_opt['limit']
                     )
    info('Executing SQL command...')
    cur.execute(sql)
    info('Fetching and writing data...')
    file_opt = {
                    'filename': sql_opt['term'] + '_tweets_json',
               }
    fetch_and_save_data_to_file(cur, file_opt, sql_opt)
    cur.close()
    conn.close()

if __name__ == '__main__':
    data_retrieval()
