import sys
import subprocess
from datetime import datetime

def create_migration(name, version):
    command = [
        "alembic", "revision",
        "--message", name,
        "--rev-id", version,
        "--version-path", "database/migrations"
    ]
    subprocess.run(command, check=True)

def create_seeder(name, version):
    command = [
        "alembic", "revision",
        "--message", name,
        "--rev-id", version,
        "--version-path", "database/seeders"
    ]
    subprocess.run(command, check=True)

if len(sys.argv) < 3:
    if sys.argv[1] == '--migration':
        print("Usage: migration 'name'")
    else:
        print("Usage: seeder 'name'")
    sys.exit(1)

name = sys.argv[2]
version = datetime.now().strftime("%Y_%m_%d_%H%M%S")

if len(sys.argv) == 3 and sys.argv[1] == '--migration':
    create_migration(name, version)
else:
    create_seeder(name, version)