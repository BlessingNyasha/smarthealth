function showModal() {
  var modal = document.getElementById("myModal");
  modal.style.display = "block";
}

function hideModal() {
  var modal = document.getElementById("myModal");
  modal.style.display = "none";
}

var contactForm = document.getElementById("contact-form");
contactForm.addEventListener("submit", function(event) {
  event.preventDefault();
  var xhr = new XMLHttpRequest();
  xhr.open(contactForm.method, contactForm.action, true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onload = function() {
    if (xhr.status === 200) {
      var response = JSON.parse(xhr.responseText);
      if (response.success) {
        showModal();
      } else {
        alert("There was an error sending your message.");
      }
    }
  };
  xhr.send(JSON.stringify({
    'name': contactForm.elements.namedItem("name").value,
    'email': contactForm.elements.namedItem("email").value,
    'message': contactForm.elements.namedItem("message").value
  }));
});

var modalClose = document.getElementsByClassName("close")[0];
modalClose.addEventListener("click", function() {
  hideModal();
});