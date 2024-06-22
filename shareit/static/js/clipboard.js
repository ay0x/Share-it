function copyToClipboard (elementId, button) {
  const urlText = document.getElementById(elementId).textContent;
  navigator.clipboard.writeText(urlText).then(() => {
    const originalText = button.textContent;
    button.textContent = 'Copied!';
    setTimeout(() => {
      button.textContent = originalText;
    }, 2000); // Revert after 2 seconds
  }).catch(err => {
    console.error('Failed to copy: ', err);
  });
}

document.getElementById('copy_download').addEventListener('click', function () {
  copyToClipboard('downloadUrl', this);
});

document.getElementById('copy_delete').addEventListener('click', function () {
  copyToClipboard('deleteUrl', this);
});
