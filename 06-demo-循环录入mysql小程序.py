import pymysql

class mysql_fs(object):
    def add_data(self,names,sex,height,weight,hobby):
        """
            作用：在数据库中添加插入信息
        :return:
        """
        #创建connection对象
        conn = pymysql.connect(host='localhost', port=3306, db='python4', user='root', passwd='123456', charset='utf8')

        #调用connection对象的cursor()方法创建cursor对象
        cs1 = conn.cursor()

        #插入一条记录
        count = cs1.execute("insert into students(names, sex, height, weight, hobby) values('%s','%s','%d','%d','%s')"%(names, sex, int(height), int(weight), hobby))
        print("数据录入成功！！！")
        #提交事件
        conn.commit()

        #关闭cursor对象
        cs1.close()

        #关闭数据库链接
        conn.close()


    def sub_data(self, names):
        """
            作用：删除数据库中的记录，以名字为引索
        :return:
        """
        #创建connection对象
        conn = pymysql.connect(host='localhost', port=3306, db='python4', user='root', passwd='123456', charset='utf8')

        #调用connection



    def up_data(self, name):
        """
            作用：修改数据库中的记录，以名字为引索
        :return:
        """
        pass

    def find_data(self):
        """
            作用：查找数据库中的一条或几条数据
        :return:
        """

    def menu_data(self):
        """
            作用：显示菜单
        :return:
        """
        print("*"*50)
        print("*"*50)
        print("欢迎使用数据库导入系统")
        print("1、插入数据\n\t")
        print("2、删除数据,请输入名字\n\t")
        print("3、修改数据,请输入名字\n\t")
        print("4、退出"*50)
        print("*"*50)

    def menu_chooes(self, menu_choose):
        input("")




if __name__ == "__main__":
    a = True
    new = mysql_fs()
    while(a):
        names = input("请输入学生姓名\n\t")
        sex = input("请输入性别\n\t")
        height = input("请输入身高\n\t")
        weight = input("请输入体重\n\t")
        hobby = input("请输入学生爱好\n\t")
        new.add_data(names, sex, height, weight, hobby)
        begin_flag = input("继续请按1，退出请按0")
        if begin_flag == 0:
            a = False
