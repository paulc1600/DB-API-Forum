# "Database code" for the DB Forum.

import psycopg2
import datetime
import bleach

def get_posts():
  """Return all posts from the 'database', most recent first."""
  conn = psycopg2.connect("dbname=forum")
  cursor = conn.cursor()
  cursor.execute("select content, time from posts order by time desc")
  all_posts_list = cursor.fetchall()
  for one_post in all_posts_list:
    one_clean_post = ((),())
    # Use bleach to clean user content of post so no Jave Script injection attack
    one_clean_post = (bleach.clean(one_post[0]), one_post[1]) 
    all_clean_list.append(one_clean_post)
     
  conn.close()
  return all_clean_list

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  conn = psycopg2.connect("dbname=forum")
  cursor = conn.cursor()
  one_post = content
  # Must code this way to prevent SQL query injection attack / Bobby Tables fix
  cursor.execute("insert into posts values (%s)", (one_post,))
  conn.commit()
  conn.close()
