document.getElementById("classroom-a").classList.add("active");
feather.replace();

function FindStudent() {
  alert("clicked");
  var email = $("#studentEmail").val();
  $.getJSON(
    "http://127.0.0.1:5000/user/get",
    {
      studentEmail: email,
    },
    function (data) {
      $("#table tr:last").after(`<tr>
            <td>${data.email}</td>
            <td>${data.name}</td>
            <td><input type="number" class="form-control coin-input" id="input1" value=${data.coins}></td>
            <td>
                <button class="feather-button edit-btn" type="button">
                    <span class="feather-20" data-feather="edit-2"></span>
                </button>
                <button class="feather-button delete-btn" type="button">
                    <span class="feather-20" data-feather="trash"></span>
                </button>
            </td>
        </tr>`);
      feather.replace();
    }
  );
}
