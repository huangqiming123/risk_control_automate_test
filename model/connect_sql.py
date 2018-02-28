import pymysql


class ConnectSql(object):
    def connect_risk_sql(self):
        # 连接风控正式环境数据库
        connect = pymysql.connect(
            host='112.74.94.26',
            port=3306,
            user='uat',
            passwd='uat',
            db='frcdb',
            charset='utf8'
        )
        return connect


    '''def connect_risk_sql(self):
        # 连接风控测试环境数据库
        connect = pymysql.connect(
            host='172.16.10.103',
            port=3306,
            user='root',
            passwd='123456',
            db='frcdb',
            charset='utf8'
        )
        return connect'''


