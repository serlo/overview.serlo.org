"""Script for generating an HTML report of all contacts."""

import sys

from datetime import datetime

import jinja2
import pytz

from serlo.model import SerloDatabase

def run_script(args):
    """Main function of the script."""
    try:
        database_file, template = args
    except ValueError:
        sys.exit(f"Error: Cannot parse arguments")

    database = SerloDatabase(database_file)
    env = jinja2.Environment(autoescape=True,
                             loader=jinja2.FileSystemLoader("."))

    template = env.get_template(template)
    timestamp = datetime.now().astimezone(pytz.timezone('Europe/Berlin'))

    print(template.render(
        serlo=database,
        timestamp=timestamp
    ))

if __name__ == "__main__":
    run_script(sys.argv[1:])
