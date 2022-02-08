# def compute_hash(file):
# 	import hashlib
# 	BLOCKSIZE = 65536
# 	hasher = hashlib.sha256()
# 	with open(file, 'rb') as afile:
# 	    buf = afile.read(BLOCKSIZE)
# 	    while len(buf) > 0:
# 	        hasher.update(buf)
# 	        buf = afile.read(BLOCKSIZE)
# 	print(hasher.hexdigest())

def compute_hash(content):
	import hashlib
	hasher = hashlib.sha256()
	hasher.update(content)
	print(hasher.hexdigest())
	return hasher.hexdigest()