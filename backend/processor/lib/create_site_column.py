from db import MySQL as DB
from constants import config
from common import url_to_json

def update_newsite(db):
  limit = 1000
  skip = 0

  while True:
    rows = db.fetchall("select id, url from taobao where id <= %s and id > %s", (limit + skip, skip))
    if not len(rows): break
    skip += limit

    for row in rows:
      id, url = row
      if not url: continue
      obj = url_to_json(url)
      if obj is None: continue
      db.execute("update taobao set newsite=%s where id = %s", (obj['host'], id))

    db.commit()

  db.close()

def main():
  db = DB(config)
  update_newsite(db)

if __name__ == '__main__':
  main()
