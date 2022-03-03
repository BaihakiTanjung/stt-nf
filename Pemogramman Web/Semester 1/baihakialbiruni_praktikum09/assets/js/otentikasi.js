const username = document.getElementById('username');
const password = document.getElementById('password');

function login() {
    if (username.value == 'ahmad2017' && password.value == '    ') {
        // alert('Login Berhasil');
        window.location.href = 'home.html';
    } else {
        alert('Login Gagal');
    }
}