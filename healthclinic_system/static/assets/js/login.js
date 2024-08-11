document.querySelectorAll('.role-btn').forEach(button => {
    button.addEventListener('click', function() {
        document.querySelectorAll('.role-btn').forEach(btn => btn.classList.remove('active'));
        this.classList.add('active');
        document.getElementById('role').value = this.getAttribute('data-role');
    });
});

document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const error = document.getElementById('error');
    const role = document.getElementById('role').value;

    // Static data for validation
    const validAdminUsername = 'admin';
    const validAdminPassword = 'password123';
    const validStudentUsername = 'student';
    const validStudentPassword = 'password456';

    let isValid = false;

    if (role === 'admin' && username === validAdminUsername && password === validAdminPassword) {
        window.location.href = '/admin/dashboard.html';
        isValid = true;
    } else if (role === 'student' && username === validStudentUsername && password === validStudentPassword) {
        window.location.href = '/student/home.html';
        isValid = true;
    }

    if (!isValid) {
        error.textContent = 'Invalid ID or password';
    }
});