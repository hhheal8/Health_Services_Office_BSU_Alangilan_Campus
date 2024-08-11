const chartData = {
  labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
  data: [45, 20, 67, 21, 53, 108, 549, 297, 121, 98, 62, 103]
};

const monthlyCommonIllnessData = [
  { labels: ['Common Cold', 'Fever', 'Hypertension', 'Diarrhea', 'Dizziness', 'Others'], data: [23, 9, 1, 14, 29, 12] }, // January
  { labels: ['Common Cold', 'Fever', 'Hypertension', 'Diarrhea', 'Dizziness', 'Others'], data: [15, 7, 2, 10, 29, 12] }, // February
  { labels: ['Common Cold', 'Fever', 'Hypertension', 'Diarrhea', 'Dizziness', 'Others'], data: [18, 8, 3, 12, 29, 12] }, // March
  { labels: ['Common Cold', 'Fever', 'Hypertension', 'Diarrhea', 'Dizziness', 'Others'], data: [12, 14, 5, 3, 29, 12] }, // April
  { labels: ['Common Cold', 'Fever', 'Hypertension', 'Diarrhea', 'Dizziness', 'Others'], data: [20, 2, 1, 17, 29, 12] }, // May
  { labels: ['Common Cold', 'Fever', 'Hypertension', 'Diarrhea', 'Dizziness', 'Others'], data: [14, 12, 4, 15, 29, 12] }, // June
  { labels: ['Common Cold', 'Fever', 'Hypertension', 'Diarrhea', 'Dizziness', 'Others'], data: [12, 11, 3, 14, 29, 12] }, // July
  { labels: ['Common Cold', 'Fever', 'Hypertension', 'Diarrhea', 'Dizziness', 'Others'], data: [19, 3, 1, 2, 29, 12] }, // August
  { labels: ['Common Cold', 'Fever', 'Hypertension', 'Diarrhea', 'Dizziness', 'Others'], data: [13, 4, 3, 12, 29, 12] }, // September
  { labels: ['Common Cold', 'Fever', 'Hypertension', 'Diarrhea', 'Dizziness', 'Others'], data: [11, 1, 5, 10, 29, 12] }, // October
  { labels: ['Common Cold', 'Fever', 'Hypertension', 'Diarrhea', 'Dizziness', 'Others'], data: [12, 2, 2, 8, 29, 12] }, // November
  { labels: ['Common Cold', 'Fever', 'Hypertension', 'Diarrhea', 'Dizziness', 'Others'], data: [16, 4, 0, 9, 29, 12] } // December
];

const monthlyConsumedMedicineData = [
  { labels: ['Paracetamol', 'Amoxicillin', 'Antibiotic Ointment', 'Loperamide', 'Ascorbic Acid'], data: [50, 30, 20, 10, 15] }, // January
  { labels: ['Paracetamol', 'Amoxicillin', 'Antibiotic Ointment', 'Loperamide', 'Ascorbic Acid'], data: [40, 25, 18, 12, 20] }, // February
  { labels: ['Paracetamol', 'Amoxicillin', 'Antibiotic Ointment', 'Loperamide', 'Ascorbic Acid'], data: [45, 28, 22, 14, 18] }, // March
  { labels: ['Paracetamol', 'Amoxicillin', 'Antibiotic Ointment', 'Loperamide', 'Ascorbic Acid'], data: [55, 30, 25, 12, 22] }, // April
  { labels: ['Paracetamol', 'Amoxicillin', 'Antibiotic Ointment', 'Loperamide', 'Ascorbic Acid'], data: [60, 35, 20, 15, 25] }, // May
  { labels: ['Paracetamol', 'Amoxicillin', 'Antibiotic Ointment', 'Loperamide', 'Ascorbic Acid'], data: [50, 28, 22, 10, 20] }, // June
  { labels: ['Paracetamol', 'Amoxicillin', 'Antibiotic Ointment', 'Loperamide', 'Ascorbic Acid'], data: [45, 30, 18, 12, 18] }, // July
  { labels: ['Paracetamol', 'Amoxicillin', 'Antibiotic Ointment', 'Loperamide', 'Ascorbic Acid'], data: [50, 32, 20, 14, 20] }, // August
  { labels: ['Paracetamol', 'Amoxicillin', 'Antibiotic Ointment', 'Loperamide', 'Ascorbic Acid'], data: [55, 30, 22, 16, 23] }, // September
  { labels: ['Paracetamol', 'Amoxicillin', 'Antibiotic Ointment', 'Loperamide', 'Ascorbic Acid'], data: [50, 25, 20, 12, 18] }, // October
  { labels: ['Paracetamol', 'Amoxicillin', 'Antibiotic Ointment', 'Loperamide', 'Ascorbic Acid'], data: [45, 28, 22, 10, 20] }, // November
  { labels: ['Paracetamol', 'Amoxicillin', 'Antibiotic Ointment', 'Loperamide', 'Ascorbic Acid'], data: [60, 35, 18, 14, 22] } // December
];

const monthlyUsedSupplyData = [
  { labels: ['Paracetamol', 'Amoxicillin', 'Antibiotic Ointment', 'Loperamide', 'Ascorbic Acid'], data: [50, 30, 20, 10, 15] }, // January
  { labels: ['Paracetamol', 'Amoxicillin', 'Antibiotic Ointment', 'Loperamide', 'Ascorbic Acid'], data: [40, 25, 18, 12, 20] }, // February
  { labels: ['Paracetamol', 'Amoxicillin', 'Antibiotic Ointment', 'Loperamide', 'Ascorbic Acid'], data: [45, 28, 22, 14, 18] }, // March
  { labels: ['Paracetamol', 'Amoxicillin', 'Antibiotic Ointment', 'Loperamide', 'Ascorbic Acid'], data: [55, 30, 25, 12, 22] }, // April
  { labels: ['Paracetamol', 'Amoxicillin', 'Antibiotic Ointment', 'Loperamide', 'Ascorbic Acid'], data: [60, 35, 20, 15, 25] }, // May
  { labels: ['Paracetamol', 'Amoxicillin', 'Antibiotic Ointment', 'Loperamide', 'Ascorbic Acid'], data: [50, 28, 22, 10, 20] }, // June
  { labels: ['Paracetamol', 'Amoxicillin', 'Antibiotic Ointment', 'Loperamide', 'Ascorbic Acid'], data: [45, 30, 18, 12, 18] }, // July
  { labels: ['Paracetamol', 'Amoxicillin', 'Antibiotic Ointment', 'Loperamide', 'Ascorbic Acid'], data: [50, 32, 20, 14, 20] }, // August
  { labels: ['Paracetamol', 'Amoxicillin', 'Antibiotic Ointment', 'Loperamide', 'Ascorbic Acid'], data: [55, 30, 22, 16, 23] }, // September
  { labels: ['Paracetamol', 'Amoxicillin', 'Antibiotic Ointment', 'Loperamide', 'Ascorbic Acid'], data: [50, 25, 20, 12, 18] }, // October
  { labels: ['Paracetamol', 'Amoxicillin', 'Antibiotic Ointment', 'Loperamide', 'Ascorbic Acid'], data: [45, 28, 22, 10, 20] }, // November
  { labels: ['Paracetamol', 'Amoxicillin', 'Antibiotic Ointment', 'Loperamide', 'Ascorbic Acid'], data: [60, 35, 18, 14, 22] } // December
];

const studentChartData = {
  labels: ['Male', 'Female'],
  data: [60, 40]
};

const stockChartData = {
  labels: ['Bandage', 'Antibiotic Ointment', 'Alcohol'],
  datasets: [
    {
      label: 'Current Stock',
      data: [275, 200, 432],
      backgroundColor: '#F12C2C',
      borderColor: '#FFF',
      borderWidth: 1
    },
    {
      label: 'Minimum Stock Level',
      data: [150, 75, 100],
      backgroundColor: '#ffa4a4',
      borderColor: '#FFF',
      borderWidth: 1
    }
  ]
};

// Initialize charts
let commonIllnessChart, consumedMedicineChart, usedSupplyChart;

function initializeCommonIllnessChart() {
  const ctx = document.getElementById('CommonIllnnessChart').getContext('2d');
  commonIllnessChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: monthlyCommonIllnessData[0].labels, // Will be updated dynamically
      datasets: [{
        label: 'Number of Illness',
        data: monthlyCommonIllnessData[0].data, // Will be updated dynamically
        backgroundColor: '#F12C2C',
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false }
      },
      scales: {
        x: {
          grid: { display: false },
          ticks: {
            font: { size: 13, weight: 'bold' }
          }
        },
        y: {
          grid: { display: true, color: 'rgba(0, 0, 0, 0.1)', lineWidth: 1 },
          ticks: {
            font: { size: 14, weight: 'bold' },
            beginAtZero: true
          }
        }
      }
    },
  });
}

function initializeConsumedMedicineChart() {
  const ctx = document.getElementById('consumedMedicineChart').getContext('2d');
  consumedMedicineChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: monthlyConsumedMedicineData[0].labels, // Will be updated dynamically
      datasets: [{
        label: 'Consumed Medicine',
        data: monthlyConsumedMedicineData[0].data, // Will be updated dynamically
        backgroundColor: '#F12C2C',
        borderColor: '#FFF',
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: true }
      },
      scales: {
        x: {
          grid: { display: false },
          ticks: {
            font: { size: 13, weight: 'bold' }
          }
        },
        y: {
          grid: { display: true, color: 'rgba(0, 0, 0, 0.1)', lineWidth: 1 },
          ticks: {
            font: { size: 14, weight: 'bold' },
            beginAtZero: true
          }
        }
      }
    }
  });
}

function initializeUsedSupplyChart() {
  const ctx = document.getElementById('usedSupplyChart').getContext('2d');
  usedSupplyChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: monthlyUsedSupplyData[0].labels, // Will be updated dynamically
      datasets: [{
        label: 'Consumed Medicine',
        data: monthlyUsedSupplyData[0].data, // Will be updated dynamically
        backgroundColor: '#F12C2C',
        borderColor: '#FFF',
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: true }
      },
      scales: {
        x: {
          grid: { display: false },
          ticks: {
            font: { size: 13, weight: 'bold' }
          }
        },
        y: {
          grid: { display: true, color: 'rgba(0, 0, 0, 0.1)', lineWidth: 1 },
          ticks: {
            font: { size: 14, weight: 'bold' },
            beginAtZero: true
          }
        }
      }
    }
  });
}

function updateCommonIllnessChart() {
  const selectedMonth = parseInt(document.getElementById('commonIllnessMonthSelector').value, 10);
  const data = monthlyCommonIllnessData[selectedMonth];
  commonIllnessChart.data.labels = data.labels;
  commonIllnessChart.data.datasets[0].data = data.data;
  commonIllnessChart.update();
}

function updateConsumedMedicineChart() {
  const selectedMonth = parseInt(document.getElementById('consumedMedicineMonthSelector').value, 10);
  const data = monthlyConsumedMedicineData[selectedMonth];
  consumedMedicineChart.data.labels = data.labels;
  consumedMedicineChart.data.datasets[0].data = data.data;
  consumedMedicineChart.update();
}

function updateUsedSupplyChart() {
  const selectedMonth = parseInt(document.getElementById('usedSupplyMonthSelector').value, 10);
  const data = monthlyUsedSupplyData[selectedMonth];
  usedSupplyChart.data.labels = data.labels;
  usedSupplyChart.data.datasets[0].data = data.data;
  usedSupplyChart.update();
}

function appointmentsChart() {
  const ctx = document.getElementById('appointmentsChart').getContext('2d');
  new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
      datasets: [{
        label: 'Appointments',
        data: [45, 20, 67, 21, 53, 108, 549, 297, 121, 98, 62, 103],
        borderColor: '#F12C2C',
        backgroundColor: 'rgba(241, 44, 44, 0.2)',
        borderWidth: 3
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: true,
      scales: {
        x: {
          ticks: {
            font: { weight: 'bold' }
          }
        },
        y: {
          ticks: {
            font: { weight: 'bold' }
          }
        }
      },
      plugins: {
        legend: {
          labels: {
            font: { weight: 'bold' }
          }
        },
        tooltip: {
          backgroundColor: '#F12C2C',
          borderColor: 'rgba(75, 192, 192, 1)',
          borderWidth: 2,
          titleFont: {
            family: 'Arial',
            size: 16,
            weight: 'bold',
            lineHeight: 1.2
          },
          bodyFont: {
            family: 'Arial',
            size: 14,
            weight: 'bold',
            lineHeight: 1.2
          },
          titleColor: '#FFFFFF',
          bodyColor: '#FFFFFF',
          padding: 10,
          cornerRadius: 5,
          displayColors: false,
          callbacks: {
            label: function (context) {
              let label = context.dataset.label || '';
              if (label) {
                label += ': ';
              }
              if (context.parsed.y !== null) {
                label += context.parsed.y;
              }
              return label;
            }
          }
        }
      }
    }
  });
}
function studentStructureChart() {
  const ctx = document.getElementById('studentChart').getContext('2d');
  new Chart(ctx, {
    type: 'pie', // Chart type
    data: {
      labels: studentChartData.labels, // Use the combined labels
      datasets: [{
        data: studentChartData.data, // Use the combined data
        backgroundColor: ['#F12C2C', '#ffa4a4'], // Colors for the segments
        borderColor: '#FFF', // Border color for the segments
        borderWidth: 1
      }]
    },
    options: {
      responsive: true, // Ensure the chart resizes with the container
      maintainAspectRatio: false, // Disable aspect ratio to fit the container
      plugins: {
        legend: {
          position: 'top', // Position the legend at the top
          labels: {
            color: '#000', // Set legend text color to white
            font: {
              size: 14,
              weight: 'bold' // Make legend text bold
            }
          }
        },
        tooltip: {
          backgroundColor: '#000', // Tooltip background color
          titleColor: '#FFF', // Tooltip title text color
          bodyColor: '#FFF' // Tooltip body text color
        }
      }
    }
  });
}


function renderStockChart() {
  const ctx = document.getElementById('stockChart').getContext('2d');
  new Chart(ctx, {
    type: 'bar',
    data: stockChartData,
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: true }
      },
      scales: {
        x: {
          stacked: true,
          grid: { display: false },
          ticks: {
            font: { size: 14, weight: 'bold' }
          }
        },
        y: {
          stacked: true,
          grid: { display: true, color: 'rgba(0, 0, 0, 0.1)', lineWidth: 1 },
          ticks: {
            font: { size: 14, weight: 'bold' },
            beginAtZero: true
          }
        }
      }
    }
  });
}

document.addEventListener('DOMContentLoaded', function () {
  initializeCommonIllnessChart();
  initializeConsumedMedicineChart();
  initializeUsedSupplyChart();
  studentStructureChart();
  appointmentsChart();
  renderStockChart();

  // Set up event listeners for month selectors
  document.getElementById('monthSelector').addEventListener('change', function () {
    updateCommonIllnessChart();
    updateConsumedMedicineChart();
  });
});
