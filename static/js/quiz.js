let question_number = 0;
let user_score = 0;
let user_answer = "";
let theme = "Cinema";
const feedback_true_en = "The answer is correct !";
const feedback_true_fr = "La réponse est bonne !";
const feedback_false_en = "The answer is wrong !";
const feedback_false_fr = "La réponse est fausse !";
let language = "English";


function start() {
  //Disable the START button
  document.getElementById("start").disabled = true;

  //Check the language
  let texte = document.getElementById("language").innerHTML;
  if (texte== "Quiz de culture générale"){
    language = "French";
  }

  console.log("language = ", language);

  // TODO : laisser en gras le bouton selectionné
  for (const elem of document.getElementsByClassName("subject-buttons")) {
    for (const button of elem.getElementsByTagName("button")) {
      button.disabled = true;
      if (button.innerText == theme) {
        button.className = "subject-buttons button:selected";
      }
    }
  }

  AddQuestion();
}

//We display a question with 4 answers
async function AddQuestion() {

  if (language == "French" && (theme == "History" || theme == "Politics")){
    let div = document.createElement("div");
    div.innerHTML =
      "<h3>Thème indisponible </h3><p>Les thèmes \"Histoire\" et \"Politique\" ne sont pas disponibles en français.</p>"
      +"<iframe src='https://giphy.com/embed/J3MJAf2FbKO8oaTaTv' width='480' height='480' frameBorder='0' class='giphy-embed' allowFullScreen></iframe>";
      document.getElementById("main").appendChild(div);
  }

  else{
    const questionObject = await fetch(
      `/newquestion?theme=${theme}&language=${language}`
    ).then((res) => {
      return res.json();
    });
  
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
    const button1 =
      "<button class='answer-buttons' id='right_answer'>" +
      right_answer +
      "</button><br>";
    const button2 =
      "<button class='answer-buttons' id='false_answer1'>" +
      false_answer1 +
      "</button><br>";
    const button3 =
      "<button class='answer-buttons' id='false_answer2'>" +
      false_answer2 +
      "</button><br>";
    const button4 =
      "<button class='answer-buttons' id='false_answer3'>" +
      false_answer3 +
      "</button><br>";
  
    let buttons = [button1, button2, button3, button4];
    shuffleArray(buttons);
  
    //Display the question in a div
    let div = document.createElement("div");
    let class_name = "answers" + question_number;
    div.className = class_name;
    let submit_text = "Submit";
    if (language=='French'){
      submit_text = "Soumettre";
    }
    div.innerHTML =
      "<h3>QUESTION " +
      question_number +
      "</h3><p>" +
      question +
      "</p>" +
      buttons[0] +
      buttons[1] +
      buttons[2] +
      buttons[3] +
      "<br><button class='submit' id='submit" +
      question_number +
      "' onclick='AnswerQuestion()'>"+submit_text+"</button>";
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
    let class_name = "answers" + question_number;
    let btns_div = document.getElementsByClassName(class_name)[0];
    let btns = btns_div.getElementsByClassName("answer-buttons");
    let feedback = "";
    for (var i = 0; i < btns.length; i++) {
      //Desactivate button
      btns[i].disabled = true;
      if (btns[i].id == "right_answer") {
        btns[i].style.backgroundColor = "green";
        if (btns[i].id == user_answer) {
          feedback = feedback_true_en;
          if (language == "French"){
            feedback = feedback_true_fr;
          }
          user_score += 1;
        }
      } else {
        if (btns[i].id == user_answer) {
          btns[i].style.backgroundColor = "red";
          feedback = feedback_false_en;
          if (language == "French"){
            feedback = feedback_false_fr;
          }
        }
      }
    }

    //Display a feedback and Next/End buttons
    let div = document.createElement("div");
    let next_message = "Next";
    let end_message = "End";
    if (language == "French"){
      next_message = "Suivant";
      end_message = "Fin";
    }
    var messagetodisplay =
      "<p>" +
      feedback +
      "</p><button class='submit' id='end" +
      question_number +
      "' style='background-color:red; margin-left:5px;' onclick='End()'>"+end_message+"</button>" +
      "<button class='submit' id='next" +
      question_number +
      "' style='margin-left:5px;' onclick='AddQuestion()'>"+next_message+"</button>";
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
  let message_score = "<p>Thank you for playing ! Your final score is ";
  if (language=='French'){
    message_score = "<p>Merci d'avoir joué ! Votre score final est ";
  }
  div.innerHTML = message_score +
    user_score +
    "/" +
    question_number +
    ".</p>";
  document.getElementById("main").appendChild(div);
  window.scrollTo(0, document.body.scrollHeight);
}

function shuffleArray(array) {
  return array.sort(() => Math.random() - 0.5);
}

function changeTheme(wantedTheme) {
  theme = wantedTheme;
}

