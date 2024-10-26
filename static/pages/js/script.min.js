document.addEventListener("DOMContentLoaded", function() {
    const navbar = document.querySelector(".navbar");
    let navbarHeight = navbar.offsetHeight;

    // Ricalcola l'altezza della navbar al ridimensionamento della finestra
    window.addEventListener('resize', function() {
        navbarHeight = navbar.offsetHeight;
    });

    // Funzione per determinare se il dispositivo è mobile
    function isMobileDevice() {
        return window.innerWidth <= 768;
    }

    // Funzione per scrollare verso un elemento con offset
    function scrollToElement(targetId) {
        const targetElement = document.getElementById(targetId);
        if (targetElement) {
            const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset;
            let offsetPosition = targetPosition - navbarHeight;

            // Aggiusta l'offset per "Chi Siamo" su dispositivi mobili
            if (isMobileDevice() && targetId === "container1-1") {
                offsetPosition -= 50; // Modifica questo valore secondo necessità
                console.log(`Offset aggiuntivo per "Chi Siamo" su mobile: ${offsetPosition}`);
            }

            console.log(`ID target: ${targetId}`);
            console.log(`Posizione originale dell'elemento: ${targetPosition}`);
            console.log(`Altezza navbar: ${navbarHeight}`);
            console.log(`Posizione finale con offset: ${offsetPosition}`);

            window.scrollTo({
                top: offsetPosition,
                behavior: "smooth"
            });
            console.log(`Scroll effettuato verso: ${offsetPosition}`);
        } else {
            console.error(`Elemento con ID ${targetId} non trovato.`);
        }
    }

    // Aggiungi event listener a tutti i link che iniziano con "#"
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener("click", function(e) {
            e.preventDefault();
            const targetId = this.getAttribute("href").substring(1);
            console.log(`Cliccato su link con destinazione: ${targetId}`);
            scrollToElement(targetId);
        });
    });
});


