from app import app, db, Project, ContactMessage, Service # Asegúrate de importar Service
from datetime import datetime # No se usa directamente aquí, pero no molesta

with app.app_context():
    # OPCIONAL: Borra todas las tablas para empezar completamente limpio
    # SI DESCOMENTAS ESTO, BORRARÁ TODOS LOS PROYECTOS Y MENSAJES DE CONTACTO
    # db.drop_all() # ¡Esto borrará TODAS las tablas! Úsalo con precaución si tienes datos de ContactMessage
    db.create_all() # Re-crea todas las tablas, incluyendo la nueva de Service (si db.drop_all() fue usado)

    # Añadir o actualizar proyectos (sin image_url por ahora)
    existing_projects_count = Project.query.count()
    if existing_projects_count == 0:
        print("No se encontraron proyectos. Añadiendo proyectos de ejemplo...")
        p1 = Project(
            title="Optimización Agrícola con Predicciones Climáticas",
            description="Aplicación de Deep Learning y Descomposición Modal Dinámica (DMD) para generar predicciones climáticas locales altamente precisas, permitiendo a empresas agrícolas optimizar la planificación de cultivos y reducir pérdidas por fenómenos adversos.",
            technologies="Deep Learning, DMD, Python, Series de Tiempo"
            # Eliminada la línea image_url="project_clima.jpg" por ahora
        )
        p2 = Project(
            title="Segmentación de Usuarios para Marketing Personalizado",
            description="Desarrollo de modelos de clusterización para identificar segmentos de usuarios con comportamientos y preferencias similares, lo que permitió a una empresa personalizar sus campañas de marketing y mejorar la tasa de conversión en un X%.",
            technologies="Clustering, Scikit-learn, Python, Marketing Digital"
            # Eliminada la línea image_url="project_clustering.jpg" por ahora
        )
        p3 = Project(
            title="Recopilación de Datos Web para Análisis Competitivo",
            description="Implementación de soluciones de web scraping para extraer datos clave de la competencia y tendencias de mercado, proporcionando insights accionables para la estrategia de precios y posicionamiento de productos.",
            technologies="Web Scraping, BeautifulSoup, Scrapy, Inteligencia de Mercado"
            # Eliminada la línea image_url="project_webscraping.jpg" por ahora
        )
        p4 = Project(
            title="Análisis de Sentimientos de Clientes",
            description="Desarrollo de un sistema de análisis de sentimientos utilizando procesamiento de lenguaje natural (NLP) sobre comentarios de clientes, permitiendo a una empresa mejorar la satisfacción del cliente y la calidad de su servicio.",
            technologies="NLP, Análisis de Sentimientos, NLTK/SpaCy, Voz del Cliente"
            # Eliminada la línea image_url="project_nlp.jpg" por ahora
        )
        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()
        print("Proyectos añadidos/actualizados en la base de datos.")
    else:
        print(f"Ya hay {existing_projects_count} proyectos en la base de datos. No se añadirán nuevos.")


    # Añadir los NUEVOS SERVICIOS simplificados (este bloque está completo y correcto)
    existing_services_count = Service.query.count()
    if existing_services_count == 0:
        print("No se encontraron servicios. Añadiendo servicios de ejemplo...")
        s1 = Service(
            title="Implementación de Sistemas de Datos",
            short_description="Desde la recolección hasta la organización, construimos la infraestructura de datos que tu negocio necesita.",
            full_description="Ayudamos a PYMES a establecer una base sólida para sus datos, implementando sistemas de recolección, almacenamiento y organización eficientes. Esto incluye la configuración de bases de datos, integración de fuentes de datos y aseguramiento de la calidad de los mismos, sentando las bases para cualquier análisis futuro."
        )
        s2 = Service(
            title="Análisis y Visualización de Datos",
            short_description="Transforma datos brutos en insights claros con dashboards interactivos y reportes a medida.",
            full_description="Convertimos tus datos en información valiosa. A través de análisis profundos, identificamos tendencias y patrones clave. Creamos dashboards interactivos y reportes visuales personalizados que te permiten comprender rápidamente el rendimiento de tu negocio y tomar decisiones basadas en evidencia."
        )
        s3 = Service(
            title="Optimización de Procesos con IA/ML",
            short_description="Automatiza tareas repetitivas y mejora la eficiencia operativa con soluciones de Machine Learning.",
            full_description="Aplicamos inteligencia artificial y Machine Learning para optimizar tus procesos internos. Esto puede incluir la predicción de demanda, clasificación de clientes, automatización de flujos de trabajo, lo que lleva a una mayor eficiencia, reducción de costos y una operación más inteligente."
        )
        s4 = Service(
            title="Estrategia de Datos y Producto",
            short_description="Define cómo usar tus datos para impulsar el crecimiento y crear productos digitales exitosos.",
            full_description="Te guiamos en la creación de una estrategia de datos clara, alineando tus objetivos de negocio con el potencial de tus datos. Ayudamos a diseñar y desarrollar productos o funcionalidades basadas en datos que resuelven problemas reales de tus clientes y generan valor."
        )

        db.session.add_all([s1, s2, s3, s4])
        db.session.commit()
        print("Servicios añadidos y guardados en la base de datos.")
    else:
        print(f"Ya hay {existing_services_count} servicios en la base de datos. No se añadirán nuevos.")

# Opcional: Verifica los servicios
    all_services = Service.query.all()
    print(f"Número total de servicios en la DB después de la operación: {len(all_services)}")
    for service in all_services:
        print(f"- {service.title}")