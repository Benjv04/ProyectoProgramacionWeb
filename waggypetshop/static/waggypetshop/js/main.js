/*Funcion para mostrar/ocultar contraseña*/
function visibilidadPassword() {
    const passCampo = $("#password");
    const icono = $("#mostrarIcono");
    if (passCampo.attr("type") === "password") {
        passCampo.attr("type", "text");
        icono.text("Ocultar");
    } else {
        passCampo.attr("type", "password");
        icono.text("Mostrar");
    }
}

$(document).ready(function() {
    $("#botonPassword").on('click', visibilidadPassword);
});