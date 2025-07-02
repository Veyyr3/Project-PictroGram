document.addEventListener('DOMContentLoaded', function() {
    const imageUploadInput = document.getElementById('imageUploadInput');
    const imagePreview = document.getElementById('imagePreview');

    imageUploadInput.addEventListener('change', function(event) {
        // Проверяем, был ли выбран файл
        if (event.target.files && event.target.files[0]) {
            const reader = new FileReader(); // Создаем объект FileReader

            reader.onload = function(e) {
                // Когда файл прочитан, обновляем src у img
                imagePreview.src = e.target.result;
            };

            // Читаем выбранный файл как Data URL (base64 строка)
            reader.readAsDataURL(event.target.files[0]);
        } else {
            // Если файл не выбран (например, пользователь отменил выбор),
            // можно вернуть заглушку или очистить img
            imagePreview.src = "{% static 'page_pictures/page decorations/img-for-upload.jpg' %}"; // Вернуть заглушку
        }
    });
});