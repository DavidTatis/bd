from config.dbconfig import pg_config
import psycopg2
from handler.dictionary import Dictionary

class OrganizationsDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=%s port=%d" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'],
                                                            pg_config['host'],
                                                            pg_config['port'])
        self.conn = psycopg2._connect(connection_url)


    def getAllOrganizations(self):
        cursor = self.conn.cursor()
        query = "select * from organization;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
