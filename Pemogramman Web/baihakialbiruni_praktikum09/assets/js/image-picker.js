const selectGambar = document.getElementById("selectGambar")
const gambar = document.getElementById("gambar");

function changeImage() {
    gambar.src = `./assets/img/${selectGambar.options[selectGambar.selectedIndex].value}.jpg`
    alert(gambar.src)
}
