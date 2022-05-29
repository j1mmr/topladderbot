import os

from dotenv import load_dotenv, find_dotenv
#requires pip package python-find_dotenv

load_dotenv(find_dotenv())

print(os.getenv('test'))
