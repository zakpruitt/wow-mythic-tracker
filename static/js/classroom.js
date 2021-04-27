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
      UpdateDatabase(data.email, "add");
      $("#table tr:last").after(`<tr>
            <td>${data.email}</td>
            <td>${data.name}</td>
            <td><input type="number" onchange="ChangeCoinValue(this)" onKeyDown="return false" class="form-control coin-input" id="input1" value=${data.coins}></td>
            <td>
                <button class="feather-button delete-btn" type="button">
                    <span class="feather-20" data-feather="trash"></span>
                </button>
            </td>
        </tr>`);
      feather.replace();
    }
  ).fail(function () {
    console.log("error");
  });
}

function UpdateDatabase(studentEmail, type) {
  email = studentEmail.toString();
  $.ajax({
    url: "http://127.0.0.1:5000/user/classroom",
    type: "PUT",
    data: { email: email, type: type },
    success: function (response) {
      console.log(response);
    },
  });
}

function ChangeCoinValue(element) {
  var currentRow = $(element).closest("tr");
  var email = currentRow.children().closest("td").html();
  UpdateDatabase(email, "tokenUpdate");
}
