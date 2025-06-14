let transactions = [];

document.addEventListener("DOMContentLoaded", async () => {
  // Load data from backend once page is redy
  await loadTransactions();
  setupFilters();
  updateDashboard(transactions);
});

// Fetch transaction data from the back-end
async function loadTransactions() {
  try {
    const res = await fetch("/data");
    const data = await res.json();
    transactions = data;
  } catch (err) {
    console.error("Could not load data:", err);
  }
}

// Set up the filter buton to apply filtering logic
function setupFilters() {
  document.getElementById("applyFilters").addEventListener("click", () => {
    const filtered = filterData(transactions);
    updateDashboard(filtered);
  });
}

// Filter data based on user input
function filterData(data) {
  const category = document.getElementById("categoryFilter").value;
  const min = parseFloat(document.getElementById("minAmount").value) || 0;
  const max = parseFloat(document.getElementById("maxAmount").value) || Infinity;

  return data.filter(tx =>
    (category === "All" || tx.category === category) &&
    tx.amount >= min && tx.amount <= max
  );
}

// Update the entier dashboard
function updateDashboard(data) {
  showTable(data);
  showCategoryChart(data);
  showMonthlyChart(data);
}

// Display the table of transactions
function showTable(data) {
  const tbody = document.getElementById("transactionTableBody");
  tbody.innerHTML = "";

  data.forEach(tx => {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${tx.date}</td>
      <td>${tx.category}</td>
      <td>${tx.amount} RWF</td>
      <td>${tx.sender || "-"}</td>
      <td>${tx.receiver || "-"}</td>
      <td>${tx.transaction_id || "-"}</td>
    `;
    tbody.appendChild(row);
  });
}

// Create a bar chart per category
function showCategoryChart(data) {
  const ctx = document.getElementById("categoryChart").getContext("2d");
  if (window.categoryChart) window.categoryChart.destroy();

  const totals = {};
  data.forEach(tx => {
    totals[tx.category] = (totals[tx.category] || 0) + tx.amount;
  });

  const labels = Object.keys(totals);
  const values = Object.values(totals);

  window.categoryChart = new Chart(ctx, {
    type: "bar",
    data: {
      labels,
      datasets: [{
        label: "Total per Category",
        data: values,
        backgroundColor: "#4b9cd3"
      }]
    },
    options: {
      responsive: true,
      plugins: { legend: { display: false } },
      scales: { y: { beginAtZero: true } }
    }
  });
}

// Create a line chart showing totals per month
function showMonthlyChart(data) {
  const ctx = document.getElementById("monthlyChart").getContext("2d");
  if (window.monthlyChart) window.monthlyChart.destroy();

  const totals = {};
  data.forEach(tx => {
    const month = tx.date.slice(0, 7); // grabs "YYYY-MM"
    totals[month] = (totals[month] || 0) + tx.amount;
  });

  const labels = Object.keys(totals).sort();
  const values = labels.map(month => totals[month]);

  window.monthlyChart = new Chart(ctx, {
    type: "line",
    data: {
      labels,
      datasets: [{
        label: "Monthly Totals",
        data: values,
        borderColor: "#2e7d32",
        fill: false,
        tension: 0.3
      }]
    },
    options: {
      responsive: true,
      plugins: { legend: { display: false } },
      scales: { y: { beginAtZero: true } }
    }
  });
}
