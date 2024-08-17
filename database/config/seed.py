import sys
import inspect
from dotenv import load_dotenv
from database.seeders import *

load_dotenv()

if len(sys.argv) < 2:
    print("Seed command: seed <seeder_class or all>")
    sys.exit(1)
else:
    seeder = sys.argv[1]
    if seeder == 'all':
        seeders_list = [cls for name, cls in globals().items() if inspect.isclass(cls)]
        for seeder in seeders_list:
            seeder()
    else:
        seeder()