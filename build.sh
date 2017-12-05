#!/bin/bash

# Create output directory
mkdir -p out

# Create main HTML file
python create_team_report.py > out/index.html

# Get CSS and JS files
curl 'https://de.serlo.org/favicon.ico' > out/favicon.ico
curl 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css' > out/style.css
