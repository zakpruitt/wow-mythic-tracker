document.getElementById("classroom-a").classList.add("active");
feather.replace();

function FindStudent() {
  alert("clicked");
  var email = $("#studentEmail").val();
  $.getJSON(
    "http://127.0.0.1:5000/user/get_student",
    {
      studentEmail: email,
    },
    function (data) {
      UpdateDatabase(data.email)
      $("#table tr:last").after(`<tr>
            <td>${data.email}</td>
            <td>${data.name}</td>
            <td><input type="number" class="form-control coin-input" id="input1" value=${data.coins}></td>
            <td>
                <button class="feather-button delete-btn" type="button">
                    <span class="feather-20" data-feather="trash"></span>
                </button>
            </td>
        </tr>`);
      feather.replace();
    }
  );
}

function UpdateDatabase(studentEmail) {
  email = studentEmail.toString();
  $.ajax({
    url: "http://127.0.0.1:5000/user/classroom",
    type: 'PUT',
    data: { email: email },
    success: function(response) {
      console.log("nice");
    }
 });
}
