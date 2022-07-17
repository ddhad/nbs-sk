import sqlite3
import os

class Articles:
    dicts = []
    db_path = os.getcwd()
    db_path = db_path.replace(r"FastAPI", "")
    db_path = db_path + r"ScrapyNbs_sk\articles.db"
    def __init__(self):
        try:
            con = sqlite3.connect(self.db_path)
            cursor = con.cursor()
            sql = "SELECT * FROM articles"
            cursor.execute(sql)
            rows = cursor.fetchall()
            cursor.close()
        except sqlite3.Error as e:
            print("Error Retrieving Results", e)
        finally:
            if con:
                con.close()
        for i, x in enumerate(rows):
            item = {
                "Id": i,
                "Title": x[1],
                "Url": x[2],
                "Labels": x[3],
                "Date": x[0],
                "Content": x[4]
            }
            self.dicts.append(item)
    def get_all(self):
        return self.dicts

    def get_one(self, id: int):

        return self.dicts[id]

    def del_one(self, id: int):
        item = self.dicts[id]['Url']
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        cur.execute('DELETE FROM articles WHERE url="'+item+'"')
        con.commit()
        con.close()
