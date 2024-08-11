
document.addEventListener('DOMContentLoaded', function() {
  // Get the dropdown menu element
  const dropdownMenu = document.querySelector('.dropdown-menu');

  // Toggle dropdown menu visibility on click
  document.querySelector('.header-right').addEventListener('click', function() {
    dropdownMenu.classList.toggle('show');
  });

  // Close dropdown menu if user clicks outside of it
  document.addEventListener('click', function(event) {
    if (!event.target.closest('.header-right')) {
      dropdownMenu.classList.remove('show');
    }
  });
});

