document.querySelectorAll('.role-btn').forEach(button => {
    button.addEventListener('click', function() {
        document.querySelectorAll('.role-btn').forEach(btn => btn.classList.remove('active'));
        this.classList.add('active');
        document.getElementById('role').value = this.getAttribute('data-role');
    });
});