# "Database code" for the DB Forum.

import psycopg2
import datetime
import bleach

def get_posts():
  """Return all posts from the 'database', most recent first."""
  conn = psycopg2.connect("dbname=forum")
  cursor = conn.cursor()
  cursor.execute("select content, time from posts order by time desc")
  all_posts = cursor.fetchall()
  clean_posts = bleach.clean(all_posts)
  conn.close()
  return clean_posts

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  conn = psycopg2.connect("dbname=forum")
  cursor = conn.cursor()
  one_post = content
  cursor.execute("insert into posts values (%s)", (one_post,))
  conn.commit()
  conn.close()
