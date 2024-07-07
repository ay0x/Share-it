const allFileSelections = [];

const dropbox = document.getElementById('dropbox');

function showFileLimitModal () {
  const warningModal = new bootstrap.Modal(document.getElementById('FileLimitModal'), {
    keyboard: true
  });
  warningModal.show();
}

function showFileSelectedModal () {
  const SameFileModal = new bootstrap.Modal(document.getElementById('SameFileModal'), {
    keyboard: true
  });
  SameFileModal.show();
}

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
  for (let i = 0; i < files.length; i++) {
    if (files[i].size > 300000000) {
      showFileLimitModal();
      continue;
    }
    if (isFileAlreadySelected(files[i])) {
      showFileSelectedModal();
      continue;
    }
    allFileSelections.push(files[i]);
  }
  appendFileSelectionsToTable();
}

function isFileAlreadySelected (file) {
  return allFileSelections.some(selectedFile => selectedFile.name === file.name && selectedFile.size === file.size);
}

function appendFileSelectionsToTable () {
  const fileTableBody = $('#fileTable tbody');

  fileTableBody.empty();

  if (allFileSelections.length > 0) {
    $('#headerInfo').hide();
    $('#dropbox').hide();
    $('#fileTable').show();
  } else {
    $('#fileTable').hide();
    $('#headerInfo').show();
    $('#dropbox').show();
  }

  allFileSelections.forEach(function (file, index) {
    let fileSize;
    if (file.size < 999) {
      fileSize = (file.size).toFixed(2) + ' Bytes';
    } else if (file.size < 1024000) {
      fileSize = (file.size / 1024).toFixed(2) + ' KB';
    } else if (file.size < 1024000000) {
      fileSize = (file.size / (1024 * 1024)).toFixed(2) + ' MB';
    } else {
      fileSize = (file.size / (1024 * 1024 * 1024)).toFixed(2) + ' GB';
    }

    const row = `<tr>
            <td>${file.name}</td>
            <td>${fileSize}</td>
            <td><i class="bi bi-trash3-fill text-danger" onclick="deleteFile(${index})"></i></td>
        </tr>`;

    fileTableBody.append(row);
  });

  if (fileTableBody.children().length === 0) {
    $('#fileTable').hide();
    $('#dropbox').show();
    $('#headerInfo').show();
  }
}

function deleteFile (index) {
  allFileSelections.splice(index, 1);
  appendFileSelectionsToTable();
  // console.log(allFileSelections);
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

document.addEventListener("DOMContentLoaded", function() {
	const goHomeButton = document.getElementById("goHome");

	goHomeButton.addEventListener("click", function() {
		window.location.href = '/';
	});
});