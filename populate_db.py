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


    # --- Añadir los NUEVOS Servicios con detalles ---
    # Borrar servicios existentes para evitar duplicados si ejecutas esto varias veces
    db.session.query(Service).delete()
    db.session.commit()
    print("Borrando servicios existentes e insertando nuevos...")

    s1 = Service(
    title="Optimiza tu Negocio: Menos Gastos, Más Ganancias",
    short_description="Descubre cómo tus datos actuales pueden revelar oportunidades para reducir costos, mejorar la eficiencia y maximizar tus utilidades. ¡Transforma tus operaciones hoy!",
    full_description="""
    <strong>Transforma tus Operaciones: Eficiencia y Rentabilidad al Alcance de tu PYME</strong>
    <br><br>
    <strong>¿Te Sientes Identificado?</strong> ¿Procesos lentos y costos elevados? Hay una solución en tus datos.
    <br>
    En el día a día de tu PYME, existen innumerables oportunidades para hacer las cosas mejor. Desde la gestión de inventario hasta la logística de entrega o la planificación de la producción, cada paso genera datos. Pero, ¿estás usando esos datos para tu beneficio? ¿Te sientes atado a procesos ineficientes que consumen tiempo y dinero sin un retorno claro?
    <br><br>
    Con nuestro servicio de Análisis de Datos para la Optimización de Procesos, te ayudamos a desentrañar el potencial oculto en la información que ya posees. Nuestro objetivo es claro: identificar y eliminar los cuellos de botella, reducir costos innecesarios y aumentar la eficiencia general de tu operación.
    <br><br>
    <strong>Nuestro Valor Único:</strong> Tu Socio Estratégico: Data Science con Visión de Negocio.
    <br>
    Mi experiencia no se limita solo al análisis de datos; como Product Manager, sé cómo se construyen y optimizan los procesos de negocio desde cero. Esto significa que no solo te entregaré análisis complejos, sino que traduciré esos hallazgos en soluciones prácticas y accionables que se integren fluidamente en tu día a día. Mi objetivo es que cada recomendación tenga un impacto real y medible en tus resultados, siempre pensando en la rentabilidad de tu negocio.
    <br><br>
    <strong>Lo que Lograrás con Este Servicio:</strong>
    <ul>
        <li>📈 <strong>Reducción de Costos:</strong> Identifica y elimina gastos operativos ocultos o innecesarios.</li>
        <li>⚡ <strong>Mayor Eficiencia Operativa:</strong> Optimiza tus flujos de trabajo para producir más en menos tiempo.</li>
        <li>✅ <strong>Decision es Basadas en Evidencia:</strong> Deja de operar por intuición y empieza a tomar decisiones respaldadas por tus propios datos.</li>
        <li>🚀 <strong>Procesos más Ágiles:</strong> Transforma tus operaciones para que respondan mejor a las demandas del mercado.</li>
    </ul>
    <br>
    <strong>¿Cómo lo Hacemos? Tu Camino Hacia la Optimización:</strong>
    <ul>
        <li>🔍 <strong>Diagnóstico de Datos:</strong> Evaluamos tus datos actuales (ventas, inventario, producción, etc.) para entender qué información tenemos y cómo podemos usarla.</li>
        <li>⚙️ <strong>Identificación de Cuellos de Botella:</strong> Analizamos tus procesos clave para pinpointar dónde se producen las demoras o los gastos excesivos.</li>
        <li>💡 <strong>Propuestas de Mejora Concretas:</strong> Desarrollamos recomendaciones prácticas y fáciles de implementar, basadas en los patrones y tendencias que encontramos en tus datos.</li>
        <li>🤝 <strong>Implementación y Soporte:</strong> Te acompañamos en la puesta en marcha de las soluciones y te aseguramos que el valor se genere desde el primer día.</li>
    </ul>
    <br><br>
    <strong>¡Transforma la Eficiencia de tu PYME Hoy!</strong>
    <br>
    No dejes que los procesos ineficientes frenen tu crecimiento. Es hora de convertir tus datos en tu mayor aliado para reducir gastos y aumentar tus ganancias.
    """,
    icon="money-bill-transfer"
    )
    s2 = Service(
        title="Vende Más: Conoce a tus Clientes, Anticipa sus Deseos",
        short_description="Usa el poder de tus datos para entender mejor a tus clientes, personalizar tu marketing y disparar tus ventas. ¡Convierte datos en ingresos!",
        full_description="""
        <strong>Marketing Inteligente: Conoce a tus Clientes y Dispara tus Ventas</strong>
        <br><br>
        <strong>¿Tus campañas de marketing no dan los resultados esperados?</strong>
        <br>
        En un mercado competitivo, el éxito de tu PYME depende de qué tan bien conoces a tus clientes. ¿Sabes quiénes son tus clientes más valiosos? ¿Qué productos les interesan realmente? ¿Por qué algunos compran y otros no?
        <br><br>
        Nuestro servicio de Segmentación de Clientes y Personalización de Marketing te permite ir más allá de las suposiciones. Usamos los datos de tus ventas, interacciones y preferencias para crear una imagen clara de tus diferentes tipos de clientes. Con esta información, podrás personalizar tus mensajes, optimizar tus ofertas y lanzar campañas mucho más rentables.
        <br><br>
        <strong>Nuestro Valor Único:</strong> Estrategia de Producto y Marketing Basada en Datos.
        <br>
        Gracias a mi experiencia como Product Manager, no solo te ayudaré a segmentar tus datos, sino que te daré una perspectiva estratégica sobre cómo cada segmento se relaciona con tus productos o servicios. Entiendo el ciclo de vida del cliente y cómo los datos pueden usarse para atraer, retener y convertir a tus compradores, asegurando que tus esfuerzos de marketing no solo sean inteligentes, sino también profundamente efectivos para el crecimiento de tu negocio.
        <br><br>
        <strong>Lo que Lograrás con Este Servicio:</strong>
        <ul>
            <li>💰 <strong>Mayor Rentabilidad en Marketing:</strong> Invierte tu presupuesto en las audiencias que realmente importan.</li>
            <li>🎯 <strong>Campañas Más Efectivas:</strong> Crea mensajes y ofertas que resuenen directamente con cada tipo de cliente.</li>
            <li>🧡 <strong>Aumento de la Fidelización:</strong> Entiende las necesidades de tus clientes para construir relaciones duraderas.</li>
            <li>📈 <strong>Crecimiento de las Ventas:</strong> Identifica nuevas oportunidades de venta cruzada y upselling.</li>
        </ul>
        <br>
        <strong>¿Cómo lo Hacemos? Conoce a tus Clientes como Nunca Antes:</strong>
        <ul>
            <li>📊 <strong>Análisis de Clientes:</strong> Recopilamos y analizamos tus datos de clientes para identificar patrones de compra y comportamiento.</li>
            <li>👥 <strong>Creación de Segmentos:</strong> Dividimos tu base de clientes en grupos con características y necesidades similares.</li>
            <li>💬 <strong>Recomendaciones de Marketing:</strong> Te proponemos estrategias claras para cada segmento, incluyendo mensajes, canales y ofertas.</li>
            <li>🔄 <strong>Optimización Continua:</strong> Te enseñamos a monitorear la efectividad de tus campañas para seguir mejorando.</li>
        </ul>
        <br><br>
        <strong>¡Vende Más con Inteligencia y Estrategia!</strong>
        <br>
        Deja de adivinar y comienza a conectar con tus clientes de una manera significativa. Transforma tus datos en campañas de marketing que realmente conviertan.
        """,
        icon="users"
    )
    s3 = Service(
        title="Tu Web no es solo una Vitrina: ¡Hazla Vender!",
        short_description="Transforma tu sitio web en una máquina de crecimiento. Analizamos el comportamiento de tus visitas para convertirlas en clientes reales y potenciar tu negocio online.",
        full_description="""
        <strong>Sitio Web Inteligente: Transforma Visitas en Clientes Reales y Multiplica tus Conversiones</strong>
        <br><br>
        <strong>¿Tu sitio web recibe visitas, pero no se traducen en suficientes clientes o ventas?</strong>
        <br>
        En el mundo digital actual, tu sitio web es mucho más que una tarjeta de presentación. Es tu vitrina 24/7, tu canal de ventas, tu centro de atención al cliente. Pero, ¿está realmente trabajando a su máximo potencial para tu PYME?
        <br><br>
        Con nuestro servicio de Inteligencia de Datos para Sitios Web, transformamos tu presencia online en una máquina de crecimiento. Implementamos herramientas y técnicas de análisis para entender cada clic, cada visita y cada interacción en tu sitio. Así, podemos identificar qué funciona, qué no y, lo más importante, qué cambios necesitas hacer para convertir más visitantes en clientes y disparar tus resultados online.
        <br><br>
        <strong>Nuestro Valor Único:</strong> Desde la Estrategia de Negocio hasta la Experiencia Digital.
        <br>
        Mi doble rol como experto en Data Science y Product Manager es crucial aquí. No solo implemento las herramientas de medición, sino que entiendo la lógica de negocio detrás de tu sitio web. Me pongo en los zapatos de tus clientes para identificar los puntos de fricción, optimizar el "viaje del usuario" y asegurarme de que cada elemento de tu web esté diseñado para lograr tus objetivos comerciales. Tu sitio web no solo será inteligente, será estratégico.
        <br><br>
        <strong>Lo que Lograrás con Este Servicio:</strong>
        <ul>
            <li>🚀 <strong>Aumento de Conversiones:</strong> Más visitantes se convertirán en clientes potenciales, ventas o leads.</li>
            <li>✨ <strong>Mejor Experiencia de Usuario (UX):</strong> Un sitio web intuitivo y atractivo que retiene a tus visitantes.</li>
            <li>📊 <strong>Optimización del ROI Digital:</strong> Maximizas el retorno de tu inversión en marketing online.</li>
            <li>💡 <strong>Decisiones Web Basadas en Datos:</strong> Deja de adivinar qué funciona y actúa con información precisa del comportamiento de tus usuarios.</li>
        </ul>
        <br>
        <strong>¿Cómo lo Hacemos? Tu Web, Tu Aliada Inteligente:</strong>
        <ul>
            <li>🎯 <strong>Marcaje de Eventos y Tracking:</strong> Configuramos tu sitio web para recopilar datos clave sobre el comportamiento de tus usuarios (ej., clics, descargas, carritos abandonados).</li>
            <li>🗺️ <strong>Análisis del Viaje del Cliente:</strong> Mapeamos cómo los usuarios interactúan con tu sitio, identificando dónde se quedan y dónde se van.</li>
            <li>🛠️ <strong>Recomendaciones de Optimización:</strong> Te entregamos un plan de acción claro para mejorar tu web y aumentar tus conversiones.</li>
            <li>📈 <strong>Soporte y Seguimiento:</strong> Te ayudamos a implementar los cambios y a monitorear los resultados para asegurar el éxito continuo.</li>
        </ul>
        <br><br>
        <strong>¡Haz que tu Sitio Web Trabaje Incansablemente para tu Negocio!</strong>
        <br>
        Es hora de transformar tu sitio web de una simple presencia online a una herramienta poderosa de generación de negocio.
        """,
        icon="globe"
    )
    s4 = Service(
        title="Tus Datos al Instante: Dashboards para Decisiones Rápidas",
        short_description="Deja de buscar información. Unifica tus datos en dashboards visuales e interactivos para tener el control total de tu negocio y decidir al momento.",
        full_description="""
        <strong>Tus Datos al Instante: Dashboards Interactivos para Decisiones Rápidas y Estratégicas</strong>
        <br><br>
        <strong>¿Datos dispersos y sin una visión clara de tu negocio?</strong>
        <br>
        Sabemos que en una PYME, el tiempo es oro y las decisiones deben ser rápidas y certeras. Si tus datos están aislados en hojas de cálculo, sistemas diferentes o informes estáticos que no te dan la visión completa de lo que está sucediendo en tu negocio, estás perdiendo una ventaja competitiva crucial.
        <br><br>
        Con nuestro servicio de Implementación de Flujos de Datos End-to-End y Dashboards Interactivos, transformamos tu información dispersa en una fuente de poder. Diseñamos y construimos sistemas que recolectan, organizan y visualizan tus datos de manera automática y en un solo lugar. El resultado: dashboards intuitivos que te muestran las métricas clave de tu negocio en tiempo real, permitiéndote tomar decisiones estratégicas en segundos, no en horas o días.
        <br><br>
        <strong>Nuestro Valor Único:</strong> Ingeniería de Datos con Visión Estratégica.
        <br>
        Mi background como Product Manager me permite ir más allá de la mera implementación técnica. Me enfoco en entender qué preguntas de negocio necesitas responder para diseñar dashboards que no solo sean visualmente atractivos, sino que también sean funcionales y accionables. Nos aseguramos de que cada métrica y cada visualización te ayude a tomar la decisión correcta, optimizando desde la base de datos hasta el "producto final" que es tu dashboard.
        <br><br>
        <strong>Lo que Lograrás con Este Servicio:</strong>
        <ul>
            <li>🌐 <strong>Visión 360° de tu Negocio:</strong> Accede a todos tus datos relevantes en un solo lugar.</li>
            <li>⏱️ <strong>Decisiones en Tiempo Real:</strong> Reacciona rápidamente a los cambios del mercado con información actualizada.</li>
            <li>💲 <strong>Ahorro de Tiempo y Recursos:</strong> Elimina la necesidad de consolidar datos manualmente y genera informes al instante.</li>
            <li>🔎 <strong>Identificación de Oportunidades y Problemas:</strong> Detecta tendencias, ineficiencias o áreas de crecimiento de forma proactiva.</li>
        </ul>
        <br>
        <strong>¿Cómo lo Hacemos? Tus Datos, Tu Poder:</strong>
        <ul>
            <li>📊 <strong>Mapeo de Fuentes de Datos:</strong> Identificamos dónde se encuentra toda tu información (ventas, inventario, marketing, etc.).</li>
            <li>🛣️ <strong>Diseño de Flujos de Datos:</strong> Creamos la "autopista" que conectará y procesará tus datos de forma automática.</li>
            <li>🖥️ <strong>Construcción de Dashboards:</strong> Desarrollamos paneles interactivos y personalizados con tus métricas clave.</li>
            <li>🎓 <strong>Capacitación y Soporte:</strong> Te enseñamos a usar tu nuevo dashboard y te brindamos el apoyo inicial para que le saques el máximo provecho.</li>
        </ul>
        <br><br>
        <strong>¡Obtén una Visión Clara y Unificada de tu Negocio!</strong>
        <br>
        No permitas que tus datos se queden en el olvido. Conviértelos en tu herramienta más poderosa para la toma de decisiones.
        """,
        icon="chart-simple"
    )
    s5 = Service(
        title="Anticipa el Futuro: Planifica con Precisión tus Ventas",
        short_description="Reduce la incertidumbre. Usamos tus datos para predecir futuras ventas y demanda, optimizando tu inventario y recursos como nunca antes.",
        full_description="""
        <strong>Anticipa el Futuro: Pronóstico de Ventas y Demanda para una Planificación Precisa</strong>
        <br><br>
        <strong>¿Incertidumbre en tus ventas futuras? Es hora de planificar con datos.</strong>
        <br>
        En el mundo de las PYMES, la incertidumbre puede ser un gran obstáculo. Comprar demasiado inventario genera costos de almacenamiento y riesgo de obsolescencia. Comprar muy poco significa perder ventas. ¿Qué pasa si pudieras tener una idea más clara de lo que se viene?
        <br><br>
        Nuestro servicio de Pronóstico de Ventas y Demanda Simple te ayuda a ver el futuro con mayor claridad. Usando tus datos históricos de ventas, podemos identificar patrones, tendencias y estacionalidades para predecir tus futuras ventas o la demanda de tus productos. Con esta información, podrás optimizar tu inventario, planificar mejor tu producción o tus servicios y asignar tus recursos de manera más inteligente, evitando sorpresas desagradables y maximizando tus oportunidades.
        <br><br>
        <strong>Nuestro Valor Único:</strong> Predicciones Claras con un Enfoque en tu Rentabilidad.
        <br>
        Mi experiencia como Product Manager me permite ir más allá de los números. Entiendo cómo las predicciones de ventas impactan directamente en la gestión de tu producto o servicio. No solo te entregaré un pronóstico, sino que te ayudaré a entender cómo usar esa información para tomar decisiones estratégicas sobre precios, promociones, lanzamientos de productos y gestión de tu cadena de suministro, asegurando que cada predicción contribuya directamente a la rentabilidad de tu negocio.
        <br><br>
        <strong>Lo que Lograrás con Este Servicio:</strong>
        <ul>
            <li>📦 <strong>Optimización de Inventario:</strong> Reduce el exceso de stock y evita roturas, ahorrando dinero.</li>
            <li>🧑‍🏭 <strong>Mejor Planificación de Recursos:</strong> Asigna tu personal y capacidad de producción de forma más eficiente.</li>
            <li>📉 <strong>Reducción de Pérdidas:</strong> Disminuye el desperdicio por productos caducados o fuera de temporada.</li>
            <li>🔮 <strong>Mayor Confianza en la Planificación:</strong> Toma decisiones futuras con mayor seguridad y menos riesgo.</li>
        </ul>
        <br>
        <strong>¿Cómo lo Hacemos? Tu Futuro, Más Predecible:</strong>
        <ul>
            <li>📈 <strong>Recopilación de Datos Históricos:</strong> Reunimos tus datos de ventas pasadas para entender las tendencias.</li>
            <li>🔍 <strong>Análisis de Patrones:</strong> Identificamos estacionalidades, picos y valles en tus ventas.</li>
            <li>🔢 <strong>Generación de Pronósticos:</strong> Creamos modelos predictivos fáciles de entender que te muestran las ventas futuras estimadas.</li>
            <li>📄 <strong>Informes Claros y Accionables:</strong> Te entregamos las predicciones de forma visual y con recomendaciones para tu planificación.</li>
        </ul>
        <br><br>
        <strong>¡Planifica tu Futuro con Datos y No con Suposiciones!</strong>
        <br>
        Deja de operar a ciegas. Conoce las tendencias de tu demanda y optimiza tus operaciones para un crecimiento sostenido.
        """,
        icon="chart-line"
    )
    s6 = Service(
        title="Rentabilidad Real: Descubre Dónde Está tu Ganancia",
        short_description="Identifica qué productos o servicios son tus mayores fuentes de ganancia y cuáles no. Optimiza tu oferta y maximiza tu rentabilidad.",
        full_description="""
        <strong>Rentabilidad Real: Descubre Qué Productos o Servicios Impulsan (o Frenan) tus Ganancias</strong>
        <br><br>
        <strong>¿Sabes realmente qué productos o servicios te generan más ganancias?</strong>
        <br>
        En tu PYME, cada producto o servicio debería contribuir a tu rentabilidad. Sin embargo, a menudo, la intuición puede engañarnos. Un producto muy vendido no siempre es el más rentable, y uno menos popular podría estar generando un margen sorprendente.
        <br><br>
        Nuestro servicio de Análisis de Rentabilidad de Productos o Servicios te ofrece una visión clara y sin filtros de tus fuentes de ingresos. Analizamos tus costos e ingresos asociados a cada oferta para identificar con precisión dónde está tu verdadera ganancia. Con esta información, podrás tomar decisiones estratégicas: potenciar tus "estrellas", revisar los precios de otros o incluso reestructurar tu oferta para maximizar tus márgenes y asegurar el crecimiento sostenible de tu negocio.
        <br><br>
        <strong>Nuestro Valor Único:</strong> Estrategia de Precios y Oferta con Visión de Negocio.
        <br>
        Mi experiencia como Product Manager me permite abordar este análisis no solo desde el dato financiero, sino desde la estrategia completa del producto. Entiendo cómo el ciclo de vida del producto, su posicionamiento en el mercado y su valor percibido influyen en la rentabilidad. Te ayudaré a tomar decisiones que no solo optimicen tus números a corto plazo, sino que también fortalezcan tu cartera de productos o servicios a largo plazo, siempre pensando en el impacto global en tu negocio.
        <br><br>
        <strong>Lo que Lograrás con Este Servicio:</strong>
        <ul>
            <li>📈 <strong>Aumento de la Rentabilidad General:</strong> Enfoca tus esfuerzos donde realmente hay ganancia.</li>
            <li>⭐ <strong>Optimización del Portafolio:</strong> Identifica productos de alto margen y reevalúa los de bajo rendimiento.</li>
            <li>💲 <strong>Decisiones de Precios Inteligentes:</strong> Ajusta tus tarifas con base en datos reales de costos y demanda.</li>
            <li>🎯 <strong>Mejor Asignación de Recursos:</strong> Invierte donde el retorno es mayor.</li>
        </ul>
        <br>
        <strong>¿Cómo lo Hacemos? Tu Ruta Hacia Más Ganancias:</strong>
        <ul>
            <li>📊 <strong>Recopilación de Datos Financieros:</strong> Consolidamos todos los costos e ingresos asociados a cada producto o servicio.</li>
            <li>💰 <strong>Cálculo de Margen de Ganancia:</strong> Determinamos la rentabilidad real de cada oferta individual.</li>
            <li>🌟 <strong>Identificación de "Estrellas" y "Vampiros":</strong> Visualizamos claramente qué productos son tus mayores contribuyentes y cuáles te están consumiendo recursos.</li>
            <li>📝 <strong>Recomendaciones Estratégicas:</strong> Te ofrecemos un plan de acción para potenciar tu rentabilidad, desde ajustes de precios hasta estrategias de marketing.</li>
        </ul>
        <br><br>
        <strong>¡Descubre el Verdadero Potencial Financiero de tu Oferta!</strong>
        <br>
        No dejes más dinero sobre la mesa. Conoce a fondo la rentabilidad de cada uno de tus productos y servicios y toma decisiones que disparen tus ganancias.
        """,
        icon="coins"
    )
    db.session.add_all([s1, s2, s3, s4, s5, s6])
    db.session.commit()
    print("Nuevos servicios con descripciones detalladas añadidos a la base de datos.")

    # Opcional: Verifica los servicios
    all_services = Service.query.all()
    print(f"Número total de servicios en la DB después de la operación: {len(all_services)}")
    for service in all_services:
        print(f"- {service.title}")