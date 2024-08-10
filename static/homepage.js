const sidebarButton = document.getElementById("sidebar");
const sidebar = document.getElementById("sideBarDiv");

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
  if (sidebar.style.display === "flex") {
    sidebar.style.display = "none";
  } else {
    sidebar.style.display = "flex";
  }
}
