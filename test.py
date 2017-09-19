
import hashlib

word = "bird"
m = hashlib.sha224()
print m
m.update(word)
print m
print m.hexdigest()
