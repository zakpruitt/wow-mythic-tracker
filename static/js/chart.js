/* globals Chart:false, feather:false */

// charts
var pie = document.getElementById("pie");
var bar = document.getElementById("bar");

feather.replace();

(function () {
  // eslint-disable-next-line no-unused-vars
  var PieChart = new Chart(pie, {
    type: "pie",
    data: {
      labels: ["Red", "Yellow", "Blue"],
      datasets: [
        {
          data: [10, 20, 30],
        },
      ],
    },
  });

  var BarChart = new Chart(bar, {
    type: "bar",
    data: {
      labels: ["January", "February", "March", "April", "May", "June", "July"],
      datasets: [
        {
          label: "My First Dataset",
          data: [65, 59, 80, 81, 56, 55, 40],
          fill: false,
          backgroundColor: [
            "rgba(255, 99, 132, 0.2)",
            "rgba(255, 159, 64, 0.2)",
            "rgba(255, 205, 86, 0.2)",
            "rgba(75, 192, 192, 0.2)",
            "rgba(54, 162, 235, 0.2)",
            "rgba(153, 102, 255, 0.2)",
            "rgba(201, 203, 207, 0.2)",
          ],
          borderColor: [
            "rgb(255, 99, 132)",
            "rgb(255, 159, 64)",
            "rgb(255, 205, 86)",
            "rgb(75, 192, 192)",
            "rgb(54, 162, 235)",
            "rgb(153, 102, 255)",
            "rgb(201, 203, 207)",
          ],
          borderWidth: 1,
        },
      ],
    },
    options: { scales: { yAxes: [{ ticks: { beginAtZero: true } }] } },
  });

  pie.style.display = "none";
})();


function showPieChart() {
  bar.style.display = "none";
  pie.style.display = "block";
}

function showBarChart() {
  pie.style.display = "none";
  bar.style.display = "block";
}
