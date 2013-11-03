from db import MySQL as DB
from constants import config
from common import md5
import datetime, time
import logging
logging.basicConfig(level=logging.INFO)

table_name = 'taobao'
uuid = 1
threshhold = 60 * 10 # 10 min

def uuid():
  uuid.counter += 1
  logging.info('set sessionid %d', uuid.counter)
  return uuid.counter

uuid.counter = 0

def timetoint(dt):
  return time.mktime(dt.timetuple())

def update_session(db, uid):
  limit = 1000
  skip  = 0

  last_date = 0
  ids_of_session = []

  while True:
    rows = db.fetchall("select id, date from " + table_name + " where uid=%s order by date limit %s offset %s", (uid, limit, skip))
    if not len(rows): break

    skip += limit

    for row in rows:
      id, date = row
      ts = timetoint(date)

      if last_date == 0 or ts - last_date < threshhold:
        ids_of_session.append(id)
      elif len(ids_of_session):
        add_sesionid(ids_of_session, uuid(), db)
        ids_of_session = [id]

      last_date = ts

  if len(ids_of_session): add_sesionid(ids_of_session, uuid(), db)

def add_sesionid(ids, sessionid, db):
  db.execute("update " + table_name + " set sessionid=%s where id IN (" + ", ".join(map(lambda x: str(x), ids)) + ")", sessionid)
  db.commit()


def main():
  db = DB(config)
  uids = map(lambda x: x[0], db.fetchall("select uid from users_have_records"))
  for uid in uids:
    update_session(db, uid)

if __name__ == '__main__':
  main()
