// Variabili globali
let isDragging = false;
let startPos = 0;
let currentTranslate = 0;
let prevTranslate = 0;
let animationID;
let currentIndex = 0;

// Selezione degli elementi
const slides = Array.from(document.querySelectorAll('.carousel-image'));
const slidesWrapper = document.querySelector('.slides-wrapper');
const carouselContainer = document.querySelector('.carousel-container');

// Eventi per ogni slide
slides.forEach((slide, index) => {
    // Previene il comportamento di trascinamento predefinito
    slide.addEventListener('dragstart', (e) => e.preventDefault());

    // Touch events
    slide.addEventListener('touchstart', touchStart(index));
    slide.addEventListener('touchend', touchEnd);
    slide.addEventListener('touchmove', touchMove);

    // Mouse events
    slide.addEventListener('mousedown', touchStart(index));
    slide.addEventListener('mouseup', touchEnd);
    slide.addEventListener('mouseleave', touchEnd);
    slide.addEventListener('mousemove', touchMove);
});

// Event listener per il resize
window.addEventListener('resize', setPositionByIndex);

// Funzioni touch
function touchStart(index) {
    return function (event) {
        currentIndex = index;
        startPos = getPositionX(event);
        isDragging = true;
        animationID = requestAnimationFrame(animation);

        slidesWrapper.classList.add('grabbing');
    };
}

function touchMove(event) {
    if (!isDragging) return;
    const currentPosition = getPositionX(event);
    const diff = currentPosition - startPos;

    currentTranslate = prevTranslate + diff;
}

function touchEnd() {
    isDragging = false;
    cancelAnimationFrame(animationID);

    const movedBy = currentTranslate - prevTranslate;

    // Soglia per cambiare slide (25% della larghezza)
    const threshold = carouselContainer.offsetWidth * 0.25;

    if (movedBy < -threshold && currentIndex < slides.length - 1) {
        currentIndex += 1;
    }

    if (movedBy > threshold && currentIndex > 0) {
        currentIndex -= 1;
    }

    setPositionByIndex();

    slidesWrapper.classList.remove('grabbing');
}

function getPositionX(event) {
    return event.type.includes('mouse')
        ? event.pageX
        : event.touches[0].clientX;
}

function animation() {
    setSliderPosition();
    if (isDragging) {
        requestAnimationFrame(animation);
    }
}

function setSliderPosition() {
    slidesWrapper.style.transform = `translateX(${currentTranslate}px)`;
}

function setPositionByIndex() {
    currentTranslate = currentIndex * -carouselContainer.offsetWidth;
    prevTranslate = currentTranslate;
    setSliderPosition();
}

// Funzioni per i bottoni di navigazione
function prevSlide() {
    if (currentIndex > 0) {
        currentIndex -= 1;
        setPositionByIndex();
    }
}

function nextSlide() {
    if (currentIndex < slides.length - 1) {
        currentIndex += 1;
        setPositionByIndex();
    }
}