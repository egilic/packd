# Flask entry point creates app and runs dev server
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)