document.addEventListener("DOMContentLoaded", function () {
  let btn = document.querySelector("#btn");
  let sidebar = document.querySelector(".sidebar");

  // Toggle the sidebar's active class when the button is clicked
  btn.onclick = function () {
    sidebar.classList.toggle("active");
  };

  // Select all list items
  const listItems = document.querySelectorAll("li");

  listItems.forEach((listItem) => {
    listItem.addEventListener("mouseover", function () {
      const homeIcon = this.querySelector(".home-icon");
      const calendarIcon = this.querySelector(".calendar-icon");
      const memberIcon = this.querySelector(".member-icon");
      const settingsIcon = this.querySelector(".settings-icon");
      const logoutIcon = this.querySelector(".logout-icon");

      // Change the icon images when hovered
      if (homeIcon) {
        if (!homeIcon.hasAttribute('data-original-src')) {
          homeIcon.setAttribute('data-original-src', homeIcon.src); // Store original src
        }
        homeIcon.src = homeIcon.getAttribute("data-hover-src");
      }
      if (calendarIcon) {
        if (!calendarIcon.hasAttribute('data-original-src')) {
          calendarIcon.setAttribute('data-original-src', calendarIcon.src); // Store original src
        }
        calendarIcon.src = calendarIcon.getAttribute("data-hover-src");
      }
      if (memberIcon) {
        if (!memberIcon.hasAttribute('data-original-src')) {
          memberIcon.setAttribute('data-original-src', memberIcon.src); // Store original src
        }
        memberIcon.src = memberIcon.getAttribute("data-hover-src");
      }
      if (settingsIcon) {
        if (!settingsIcon.hasAttribute('data-original-src')) {
          settingsIcon.setAttribute('data-original-src', settingsIcon.src); // Store original src
        }
        settingsIcon.src = settingsIcon.getAttribute("data-hover-src");
      }
      if (logoutIcon) {
        if (!logoutIcon.hasAttribute('data-original-src')) {
          logoutIcon.setAttribute('data-original-src', logoutIcon.src); // Store original src
        }
        logoutIcon.src = logoutIcon.getAttribute("data-hover-src");
      }
    });

    listItem.addEventListener("mouseout", function () {
      const homeIcon = this.querySelector(".home-icon");
      const calendarIcon = this.querySelector(".calendar-icon");
      const memberIcon = this.querySelector(".member-icon");
      const settingsIcon = this.querySelector(".settings-icon");
      const logoutIcon = this.querySelector(".logout-icon");

      // Restore original icon images
      if (homeIcon && homeIcon.hasAttribute('data-original-src')) {
        homeIcon.src = homeIcon.getAttribute('data-original-src');
      }
      if (calendarIcon && calendarIcon.hasAttribute('data-original-src')) {
        calendarIcon.src = calendarIcon.getAttribute('data-original-src');
      }
      if (memberIcon && memberIcon.hasAttribute('data-original-src')) {
        memberIcon.src = memberIcon.getAttribute('data-original-src');
      }
      if (settingsIcon && settingsIcon.hasAttribute('data-original-src')) {
        settingsIcon.src = settingsIcon.getAttribute('data-original-src');
      }
      if (logoutIcon && logoutIcon.hasAttribute('data-original-src')) {
        logoutIcon.src = logoutIcon.getAttribute('data-original-src');
      }
    });
  });
});
