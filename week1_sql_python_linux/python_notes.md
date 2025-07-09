## 1. 数据类型
- 整数（int）：如 1, 100, -5
- 浮点数（float）：如 3.14, -0.5
- 字符串（str）：文本，必须用引号包裹，如 "hello"
- 布尔值（bool）：True 或 False

## 2. 基本操作
```python
a = 10
b = 3.14
c = "数据工程"
d = True
```
## 3.列表
```python
my_list=[1,2,3,4]
```
## 4.dictionary
```python
my_dict=["name":"ming","age":"18"]
```
### 5.for if else
```python
for i in range(3):
print(i)
if a>5:
  print("a>5")
else:
  print("a!>5")
```
### 6.Sqlite operations
```python
import sqlite3
创建并连接sqlite
conn = sqlite3.connect('databaseName')
创建变量
Name = conn.cursor()
进行数据库操作
Name.execute(operations)
conn.commit()//提交操作,提交后数据库进行永久更改
```
### 7.pands库 operations
```python
.read_csv('name',encoding=)//读取文件
.dropna()//去除含有空的行
.drop_duplicates()//去除完全重复的行
.to_csv('name',index=,encoding=)//保存文件
index=Fales,不保存DateFrame的行标签,默认为保存
DataFrame是pands的核心数据结构,为一个二维表格,有行和列标签,每列的数据格式可以不同,可以进行一些列操作
```

