import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class StorageUtils:
    def get_JWT(path: str) -> str:
        return '../storage/JWT/' + path