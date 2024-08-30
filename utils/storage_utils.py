import os
import classutilities
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class StorageUtils():
    @classutilities.classproperty
    def private_key(cls) -> str:
        with open('../storage/JWT/private.pem') as file:
            return file.read()
    
    @classutilities.classproperty
    def public_key(cls) -> str:
        with open('../storage/JWT/public.pem') as file:
            return file.read()