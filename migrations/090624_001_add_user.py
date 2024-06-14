"""
    ADD user table 
"""

from yoyo import step

__depends__ = {}

steps = [
    step("""
        CREATE TABLE IF NOT EXISTS user (
         tg_id int index,
         first_name text NOT NULL,
         last_name text,
         username text,
         language_code text,
         is_premium bool default false,
         photo_url text

         amount int NOT NULL default 0,
         last_earn timestaptz
        );
    """),
    step("""
        DROP TABLE IF EXISTS users;
    """)
]


        CREATE TABLE IF NOT EXISTS user (
         id int primary key,
         tg_id int,
         first_name text NOT NULL,
         last_name text,
         username text,
         language_code text,
         is_premium bool default false,
         photo_url text,

         amount int NOT NULL default 0,
         last_earn timestamp with time zone
        );