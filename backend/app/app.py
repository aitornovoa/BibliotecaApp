from backend.app import app, db
from flask import Flask

# Importa los modelos para que se reconozcan al crear la base de datos
from backend.app.models import Book
from backend.app import routes

if __name__ == '__main__':
    # Crear las tablas en la base de datos si no existen
    with app.app_context():
        db.create_all()
    # Ejecutar la aplicación Flask
    app.run(host='0.0.0.0', port=5000)
