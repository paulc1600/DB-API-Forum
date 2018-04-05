# "Database code" for the DB Forum.

import psycopg2
import datetime

def get_posts():
  """Return all posts from the 'database', most recent first."""
  conn = psycopg2.connect("dbname=forum")
  cursor = conn.cursor()
  cursor.execute("select content, time from posts order by time desc")
  conn.close()
  return cursor.fetchall()

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  conn = psycopg2.connect("dbname=forum")
  cursor = conn.cursor()
  cursor.execute("insert into posts values ('%s')" % content)
  conn.commit()
  conn.close()
