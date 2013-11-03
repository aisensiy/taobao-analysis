from db import MySQL as DB
from constants import config
from common import md5

table_name = 'taobao'

def update_md5(db):
  limit = 1000
  skip = 0

  while True:
    rows = db.fetchall("select id, url from " + table_name + " where id <= %s and id > %s", (limit + skip, skip))

    if not len(rows): break

    skip += limit

    for row in rows:
      id, url = row
      if not url: continue
      db.execute("update " + table_name + " set url_md5='%s' where id = '%s'", (md5(url), id))

    db.commit()

  db.close()

def main():
  db = DB(config)
  update_md5(db)

if __name__ == '__main__':
  main()
