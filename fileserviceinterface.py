from typing import Tuple


class FileServiceInterface:
    def save_file(self, file_storage_object) -> str:
        pass
    def search_file(self, filename) -> Tuple[bool, str]:
        pass
