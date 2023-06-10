const form = document.querySelector('.my-form');

// Listen for the form submission event
form.addEventListener('submit', function(event) {
  event.preventDefault();

  // Get the form data
  const formData = new FormData(form);

  // Send a POST request to the server with the form data
  fetch(form.action, {
    method: 'POST',
    body: formData
  })
  .then(response => {
    if (response.ok || response.status === 400) {
      // If the response is successful or there was an error but the email was sent successfully, show the success modal
      $('#success-modal').modal('show');
      form.reset();
    } else {
      // If the response is not successful, show the error modal
      $('#error-modal').modal('show');
    }
  })
  .catch(error => {
    // If there is an error, show the error modal
    $('#error-modal').modal('show');
  });
});