from fileserviceinterface import FileServiceInterface
from firebasefileservice import FirebaseFileStore
from systemfileservice import SystemFileStore

FIREBASE = 'firebase'
SYSTEM = 'system'
def get_file_service(service_type) -> FileServiceInterface:
    if(service_type == FIREBASE):
        return FirebaseFileStore()
    elif(service_type == SYSTEM):
        return SystemFileStore()
    else:
        raise Exception("Unknown service type.")