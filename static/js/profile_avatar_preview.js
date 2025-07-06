document.addEventListener('DOMContentLoaded', function() {
    // стандартный ID 'id_avatar', который генерирует джанго
    const imageUploadInput = document.getElementById('id_avatar'); 
    const imagePreview = document.getElementById('imagePreview');

    if (imageUploadInput && imagePreview) { 
        imageUploadInput.addEventListener('change', function(event) {
            if (event.target.files && event.target.files[0]) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    imagePreview.src = e.target.result;
                };
                reader.readAsDataURL(event.target.files[0]);
            } else {
                imagePreview.src = '/static/page_pictures/page decorations/img-for-upload.jpg'; 
            }
        });
    }
});