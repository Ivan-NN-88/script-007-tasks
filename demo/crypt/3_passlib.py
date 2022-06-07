
# https://passlib.readthedocs.io/en/stable/

from passlib.hash import pbkdf2_sha256

# generate new salt, and hash a password
hash = pbkdf2_sha256.hash("secret1") # $pbkdf2-sha256$29000$gJBSqhWC8D6HsDZmbE0JwQ$MsTilUtkSkfR4jZdCGJy28Vjesz4490yjp3.FALk9vk

# verifying the password
assert pbkdf2_sha256.verify("secret1", hash)
assert not pbkdf2_sha256.verify("secret2", hash)

