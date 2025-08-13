from hashlib import *

message = "AAAA".encode()

print(sha224(message).hexdigest())