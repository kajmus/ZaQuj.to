import hashlib

def our_hash(password :str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

