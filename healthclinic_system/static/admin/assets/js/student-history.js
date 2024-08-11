
function deleteRow(button) {
  const row = button.closest('tr');
  row.remove();
}

let currentEditRow;

function openEditModal(button) {
  const row = button.closest('tr');
  currentEditRow = row;

  // Get current data
  const studentID = row.cells[0].innerText;
  const name = row.cells[1].innerText;
  const date = row.cells[2].innerText;
  const time = row.cells[3].innerText;
  const nurse = row.cells[4].innerText;
  const purpose = row.cells[5].innerText;

  // Fill form with current data
  document.getElementById('editStudentID').value = studentID;
  document.getElementById('editName').value = name;
  document.getElementById('editDate').value = date;
  document.getElementById('editTime').value = time;
  document.getElementById('editNurse').value = nurse;
  document.getElementById('editPurpose').value = purpose;

  document.getElementById('editModal').style.display = 'block';
}

function closeEditModal() {
  document.getElementById('editModal').style.display = 'none';
}

function saveEdit() {
  const studentID = document.getElementById('editStudentID').value;
  const name = document.getElementById('editName').value;
  const date = document.getElementById('editDate').value;
  const time = document.getElementById('editTime').value;
  const nurse = document.getElementById('editNurse').value;
  const purpose = document.getElementById('editPurpose').value;

  // Update table row with new data
  currentEditRow.cells[0].innerText = studentID;
  currentEditRow.cells[1].innerText = name;
  currentEditRow.cells[2].innerText = date;
  currentEditRow.cells[3].innerText = time;
  currentEditRow.cells[4].innerText = nurse;
  currentEditRow.cells[5].innerText = purpose;

  closeEditModal();
}

// Close the modal when clicking outside of it
window.onclick = function(event) {
  if (event.target == document.getElementById('editModal')) {
    closeEditModal();
  }
}
