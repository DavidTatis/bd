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

    def insert(self,name,email,phone,address,zipcode):
        cursor = self.conn.cursor()
        query = "insert into organization(name,email,phone,address,zipcode) values (%s, %s, %s, %s,%s) returning org_id;"
        cursor.execute(query, (name,email,phone,address,zipcode,))
        org_id = cursor.fetchone()[0]
        self.conn.commit()
        return org_id
