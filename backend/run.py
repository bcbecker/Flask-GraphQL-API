from api import create_app
from populate_db import populate_db

app = create_app()

if __name__ == "__main__":
    populate_db()
    app.run(host='0.0.0.0')
