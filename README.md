## flask crud示例

flask-sqlalchemy、pymysql、sqlalchemy

## 参考文档

[flask-sqlalchemy](https://flask-sqlalchemy.readthedocs.io/en/stable/api/)



[sqlalchemy mysql数据类型](https://docs.sqlalchemy.org/en/20/dialects/mysql.html#mysql-data-types)

[sqlalchemy  orm](https://docs.sqlalchemy.org/en/20/orm/)

[orm query](https://docs.sqlalchemy.org/en/20/orm/queryguide/query.html#sqlalchemy.orm.Query)

[sqlalchemy 表关系](https://docs.sqlalchemy.org/en/20/orm/relationships.html)

[flask](https://dormousehole.readthedocs.io/en/latest/index.html#api)



## requirements.txt 生成 与使用

``` bash
pip freeze
pip freeze > requirements.txt

# 查找某个应用程序的所有模块
pip install pipreqs
pipreqs ./ # 根目录
# 自动生成requirements.txt 

# 进入程序目录, 执行命令 安装所有涉及到的组件
pip install -r requirements.txt
```





- TODO: 自定义异常处理装饰器