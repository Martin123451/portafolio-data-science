from app import app, db, Project
with app.app_context():
    # Borra proyectos existentes para empezar limpio (opcional, pero útil si pruebas varias veces)
    db.session.query(Project).delete()
    db.session.commit()

    # Añade tus proyectos
    p1 = Project(
        title="Optimización Agrícola con Predicciones Climáticas",
        description="Aplicación de Deep Learning y Descomposición Modal Dinámica (DMD) para generar predicciones climáticas locales altamente precisas, permitiendo a empresas agrícolas optimizar la planificación de cultivos y reducir pérdidas por fenómenos adversos.",
        technologies="Deep Learning, DMD, Python, Series de Tiempo"
    )
    p2 = Project(
        title="Segmentación de Usuarios para Marketing Personalizado",
        description="Desarrollo de modelos de clusterización para identificar segmentos de usuarios con comportamientos y preferencias similares, lo que permitió a una empresa personalizar sus campañas de marketing y mejorar la tasa de conversión en un X%.",
        technologies="Clustering, Scikit-learn, Python, Marketing Digital"
    )
    p3 = Project(
        title="Recopilación de Datos Web para Análisis Competitivo",
        description="Implementación de soluciones de web scraping para extraer datos clave de la competencia y tendencias de mercado, proporcionando insights accionables para la estrategia de precios y posicionamiento de productos.",
        technologies="Web Scraping, BeautifulSoup, Scrapy, Inteligencia de Mercado"
    )
    #p4 = Project(
    #    title="Análisis de Sentimientos de Clientes",
    #    description="Desarrollo de un sistema de análisis de sentimientos utilizando procesamiento de lenguaje natural (NLP) sobre comentarios de clientes, permitiendo a una empresa mejorar la satisfacción del cliente y la calidad de su servicio.",
    #    technologies="NLP, Análisis de Sentimientos, NLTK/SpaCy, Voz del Cliente"
    #)
    p4 = Project(
        title="Prueba",
        description="Prueba base de datos",
        technologies="Python, HTML, CSS"
    )

    db.session.add_all([p1, p2, p3, p4])
    db.session.commit()
    print("Proyectos añadidos a la base de datos.")

    # Opcional: Verifica que se hayan añadido
    all_projects = Project.query.all()
    print(f"Número total de proyectos en la DB: {len(all_projects)}")
    for project in all_projects:
        print(f"- {project.title}")