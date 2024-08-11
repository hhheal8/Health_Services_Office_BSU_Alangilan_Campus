
    // Function to save the profile changes
    function saveProfile() {
        
        const updatedName = document.getElementById('editName').value;
        const updatedSRCode = document.getElementById('editSRCode').value;
        const updatedAge = document.getElementById('editAge').value;
        const updatedSex = document.getElementById('editSex').value;
        const updatedContact = document.getElementById('editContact').value;
        const updatedAddress = document.getElementById('editAddress').value;
        const updatedEmail = document.getElementById('editEmail').value;
  
        console.log('Profile updated:', {
          Name: updatedName,
          SRCode: updatedSRCode,
          Age: updatedAge,
          Sex: updatedSex,
          Contact: updatedContact,
          Address: updatedAddress,
          Email: updatedEmail
        });
  
       
        alert('Profile updated successfully!');
      }