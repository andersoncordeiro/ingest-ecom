from sqlalchemy import create_engine
from decouple import config

HOST     = config('HOST')
DATABASE = config('DATABASE')
USER     = config('USER')
PASSWORD = config('PASSWORD')
PORT     = config('PORT')


string_conexao = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
conn_olist = create_engine(string_conexao)