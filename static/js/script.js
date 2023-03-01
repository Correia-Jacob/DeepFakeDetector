// Wait for the page to load
window.addEventListener("load", function() {
    // Get the form and add an event listener for when it is submitted
    const form = document.querySelector("#upload-form");
    form.addEventListener("submit", function(event) {
      // Prevent the default form submission behavior
      event.preventDefault();
      // Get the file input and the preview image
      const fileInput = document.querySelector("#file-input");
      const previewImage = document.querySelector("#preview-image");
      // Check if a file was selected
      if (fileInput.files.length === 0) {
        alert("Please select a file to upload.");
        return;
      }
      // Create a FormData object and append the file to it
      const formData = new FormData();
      formData.append("file", fileInput.files[0]);
      // Send a POST request to the server with the form data
      fetch("/predict", {
        method: "POST",
        body: formData
      })
      .then(response => response.json())
      .then(data => {
        // Update the preview image with the result image
        previewImage.src = "data:image/png;base64," + data.result;
      })
      .catch(error => {
        console.error(error);
        alert("An error occurred while processing the image.");
      });
    });
  });
  