import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Logger:
    @staticmethod
    def log(str: str) -> str:
        with open('../log.txt', 'a', encoding='utf-8') as file:
            file.write(str + '\n')