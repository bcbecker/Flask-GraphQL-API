from api import create_app
import populate_db

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    populate_db()
