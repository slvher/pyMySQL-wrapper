#!/bin/env python
#-*- encoding:utf-8 -*-

import time
import os
import MySQLdb
from hs_log import *

class pyMySQL():
    def __init__(self, host, user, passwd, dbname, port = '3306'):
        self.bConned = False
        self.dbHandle = None
        self.host = host
        self.user = user
        self.passwd = passwd
        self.dbname = dbname
        self.port = int(port)
    

    def __del__(self):
        self.disconnect_to_mysql()
        g_log_inst.get().debug('disconnect_to_mysql() success, host=%s, user=%s, db=%s, port=%u' % (self.host, self.user, self.dbname, self.port))
        

    def connect_to_mysql(self, char_set = None):
        try:
            if True == self.bConned:
                return True
            if char_set is None:
                self.dbHandle = MySQLdb.connect(host = self.host, user = self.user, passwd = self.passwd, db = self.dbname, port = self.port)
            else:
                self.dbHandle = MySQLdb.connect(host = self.host, user = self.user, passwd = self.passwd, db = self.dbname, port = self.port, charset = char_set)
            self.bConned = True
            g_log_inst.get().debug('Connect to MySQL Server success, host=%s, user=%s, db=%s, port=%u' % (self.host, self.user, self.dbname, self.port))
            return True 
        except Exception, e:
            g_log_inst.get().warning('Connect to MySQL Server Failed, host=%s, user=%s, db=%s, port=%u, errmsg=%s' % (self.host, self.user, self.dbname, self.port, e))
            return False


    def disconnect_to_mysql(self):
        try:    
            if (True == self.bConned) and (self.dbHandle is not None):
                self.dbHandle.close()
                self.dbHandle = None
                self.bConned = False
        except Exception, e:
            g_log_inst.get().warning('Disconnect to MySQL Server Failed, errmsg=%s' % (e))
            

    def do_QUERY(self, sql_cmd):
        try:
            if (False == self.bConned) or (self.dbHandle is None):
                if True != self.connect_to_mysql():
                    g_log_inst.get().warning('do_QUERY() failed: self.dbHandle = None')
                    return None
            # if connected, do the query
            cursor = self.dbHandle.cursor()
            cursor.execute(sql_cmd)
            rows = cursor.fetchall()
            cursor.close()
            self.dbHandle.commit() 
            g_log_inst.get().debug('query completed, %d records fetched from mysql server' % (len(rows)))
            return rows
        except Exception, e:
            g_log_inst.get().warning('do_QUERY() failed, errmsg=%s' % (e))
            return None


    def do_INSERT(self, sql_cmd):
        try:
            if (False == self.bConned) or (self.dbHandle is None):
                if True != self.connect_to_mysql():
                    g_log_inst.get().warning('do_QUERY() failed: self.dbHandle = None')
                    return None
            # if connected, do the insert operation
            cursor = self.dbHandle.cursor()
            cursor.execute(sql_cmd)
            self.dbHandle.commit() 
            cursor.close()
            g_log_inst.get().debug('insert completed, return success')
            return 0
        except Exception, e:
            g_log_inst.get().warning('do_INSERT() failed, errmsg=%s' % (e))
            return None


    def do_UPDATE(self, sql_cmd):
        try:
            if (False == self.bConned) or (self.dbHandle is None):
                if True != self.connect_to_mysql():
                    g_log_inst.get().warning('do_QUERY() failed: self.dbHandle = None')
                    return None
            # if connected, do the update operation
            cursor = self.dbHandle.cursor()
            cursor.execute(sql_cmd)
            self.dbHandle.commit() 
            cursor.close()
            g_log_inst.get().debug('update completed, return success')
            return 0
        except Exception, e:
            g_log_inst.get().warning('do_UPDATE() failed, errmsg=%s' % (e))
            return None

    def do_DELETE(self, sql_cmd):
        try:
            if (False == self.bConned) or (self.dbHandle is None):
                if True != self.connect_to_mysql():
                    g_log_inst.get().warning('do_QUERY() failed: self.dbHandle = None')
                    return None
            # if connected, do the delete operation
            cursor = self.dbHandle.cursor()
            cursor.execute(sql_cmd)
            self.dbHandle.commit() 
            cursor.close()
            g_log_inst.get().debug('delete completed, return success')
            return 0
        except Exception, e:
            g_log_inst.get().warning('do_DELETE() failed, errmsg=%s' % (e))
            return None

   
def main():
    import ConfigParser
    cfg = ConfigParser.ConfigParser()
    cfg.read('inst.conf')
    g_log_inst.log_level = logging.DEBUG
    g_log_inst.log_name = cfg.get("log", "logname")
    g_log_inst.log_file = cfg.get("log", "filename")
    g_log_inst.log_size= int(cfg.get("log", "max_file_size"))*1024*1024
    g_log_inst.start()

    host = cfg.get('mysql', 'host')
    user = cfg.get('mysql', 'user')
    passwd = cfg.get('mysql', 'passwd')
    dbname = cfg.get('mysql', 'dbname')
    port = cfg.get('mysql', 'port')

    db_obj = pyMySQL(host, user, passwd, dbname, port);
    sql_cmd = 'select * from xxx'
    db_obj.do_QUERY(sql_cmd)


if __name__ == '__main__':
    main()

