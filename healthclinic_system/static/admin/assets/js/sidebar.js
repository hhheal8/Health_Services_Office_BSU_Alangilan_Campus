

document.querySelectorAll('.sidebar-menu a').forEach(item => {
  item.addEventListener('click', function() {
    document.querySelectorAll('.sidebar-menu a').forEach(link => {
      link.classList.remove('active');
    });
    this.classList.add('active');
  });
});

document.addEventListener('DOMContentLoaded', function () {
  var dropdown = document.getElementsByClassName("dropdown-container");
  for (var i = 0; i < dropdown.length; i++) {
    dropdown[i].addEventListener("click", function () {
      this.classList.toggle("active");
      var dropdownContent = this.nextElementSibling;
      var arrow = this.querySelector(".arrow");
      if (dropdownContent.style.display === "block") {
        dropdownContent.style.display = "none";
        arrow.classList.remove("down");
      } else {
        dropdownContent.style.display = "block";
        arrow.classList.add("down");
      }
    });
  }

  // Ensure the dropdown content stays open if a link inside it is clicked
  var dropdownContentLinks = document.querySelectorAll('.drop-down-content a');
  dropdownContentLinks.forEach(link => {
    link.addEventListener('click', function(event) {
      event.stopPropagation(); // Prevent the dropdown from closing
      document.querySelectorAll('.drop-down-content a').forEach(link => {
        link.classList.remove('active');
      });
      this.classList.add('active');
    });
  });
});