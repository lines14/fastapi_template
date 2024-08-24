import os
import sys
from datetime import datetime
cwd = os.getcwd()

if len(sys.argv) < 2 or len(sys.argv) > 2:
    print("Create seeder command: seeder 'name'")
    sys.exit(1)
else:
    name = sys.argv[1]
    file_name = name.replace(' ', '_')
    class_name = ''.join([word.capitalize() for word in name.split()])
    version = datetime.now().strftime("_%Y_%m_%d_%H%M%S")
    print(f'  Generating /app/database/seeders/{version}_{file_name}.py ...  done')

    content = f"""from database.database import Database\n
class {class_name}():
    revision: str = '{version}'\n
    def __init__(self):
        database = Database()
        database.seed([
            # Add your seed data here
        ])
"""

    with open(os.path.join(cwd, 'database/seeders', version + '_' + file_name + '.py'), 'w') as file:
        file.write(content)
    with open(os.path.join(cwd, 'database/seeders/__init__.py'), 'a') as file:
        file.write(f'\nfrom .{version}_{file_name} import {class_name}')