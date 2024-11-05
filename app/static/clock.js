// static/clock.js
function updateClock() {
  const now = new Date();
  let hours = now.getHours();
  let minutes = now.getMinutes();
  let seconds = now.getSeconds();

  hours = hours < 10 ? "0" + hours : hours;
  minutes = minutes < 10 ? "0" + minutes : minutes;
  seconds = seconds < 10 ? "0" + seconds : seconds;

  // Update each part of the clock
  document.getElementById("hours").textContent = hours;
  document.getElementById("minutes").textContent = minutes;
  document.getElementById("seconds").textContent = seconds;
}

window.onload = function () {
  setInterval(updateClock, 1000);
};

document.addEventListener("keydown", function (event) {
  if (/^[a-z]$/i.test(event.key)) {
    // This regex matches any single character from a to z, case-insensitive
    fetch("/keypress", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ key: event.key.toLowerCase() }),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(
            "Network response was not ok: " + response.statusText,
          );
        }
        return response.json();
      })
      .then((data) => console.log(data))
      .catch((error) => console.error("Fetch error:", error));
  }
});
