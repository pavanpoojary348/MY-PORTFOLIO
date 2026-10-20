import os
import sys

# Add project root directory to sys.path so app and its templates/static are properly located
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from app import app

# Vercel looks for the WSGI application instance named `app`
if __name__ == "__main__":
    app.run()
