from db import MySQL as DB
from constants import config

def list_url(conn, urlpath, limit=5):
  """list #{limit} url which url's urlpath = #{urlpath}"""
  rows = conn.fetchall("select url from url where urlpath = %s limit %s", (urlpath, limit))
  return [ row[0] for row in rows ]

def fetch_top_urlpath(conn, limit=100):
  rows = conn.fetchall("select urlpath from urlpath_count_for_taobao limit %s", (limit,))
  return [ row[0] for row in rows ]

def main():
  db = DB(config)
  urlpaths = fetch_top_urlpath(db, 100)
  for urlpath in urlpaths:
    rows = list_url(db, urlpath)
    print '\n'.join(rows)

if __name__ == '__main__':
  main()
