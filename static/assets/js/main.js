
let patientForm = document.getElementById("patient_form");

document.addEventListener("DOMContentLoaded", function () {
    if (patientForm) {
        const genderF = document.getElementById('id_gender_1');
        let gender = document.querySelector("#id_gender");
        let pregnantField = document.querySelector(".field-pregnant");

        pregnantField.style.display = (genderF.checked) ? "block" : "none";

        gender.addEventListener("change", function () {
            if (genderF.checked) {
                pregnantField.style.display = "block";
            } else {
                pregnantField.style.display = "none";
            }
        });

        document.getElementById('id_date_of_birth').addEventListener('change', function () {
            const dob = new Date(this.value);
            const today = new Date();
            let age = today.getFullYear() - dob.getFullYear() - (today.getMonth() < dob.getMonth() || (today.getMonth() == dob.getMonth() && today.getDate() < dob.getDate()));
            document.getElementById('id_age').value = age;
        });
    }
});






// $('#myModal').on('shown.bs.modal', function () {
//     $('#myInput').trigger('focus')
// })
