#!/usr/bin/env python
from cryptography.fernet import Fernet
import gzip, sys, math, random, keyword, builtins, string, argparse

OPTIONS = {
    "encode": [
        "encode()",
        "encode('utf-8')",
        "encode(errors='strict')",
        "encode('utf8')",
        "encode('UTF-8')",
        "encode('cp65001')",
    ],

    "decode": [
        "decode()",
        "decode('utf-8')",
        "decode(errors='strict')",
        "decode('utf8')",
        "decode('UTF-8')",
        "decode('cp65001')",
    ],

    "decrypt": [
        "decrypt",
    ],

    "cryptography": [
        "import cryptography.fernet",
        "from cryptography import fernet",
    ],

    "alias": [],

    "decompress": [
        "decompress",
        "decompress ",
    ],
}

Chosen = {}

def random_alias(length=3):
    while True:
        first = random.choice(string.ascii_letters)
        rest = ''.join(random.choices(string.ascii_letters + string.digits + "_", k=length-1))
        name = first + rest
        if not keyword.iskeyword(name) and not hasattr(builtins, name):
            return name

def GetRandom(opt):
    if opt == "alias":
        return random_alias(random.randint(2,5))
    return random.choice(OPTIONS[opt])

for i in OPTIONS:
    Chosen[i] = GetRandom(i)

code_tpl = (
    "{crypt} as {alias};"
    "import gzip;"
    "exec(gzip.{decomp}({alias}.Fernet({key!r}).{decrypt}({cipher!r}.{encode})).{decode})"
)

code_base = code_tpl.format(
    crypt=Chosen["cryptography"],
    alias=Chosen["alias"],
    decomp=Chosen["decompress"],
    decrypt=Chosen["decrypt"],
    encode=Chosen["encode"],
    decode=Chosen["decode"],
    key="{KEY}",
    cipher="{CIPHER}",
)

ap = argparse.ArgumentParser()
ap.add_argument("src")
ap.add_argument("-o","--out", default="test.py")
args = ap.parse_args()

with open(args.src, 'r', encoding='utf-8') as file:
    contents = file.read()

    txt = contents.encode()
    txt = gzip.compress(txt)

    key = Fernet.generate_key()
    f = Fernet(key)
    txt = f.encrypt(txt)

    txt = txt.decode()

    final_code = code_base.format(
        KEY=key.decode(),
        CIPHER=txt
    )

    with open(args.out, "w", encoding="utf-8") as f:
        f.write(final_code)
