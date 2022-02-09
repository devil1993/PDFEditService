import pyrebase
from fileserviceinterface import FileServiceInterface
from firebase_config import config

class FirebaseFileStore(FileServiceInterface):
    def __init__(self, configuration = config) -> None:
        self.firebase = pyrebase.initialize_app(config)

    # def save_file(self, file_storage_object) -> str:
    #     fstream = file_storage_object.read()
    #     print(fstream)
    #     hash = compute_hash(fstream)
    #     print(hash)
    #     path = os.path.join(self.basedir, hash)
    #     f = open(path, 'wb')
    #     f.write(fstream)
    #     f.close()
    #     return hash

        
    # def search_file(self, filename):
    #     if(filename in os.listdir(self.basedir)):
    #         return (True,filename)
    #     else:
    #         return (False, 'Not found')
