import subprocess
import sys

def dump(url):
    try:
        return subprocess.Popen(['pg_dump', url], stdout=subprocess.PIPE)
    except OSError as err:
        print(f"Error: {err}")
        sys.exit(1)


def dump_file_name(url, timestamp=None):
    db_name = url.split('/')[-1]
    db_name = db_name.split('?')[0]

    return f"{db_name}{('-' + timestamp) if timestamp else ''}.sql"

