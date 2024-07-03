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
const emailInput = document.querySelector('#email');
const passwordInput = document.querySelector('#password');
const confirm_passwordInput = document.querySelector('#confirm-password');
const loginButton = document.querySelector('#loginButton');

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function validateInputs() {
    const full_nameValid = full_nameInput.value.trim().length >= 5;
    const emailValid = validateEmail(emailInput.value.trim());
    const passwordValid = passwordInput.value.trim().length >= 8;
    const passwordsMatch = passwordInput.value.trim() === confirm_passwordInput.value.trim();

    if (full_nameValid && emailValid && passwordValid && passwordsMatch) {
        loginButton.disabled = false;
        loginButton.classList.add('enabled');
    } else {
        loginButton.disabled = true;
        loginButton.classList.remove('enabled');
    }
}

full_nameInput.addEventListener('input', validateInputs);
emailInput.addEventListener('input', validateInputs);
passwordInput.addEventListener('input', validateInputs);
confirm_passwordInput.addEventListener('input', validateInputs);
