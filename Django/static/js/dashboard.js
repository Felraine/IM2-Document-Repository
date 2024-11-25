document.addEventListener('DOMContentLoaded', function() {
  
  var calendarEl = document.getElementById('calendar');
  var calendar = new FullCalendar.Calendar(calendarEl, {
      initialView: 'dayGridMonth',
      timeZone: 'Asia/Manila',
      fixedWeekCount: false,
      showNonCurrentDates: true,
      events: '/dashboard/get_events/',
      eventDisplay: 'block',
      eventTimeFormat: { 
          hour: 'numeric',
          minute: '2-digit',
          meridiem: 'short'
      },
      eventDidMount: function (info) {
          // Set background color and border color for events
          info.el.style.backgroundColor = "#FED534";
          info.el.style.borderColor = "#FED534";
          info.el.style.fontSize = "6px";

          // Select the event time and title
          const titleEl = info.el.querySelector('.fc-event-title');
          const timeEl = info.el.querySelector('.fc-event-time');

          // Modify title and time display
          if (titleEl && timeEl) {
              // Force the time to go on a new line
              timeEl.style.display = 'block';         // Ensure time is on a new line
              timeEl.style.marginTop = '5px';         // Add space between time and title
              titleEl.style.whiteSpace = 'normal';    // Allow title text to wrap
              titleEl.style.wordWrap = 'break-word';  // Break long words
          }
      },
      windowResize: function(view) {
          calendar.render();
      },
      datesRender: function(info) {
          // Select the calendar's month view element
          var gridEl = info.view.el.querySelector('.fc-dayGridMonth-view');
          
          // Get all the rows in the month view
          var rows = gridEl.querySelectorAll('.fc-dayGridWeek');
          
          // Ensure only 5 rows are visible
          if (rows.length > 5) {
              // Hide extra rows beyond the 5th one
              for (var i = 5; i < rows.length; i++) {
                  rows[i].style.display = 'none';
              }
          }
      }
  });
  calendar.render();
});




  let edit = false; // if edit btn pressed or nah
  let deleteForm = null; //modal form
  
  // confirm
  function confirmDel(form) {
      deleteForm = form;
      const modal = document.getElementById('deleteConfirmationModal');
      modal.style.display = 'block';
      document.getElementById('overlay').style.display = 'block';
      return false;
  }

  document.getElementById('confirmDeleteBtn').onclick = function() {
  if (deleteForm) {
      deleteForm.submit(); 
  }
  hideModal(); 
};

  function hideModal() {
  const modal = document.getElementById('deleteConfirmationModal');
  modal.style.display = 'none';
  document.getElementById('overlay').style.display = 'none';
  }

document.getElementById('cancelDeleteBtn').onclick = hideModal;
document.getElementById('overlay').onclick = hideModal;
  
//UPDATING FORMS SECTION

  // edit event form
function openEditForm(id, title, description, location, dateTime) {
    document.getElementById('edit_event_id').value = id;
    document.getElementById('title').value = title;
    document.getElementById('description').value = description;
    document.getElementById('location').value = location;
    document.getElementById('date_time').value = dateTime;

    // Change the form title and action URL
    document.getElementById('formTitle').innerText = "Edit Event";
    document.getElementById('eventForm').action = "{% url 'updateEvent' %}"; 

    edit = true;

    document.getElementById('eventFormContainer').style.display = "block";
   
}

function showToast(message, isSuccess = true) {
  const toast = document.getElementById("toast");
  toast.textContent = message; 
  toast.className = `toast show ${isSuccess ? '' : 'error'}`; 
  setTimeout(() => {
      toast.className = "toast"; 
  }, 3000);
}

const saveEventBtn = document.getElementById('saveEventBtn');
saveEventBtn.onclick = function(){
  if (edit && document.getElementById('date_time').value) {
        showToast("Event details changed successfully!");
    } else {
        showToast("Please fill out the entire form.",false);
    }

}

// Open add event form
const addEventBtn = document.getElementById('addEventBtn');
addEventBtn.onclick = function() {
    edit = false;
    document.getElementById('formTitle').innerText = "Add New Event";
    document.getElementById('eventForm').action = "{% url 'addEvents' %}";
    document.getElementById('eventForm').reset(); 
    document.getElementById('eventFormContainer').style.display = "block";
    document.getElementById('overlay').style.display = "block";

}

// Close form
function closeForm() {
    document.getElementById('eventFormContainer').style.display = "none";
    document.getElementById('overlay').style.display = "none";
    document.getElementById('overlay').onclick = hideModal;
  
}

document.getElementById('overlay').onclick = function() {
    closeForm();
}