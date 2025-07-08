// open_comments.js
document.addEventListener('DOMContentLoaded', function() {
    const commentModal = document.getElementById('commentModal');
    const closeButton = document.querySelector('.close-button');
    const commentForm = document.getElementById('commentForm');
    const modalPublicationIdInput = document.getElementById('modal_publication_id');

    // Открытие модального окна при клике на кнопку "Добавить комментарий"
    document.querySelectorAll('.add-comment-button').forEach(button => {
        button.addEventListener('click', function() {
            const publicationId = this.dataset.publicationId;
            const addCommentUrl = this.dataset.addCommentUrl; 

            modalPublicationIdInput.value = publicationId;
            commentForm.action = addCommentUrl; // Устанавливаем action формы

            commentModal.style.display = "block"; // Показываем модальное окно
        });
    });

    // Закрытие модального окна при нажатии на кнопку закрытия (x)
    closeButton.addEventListener('click', function() { // Используем addEventListener
        commentModal.style.display = "none"; // Правильное использование commentModal
        commentForm.reset(); // Очищаем форму
        modalPublicationIdInput.value = ''; // Очищаем скрытое поле ID
        commentForm.action = ''; // Очищаем action
    });

    // Закрытие модального окна при клике в любом месте за пределами окна
    window.addEventListener('click', function(event) { // Используем addEventListener
        if (event.target == commentModal) { // Правильное использование commentModal
            commentModal.style.display = "none";
            commentForm.reset(); 
            modalPublicationIdInput.value = '';
            commentForm.action = '';
        }
    });
});