# coding=utf-8
from functools import wraps
import pymysql  #1.引入mysql api
import logging,sys

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db':'mysql',
    'charset':'utf8'
    }

logger=logging.getLogger('dblog')
logger.setLevel(logging.DEBUG)
# 指定logger输出格式
formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')

# 文件日志
file_handler = logging.FileHandler("test.log")
file_handler.setFormatter(formatter)
# 控制台日志
console_handler = logging.StreamHandler(sys.stdout)
console_handler.formatter = formatter

# 为logger添加的日志处理器
logger.addHandler(file_handler)
logger.addHandler(console_handler)
#logger.removeHandler(file_handler)

class mysqlDbo(object):
    def __init__(self,dbPath=config):
        #初始化连接数据库所需要的参数
        self.config=config

    def connect(self):
        #尝试连接数据库
        try:
            logger.info('开始连接数据库...')
            self.conn = pymysql.connect(**self.config)
        except Exception:
            logger.exception("传入的数据库的config有误，应该为字典格式，如：{'host':'localhost','user':'root','password':'123456','port':3306}")
        #2.获取与数据库的连接
        self.cur=self.conn.cursor()
        logger.info('连接数据库成功')
        return self.cur

    def execSQL(self,sqlstr='select * from user '):
        #3.执行sql
        logger.info('查询数据中：{}'.format(sqlstr))
        rawcount = self.cur.execute(sqlstr)
        for data in self.cur:
            logger.info(data)
        return rawcount

    def close(self):
        #4.关闭数据库和游标
        logger.info('开始关闭数据库连接...')
        self.cur.close()
        self.conn.close()
        logger.info('已关闭数据库连接！')

if __name__=='__main__':
    dbo=mysqlDbo({'host':'localhost','user':'root','password':'root','port':3306})
    cur=dbo.connect()
    count=dbo.execSQL()
    dbo.close()
