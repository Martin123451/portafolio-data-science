// Espera a que el DOM (Document Object Model) esté completamente cargado
document.addEventListener('DOMContentLoaded', function() {
    // Selecciona el botón de toggle del menú
    const menuToggle = document.querySelector('.menu-toggle');
    // Selecciona la lista de navegación (el menú en sí)
    const navMenu = document.querySelector('nav ul');

    // Verifica que ambos elementos existan antes de intentar añadir un evento
    if (menuToggle && navMenu) {
        // Añade un 'event listener' (escuchador de eventos) al botón de toggle
        menuToggle.addEventListener('click', function() {
            // Alterna la clase 'active' en la lista de navegación
            // Si tiene la clase 'active', la quita. Si no la tiene, la añade.
            navMenu.classList.toggle('active');
        });

        // Opcional: Cerrar el menú cuando se hace clic en un enlace (para mejorar UX en móviles)
        const navLinks = document.querySelectorAll('nav ul li a');
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                if (navMenu.classList.contains('active')) {
                    navMenu.classList.remove('active');
                }
            });
        });
    } else {
        console.warn("Elementos 'menu-toggle' o 'nav ul' no encontrados. El menú responsivo puede no funcionar.");
    }
});