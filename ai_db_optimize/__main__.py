import sys
import os

# If running as 'python ai_db_optimize', ensure the directory's parent is in path
# so we can import 'ai_db_optimize' as a package.
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

try:
    from ai_db_optimize.main import analyze
except ImportError:
    # Fallback for some execution contexts
    try:
        from .main import analyze
    except ImportError:
        # If relative import fails, try absolute import assuming main is in path (run as script)
        import main
        analyze = main.analyze

import typer

if __name__ == "__main__":
    typer.run(analyze)
