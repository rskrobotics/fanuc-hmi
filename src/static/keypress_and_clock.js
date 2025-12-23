function updateClock() {
  const now = new Date();
  let hours = now.getHours();
  let minutes = now.getMinutes();
  let seconds = now.getSeconds();

  hours = hours < 10 ? "0" + hours : hours;
  minutes = minutes < 10 ? "0" + minutes : minutes;
  seconds = seconds < 10 ? "0" + seconds : seconds;

  document.getElementById("hours").textContent = hours;
  document.getElementById("minutes").textContent = minutes;
  document.getElementById("seconds").textContent = seconds;
}

window.onload = function () {
  setInterval(updateClock, 1000);
};

function showAlertOverlay() {
  const overlay = document.getElementById("alert-overlay");
  overlay.style.display = "flex";
  setTimeout(() => {
    overlay.style.display = "none";
  }, 2000);
}

document.addEventListener("keydown", function (event) {
  if (/^[a-z]$/i.test(event.key)) {
    showAlertOverlay();

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
