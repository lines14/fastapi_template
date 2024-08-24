import os

class Logger:
    @staticmethod
    def log(str: str) -> str:
        with open(os.path.join(os.getcwd(), 'log.txt'), 'a') as file:
            file.write(str + '\n')