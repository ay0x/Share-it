document.querySelector('.password-toggle').addEventListener('click', function() {
    const passwordField = document.querySelector('#password');
    const eyeIcon = document.querySelector('#eye');
    const reveal = eyeIcon.getAttribute('class') === 'bi bi-eye' ? 'bi bi-eye-slash' : 'bi bi-eye';
    eyeIcon.setAttribute('class', reveal);
    const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordField.setAttribute('type', type);
});

document.querySelector('.password-toggle1').addEventListener('click', function() {
    const passwordField = document.querySelector('#confirm-password');
    const eyeIcon = document.querySelector('#eye1');
    const reveal = eyeIcon.getAttribute('class') === 'bi bi-eye' ? 'bi bi-eye-slash' : 'bi bi-eye';
    eyeIcon.setAttribute('class', reveal);
    const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordField.setAttribute('type', type);
});

const full_nameInput = document.querySelector('#fullname');
const passwordInput = document.querySelector('#password');
const confirm_passwordInput = document.querySelector('#confirm-password');
const updateButton = document.querySelector('#updateButton');

function validateInputs() {
    const full_nameValid = full_nameInput.value.trim().length >= 5;
    const passwordValid = passwordInput.value.trim().length >= 8;
    const passwordsMatch = passwordInput.value.trim() === confirm_passwordInput.value.trim();

    if (full_nameValid) {
        updateButton.disabled = false;
        updateButton.classList.add('enabled');
    } else {
        updateButton.disabled = true;
        updateButton.classList.remove('enabled');
    }

	if (passwordValid && passwordsMatch) {
        updateButton.disabled = false;
        updateButton.classList.add('enabled');
    } else {
        updateButton.disabled = true;
        updateButton.classList.remove('enabled');
    }


}

full_nameInput.addEventListener('input', validateInputs);
passwordInput.addEventListener('input', validateInputs);
confirm_passwordInput.addEventListener('input', validateInputs);

document.addEventListener('DOMContentLoaded', (event) => {
	const floatingMessage = document.getElementById('floatingMessage');
	if (floatingMessage) {
		setTimeout(() => {
			floatingMessage.classList.add('fade-out');
		}, 3000);
		setTimeout(() => {
			floatingMessage.remove();
		}, 3500);
	}
});
