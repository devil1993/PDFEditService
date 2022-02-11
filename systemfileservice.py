from hasher import compute_hash
import os
from fileserviceinterface import FileServiceInterface

class SystemFileStore(FileServiceInterface):
	def __init__(self, basedir = '.') -> None:
		self.basedir = basedir

	def save_file(self, file_storage_object) -> str:
		fstream = file_storage_object.read()
		print("File read")
		# print(fstream)
		hash = compute_hash(fstream)
		print("Hash Computed: ")
		print(hash)
		path = os.path.join(self.basedir, str(hash))
		f = open(path, 'wb')
		f.write(fstream)
		f.close()
		return hash

		
	def search_file(self, filename):
		if(filename in os.listdir(self.basedir)):
			return (True,filename)
		else:
			return (False, 'Not found')
