# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class MyspiderPipeline:

    def __init__(self):
        # 连接数据库的配置
        self.conn = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='123456',
            db='spider',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.conn.cursor()
    ## 爬虫文件中提取数据的方法每yeild一次item，就会运行一次
    ## 该方法为固定名称函数
    ## procecss_item 方法处理完item 之后必须返回给引擎
    def process_item(self, item, spider):
        try:
            # 假设item中有'title', 'link', 'date'三个字段
            sql = """
            INSERT INTO users (title, link, date)
            VALUES (%s, %s, %s)
            """
            # 将item的字段值作为元组传入SQL语句
            self.cursor.execute(sql, (item.get('title'), item.get('link'), item.get('date')))
            self.conn.commit()
            print(f"Item stored in database: {item}")
        except Exception as e:
            print(f"Error storing item: {e}")
            self.conn.rollback()  # 发生错误时回滚事务
        finally:
            return item  # 不论是否成功，都返回item让Scrapy处理

    def close_spider(self, spider):
        """爬虫关闭时，关闭数据库连接"""
        self.cursor.close()
        self.conn.close()

