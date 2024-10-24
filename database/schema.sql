DROP TABLE IF EXISTS game, game_mode, hero;

CREATE TABLE hero(
    hero_id SMALLINT UNIQUE NOT NULL,
    hero_name VARCHAR(30) NOT NULL,
    PRIMARY KEY (hero_id)
);

CREATE TABLE game_mode(
    game_mode_id SMALLINT UNIQUE NOT NULL,
    game_mode_name VARCHAR(50) NOT NULL,
    PRIMARY KEY (game_mode_id)
);

CREATE TABLE game(
    game_id BIGINT UNIQUE NOT NULL,
    is_radiant BOOLEAN NOT NULL,
    radiant_won BOOLEAN NOT NULL,
    duration BIGINT NOT NULL,
    time TIMESTAMPTZ NOT NULL,
    kills SMALLINT NOT NULL,
    deaths SMALLINT NOT NULL,
    assists SMALLINT NOT NULL,
    hero_id SMALLINT NOT NULL,
    game_mode_id SMALLINT NOT NULL,
    PRIMARY KEY (game_id),
    FOREIGN KEY (hero_id) REFERENCES hero(hero_id),
    FOREIGN KEY (game_mode_id) REFERENCES game_mode(game_mode_id)
);