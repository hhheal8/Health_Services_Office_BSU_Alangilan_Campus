const roleButtons = document.querySelectorAll('.role-btn');
const roleInput = document.getElementById('role');

roleButtons.forEach(button => {
    button.addEventListener('click', function() {
        // Remove the active class from all buttons
        roleButtons.forEach(btn => btn.classList.remove('active'));
        // Add the active class to the clicked button
        this.classList.add('active');
        // Set the hidden input value to the selected role
        roleInput.value = this.dataset.role;
    });
});