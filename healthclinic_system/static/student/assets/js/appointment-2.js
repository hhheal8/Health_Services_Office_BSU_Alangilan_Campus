const calendarBody = document.getElementById('calendar-body');
    const calendarMonth = document.getElementById('calendar-month');
    const selectionDisplay = document.getElementById('selection-display');
    const note = document.getElementById('note');
    let selectedDate = null;
    let selectedTimeSlot = null;

    const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    let currentMonth = new Date().getMonth();
    let currentYear = new Date().getFullYear();

    function renderCalendar(month, year) {
      calendarBody.innerHTML = '';
      calendarMonth.textContent = `${monthNames[month]} ${year}`;

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
              selectedDate = `${year}-${String(month + 1).padStart(2, '0')}-${String(dayCounter).padStart(2, '0')}`;
              document.querySelectorAll('.calendar-table td').forEach(td => td.classList.remove('selected'));
              cell.classList.add('selected');
              updateSelectionDisplay();
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

    function updateSelectionDisplay() {
      if (selectedDate && selectedTimeSlot) {
        note.style.display = 'none';
        selectionDisplay.textContent = `Selected Date: ${selectedDate}, Selected Time: ${selectedTimeSlot}`;
      } else {
        note.style.display = 'block';
        selectionDisplay.textContent = '';
      }
    }

    document.addEventListener('DOMContentLoaded', function () {
      renderCalendar(currentMonth, currentYear);
      const steps = document.querySelectorAll('.step');
      steps.forEach(step => {
        step.addEventListener('click', function () {
          const url = this.getAttribute('data-href');
          if (url) {
            window.location.href = url;
          }
        });
      });

      const dropdownItems = document.querySelectorAll('.dropdown-item');
      const dropdownToggle = document.querySelector('.dropdown-toggle');

      dropdownItems.forEach(item => {
        item.addEventListener('click', function (event) {
          event.preventDefault();
          selectedTimeSlot = this.textContent;
          dropdownToggle.textContent = selectedTimeSlot;
          updateSelectionDisplay();
        });
      });
    });

///steps function///
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

    document.getElementById('nextButton').addEventListener('click', function () {
      window.location.href = 'appointment-3.html';
    });
  });