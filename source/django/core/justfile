# This is a Justfile.
# A Justfile is used with the "just" command-line tool to define and run project tasks.
# Each section (like "install", "clean", "run") is a shortcut for a group of commands,
# so you don’t have to type them manually every time.
# Example: run "just install" in the terminal to set up the project.
#
# To install "just":
# Visit: https://github.com/casey/just
# Or install using a package manager:
#   - macOS (Homebrew): brew install just
#   - Ubuntu/Debian: sudo apt install just
#   - Windows (Scoop): scoop install just
# 
# you can install it too via executable, just visit: https://github.com/casey/just/releases/latest
#
# After installing, you can run commands like:
#   just install
#   just run
# To see explanation of each command run the command
# just --list

# to run this scripts is required to install uv
# https://github.com/astral-sh/uv

# Run Django development server
dev:
    source ./.venv/Scripts/activate
    uv run python manage.py runserver

# Collect static files
static:
    source ./.venv/Scripts/activate
    uv run python manage.py collectstatic --no-input

# Run migrations
migrate:
    source ./.venv/Scripts/activate
    uv run python manage.py migrate

# Install dependencies from requirements.txt
install:
    uv venv
    source ./.venv/Scripts/activate
    uv pip install -r requirements.txt

activatevenv:
    source ./.venv/Scripts/activate

deactivatevenv:
    deactivate

# remove virtual environment 
clean:
    rm -rf .venv

checkdbconnection:
    source ./.venv/Scripts/activate
    uv run python manage.py check

createapp:
    source ./.venv/Scripts/activate
    uv run python manage.py startapp appname ./applications/appname

createadminuser:
    source ./.venv/Scripts/activate
    # uv run python manage.py migrate
    uv run python manage.py createsuperuser
