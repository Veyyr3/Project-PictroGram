// Получаем элементы
const modal = document.getElementById("commentModal");
const openModalBtn = document.getElementById("add_comment_button");
const closeButton = document.getElementsByClassName("close-button")[0];

// При нажатии на кнопку открытия, показать модальное окно
openModalBtn.onclick = function() {
  modal.style.display = "flex"; // Используем flex для центрирования
}

// При нажатии на кнопку закрытия (x), скрыть модальное окно
closeButton.onclick = function() {
  modal.style.display = "none";
}

// При клике в любом месте за пределами модального окна, закрыть его
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}