const sidebarButton = document.getElementById("sidebar");

sidebarButton.onclick = turnAround;

function turnAround() {
  if (
    sidebarButton.style.transform === "" ||
    sidebarButton.style.transform === "rotate(0deg)"
  ) {
    sidebarButton.style.transform = "rotate(90deg)";
  } else {
    sidebarButton.style.transform = "rotate(0deg)";
  }
}
