
const calendarBody = document.getElementById('calendar-body');
const calendarMonth = document.getElementById('calendar-month');
const dateInputContainer = document.getElementById('date-input-container');
const dateInput = document.getElementById('dateInput');

const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
let currentMonth = new Date().getMonth();
let currentYear = new Date().getFullYear();

function renderCalendar(month, year) {
  calendarBody.innerHTML = '';
  calendarMonth.textContent = monthNames[month] + ' ' + year;

  const firstDay = new Date(year, month, 1).getDay();
  const daysInMonth = new Date(year, month + 1, 0).getDate();

  let dayCounter = 1;
  for (let week = 0; week < 6; week++) {
    const row = document.createElement('tr');
    for (let day = 0; day < 7; day++) {
      const cell = document.createElement('td');
      if (week === 0 && day < firstDay) {
        cell.innerHTML = '';
      } else if (dayCounter <= daysInMonth) {
        cell.innerHTML = dayCounter;
        cell.addEventListener('click', function () {
          const selectedDate = year + '-' + String(month + 1).padStart(2, '0') + '-' + String(dayCounter).padStart(2, '0');
          document.querySelectorAll('.calendar-table td').forEach(td => td.classList.remove('selected', 'highlighted-date'));
          cell.classList.add('selected', 'highlighted-date');
          filterAppointmentsByDate(selectedDate);
          highlightSelectedDate(selectedDate);
        });
        dayCounter++;
      } else {
        cell.innerHTML = '';
      }
      row.appendChild(cell);
    }
    calendarBody.appendChild(row);
  }
}

function prevMonth() {
  if (currentMonth === 0) {
    currentMonth = 11;
    currentYear--;
  } else {
    currentMonth--;
  }
  renderCalendar(currentMonth, currentYear);
}

function nextMonth() {
  if (currentMonth === 11) {
    currentMonth = 0;
    currentYear++;
  } else {
    currentMonth++;
  }
  renderCalendar(currentMonth, currentYear);
}

function filterAppointmentsByDate(selectedDate) {
  const appointments = document.querySelectorAll('#appointmentList tr');
  appointments.forEach(appointment => {
    const appointmentDate = appointment.getAttribute('data-date');
    if (selectedDate === appointmentDate || !selectedDate) {
      appointment.style.display = '';
    } else {
      appointment.style.display = 'none';
    }
  });
}

function filterAppointments() {
  const selectedDate = document.getElementById('dateFilter').value;
  filterAppointmentsByDate(selectedDate);
}

function toggleDateInput() {
  if (dateInputContainer.style.display === 'none') {
    dateInputContainer.style.display = 'flex';
  } else {
    dateInputContainer.style.display = 'none';
  }
}

function goToSelectedDate() {
  const selectedDate = new Date(dateInput.value);
  currentMonth = selectedDate.getMonth();
  currentYear = selectedDate.getFullYear();
  renderCalendar(currentMonth, currentYear);
  filterAppointmentsByDate(dateInput.value);
  highlightSelectedDate(dateInput.value);
}

function markAsComplete(button) {
  const row = button.closest('tr');
  row.querySelector('.status').classList.remove('ongoing', 'declined');
  row.querySelector('.status').classList.add('complete');
  row.querySelector('.status').textContent = 'Complete';
}

function markAsDeclined(button) {
  const row = button.closest('tr');
  row.querySelector('.status').classList.remove('ongoing', 'complete');
  row.querySelector('.status').classList.add('declined');
  row.querySelector('.status').textContent = 'Declined';
}

function highlightSelectedDate(selectedDate) {
  const date = new Date(selectedDate);
  const day = date.getDate();
  const month = date.getMonth();
  const year = date.getFullYear();
  if (month === currentMonth && year === currentYear) {
    const cells = calendarBody.querySelectorAll('td');
    cells.forEach(cell => {
      if (parseInt(cell.textContent) === day) {
        cell.classList.add('highlighted-date');
      } else {
        cell.classList.remove('highlighted-date');
      }
    });
  }
}

renderCalendar(currentMonth, currentYear);
