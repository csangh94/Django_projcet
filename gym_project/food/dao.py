import pymysql

def fooddao(food): # 정보 검색
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='1234', db='gym', charset='utf8')
    curs = conn.cursor()
    sql = "select * from food where food_name='"+food+"'"
    curs.execute(sql)
    rows = curs.fetchone()
    return rows
    conn.close()
def facility():
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='1234', db='gym', charset='utf8')
    curs = conn.cursor()
    sql = "select * from facility"
    curs.execute(sql)
    rows = curs.fetchall()
    return rows
    conn.close()
def test_facility(division):
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='1234', db='gym', charset='utf8')
    curs = conn.cursor()
    sql = "select * from facility where division='"+division+"'"
    curs.execute(sql)
    rows = curs.fetchall()
    return rows
    conn.close()

def serch_rank():
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='1234', db='gym', charset='utf8')
    curs = conn.cursor()
    sql = "select * from serch_rank order by countint desc limit 5"
    curs.execute(sql)
    rows = curs.fetchall()
    return rows