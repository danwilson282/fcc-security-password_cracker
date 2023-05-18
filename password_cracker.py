import hashlib

def crack_sha1_hash(hash, use_salts=False):
    f = open('top-10000-passwords.txt', 'r')
    s = open('known-salts.txt', 'r')
    passwords = f.read().split('\n')
    salts = s.read().split('\n')
    #print(salts)
    if use_salts==False:
        for password in passwords:
        
            hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest()
            if hashed_password==hash:
                return password
    else:
        for password in passwords:
            for salt in salts:
                pre_pwd = salt+password
                app_pwd = password+salt
                preapp_pwd = salt+password+salt
                hashed_password1 = hashlib.sha1(pre_pwd.encode('utf-8')).hexdigest()
                hashed_password2 = hashlib.sha1(app_pwd.encode('utf-8')).hexdigest()
                hashed_password3 = hashlib.sha1(preapp_pwd.encode('utf-8')).hexdigest()
                if hashed_password1==hash or hashed_password2==hash or hashed_password3==hash:
                    return password
    return "PASSWORD NOT IN DATABASE"