import random
import time
import hashlib
RD_STRING="zyxwvutsrqponmlkjihgfedcba1234567890"
def generate_token(key,app_key=None):
    timestatmp=int(time.time())
    key = key + str(timestatmp)
    if app_key:
        key+=app_key
    key+="".join(random.sample(RD_STRING,5))
    hl = hashlib.md5()
    hl.update(key.encode("utf8"))  # 指定编码格式，否则会报错
    token = hl.hexdigest()
    return token
# print(generate_token('ac'))