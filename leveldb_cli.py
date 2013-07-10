#! /bin/env python
# encoding=utf-8
# gusimiu@baidu.com
# 

import sys
import leveldb
from arg import *

def proc_get(ldb):
    sys.stdout.write('Input a key> ')
    l = raw_input()
    key = l.strip('\n')
    out = ldb.Get(key)
    print 'Key : %s' % key
    print 'Output : %s' % out

def proc_put(ldb):
    sys.stdout.write('Input key[tab]value> ')
    l = raw_input()
    key, value = l.strip('\n').split('\t')
    print 'Key : %s' % key
    print 'Value : %s' % value
    ldb.Put(key, value)

if __name__=='__main__':
    arg = Arg('LevelDB cli.')
    arg.str_opt('path', 'p', 'database path', required=True)
    arg.str_opt('import_file', 'i', 'import file with first key')
    opt = arg.init_arg()

    ldb = leveldb.LevelDB(opt.path)
    if opt.import_file:
        logging.info('IMPORT MODE.')
        batch = leveldb.WriteBatch()
        for l in file(opt.import_file).readlines():
            arr = l.strip('\n').split('\t')
            key, value = arr[0], '\t'.join(arr[1:])
            batch.Put(key, value)
        logging.info('Begin to write back batch')
        ldb.Write(batch)
        logging.info('WRITE OVER!')
    else:
        while 1:
            sys.stdout.write('GET or PUT> ')
            line = raw_input()
            cmd_type = line.strip('\n')
            if cmd_type=='GET' or cmd_type=='get':
                proc_get(ldb)
            elif cmd_type=='put' or cmd_type=='PUT':
                proc_put(ldb)






