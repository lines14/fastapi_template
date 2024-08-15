import sys
import subprocess
from datetime import datetime

def create_migration(name, version):
    command = [
        "alembic", "revision",
        "--message", name,
        "--rev-id", version
    ]
    subprocess.run(command, check=True)

if len(sys.argv) < 2:
    print("Usage: migration 'name'")
    sys.exit(1)

name = sys.argv[1]
version = datetime.now().strftime("%Y_%m_%d_%H%M%S")
create_migration(name, version)