-- migrate up 
CREATE TABLE IF NOT EXISTS checks(
  tg_id int,
  is_telegram_subscribed bool default false,
  is_twitter_subscribed bool default false,
  is_discord_subscribed bool default false,
  is_linkedin_subscribed bool default false,
  is_instagram_subscribed bool default false,
  is_youtube_subscribed bool default false,
  CONSTRAINT fk_tg_id
    FOREIGN KEY (tg_id)
      REFERENCES user(tg_id)
      ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS checks_tg_id_index on checks(tg_id);

-- migrate down

DROP INDEX checks_tg_id_index;
DROP TABLE check;
