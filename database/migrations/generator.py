import sys
import subprocess
from datetime import datetime

def create_migration(name, revision):
    command = [
        "alembic", "revision",
        "--message", name,
        "--rev-id", revision
    ]
    subprocess.run(command, check=True)

if len(sys.argv) < 2:
    print("Usage: migration 'name'")
    sys.exit(1)

name = sys.argv[1]
revision = datetime.now().strftime("%Y_%m_%d_%H%M%S")
create_migration(name, revision)