import pymysql


#开始连接数据库
#设定mysql数据库连接信息，创建connection对象
"""
connection对象

    作用：用于建立与数据库的连接
    创建对象：调用connect()方法
        conn = connect(参数列表)

    对象的方法:
        close() 关闭链接
        commit() 事物，所以需要提交才会生效
        rollback() 事务，放弃之前的操作
        cursor()返回Cursor对象，用于执行sql语句并获得结果
"""
conn = pymysql.connect(host = 'localhost', port = 3306, db = 'python4', user = 'root', passwd = '123456', charset="utf8")

#Cursor对象
"""
Cursor对象

    作用：执行sql语句
    创建对象：调用Connection对象的cursor()方法
        cursor1 = conn.cursor()

    对象的方法：
        close() 关闭连接
        execute(operation [,parameters ]) 执行语句，返回受影响的行数
        fetchone() 执行查询语句时，获取查询结果集的第一行数据，返回一个元组
        next() 执行查询时，获取结果集的所有行，一行构成一个元组，再将这些元组装入一个元组返回
"""
cs1= conn.cursor()
count = cs1.execute("insert into students(names,sex,height,weight,hobby) values('李氏',1,170,75,'踢足球')")
print(count)
#connection对象的提交事务，使其sql生效。
conn.commit()
cs1.close()
conn.close()




