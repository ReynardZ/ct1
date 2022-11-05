from sqlalchemy import create_engine
from sqlalchemy.sql import text
import os


class Models:
    # checked
    def __init__(self):
        SQLALCHEMY_DATABASE_URI = 'postgresql://sfgfsntzceuzfr:2308dd0efa4e1ef829c8ed17b481707285d8a0ee81a92a020cda7339c51a751a@ec2-35-170-21-76.compute-1.amazonaws.com:5432/dek4ggasgftq1t'
        self.engine = create_engine(SQLALCHEMY_DATABASE_URI)

    def execute_sql(self, statement, parameters={}):
        with self.engine.connect() as connection:
            out = connection.execute(text(statement), parameters)
        connection.close()
        return out

    # checked
    def initialize(self):
        self.execute_sql("CREATE TABLE IF NOT EXISTS users ("
                         "email TEXT PRIMARY KEY, "
                         "password TEXT NOT NULL, "
                         "area varchar(32), "
                         "age varchar(8)"
                         ");")
        self.execute_sql("create table if not exists ticket_type_dimension ("
                         "ticket_number varchar(16) primary key, "
                         "ticket_price float not null,"
                         "ticket_class varchar(16) not null"
                         ");")
        self.execute_sql("create table if not exists host_dimension ("
                         "venue_id varchar(64) primary key, "
                         "schedule_time varchar(64) not null, "
                         "mask_restriction boolean not null, "
                         "venue_address varchar(64) not null, "
                         "venue_name varchar(64) not null"
                         ");")
        self.execute_sql(" create table if not exists concert_dimension ("
                         "concert_id varchar(128) primary key, "
                         "concert_name varchar(256) not null, "
                         "genre varchar(128) not null, "
                         "artist_name varchar(256) not null"
                         ");")
        self.execute_sql("create table if not exists date_dimension ("
                         "date varchar(64) primary key, "
                         "anniversary boolean not null"
                         ");")
        self.execute_sql(" create table if not exists aggregated_fact_table ("
                         "ticket_number varchar(16) references ticket_type_dimension(ticket_number) on update cascade on delete cascade deferrable initially deferred, "
                         "venue_id varchar(64) references host_dimension(venue_id) on update cascade on delete cascade deferrable initially deferred, "
                         "concert_id varchar(128) references concert_dimension(concert_id) on update cascade on delete cascade deferrable initially deferred, "
                         "date varchar(128) references date_dimension(date) on update cascade on delete cascade deferrable initially deferred, "
                         "sales_quantity int , sales_revenue float, primary key (ticket_number,date, venue_id, concert_id)"
                         ");")
        self.execute_sql("create table if not exists aggregated ("
                         "sales_quantity int ,"
                         "sales_revenue float "
                         ");")

    def create_user(self, values):
        try:
            self.execute_sql("INSERT INTO users (email, password, area, age) "
                             "VALUES (:email,:password, :area, :age)",
                             values
                             )
        except Exception as error:
            raise error

    def get_user_password(self, email):
        user = self.execute_sql(
            "SELECT * FROM users WHERE email='{}';".format(email),
        ).mappings().all()
        if len(user) == 0:
            raise Exception("Invalid User name. Please check or register.")
        else:
            return user[0].password

    def get_concerts_data(self):
        result = self.execute_sql("SELECT Concert_id, Concert_Name, Genre, Artist_Name FROM CONCERT_DIMENSION "
                                  "ORDER BY CONCERT_ID LIMIT 25").mappings().all()
        return result

    def add_concert(self, value):
        self.execute_sql("INSERT INTO CONCERT_DIMENSION (concert_id, concert_name, genre, artist_name) VALUES"
                         "(:id, :name, :genre, :artist)", value)

    def advanced_search(self, statement):
        with self.engine.connect() as connection:
            result = connection.execute(text(statement))
        return len(result), result

    def delete_data(self, c_id):
        self.execute_sql("DELETE FROM concert_dimension WHERE concert_id='{}'".format(c_id))

    def update_data(self, c_id, name, genre, artist):
        self.execute_sql("UPDATE concert_dimension SET concert_name = '{}', genre='{}', artist_name='{}' "
                         "WHERE concert_id='{}';".format(name, genre, artist, c_id))
