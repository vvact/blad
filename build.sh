#!/usr/bin/env bash

# Exit immediately if a command exits with a non-zero status
set -e

# Install dependencies
# Modify the following line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt
# Uncomment if using Poetry:
# poetry install

# Convert static asset files
# Replace "your_static_folder" and "your_dist_folder" with actual folder names
python manage.py collectstatic --noinput

# Apply any outstanding database migrations
python manage.py migrate

# # Create a distribution package
# python setup.py sdist bdist_wheel

# # Create a source distribution package
# python setup.py sdist

# # Create a binary distribution package (already included in bdist_wheel above; can be omitted if unnecessary)