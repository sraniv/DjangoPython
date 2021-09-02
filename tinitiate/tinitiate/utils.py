"""
from django.utils.crypto import get_random_string


def generate_secret_key(env_file_name):
    env_file = open(env_file_name, "w+")
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    generated_secret_key = get_random_string(50, chars)
    env_file.write("SECRET_KEY = '{}'\n".format(generated_secret_key))
    env_file.close()
"""
#https://stackoverflow.com/questions/4664724/distributing-django-projects-with-unique-secret-keys

from django.core.management.utils import get_random_secret_key

def generate_secret_key(env_file_name):
    env_file = open(env_file_name, "w+")
    secret = "SECRET_KEY= " + "\"" + get_random_secret_key() + "\"" + "\n"
    env_file.write(secret)
    env_file.close()