document.getElementById('upload-form').addEventListener('submit', function (event) {
  event.preventDefault();
  const formData = new FormData(this);
  const xhr = new XMLHttpRequest();
  const startTime = Date.now();
  xhr.open('POST', '{% url "upload_file" %}', true);
  xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
  xhr.upload.addEventListener('progress', function (event) {
    if (event.lengthComputable) {
      const percentComplete = (event.loaded / event.total) * 100;
      const progressBar = document.getElementById('progress_bar');
      progressBar.style.width = percentComplete + '%';
      progressBar.setAttribute('aria-valuenow', percentComplete);
      // Update upload information
      const elapsedTime = (Date.now() - startTime) / 1000; // elapsed time in seconds
      const uploadSpeed = event.loaded / elapsedTime; // upload speed in bytes per second
      let speedUnit;
      let displaySpeed;
      if (uploadSpeed < 1024) {
        displaySpeed = uploadSpeed.toFixed(2);
        speedUnit = 'B/s';
      } else if (uploadSpeed < 1024 * 1024) {
        displaySpeed = (uploadSpeed / 1024).toFixed(2);
        speedUnit = 'KB/s';
      } else if (uploadSpeed < 1024 * 1024 * 1024) {
        displaySpeed = (uploadSpeed / (1024 * 1024)).toFixed(2);
        speedUnit = 'MB/s';
      } else {
        displaySpeed = (uploadSpeed / (1024 * 1024 * 1024)).toFixed(2);
        speedUnit = 'GB/s';
      }
      const uploadedSize = event.loaded;
      const totalSize = event.total;
      let displaySize;
      let displayTotalSize;
      let sizeUnit;
      if (uploadedSize < 1024) {
        displaySize = uploadedSize.toFixed(2);
        sizeUnit = 'B';
      } else if (uploadedSize < 1024 * 1024) {
        displaySize = (uploadedSize / 1024).toFixed(2);
        sizeUnit = 'KB';
      } else if (uploadedSize < 1024 * 1024 * 1024) {
        displaySize = (uploadedSize / (1024 * 1024)).toFixed(2);
        sizeUnit = 'MB';
      } else {
        displaySize = (uploadedSize / (1024 * 1024 * 1024)).toFixed(2);
        sizeUnit = 'GB';
      }
      if (totalSize < 1024) {
        displayTotalSize = totalSize.toFixed(2);
        TotalsizeUnit = 'B';
      } else if (totalSize < 1024 * 1024) {
        displayTotalSize = (totalSize / 1024).toFixed(2);
        TotalsizeUnit = 'KB';
      } else if (totalSize < 1024 * 1024 * 1024) {
        displayTotalSize = (totalSize / (1024 * 1024)).toFixed(2);
        TotalsizeUnit = 'MB';
      } else {
        displayTotalSize = (totalSize / (1024 * 1024 * 1024)).toFixed(2);
        TotalsizeUnit = 'GB';
      }
      document.getElementById('upload-info').innerHTML = `
                  
    <div class="row">
      <div class="col-8">
        <p class="text-start mt-1 mb-0 progress-text">
          <b>Remaining Time:</b> 00:00:00 at ${displaySpeed} ${speedUnit} ( 
          <b>Elapsed:</b>  ${elapsedTime.toFixed(2)} seconds)
                          
        </p>
      </div>
      <div class="col-4 ">
        <p class="text-end mt-1 mb-0 progress-text">
          <b>Uploaded</b> ${displaySize} ${sizeUnit} of ${displayTotalSize} ${sizeUnit}
                          
        </p>
      </div>
    </div>
        `;
    }
  });

  xhr.addEventListener('load', function (event) {
    const uploadStatus = document.getElementById('upload-status');
    if (xhr.status === 200) {
      uploadStatus.innerHTML = ' < div class = "alert alert-success" > File uploaded successfully! < /div>';
    } else {
      uploadStatus.innerHTML = ' < div class = "alert alert-danger" > File upload failed. < /div>';
    }
  });
  xhr.send(formData);


});
