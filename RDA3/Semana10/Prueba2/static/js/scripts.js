// static/js/scripts.js
function abrir_calculadora() {
  window.location.href = "/calculadora";
}

document.addEventListener("DOMContentLoaded", function () {
  const btn = document.getElementById("btn-abrir");
  if (btn) {
    btn.addEventListener("click", abrir_calculadora);
  }
});

function abrir_inicio() {
  window.location.href = "/";
}

document.addEventListener("DOMContentLoaded", function () {
  const btn = document.getElementById("btn-inicio");
  if (btn) {
    btn.addEventListener("click", abrir_inicio);
  }
});