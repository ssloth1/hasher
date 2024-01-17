import hashlib

# Below are the hash functions that are available to the user.

def hash_md5(password):
    return hashlib.md5(password.encode()).hexdigest()

def hash_sha1(password):
    return hashlib.sha1(password.encode()).hexdigest()

def hash_sha224(password):
    return hashlib.sha224(password.encode()).hexdigest()

def hash_sha256(password):
    return hashlib.sha256(password.encode()).hexdigest()

def hash_sha384(password):
    return hashlib.sha384(password.encode()).hexdigest()

def hash_sha512(password):
    return hashlib.sha512(password.encode()).hexdigest()

def hash_sha3_224(password):
    return hashlib.sha3_224(password.encode()).hexdigest()

def hash_sha3_256(password):
    return hashlib.sha3_256(password.encode()).hexdigest()

def hash_sha3_384(password):
    return hashlib.sha3_384(password.encode()).hexdigest()

def hash_sha3_512(password):
    return hashlib.sha3_512(password.encode()).hexdigest()

def hash_blake2b(password):
    return hashlib.blake2b(password.encode()).hexdigest()

def hash_blake2s(password):
    return hashlib.blake2s(password.encode()).hexdigest()

# SHAKE algorithms require a length parameter for the output hash
def hash_shake_128(password, length=128):
    return hashlib.shake_128(password.encode()).hexdigest(length)

def hash_shake_256(password, length=256):
    return hashlib.shake_256(password.encode()).hexdigest(length)

# Note: Users must specify the length for SHAKE algorithms when calling these functions
