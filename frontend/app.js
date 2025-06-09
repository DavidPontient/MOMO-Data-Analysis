// Exampless
const transactions = [
  { date: "2024-01-01", type: "incoming", amount: 5000, description: "From John Doe" },
  { date: "2024-01-02", type: "payment", amount: 1500, description: "To Jane Smith" },
  { date: "2024-01-03", type: "payment", amount: 3000, description: "To Airtime" },
  { date: "2024-01-04", type: "withdrawal", amount: 20000, description: "Via agent Jane Doe" },
  { date: "2024-01-05", type: "bundle", amount: 2000, description: "1GB of interenet" },
];

// Add tables
function populateTable(data) {
  const tbody = document.getElementById("transaction-table-body");
  tbody.innerHTML = "";
  data.forEach(tx => {
    const row = `<tr>
      <td>${tx.date}</td>
      <td>${tx.type}</td>
      <td>${tx.amount}</td>
      <td>${tx.description}</td>
    </tr>`;
    tbody.insertAdjacentHTML("beforeend", row);
  });
}

// Filters (basic implementation)
function applyFilters() {
  const type = document.getElementById("transaction-type").value;
  const fromDate = document.getElementById("date-from").value;
  const toDate = document.getElementById("date-to").value;

  let filtered = transactions;

  if (type !== "all") {
    filtered = filtered.filter(tx => tx.type === type);
  }
  if (fromDate) {
    filtered = filtered.filter(tx => tx.date >= fromDate);
  }
  if (toDate) {
    filtered = filtered.filter(tx => tx.date <= toDate);
  }

  populateTable(filtered);
}

// Chart.js - Transaction Volume by Type
function drawTypeChart() {
  const ctx = document.getElementById("typeChart").getContext("2d");
  const types = {};
  transactions.forEach(tx => {
    types[tx.type] = (types[tx.type] || 0) + tx.amount;
  });

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: Object.keys(types),
      datasets: [{
        label: "Total Volume (RWF)",
        data: Object.values(types),
        backgroundColor: "#ffd700",
        borderColor: "#003366",
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      scales: { y: { beginAtZero: true } }
    }
  });
}

// Monthly summary
function drawMonthlyChart() {
  const ctx = document.getElementById("monthlyChart").getContext("2d");
  const months = {};

  transactions.forEach(tx => {
    const month = tx.date.slice(0, 7); // "YYYY-MM"
    months[month] = (months[month] || 0) + tx.amount;
  });

  new Chart(ctx, {
    type: 'line',
    data: {
      labels: Object.keys(months),
      datasets: [{
        label: "Monthly Transaction Total",
        data: Object.values(months),
        borderColor: "#003366",
        backgroundColor: "rgba(0, 51, 102, 0.2)",
        fill: true
      }]
    },
    options: {
      responsive: true,
      scales: { y: { beginAtZero: true } }
    }
  });
}

// Initial load
populateTable(transactions);
drawTypeChart();
drawMonthlyChart();
