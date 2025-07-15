from flask import Flask, render_template, request, redirect, url_for, flash
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
app.config['SECRET_KEY'] = 'una_clave_muy_secreta_y_larga_que_deberias_cambiar_en_produccion'
# ¡IMPORTANTE! En un proyecto real, esta clave NO debe estar directamente aquí.
# Deberías cargarla desde una variable de entorno (ej. os.environ.get('SECRET_KEY')).
# Pero para desarrollo local, está bien por ahora. Asegúrate que sea una cadena compleja.

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
    phone_number = db.Column(db.String(50), nullable=True) # Nuevo campo para el teléfono
    message = db.Column(db.Text, nullable=False)
    date_sent = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<ContactMessage {self.email}>'

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    short_description = db.Column(db.String(250), nullable=False) # Descripción corta para la tarjeta
    full_description = db.Column(db.Text, nullable=False) # Descripción detallada para la página del servicio
    icon = db.Column(db.String(50), nullable=True) # Opcional: para un icono visual

    def __repr__(self):
        return f'<Service {self.title}>'

# --- Rutas (Endpoints) de la Aplicación ---

# Ruta para la página de inicio (portafolio)
@app.route('/')
def index():
    projects = Project.query.all()
    services = Service.query.all() # Nueva línea para obtener los servicios
    return render_template('index.html', projects=projects, services=services) # Pasa services a la plantilla

# Ruta para manejar el formulario de contacto (POST)
@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone_number = request.form.get('phone_number') # Usamos .get() por si el campo no se envía o es opcional
        message = request.form['message']

        new_message = ContactMessage(
            name=name,
            email=email,
            phone_number=phone_number, # ¡Asegúrate de añadir esto!
            message=message
        )
        try:
            db.session.add(new_message)
            db.session.commit()
            flash('¡Tu mensaje ha sido enviado con éxito! Te responderé pronto.', 'success') # 'success' es una categoría
            return redirect(url_for('index')) # Ya no necesitamos el parámetro 'success'
        except Exception as e:
            db.session.rollback()
            print(f"Error al guardar mensaje: {e}")
            flash('Hubo un error al enviar tu mensaje. Por favor, inténtalo de nuevo más tarde.', 'error') # 'error' es otra categoría
            return redirect(url_for('index')) # Ya no necesitamos el parámetro 'error'
        
# Ruta para la página de detalle de un proyecto
@app.route('/project/<int:project_id>')
def project_detail(project_id):
    # Busca el proyecto por su ID. Si no lo encuentra, devuelve un error 404.
    project = Project.query.get_or_404(project_id)
    return render_template('project_detail.html', project=project)

@app.route('/service/<int:service_id>')
def service_detail(service_id):
    service = Service.query.get_or_404(service_id)
    return render_template('service_detail.html', service=service)

# --- Ejecución de la Aplicación ---
if __name__ == '__main__':
    # Esto creará las tablas de la base de datos si no existen
    # NECESITAS EJECUTAR ESTO AL MENOS UNA VEZ PARA QUE SE CREE LA DB
    with app.app_context():
        db.create_all()
    app.run(debug=True) # debug=True permite recarga automática y depuración