document.addEventListener('DOMContentLoaded', function () {
    const navbarHeight = document.querySelector('.navbar').offsetHeight;

    // Funzione per gestire lo scroll con un offset per tenere conto della navbar
    function scrollToElement(targetId) {
        const targetElement = document.getElementById(targetId);

        if (targetElement) {
            // Ottieni la posizione dell'elemento rispetto al viewport
            const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset;

            // Calcola la posizione finale con l'offset della navbar
            const offsetPosition = targetPosition - navbarHeight;

            // Log di debug per visualizzare i valori
            console.log(`ID target: ${targetId}`);
            console.log(`Posizione originale dell'elemento: ${targetPosition}`);
            console.log(`Altezza navbar: ${navbarHeight}`);
            console.log(`Posizione finale con offset: ${offsetPosition}`);

            // Esegui lo scroll con effetto fluido
            window.scrollTo({
                top: offsetPosition,
                behavior: 'smooth'
            });

            // Log per confermare lo scroll
            console.log(`Scroll effettuato verso: ${offsetPosition}`);
        } else {
            console.error(`Elemento con ID ${targetId} non trovato.`);
        }
    }

    // Aggiungi un evento click su tutti i link che puntano a un ID
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1); // Ottieni l'ID di destinazione

            // Log per confermare che il click è stato catturato
            console.log(`Cliccato su link con destinazione: ${targetId}`);

            scrollToElement(targetId); // Esegui lo scroll con offset
        });
    });
});
document.addEventListener('DOMContentLoaded', function () {
    const navbarHeight = document.querySelector('.navbar').offsetHeight;

    // Funzione per rilevare se l'utente è su un dispositivo mobile
    function isMobileDevice() {
        return window.innerWidth <= 768; // Breakpoint mobile
    }

    // Funzione per gestire lo scroll con un offset per tenere conto della navbar
    function scrollToElement(targetId) {
        const targetElement = document.getElementById(targetId);

        if (targetElement) {
            // Ottieni la posizione dell'elemento rispetto al viewport
            const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset;

            // Calcola la posizione finale con l'offset della navbar
            let offsetPosition = targetPosition - navbarHeight;

            // Se siamo su mobile, aggiungiamo un offset extra
            if (isMobileDevice() && targetId === 'container1-1') {
                offsetPosition = targetPosition - navbarHeight + 150; // Extra offset per "Chi Siamo" su mobile
            }

            // Esegui lo scroll con effetto fluido
            window.scrollTo({
                top: offsetPosition,
                behavior: 'smooth'
            });

            // Log per il debug
            console.log(`Scroll verso: ${targetId}, offset: ${offsetPosition}`);
        } else {
            console.error(`Elemento con ID ${targetId} non trovato.`);
        }
    }

    // Aggiungi un evento click su tutti i link che puntano a un ID
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1); // Ottieni l'ID di destinazione

            scrollToElement(targetId); // Esegui lo scroll con offset
        });
    });
});