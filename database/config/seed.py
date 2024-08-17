import sys
import inspect
from dotenv import load_dotenv
from database.seeders import *

load_dotenv()

if len(sys.argv) < 2:
    print("Seed command: seed <seeder_class or all>")
    sys.exit(1)
else:
    seeder_name = sys.argv[1]
    if seeder_name == 'all':
        seeders_list = [cls for name, cls in globals().items() if inspect.isclass(cls)]
        for seeder in seeders_list:
            print(f'Run {seeder.__name__} seeder')
            seeder()
    else:
        seeder = globals().get(seeder_name)
        print(f'Run {seeder.__name__} seeder')
        seeder()