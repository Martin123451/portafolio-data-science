from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os # Módulo para interactuar con el sistema operativo (rutas de archivos)
from datetime import datetime

# --- Configuración de la Aplicación Flask ---
app = Flask(__name__)

# Configuración de la base de datos SQLite
# os.path.abspath(__file__) obtiene la ruta absoluta de app.py
# os.path.dirname(...) obtiene el directorio de app.py
# os.path.join(...) une rutas de forma segura para diferentes SO
# Esto asegura que la base de datos se cree en la raíz de tu proyecto
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'site.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Para deshabilitar eventos de seguimiento de SQLAlchemy (no necesarios para nosotros)

db = SQLAlchemy(app)

# --- Modelos de Base de Datos (Tablas) ---
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    technologies = db.Column(db.String(200), nullable=False) # Separadas por coma: "Python, Flask, SQL"
    # url = db.Column(db.String(200), nullable=True) # Si tienes un enlace externo al proyecto

    def __repr__(self):
        return f'<Project {self.title}>'

class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
    date_sent = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<ContactMessage {self.email}>'

# --- Rutas (Endpoints) de la Aplicación ---

# Ruta para la página de inicio (portafolio)
@app.route('/')
def index():
    # Aquí podríamos consultar proyectos de la BD en el futuro
    # Por ahora, renderizamos la plantilla estática
    return render_template('index.html')

# Ruta para manejar el formulario de contacto (POST)
@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        new_message = ContactMessage(name=name, email=email, message=message)
        try:
            db.session.add(new_message)
            db.session.commit()
            # Puedes añadir un mensaje flash para el usuario aquí
            return redirect(url_for('index', success=True)) # Redirige a la página principal con un parámetro de éxito
        except Exception as e:
            # Manejo de errores, por ejemplo, rollback de la transacción
            db.session.rollback()
            print(f"Error al guardar mensaje: {e}") # Imprimir error en consola del servidor
            return redirect(url_for('index', error=True)) # Redirige con un parámetro de error

# --- Ejecución de la Aplicación ---
if __name__ == '__main__':
    # Esto creará las tablas de la base de datos si no existen
    # NECESITAS EJECUTAR ESTO AL MENOS UNA VEZ PARA QUE SE CREE LA DB
    with app.app_context():
        db.create_all()
    app.run(debug=True) # debug=True permite recarga automática y depuración