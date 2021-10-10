const startBtn = document.querySelector("#start-btn");
const diagnosis = document.querySelector("#diagnosis");
//Symptoms here

let my_speech = document.querySelector("#my_speech");

typhoid = ["fever", "headache", "diarrhoea"];
maleria = ["fever", "shivering", "headache", "vomiting", "muscle"];
chickenpox = ["fever", "appetite", "headache", "tiredness"];
common_cold = ["sore", "cough", "congestion", "sneezing"];
dengue = ["muscle", "headache", "nausea", "vomiting", "Rash", "fever"];

const recognition = new webkitSpeechRecognition();
recognition.continous = true;
recognition.lang = "en-US";
recognition.interimResults = false;
recognition.maxAlternatives = 1;

startBtn.addEventListener("click", () => {
  recognition.start();
});

recognition.onresult = (e) => {
  let transcript = e.results[e.results.length - 1][0].transcript.trim();
  //   console.log(transcript);
  const myArr = transcript.split(" ");
  console.log(myArr);
  document.getElementById("1").value = transcript;
  
  diagnosis.innerHTML = "You response has been recorded. Please check the Timeline";
  document.getElementById("2").click();
  my_speech.innerHTML = transcript;
};
