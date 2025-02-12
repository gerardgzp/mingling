import csv
import mysql.connector

# 连接到 MySQL 数据库
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="sinx1234",
    database="db2"
)
print(mydb)
print(1)
# 创建一个游标对象，用于执行 SQL 语句。游标就像是一个指针，它允许我们在数据库中执行各种操作，
# 比如创建表、插入数据、查询数据等。通过游标，我们可以向数据库发送 SQL 命令并获取执行结果。
mycursor = mydb.cursor()

# 创建一个示例表
# 定义要创建的数据库表的名称，这里将表名设置为 "your_table"，
# 你可以根据实际需求修改为其他合适的表名。
table_name = "movies5"

# 初始化一个 SQL 语句字符串，用于创建表。该语句使用了 f-string 格式化字符串的方式，
# 其中包含了表名和一个自增的主键字段 "id"。"CREATE TABLE IF NOT EXISTS" 表示如果该表不存在则创建，
# "id INT AUTO_INCREMENT PRIMARY KEY" 表示创建一个名为 "id" 的整数类型字段，该字段会自动递增，并且作为表的主键。
create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ( "

# 打开指定的 CSV 文件，以只读模式 ('r') 进行操作。使用 with 语句可以确保文件在使用完后自动关闭，
# 避免资源泄漏。这里的 'your_file.csv' 需要替换为实际的 CSV 文件路径。
with open(r"D:\aguo\数据集\临时\archive\Titanic-Dataset.csv", 'r',encoding='utf-8') as csvfile:
    # 创建一个 CSV 文件读取器对象，用于逐行读取 CSV 文件的内容。
    reader = csv.reader(csvfile)
    # 读取 CSV 文件的第一行，通常第一行是表头，包含了各个字段的名称。
    # next() 函数用于获取迭代器的下一个元素，这里获取的就是 CSV 文件的第一行。
    headers = next(reader)
    # 遍历 CSV 文件的表头字段。
    for header in headers:
        # if header =='keywords':
        #     continue
        # 为创建表的 SQL 语句添加新的字段定义。每个字段的数据类型设置为 VARCHAR(255)，
        # 表示该字段可以存储最大长度为 255 的字符串。字段名就是 CSV 文件的表头字段名。
        create_table_query += f"{header} VARCHAR(255), "
    # 移除 SQL 语句末尾多余的逗号和空格，然后添加右括号，完成创建表的 SQL 语句。
    create_table_query = create_table_query.rstrip(", ") + ")"
    # 使用游标对象执行创建表的 SQL 语句。如果表不存在，该语句会在数据库中创建一个新的表。
    mycursor.execute(create_table_query)

# 读取 CSV 文件并插入数据
# 再次打开 CSV 文件，以只读模式进行操作，用于读取文件中的数据行。
with open(r"D:\aguo\数据集\临时\archive\Titanic-Dataset.csv", 'r',encoding='utf-8') as csvfile:
    # 创建一个新的 CSV 文件读取器对象。
    reader = csv.reader(csvfile)
    # 再次读取 CSV 文件的第一行（表头），这里只是为了获取表头字段名。
    headers = next(reader)
    # 将表头字段名用逗号连接成一个字符串，用于后续的 INSERT 语句中的列名部分。
    columns = ', '.join(headers)
    # 根据表头字段的数量，生成相应数量的占位符 '%s'，用于 INSERT 语句中的值部分。
    # 每个 '%s' 代表一个待插入的值。
    placeholders = ', '.join(['%s'] * len(headers))
    # 构建插入数据的 SQL 语句，使用 f-string 格式化字符串，将表名、列名和占位符组合在一起。
    insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    # 遍历 CSV 文件中的每一行数据（除了表头）。
    for row in reader:
        # del row[4]
        print(row)
        print(type(row))
        # 使用游标对象执行插入数据的 SQL 语句，并将当前行的数据作为参数传递给该语句。
        # 这里的 row 是一个列表，包含了当前行的各个字段值。
        mycursor.execute(insert_query, row)

# 提交更改并关闭连接
# 将之前执行的所有 SQL 语句（如创建表、插入数据等）所做的更改提交到数据库中。
# 在 MySQL 中，默认情况下，对数据库的修改操作需要手动提交才能生效。
mydb.commit()
# 关闭游标对象，释放相关资源。游标使用完后应该及时关闭，避免占用不必要的资源。
mycursor.close()
# 关闭数据库连接，释放与数据库服务器的连接资源。
mydb.close()