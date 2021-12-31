let question_number = 0;
let user_score = 0;
let user_answer = "";
const feedback_true = "The answer is correct !"
const feedback_false = "The answer is wrong !"

function start() {
    //Disable the START button
    document.getElementById("start").disabled = true;

    //!!!!!Pour freeze tous les boutons sur les thèmes mais ça marche pas
    var subjects_buttons = document.getElementsByClassName("subject-buttons");
    for (var i = 0; i < subjects_buttons.length; i++) {
        subjects_buttons[i].disabled = true;
    }

    AddQuestion();
}


//We display a question with 4 answers
async function AddQuestion() {

    const questionObject = await fetch("http://127.0.0.1:5000/newquestion").then((res) => {
        return res.json();
    })

    //Disable Continue and End buttons if there are there
    continue_button_id = "next" + question_number;
    let continue_button = document.getElementById(continue_button_id);
    if (continue_button != null) {
        continue_button.disabled = true;
        end_button_id = "end" + question_number;
        document.getElementById(end_button_id).disabled = true;
    }

    //Create a new question
    question_number += 1;
    const question = questionObject[0]["question"];
    const right_answer = questionObject[0]["right_answer"];
    const false_answer1 = questionObject[0]["wrong_answers"][0];
    const false_answer2 = questionObject[0]["wrong_answers"][1];
    const false_answer3 = questionObject[0]["wrong_answers"][2];

    //Create a list with the buttons and shuffle it in order to display them in a random order (to not have the right answer at the same place all the time)
    const button1 = "<button class='answer-buttons' id='right_answer'>" + right_answer + "</button><br>";
    const button2 = "<button class='answer-buttons' id='false_answer1'>" + false_answer1 + "</button><br>";
    const button3 = "<button class='answer-buttons' id='false_answer2'>" + false_answer2 + "</button><br>";
    const button4 = "<button class='answer-buttons' id='false_answer3'>" + false_answer3 + "</button><br>";

    let buttons = [button1, button2, button3, button4];
    shuffleArray(buttons);

    //Display the question in a div
    let div = document.createElement("div");
    let class_name = 'answers' + question_number;
    div.className = class_name
    div.innerHTML = "<h3>QUESTION " + question_number + "</h3><p>" + question + "</p>"
        + buttons[0]
        + buttons[1]
        + buttons[2]
        + buttons[3]
        + "<br><button class='submit' id='submit" + question_number + "' onclick='AnswerQuestion()'>Submit</button>";
    document.getElementById("main").appendChild(div);

    //Add an event listener to the buttons to know which one was clicked
    //only to the buttons of the actual question
    let btns_div = document.getElementsByClassName(class_name)[0];
    let btns = btns_div.getElementsByClassName("answer-buttons");
    for (var i = 0; i < btns.length; i++) {
        btns[i].addEventListener("click", (e) => {
            user_answer = e.target.id;
        });
    }

    window.scrollTo(0, document.body.scrollHeight);
}


function AnswerQuestion() {
    //if the user answered a question
    if (user_answer != "") {

        //Disable previous buttons
        submit_button = "submit" + question_number;
        document.getElementById(submit_button).disabled = true;

        //Get the answer of the user and change button color
        let class_name = 'answers' + question_number;
        let btns_div = document.getElementsByClassName(class_name)[0];
        let btns = btns_div.getElementsByClassName("answer-buttons");
        let feedback = "";
        for (var i = 0; i < btns.length; i++) {
            //Desactivate button
            btns[i].disabled = true;
            if (btns[i].id == "right_answer") {
                btns[i].style.backgroundColor = 'green';
                if (btns[i].id == user_answer) {
                    feedback = feedback_true;
                    user_score += 1
                }
            } else {
                if (btns[i].id == user_answer) {
                    btns[i].style.backgroundColor = 'red';
                    feedback = feedback_false;
                }
            }
        }

        //Display a feedback and Next/End buttons
        let div = document.createElement("div");
        var messagetodisplay = "<p>" + feedback
            + "</p><button class='submit' id='next" + question_number + "' onclick='AddQuestion()'>Next</button>"
            + "<button class='submit' id='end" + question_number + "' style='background-color:red; margin-left:5px;' onclick='End()'>End</button>";
        div.innerHTML = messagetodisplay;
        document.getElementById("main").appendChild(div);

        user_answer = "";
    }
    window.scrollTo(0, document.body.scrollHeight);
}

function End() {
    //Disable Next button
    continue_button_id = "next" + question_number;
    document.getElementById(continue_button_id).disabled = true;
    end_button_id = "end" + question_number;
    document.getElementById(end_button_id).disabled = true;

    //Display a final message with the player's score
    let div = document.createElement("div");
    div.innerHTML = "<p>Thank you for playing ! Your final score is " + user_score + "/" + question_number + ".</p>";
    document.getElementById("main").appendChild(div);
    window.scrollTo(0, document.body.scrollHeight);

}


function shuffleArray(array) {
    return array.sort(() => Math.random() - 0.5);

}