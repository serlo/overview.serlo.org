#!/bin/bash

# Create output directory
mkdir -p out

# Create main HTML file
python create_team_report.py > out/index.html

# Get additional files like CSS and JS
curl 'https://de.serlo.org/favicon.ico' > out/favicon.ico

curl 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css' > out/style.css
curl 'http://getbootstrap.com/docs/4.0/examples/dashboard/dashboard.css' >> out/style.css
curl 'https://cdn.datatables.net/1.10.16/css/jquery.dataTables.css' >> out/style.css

curl 'https://code.jquery.com/jquery-3.2.1.min.js' > out/script.js
curl 'https://cdn.datatables.net/1.10.16/js/jquery.dataTables.js' >> out/script.js
