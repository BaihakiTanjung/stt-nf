const nilai = document.getElementById('nilai');
const hasil = document.getElementById('hasil');
const mataUang = document.getElementById('mataUang');

function convertMataUang() {
    let rupiah = 0

    switch (mataUang.options[mataUang.selectedIndex].value) {
        
        case "Dollar US":
            rupiah = 9915
            break;
        case "Dollar Singapore":
            rupiah = 13472
            break;
        case "Ringgit Malaysia":
            rupiah = 874
            break;
        case "Yen Jepan":
            rupiah = 120
            break;
        case "Euro":
            rupiah = 15888
            break;
        case "Riyal Arab Saudi":
            ruapiah = 3592
            break;
    
        default:
            break;
    }

    hasil.value = rupiah * parseInt(nilai.value);
}