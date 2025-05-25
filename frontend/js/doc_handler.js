document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('fileInput');
    const fileUploadArea = document.getElementById('fileUploadArea');
    const fileList = document.getElementById('fileList');
    const workTitle = document.getElementById('workTitle');
    const submitBtn = document.getElementById('submitBtn');

    let filesToUpload = []; // Массив для хранения файлов

    // Инициализация обработчиков
    fileUploadArea.addEventListener('click', () => fileInput.click());
    fileInput.addEventListener('change', handleFileSelect);
    setupDragAndDrop();

    // Обработка выбора файлов
    function handleFileSelect(e) {
        if (!validateForm()) {
            fileInput.value = '';
            return;
        }
        filesToUpload = Array.from(e.target.files);
        updateFileList();
    }

    // Валидация формы
    function validateForm() {
        if (!workTitle.value.trim()) {
            showError('Пожалуйста, введите название работы');
            return false;
        }
        return true;
    }

    // Отображение ошибок
    function showError(message) {
        const alert = document.createElement('div');
        alert.className = 'alert alert-danger mt-2';
        alert.textContent = message;
        
        const existingAlert = fileUploadArea.parentElement.querySelector('.alert');
        if (existingAlert) existingAlert.remove();
        
        fileUploadArea.parentElement.appendChild(alert);
    }

    // Обновление списка файлов
    function updateFileList() {
        fileList.innerHTML = '';
        filesToUpload.forEach((file, index) => {
            const fileItem = document.createElement('div');
            fileItem.className = 'd-flex justify-content-between align-items-center mb-2 p-2 border rounded';
            fileItem.innerHTML = `
                <div class="d-flex align-items-center">
                    <i class="bi bi-file-text me-3"></i>
                    <div>
                        <div class="fw-medium">${file.name}</div>
                        <div class="text-muted small">${(file.size/1024/1024).toFixed(2)} MB</div>
                    </div>
                </div>
                <div class="d-flex align-items-center gap-2">
                    <div class="text-muted small">${workTitle.value.trim()}</div>
                    <button class="btn btn-sm btn-danger delete-btn" data-index="${index}">
                        <i class="bi bi-trash"></i>
                    </button>
                </div>
            `;
            fileList.appendChild(fileItem);
        });

        // Добавляем обработчики удаления
        document.querySelectorAll('.delete-btn').forEach(btn => {
            btn.addEventListener('click', handleDeleteFile);
        });
    }

    // Удаление файла
    function handleDeleteFile(e) {
        const index = parseInt(e.currentTarget.getAttribute('data-index'));
        filesToUpload.splice(index, 1); // Удаляем файл из массива
        updateFileList();
        updateFileInput(); // Обновляем файловый инпут
    }

    // Обновление инпута файлов
    function updateFileInput() {
        const dataTransfer = new DataTransfer();
        filesToUpload.forEach(file => dataTransfer.items.add(file));
        fileInput.files = dataTransfer.files;
    }

    // Drag and drop обработчики
    function setupDragAndDrop() {
        ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
            fileUploadArea.addEventListener(eventName, preventDefaults, false);
        });

        fileUploadArea.addEventListener('drop', handleDrop, false);
    }

    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }

    function handleDrop(e) {
        if (!validateForm()) return;
        
        const dt = e.dataTransfer;
        filesToUpload = Array.from(dt.files);
        updateFileList();
        updateFileInput();
    }

    // Обработка отправки формы
    submitBtn.addEventListener('click', async () => {
        if (!validateForm() || filesToUpload.length === 0) {
            showError('Заполните все обязательные поля');
            return;
        }

        // Ваша логика отправки
        console.log('Отправка файлов:', {
            title: workTitle.value.trim(),
            files: filesToUpload
        });
    });
});