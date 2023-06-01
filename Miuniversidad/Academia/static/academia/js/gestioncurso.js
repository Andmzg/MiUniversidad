//script.js
(function () {
    const btnEliminacion = document.querySelectorAll(".btnEliminacion");
    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm("Seguro de eliminar el curso?");
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });
})();

setTimeout(function() {
    document.getElementById("message").remove();
}, 3000);