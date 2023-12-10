import binascii
import secrets
import hashlib
import os
import bcrypt

class Random_generator:

    # generates a random token using the secrets library for true randomness
    def generate_token(self, length=8, alphabet=(
    '0123456789'
    'abcdefghijklmnopqrstuvwxyz'
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    )):
        return ''.join(secrets.choice(alphabet) for i in range(length))

    # generates salt using the bcrypt library which is a safe implementation
    def generate_salt(self, rounds=12):
        return bcrypt.gensalt(rounds)

class bcrypt_hasher:

    # produces the password hash by combining password + salt because hashing
    def password_hash(self, password, salt):
        password = binascii.hexlify(password.encode())
        password_hash = bcrypt.hashpw(password, salt)
        return password_hash.decode('ascii')

    # verifies that the hashed password reverses to the plain text version on verification
    def password_verification(self, password, password_hash):
        password = binascii.hexlify(password.encode())
        password_hash = password_hash.encode('ascii')
        return bcrypt.checkpw(password, password_hash)

# a collection of sensitive secrets necessary for the software to operate
PRIVATE_KEY = os.environ.get('PRIVATE_KEY')
PUBLIC_KEY = os.environ.get('PUBLIC_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')
PASSWORD_HASHER = 'bcrypt_hasher'

