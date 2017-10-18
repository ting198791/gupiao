import pymysql.cursors
from gupiao import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

connection = pymysql.connect(host=MYSQL_HOSTS,
                             user=MYSQL_USER,
                             password=MYSQL_PASSWORD,
                             db=MYSQL_DB,
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)






class Sql:
    @classmethod
    def insert_house_sales(cls,corp_name,book_num,order_num,amount,ts):
     try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `house_sales` (`corp_name`, `book_num`,`order_num`,`amount`,`ts`) VALUES (%(corp_name)s, %(book_num)s,%(order_num)s,%(amount)s,%(ts)s)"
            value = {
                'corp_name': corp_name,
                'book_num': book_num,
                'order_num': order_num,
                'amount': amount,
                'ts': ts
            }
            cursor.execute(sql, value)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        # connection.commit()


     finally:
         connection.commit()

    def insert_gupiao(cls, code, name, market):
             try:
                 with connection.cursor() as cursor:
                     # Create a new record
                     sql = "INSERT INTO `gupiao` (`code`, `name`,`market`) VALUES (%(code)s, %(name)s,%(market)s)"
                     value = {
                         'code': code,
                         'name': name,
                         'market': market

                     }
                     cursor.execute(sql, value)

                     # connection is not autocommit by default. So you must commit to save
                     # your changes.
                     # connection.commit()


             finally:
                 connection.commit()
    #
    # @classmethod
    # def insert_dd_name(cls, xs_name, xs_author, category, name_id):
    #     sql = 'INSERT INTO dd_name (`xs_name`, `xs_author`, `category`, `name_id`) VALUES (%(xs_name)s, %(xs_author)s, %(category)s, %(name_id)s)'
    #     value = {
    #         'xs_name': xs_name,
    #         'xs_author': xs_author,
    #         'category': category,
    #         'name_id': name_id
    #     }
    #     cur.execute(sql, value)
    #     cnx.commit()
    #
    # @classmethod
    # def insert_dd_chaptername(cls, xs_chaptername, xs_content, id_name, num_id, url):
    #     sql = 'INSERT INTO dd_chaptername (`xs_chaptername`, `xs_content`, `id_name`, `num_id`, `url`) \
    #             VALUES (%(xs_chaptername)s, %(xs_content)s, %(id_name)s, %(num_id)s, %(url)s)'
    #     value = {
    #         'xs_chaptername': xs_chaptername,
    #         'xs_content': xs_content,
    #         'id_name': id_name,
    #         'num_id': num_id,
    #         'url': url
    #     }
    #     cur.execute(sql, value)
    #     cnx.commit()
    #
    # @classmethod
    # def id_name(cls, xs_name):
    #     sql = 'SELECT id FROM dd_name WHERE xs_name=%(xs_name)s'
    #     value = {
    #         'xs_name': xs_name
    #     }
    #     cur.execute(sql, value)
    #     for name_id in cur:
    #         return name_id[0]
    #
    # @classmethod
    # def select_name(cls, name_id):
    #     sql = "SELECT EXISTS(SELECT 1 FROM dd_name WHERE name_id=%(name_id)s)"
    #     value = {
    #         'name_id': name_id
    #     }
    #     cur.execute(sql, value)
    #     return cur.fetchall()[0]
    #
    # @classmethod
    # def sclect_chapter(cls, url):
    #     sql = "SELECT EXISTS(SELECT 1 FROM dd_chaptername WHERE url=%(url)s)"
    #     value = {
    #         'url': url
    #     }
    #     cur.execute(sql, value)
    #     return cur.fetchall()[0]