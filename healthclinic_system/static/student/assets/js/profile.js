    // Function to open the modal
    function openModal() {
      document.getElementById('editModal').style.display = 'block';
      
      document.getElementById('editName').value = document.getElementById('profile-name').textContent;
      document.getElementById('editSRCode').value = document.getElementById('profile-sr-code').textContent;
      document.getElementById('editAge').value = document.getElementById('profile-age').textContent;
      document.getElementById('editSex').value = document.getElementById('profile-sex').textContent;
      document.getElementById('editContact').value = document.getElementById('profile-contact').textContent;
      document.getElementById('editAddress').value = document.getElementById('profile-address').textContent;
      document.getElementById('editEmail').value = document.getElementById('profile-email').textContent;
    }

    // Function to close the modal
    function closeModal() {
      document.getElementById('editModal').style.display = 'none';
    }

    // Function to save the profile changes
    function saveProfile() {
      
      const updatedName = document.getElementById('editName').value;
      const updatedSRCode = document.getElementById('editSRCode').value;
      const updatedAge = document.getElementById('editAge').value;
      const updatedSex = document.getElementById('editSex').value;
      const updatedContact = document.getElementById('editContact').value;
      const updatedAddress = document.getElementById('editAddress').value;
      const updatedEmail = document.getElementById('editEmail').value;

      // Update the profile information on the main page
      document.getElementById('profile-name').textContent = updatedName;
      document.getElementById('profile-sr-code').textContent = updatedSRCode;
      document.getElementById('profile-age').textContent = updatedAge;
      document.getElementById('profile-sex').textContent = updatedSex;
      document.getElementById('profile-contact').textContent = updatedContact;
      document.getElementById('profile-address').textContent = updatedAddress;
      document.getElementById('profile-email').textContent = updatedEmail;

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

