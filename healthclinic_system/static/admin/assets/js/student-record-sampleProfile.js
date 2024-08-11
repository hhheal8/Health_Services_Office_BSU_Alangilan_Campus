
$(document).ready(function() {
    $('.header-right a, .fa-chevron-down').on('click', function() {
      $('.dropdown-menu').toggleClass('show');
    });
  });
  // Function to open the modal
  function openModal() {
    document.getElementById('editModal').style.display = 'block';
    
    document.getElementById('editLname').value = document.getElementById('lname').textContent;
    document.getElementById('editFname').value = document.getElementById('fname').textContent;
    document.getElementById('editMname').value = document.getElementById('mname').textContent;
    document.getElementById('editAge').value = document.getElementById('age').textContent;
    document.getElementById('editSex').value = document.getElementById('sex').textContent;
    document.getElementById('editBirthdate').value = document.getElementById('birthdate').textContent;
    document.getElementById('editDate').value = document.getElementById('date').textContent;
    document.getElementById('editCivilStatus').value = document.getElementById('civilStatus').textContent;
    document.getElementById('editTelephoneNumber').value = document.getElementById('telephoneNumber').textContent;
    document.getElementById('editContactNumber').value = document.getElementById('contactNumber').textContent;
    document.getElementById('editAddress').value = document.getElementById('address').textContent;
    document.getElementById('editPosition').value = document.getElementById('position').textContent;

    

  }

  // Function to close the modal
  function closeModal() {
    document.getElementById('editModal').style.display = 'none';
  }
function saveProfile() {
const updatedLname = document.getElementById('editLname').value;
const updatedFname = document.getElementById('editFname').value;
const updatedMname = document.getElementById('editMname').value;
const updatedAge = document.getElementById('editAge').value;
const updatedSex = document.getElementById('editSex').value;
const updatedBirthdate = document.getElementById('editBirthdate').value;
const updatedDate = document.getElementById('editDate').value;
const updatedCivilStatus = document.getElementById('editCivilStatus').value;
const updatedTelephoneNumber = document.getElementById('editTelephoneNumber').value;
const updatedContactNumber = document.getElementById('editContactNumber').value;
const updatedAddress = document.getElementById('editAddress').value;
const updatedPosition = document.getElementById('editPosition').value;

// Update the profile information on the main page
document.getElementById('lname').textContent = updatedLname;
document.getElementById('fname').textContent = updatedFname;
document.getElementById('mname').textContent = updatedMname;
document.getElementById('age').textContent = updatedAge;
document.getElementById('sex').textContent = updatedSex;
document.getElementById('birthdate').textContent = updatedBirthdate;
document.getElementById('date').textContent = updatedDate;
document.getElementById('civilstatus').textContent = updatedCivilStatus;
document.getElementById('telephoneNumber').textContent = updatedTelephoneNumber;
document.getElementById('contactNumber').textContent = updatedContactNumber;
document.getElementById('address').textContent = updatedAddress;
document.getElementById('position').textContent = updatedPosition;

// Update the profile image if a new file is selected
const editImage = document.getElementById('editImage');
if (editImage.files && editImage.files[0]) {
  const reader = new FileReader();
  reader.onload = function(e) {
    document.getElementById('profile-image').src = e.target.result;
  };
  reader.readAsDataURL(editImage.files[0]);
}

// Close the modal
closeModal();
}


  // Function to update file name in the modal
  document.getElementById('editImage').addEventListener('change', function(event) {
    const fileName = event.target.files[0] ? event.target.files[0].name : 'No file chosen';
    document.getElementById('fileName').textContent = fileName;
  });

  // Close the modal when clicking outside of the modal content
  window.onclick = function(event) {
    const modal = document.getElementById('editModal');
    if (event.target == modal) {
      modal.style.display = 'none';
    }
  }

