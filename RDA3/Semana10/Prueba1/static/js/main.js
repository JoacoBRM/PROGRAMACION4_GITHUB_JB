document.addEventListener("DOMContentLoaded", function () {
  const boton = document.getElementById("miBoton");

  if (boton && typeof mensajeAlerta !== "undefined") {
    boton.addEventListener("click", function () {
      Swal.fire({
        title: "¡Bienvenido!",
        text: mensajeAlerta,
        icon: "success",
        confirmButtonText: "Aceptar"
      }).then((result) => {
        if (result.isConfirmed) {
          // Redirige a la ruta de Flask "/base.html"
          window.location.href = "/base.html";
        }
      });
    });
  }
});
