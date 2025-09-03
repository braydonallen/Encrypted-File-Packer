#!/usr/bin/env python
from cryptography.fernet import Fernet
import base64, gzip
import sys

code = '''#!/usr/bin/env python
from cryptography.fernet import Fernet
import base64, gzip

blob = {1}{0}{1}
key = {1}{2}{1}

f = Fernet(key)

code = blob.encode('utf-8')
code = f.decrypt(code)
code = gzip.decompress(code)
code = code.decode('utf-8')

exec(code)
'''

if len(sys.argv) != 2:
    print(f'err: incorrent num of arguments (expected 2, got {len(sys.argv)})')
    exit(-1)

with open(sys.argv[1], 'r') as file:
    contents = file.read()

    txt = contents.encode('utf-8')
    txt = gzip.compress(txt)

    key = Fernet.generate_key()
    f = Fernet(key)
    txt = f.encrypt(txt)

    txt = txt.decode('utf-8')

    txt = code.format(txt, "'''", key.decode('utf-8'))

    print(txt)
