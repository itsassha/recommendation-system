CREATE TABLE ratings_table (
    user_id INT NOT NULL,
    item_id INT NOT NULL,
    rating FLOAT NOT NULL,
    PRIMARY KEY (user_id, item_id)
);
