function lingkaran() {
	document.getElementById('hasilJari').innerHTML = 3.14 * 2 * parseFloat(jari.value);

	document.getElementById('hasilLuas').innerHTML = 3.14 * parseFloat(Math.pow(luas.value, 2));
}

function convertDollarToRupiah() {
	let angka = document.getElementById('dollar').value;

	let hasil = angka * 14000;

	var number_string = hasil.toString(),
		sisa = number_string.length % 3,
		rupiah = number_string.substr(0, sisa),
		ribuan = number_string.substr(sisa).match(/\d{3}/g);

	if (ribuan) {
		separator = sisa ? '.' : '';
		rupiah += separator + ribuan.join('.');
	}

	document.getElementById('hasilConvert').innerHTML = " Rp " +rupiah;
}

function lamaParkir() {
	let masuk = document.getElementById('masuk').value;
	let keluar = document.getElementById('keluar').value;

	let lamaParkir = keluar - masuk;

	let bayar

	if (lamaParkir < 3) {
		bayar = 3000
	} else {
		bayar = (lamaParkir * 2000) - 3000
	}

	document.getElementById('hasilLamaParkir').innerHTML = lamaParkir + " Jam";
	document.getElementById('hasilBiayaParkir').innerHTML = bayar;
}

function hasilDuaBilangan() {
	document.getElementById('hasilDuaBilangan').innerHTML = parseInt(bilangan1.value) + parseInt(bilangan2.value);
}