import pymysql
class ConnectSql:
    def __init__(self,host,user,password,database,port):
        #conn=pymysql.connect(host="106.52.86.156",user="selecter",password="selecter_Qitan.123#",db="qitan",port=3063,charset="utf8")#连接数据库
        self.connect=pymysql.Connect(host=host,user=user,password=password,database=database,port=port)
        self.curson=self.connect.cursor()#获取游标

    def excute_sql(self,sql):
        self.curson.execute(sql)
        # self.curson.fetchall() #获取数据  fetchone获取一条数据，fetchall获取全部数据 dat=self.curson.fetchall()
        return self.curson.fetchall()


if __name__=="__main__":
    SQL=ConnectSql("42.193.175.165","qitanbe","aitech@0755","qitan",3456)
    print(SQL.excute_sql('SELECT * FROM t_general_diagnosis WHERE id=6528'))
