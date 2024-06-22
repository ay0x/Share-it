// Development JS
const dropbox = document.getElementById('dropbox');

function preventDefaults (e) {
  e.preventDefault();
  e.stopPropagation();
}

function highlight () {
  dropbox.classList.add('dragover');
}

function unhighlight () {
  dropbox.classList.remove('dragover');
}

function handleDrop (e) {
  const dt = e.dataTransfer;
  const files = dt.files;

  handleFiles(files);
}

function handleFiles (files) {
  const header = document.getElementById('headerInfo');
  const table = document.getElementById('fileTable');
  const fileUpload = document.getElementById('dropbox');
  const tableBody = document.querySelector('.table tbody');

  tableBody.innerHTML = ''; // Clear the existing rows

  if (files.length > 0) {
    header.style.display = 'none';
    fileUpload.style.display = 'none';
    table.style.display = 'table';
  } else {
    table.style.display = 'none';
  }

  for (let i = 0; i < files.length; i++) {
    const file = files[i];
    const row = document.createElement('tr');

    const fileNameCell = document.createElement('td');
    fileNameCell.textContent = file.name;
    row.appendChild(fileNameCell);

    const fileSizeCell = document.createElement('td');
    if (file.size < 1024000) {
      fileSizeCell.textContent = (file.size / 1024).toFixed(2) + ' KB';
    } else if (file.size < 1024000000) {
      fileSizeCell.textContent = (file.size / (1024 * 1024)).toFixed(2) + ' MB';
    } else {
      fileSizeCell.textContent = (file.size / (1024 * 1024 * 1024)).toFixed(2) + ' GB';
    }
    row.appendChild(fileSizeCell);
    const actionCell = document.createElement('td');
    const deleteButton = document.createElement('button');
    deleteButton.textContent = 'Delete';
    deleteButton.classList.add('btn', 'btn-danger', 'btn-sm');
    deleteButton.onclick = function () {
      row.remove();
      if (tableBody.children.length === 0) {
        table.style.display = 'none';
        fileUpload.style.display = 'table';
        header.style.display = 'table';
      }
    };
    actionCell.appendChild(deleteButton);
    row.appendChild(actionCell);

    tableBody.appendChild(row);
  }
}

dropbox.addEventListener('dragenter', preventDefaults, false);
dropbox.addEventListener('dragover', preventDefaults, false);
dropbox.addEventListener('dragleave', preventDefaults, false);
dropbox.addEventListener('drop', preventDefaults, false);
dropbox.addEventListener('dragenter', highlight, false);
dropbox.addEventListener('dragover', highlight, false);
dropbox.addEventListener('dragleave', unhighlight, false);
dropbox.addEventListener('drop', unhighlight, false);
dropbox.addEventListener('drop', handleDrop, false);

document.getElementById('customFileInput').addEventListener('change', function () {
  handleFiles(this.files);
});
