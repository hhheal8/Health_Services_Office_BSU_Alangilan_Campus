
// Function to open the edit modal and populate it with current row data
function openEditModal(button) {
  const row = button.closest('tr');
  const studentId = row.cells[0].innerText;
  const name = row.cells[1].innerText;
  const sex = row.cells[2].innerText;
  const year = row.cells[3].innerText;
  const department = row.cells[4].innerText;

  document.getElementById('editStudentId').value = studentId;
  document.getElementById('editName').value = name;
  document.getElementById('editSex').value = sex;
  document.getElementById('editYear').value = year;
  document.getElementById('editDepartment').value = department;

  document.getElementById('editModal').style.display = 'block';
  document.getElementById('editForm').dataset.rowIndex = row.rowIndex;
}

// Function to close the edit modal
function closeEditModal() {
  document.getElementById('editModal').style.display = 'none';
}

// Function to save changes to the table
function saveChanges() {
  const rowIndex = document.getElementById('editForm').dataset.rowIndex;
  const table = document.getElementById('employeeTableBody');
  const row = table.rows[rowIndex - 1];

  row.cells[1].innerText = document.getElementById('editName').value;
  row.cells[2].innerText = document.getElementById('editSex').value;
  row.cells[3].innerText = document.getElementById('editYear').value;
  row.cells[4].innerText = document.getElementById('editDepartment').value;

  closeEditModal();
}

// Function to delete a row
function deleteRow(button) {
  const row = button.closest('tr');
  row.remove();
}

// Close the modal if the user clicks outside of it
window.onclick = function(event) {
  if (event.target == document.getElementById('editModal')) {
    closeEditModal();
  }
}
