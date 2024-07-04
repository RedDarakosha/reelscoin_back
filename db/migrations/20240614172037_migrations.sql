-- migrate:up
CREATE TABLE IF NOT EXISTS users (
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

CREATE INDEX IF NOT EXISTS tg_id_index ON users(tg_id);
-- migrate:down

