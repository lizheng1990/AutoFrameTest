# coding:utf8

import pymysql


def __read_sql_file(file_path):
    # 打开SQL文件到f
    sql_list = []
    with open(file_path, 'r', encoding='utf8') as f:
        # 逐行读取和处理SQL文件
        for line in f.readlines():
            # 如果是配置数据库的SQL语句，就去掉末尾的换行
            if line.startswith('SET'):
                sql_list.append(line.replace('\n', ''))
            # 如果是删除表的语句，则改成删除表中的数据
            elif line.startswith('DROP'):
                sql_list.append(line.replace('DROP', 'TRUNCATE').replace(' IF EXISTS', '').replace('\n', ''))
            # 如果是插入语句，也删除末尾的换行
            elif line.startswith('INSERT'):
                sql_list.append(line.replace('\n', ''))
            # 如果是其他语句，就忽略
            else:
                pass
    return sql_list

mysql_config = {
            'mysqluser': "Will",
            'mysqlpassword': "willfqng",
            'mysqlport': 3306,
            'mysqlhost': '112.74.191.10',
            'mysqldb': 'test_project',
            'mysqlcharset': "utf8"
        }

connect = pymysql.connect(
            user=mysql_config['mysqluser'],
            password=mysql_config['mysqlpassword'],
            port=mysql_config['mysqlport'],
            host=mysql_config['mysqlhost'],
            db=mysql_config['mysqldb'],
            charset=mysql_config['mysqlcharset']
        )

cursor = connect.cursor()
# 一行一行执行SQL语句
# for sql in __read_sql_file("C:\\Users\\leez\\Documents\\Navicat\\MySQL\\servers\\112\\test_project\\userinfo.sql"):
#     cursor.execute(sql)
#     connect.commit()

cursor.execute("SELECT * from userinfo LIMIT 10;")
desc = cursor.description  # 获取字段的描述，默认获取数据库字段名称，重新定义时通过AS关键重新命名即可
data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
print(data_dict)
connect.commit()
# 关闭游标和连接
cursor.close()
connect.close()