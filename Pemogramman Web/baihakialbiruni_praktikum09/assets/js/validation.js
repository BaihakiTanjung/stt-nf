function validateFormOnSubmit(form) {
  console.log(form);
  reason = "";
  reason += validateNamaPelanggan(form.namaPelanggan);
  reason += validateEmail(form.email);
  reason += validateJamKeberangkatan(form.jamKeberangkatan);
  reason += validateTujuanKeberangkatan(form.tujuanKeberangkatan);
  reason += validateJumlahTicket(form.jumlahTicket);

  console.log(reason);
  if (reason.length > 0) {
    return false;
  } else {
    return false;
  }
}

function clearValidation(target, targetError) {
  const targetId = document.getElementById(target);
  const targetErrorId = document.getElementById(targetError);

  targetId.classList.remove("border-red-500");
  targetErrorId.innerText = "";
}

function addValidation(target, targetError, MessageError) {
  const targetId = document.getElementById(target);
  const targetErrorId = document.getElementById(targetError);

  targetId.classList.add("border-red-500");
  targetErrorId.innerText = MessageError;
}

function validateNamaPelanggan(params) {
  // max character is max 30
  let maxChar30 = /^[a-zA-Z.0-9]{0,30}$/;
  let error = "";

  if (params.value == "") {
    addValidation(
      "namaPelanggan",
      "namaPelangganError",
      "Please enter an nama panggilan."
    );
    error = "1";
  } else if (params.value.match(maxChar30)) {
    console.log("test");
    addValidation(
      "namaPelanggan",
      "namaPelangganError",
      "Please enter a max 30 characters."
    );
    error = "2";
  } else {
    clearValidation("namaPelanggan", "namaPelangganError");
  }

  return error;
}

function validateEmail(params) {
  let error = "";
  let temail = trim(params.value); // value of field with whitespace trimmed off
  let emailFilter = /^[^@]+@[^@.]+\.[^@]*\w\w$/;
  let illegalChars = /[\(\)\<\>\,\;\:\\\"\[\]]/;

  if (params.value == "") {
    addValidation("email", "emailError", "Please enter an email address.");
    error = "2";
  } else if (!emailFilter.test(temail)) {
    //test email for illegal characters
    addValidation("email", "emailError", "Please enter a valid email address.");
    error = "3";
  } else if (params.value.match(illegalChars)) {
    addValidation("email", "emailError", "Email contains invalid characters.");
    error = "4";
  } else {
    clearValidation("email", "emailError");
  }
  return error;
}

function validateJamKeberangkatan(params) {
  console.log(params.value);

  let error = "";

  if (params.value == "") {
    addValidation(
      "jamKeberangkatan",
      "jamKeberangkatanError",
      "Please enter an jam keberangkatan."
    );
    error = "1";
  } else {
    clearValidation("jamKeberangkatan", "jamKeberangkatanError");
  }
  return error;
}

function validateTujuanKeberangkatan(params) {
  console.log(params.value);
  let error = "";

  if (params.value == "") {
    addValidation(
      "tujuanKeberangkatan",
      "tujuanKeberangkatanError",
      "Please enter an tujuan keberangkatan."
    );
    error = "1";
  } else {
    clearValidation("tujuanKeberangkatan", "tujuanKeberangkatanError");
  }
  return error;
}

function validateJumlahTicket(params) {
  console.log(params.value);

  let error = "";

  let integers1between10 = /^([1-9]|10)$/;

  if (params.value == "") {
    addValidation(
      "jumlahTicket",
      "jumlahTicketError",
      "Please enter an jumlah ticket."
    );
    error = "1";
  } else if (!params.value.match(integers1between10)) {
    addValidation(
      "jumlahTicket",
      "jumlahTicketError",
      "Please enter between 1 - 10."
    );
    error = "2";
  } else {
    clearValidation("jumlahTicket", "jumlahTicketError");
  }
  return error;
}

// validate email as required field and format
function trim(s) {
  return s.replace(/^\s+|\s+$/, "");
}
