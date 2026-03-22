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

# Set up the project (create venv and install dependencies)
install: 
  @ echo creating virtual environment
  python -m venv .venv
  @ echo installing dependencies
  ./.venv/Scripts/pip install -r requirements.txt
  @ echo done

# Remove generated files (venv and database)
clean:
  @ echo removing virtual environment
  rm -rf .venv
  @ echo deleting db.sqlite3 file
  rm -rf db.sqlite3

# Run the app in development mode
run:
  @ echo running app in development mode
  ./.venv/Scripts/python manage.py runserver
