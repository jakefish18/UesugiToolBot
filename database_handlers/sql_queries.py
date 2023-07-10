"""All sql queries to the database in this file."""

from typing import Tuple


# Users table queries.
CREATE_USERS_TABLE = "CREATE TABLE IF NOT EXISTS users(" \
                        "user_id serial," \
                        "telegram_id bigint," \
                        "learning_session_id bigint" \
                        ")"
ADD_USER = "INSERT INTO users (telegram_id) VALUES (%s)"
GET_USER = "SELECT * FROM users WHERE telegram_id=%s"
GET_USER_ID = "SELECT user_id FROM users WHERE telegram_id=%s"
SET_USER_LEARNING_SESSION_ID = "UPDATE users SET learning_session_id=%s WHERE user_id=%s"

# Learning collections table queries.
CREATE_USER_LEARNING_COLLECTIONS_TABLE = "CREATE TABLE IF NOT EXISTS user_learning_collections(" \
                              "learning_collection_id serial," \
                              "learning_collection_name text," \
                              "user_id bigint" \
                              ")"
ADD_USER_LEARNING_COLLECTIONS = "INSERT INTO user_learning_collections (learning_collection_name, user_id) VALUES " \
                          "(%s, %s)"
GET_USER_LEARNING_COLLECTION_ID = "SELECT * FROM user_learning_collections WHERE user_id=%s AND learning_collection_name=%s"
GET_USER_LEARNING_COLLECTION_NAMES = "SELECT learning_collection_name FROM user_learning_collections WHERE user_id=%s"

# Learning collection items table queries.
CREATE_LEARNING_COLLECTION_ITEMS_TABLE = "CREATE TABLE IF NOT EXISTS learning_collection_items(" \
                                   "card_id serial," \
                                   "learning_collection_id bigint," \
                                   "card_question text," \
                                   "card_answer text" \
                                   ")"
ADD_LEARNING_COLLECTION_ITEMS = "INSERT INTO learning_collection_items " \
                                "(learning_collection_id, card_question, card_answer) VALUES %s"
GET_LEARNING_COLLECTION_CARD_IDS = "SELECT card_id FROM learning_collection_items WHERE learning_collection_id=%s"
GET_CARD = "SELECT card_question, card_answer FROM learning_collection_items WHERE card_id=%s"

# User learning sessions table queries.
CREATE_USER_LEARNING_SESSIONS_TABLE = "CREATE TABLE IF NOT EXISTS user_learning_sessions(" \
                             "learning_session_id serial," \
                             "user_id bigint," \
                             "learning_collection_id bigint" \
                             ")"
CREATE_USER_LEARNING_SESSION = "INSERT INTO user_learning_sessions (user_id, learning_collection_id) " \
                               "VALUES (%s, %s) RETURNING learning_session_id"

# Learning sessions table queries.
CREATE_LEARNING_SESSIONS_TABLE = "CREATE TABLE IF NOT EXISTS learning_sessions(" \
                                "learning_session_id bigint," \
                                "card_id bigint," \
                                "passed boolean DEFAULT false" \
                                ")"
ADD_LEARNING_SESSION_CARDS = "INSERT INTO learning_sessions (learning_session_id, card_id) VALUES %s"
GET_RANDOM_UNANSWERED_CARD = "SELECT card_id FROM learning_sessions WHERE learning_session_id=%s AND passed=false ORDER BY random() limit 1"
GET_RANDOM_CARDS = "SELECT card_id FROM learning_sessions WHERE learning_session_id=%s AND card_id!=%s ORDER BY random() limit %s"
