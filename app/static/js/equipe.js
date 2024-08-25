var menu = document.querySelector('.menu')
var small_menu = document.querySelector('.toggle')
small_menu.onclick = function() {
    small_menu.classList.toggle('active')
    menu.classList.toggle('responsive')
};
window.addEventListener('scroll', function() {
    const containers = [
        document.getElementById('equipe'),
        document.getElementById('footer')
    ];

    const windowHeight = window.innerHeight;
    const scrollPosition = window.scrollY;

    containers.forEach(container => {
        const divs = container.querySelectorAll('.item');

        divs.forEach(div => {
            const divTop = div.getBoundingClientRect().top + scrollPosition;
            const divBottom = divTop + div.offsetHeight;
            const offset = 200
            // Définir le début et la fin de la zone visible
            const start = scrollPosition ;
            const end = scrollPosition + windowHeight ;

            // Vérifier si l'élément est dans la zone visible lors du défilement
            if (divBottom > start && divTop < end) {
                div.classList.add('visible');
            } else {
                div.classList.remove('visible');
            }
        });
    });
});
