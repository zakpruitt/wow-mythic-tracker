var questions = 1;

document.getElementById("create-a").classList.add("active");
feather.replace();


function AppendQuestion() {
  questions += 1;
  $("#questions").append(
    `<div class="accordion-item">
        <h2 class="accordion-header" id="heading${questions}">
            <button class="accordion-button" type="button" data-bs-toggle="collapse"
                data-bs-target="#collapse${questions}" aria-expanded="true" aria-controls="collapse${questions}">
                Question #${questions}
            </button>
        </h2>
        <div id="collapse${questions}" class="accordion-collapse collapse show" aria-labelledby="heading${questions}"
            data-bs-parent="#questions">
            <div class="accordion-body">
            <!--QUESTION TITLE AND TYPE-->
            <div class="row">
                <!--QUESTION TITLE-->
                <div class="col-lg-9">
                    <div class="form-floating">
                        <textarea class="form-control question-input" name="title${questions}"
                            id="title${questions}" required></textarea>
                        <label for="title${questions}">Question Title</label>
                    </div>
                </div>
                <!--QUESTION TYPE-->
                <div class="col-lg-3">
                    <div class="form-floating">
                        <select onchange="ChangeQuestionType(this)" class="form-select type-input" id="inputGroupSelect${questions}">
                            <option selected value="1">
                                4 Question Multiple Choice
                            </option>
                            <option value="2">True/False</option>
                        </select>
                        <label for="inputGroupSelect${questions}">Question Type</label>
                    </div>
                </div>
            </div>

            <hr>

            <!--QUESTION ANSWERS-->
            <div id="question-body${questions}">
                <!--OPTION 1-->
                <div class="row align-items-center" id="questionsBody">
                    <div class="col-lg-6">
                        <div class="form-floating">
                            <input type="text" class="form-control" id="q${questions}option1" name="q${questions}option1" required>
                            <label for="q${questions}option1">Option 1</label>
                        </div>
                    </div>

                    <div class="col-lg-2">
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" onchange=RadioCheckmarks(this) name="q${questions}correct1" id="q${questions}correct1">
                            <label class="form-check-label checkbox-text" for="q${questions}correct1">
                              Correct Answer
                            </label>
                        </div>
                    </div>
                </div>

                <!--OPTION 2-->
                <div class="row align-items-center options-input" id="questionsBody">
                    <div class="col-lg-6">
                        <div class="form-floating">
                            <input type="text" class="form-control" id="q${questions}option2" name="q${questions}option2" required>
                            <label for="q${questions}option2">Option 2</label>
                        </div>
                    </div>

                    <div class="col-lg-2">
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" onchange=RadioCheckmarks(this) name="q${questions}correct2" id="q${questions}correct2">
                            <label class="form-check-label checkbox-text" for="q${questions}correct2">
                              Correct Answer
                            </label>
                        </div>
                    </div>
                </div>

                <!--OPTION 3-->
                <div class="row align-items-center options-input" id="questionsBody">
                    <div class="col-lg-6">
                        <div class="form-floating">
                            <input type="text" class="form-control" id="q${questions}option3" name="q${questions}option3" required>
                            <label for="q${questions}option3">Option 3</label>
                        </div>
                    </div>

                    <div class="col-lg-2">
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" onchange=RadioCheckmarks(this) name="q${questions}correct3" id="q${questions}correct3">
                            <label class="form-check-label checkbox-text" for="q${questions}correct3">
                              Correct Answer
                            </label>
                        </div>
                    </div>
                </div>

                <!--OPTION 4-->
                <div class="row align-items-center options-input" id="questionsBody">
                    <div class="col-lg-6">
                        <div class="form-floating">
                            <input type="text" class="form-control" id="q${questions}option4" name="q${questions}option4" required>
                            <label for="q${questions}option4">Option 4</label>
                        </div>
                    </div>

                    <div class="col-lg-2">
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" onchange=RadioCheckmarks(this) name="q${questions}correct4" id="q${questions}correct4">
                            <label class="form-check-label checkbox-text" for="q${questions}correct4">
                              Correct Answer
                            </label>
                        </div>
                    </div>
                </div>
            </div>
            </div>
        </div>
    </div>`
  );
}

function ChangeQuestionType(element) {
  var selected = $("option:selected", element).text().trim();
  var questionNumber = $(element).attr("id").match(/\d+/);

  switch (selected) {
    case "4 Question Multiple Choice":
      $(`#question-body${questionNumber}`).replaceWith(
        `<!--QUESTION ANSWERS-->
        <div id="question-body${questionNumber}">
            <!--OPTION 1-->
            <div class="row align-items-center" id="questionsBody">
                <div class="col-lg-6">
                    <div class="form-floating">
                        <input type="text" class="form-control" id="q${questionNumber}option1" name="q${questionNumber}option1" required>
                        <label for="q${questionNumber}option1">Option 1</label>
                    </div>
                </div>

                <div class="col-lg-2">
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" onchange=RadioCheckmarks(this) name="q${questionNumber}correct1" id="q${questionNumber}correct1">
                        <label class="form-check-label checkbox-text" for="q${questionNumber}correct1">
                        Correct Answer
                        </label>
                    </div>
                </div>
            </div>

            <!--OPTION 2-->
            <div class="row align-items-center options-input" id="questionsBody">
                <div class="col-lg-6">
                    <div class="form-floating">
                        <input type="text" class="form-control" id="q${questionNumber}option2" name="q${questionNumber}option2" required>
                        <label for="q${questionNumber}option2">Option 2</label>
                    </div>
                </div>

                <div class="col-lg-2">
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" onchange=RadioCheckmarks(this) name="q${questionNumber}correct2" id="q${questionNumber}correct2">
                        <label class="form-check-label checkbox-text" for="q${questionNumber}correct2">
                        Correct Answer
                        </label>
                    </div>
                </div>
            </div>

            <!--OPTION 3-->
            <div class="row align-items-center options-input" id="questionsBody">
                <div class="col-lg-6">
                    <div class="form-floating">
                        <input type="text" class="form-control" id="q${questionNumber}option3" name="q${questionNumber}option3" required>
                        <label for="q${questionNumber}option3">Option 3</label>
                    </div>
                </div>

                <div class="col-lg-2">
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" onchange=RadioCheckmarks(this) name="q${questionNumber}correct3" id="q${questionNumber}correct3">
                        <label class="form-check-label checkbox-text" for="q${questionNumber}correct3">
                        Correct Answer
                        </label>
                    </div>
                </div>
            </div>

            <!--OPTION 4-->
            <div class="row align-items-center options-input" id="questionsBody">
                <div class="col-lg-6">
                    <div class="form-floating">
                        <input type="text" class="form-control" id="q${questionNumber}option4" name="q${questionNumber}option4" required>
                        <label for="q${questionNumber}option4">Option 4</label>
                    </div>
                </div>

                <div class="col-lg-2">
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" onchange=RadioCheckmarks(this) name="q${questionNumber}correct4" id="q${questionNumber}correct4">
                        <label class="form-check-label checkbox-text" for="q${questionNumber}correct4">
                        Correct Answer
                        </label>
                    </div>
                </div>
            </div>
        </div>`
      );
      break;
    case "True/False":
      $(`#question-body${questionNumber}`).replaceWith(
        `<!--QUESTION ANSWERS-->
            <div id="question-body${questionNumber}">
                <!--OPTION 1-->
                <div class="row align-items-center" id="questionsBody">
                    <div class="col-lg-6">
                        <div class="form-floating">
                            <input type="text" class="form-control" id="q${questionNumber}option1" name="q${questionNumber}option1" readonly="readonly">
                            <label for="q${questionNumber}option1">Option 1</label>
                        </div>
                    </div>
    
                    <div class="col-lg-2">
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" onchange=RadioCheckmarks(this) name="q${questionNumber}correct1" id="q${questionNumber}correct1">
                            <label class="form-check-label checkbox-text" for="q${questionNumber}correct1">
                            Correct Answer
                            </label>
                        </div>
                    </div>
                </div>
    
                <!--OPTION 2-->
                <div class="row align-items-center options-input" id="questionsBody">
                    <div class="col-lg-6">
                        <div class="form-floating">
                            <input type="text" class="form-control" id="q${questionNumber}option2" name="q${questionNumber}option2" readonly="readonly">
                            <label for="q${questionNumber}option2">Option 2</label>
                        </div>
                    </div>
    
                    <div class="col-lg-2">
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" onchange=RadioCheckmarks(this) name="q${questionNumber}correct2" id="q${questionNumber}correct2">
                            <label class="form-check-label checkbox-text" for="q${questionNumber}correct2">
                            Correct Answer
                            </label>
                        </div>
                    </div>
                </div>
            </div>`
      );
      $(`#q${questionNumber}option1`).val("True");
      $(`#q${questionNumber}option2`).val("False");
      break;
  }
}

function RadioCheckmarks(element) {
  var id = $(element).attr("id");
  var questionNumber = id.substring(0, id.indexOf("c")).match(/\d+/);
  var checkNumber = id.substring(id.indexOf('t')).match(/\d+/)

  if ($(element).is(":checked")) {
    for (var i = 1; i < 5; i++) {
        if (i != checkNumber) {
            $(`#q${questionNumber}correct${i}`).prop("checked", false);
        }
    }
  }
}

function ChangeAssignmentTitle() {
    var newTitle = $("#assignmentTitle").val();
    $("#titleDisplay").text(newTitle);
    $("#assignment-title").val(newTitle);
}

function Display() {
    alert($('#create').serialize());
}
