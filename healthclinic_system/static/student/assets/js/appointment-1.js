document.addEventListener('DOMContentLoaded', function () {
    const steps = document.querySelectorAll('.step');
    steps.forEach(step => {
      step.addEventListener('click', function () {
        const url = this.getAttribute('data-href');
        if (url) {
          window.location.href = url;
        }
      });
    });

    const nextButton = document.getElementById('nextButton');
    nextButton.addEventListener('click', function () {
      window.location.href = 'appointment-2.html';
    });
  });