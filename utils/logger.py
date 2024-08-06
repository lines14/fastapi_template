import os
cwd = os.getcwd()

class Logger:
    @staticmethod
    def log(str: str) -> str:
        with open(os.path.join(cwd, 'log.txt'), 'a') as file:
            file.write(str + '\n')