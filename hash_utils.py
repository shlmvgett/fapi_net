import bcrypt


def get_hash(pwd: str):
    pwd_bytes = pwd.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pwd_bytes, salt)


def check_hash(input_value: str, hash: bytes):
    input_value_bytes = input_value.encode('utf-8')
    return bcrypt.checkpw(input_value_bytes, hash)

