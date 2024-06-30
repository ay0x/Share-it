document.querySelector('.password-toggle').addEventListener('click', function () {
  const passwordField = document.querySelector('#password');
  const eyeIcon = document.querySelector('#eye');
  const reveal = eyeIcon.getAttribute('class') === 'bi bi-eye' ? 'bi bi-eye-slash' : 'bi bi-eye';
  eyeIcon.setAttribute('class', reveal);
  const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
  passwordField.setAttribute('type', type);
});

const emailInput = document.querySelector('#email');
const passwordInput = document.querySelector('#password');
const loginButton = document.querySelector('#loginButton');

function validateEmail(email) {
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return re.test(email);
}

function validateInputs() {
  const emailValid = validateEmail(emailInput.value.trim());
  const passwordValid = passwordInput.value.trim().length >= 8;

  if (emailValid && passwordValid) {
      loginButton.disabled = false;
      loginButton.classList.add('enabled');
  } else {
      loginButton.disabled = true;
      loginButton.classList.remove('enabled');
  }
}

emailInput.addEventListener('input', validateInputs);
passwordInput.addEventListener('input', validateInputs);