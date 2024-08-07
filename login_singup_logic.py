import argon2
import db_users as dbu


def hash_password(password):
    ph = argon2.PasswordHasher()
    return ph.hash(password)


def check_password(email, password):
    ph = argon2.PasswordHasher()
    hashed_password = dbu.get_hashed_password(email)
    if hashed_password != None:
        try:
            ph.verify(hashed_password, password)
            return True
        except:
            return False
    else:
        return False


def main_login(email, password):
    if check_password(email, password):
        return True
    else:
        return False


def sing_up(username, email, password):
    hashed_password = hash_password(password)
    if dbu.add_user(username, email, hashed_password):
        return True
    else:
        return False
