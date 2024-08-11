function cancelAppointment(button) {
    
    var cell = button.parentNode;
    cell.innerHTML = '<span class="text-danger">Cancelled</span>';
}