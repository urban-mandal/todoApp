const sidebarButton = document.getElementById("sidebar");
const sidebar = document.getElementById("sideBarDiv");
const taskDiv = document.getElementById("tasks");
const profileDiv = document.getElementById("profile");
const profileTools = document.getElementById("profileTools");
const closeDivButton = document.getElementById("closeDiv");

sidebarButton.onclick = turnAround;
closeDivButton.onclick = closeSideBars;

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

taskDiv.addEventListener("click", function () {
  closeSideBars();
});

function closeSideBars() {
  if (sidebar.style.display === "flex") {
    sidebar.style.display = "none";
    sidebarButton.style.transform = "rotate(0deg)";
    taskDiv.style.marginLeft = "0%";
    taskDiv.style.width = "100%";
  }
  if (profileTools.style.display === "flex") {
    profileTools.style.display = "none";
  }
}

profileDiv.addEventListener("click", function () {
  if (profileTools.style.display === "flex") {
    profileTools.style.display = "none";
  } else {
    profileTools.style.display = "flex";
  }
});
