
document.addEventListener("DOMContentLoaded", function() {
    const gender2 = document.getElementById('id_gender_1');
    let gender = document.querySelector("#id_gender");
    let pregnantField = document.querySelector("#id_pregnant").closest(".form-row");
 
    pregnantField.style.display = (gender2.checked) ? "block" : "none";

    gender.addEventListener("change", function() {
        if (gender2.checked) {
            pregnantField.style.display = "block";
        } else {
            pregnantField.style.display = "none";
        }
    });
});