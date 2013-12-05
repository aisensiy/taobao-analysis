import os

if os.environ.get('PYTHON_ENV', '') == 'production':
  config = {
    'host': 'localhost',
    'user': 'kv',
    'passwd': 'kvlab2013',
    'port': 3306,
    'charset': 'utf8',
    'db': 'spide'
  }
else:
  config = {
    'host': 'localhost',
    'user': 'root',
    'passwd': '000000',
    'port': 3306,
    'charset': 'utf8',
    'db': 'spider'
  }

if __name__ == '__main__':
  print config
