"""Script for generating an HTML report of all contacts."""

import sys

from datetime import datetime

import jinja2

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

    print(template.render(
        serlo=database,
        timestamp=datetime.now().strftime("%Y-%M-%d %H:%M")
    ))

if __name__ == "__main__":
    run_script(sys.argv[1:])
