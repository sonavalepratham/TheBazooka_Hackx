const startBtn = document.querySelector("#start-btn");
const diagnosis = document.querySelector("#diagnosis");
//Symptoms here
// const btn = document.querySelector('#2');
// btn.addEventListener('click', ()=>{
//   pos
// })
let my_speech = document.querySelector("#my_speech");

typhoid = ["fever", "headache", "diarrhoea"];
maleria = ["fever", "shivering", "headache", "vomiting", "muscle"];
chickenpox = ["fever", "appetite", "headache", "tiredness"];
common_cold = ["sore", "cough", "congestion", "sneezing", "unwell"];
dengue = ["muscle", "headache", "nausea", "vomiting", "rash", "fever"];

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
  document.getElementById("2").click();
  let cnt = 0;
  let cnt2 = 0;
  let cnt3 = 0;
  let cnt4 = 0;
  let cnt5 = 0;
  myArr.forEach((e1) => {
    typhoid.forEach((element) => {
      if (e1 === element) cnt++;
    });
  });

  if (cnt === typhoid.length) diagnosis.innerHTML = "You have Typhoid";
  else {
    myArr.forEach((e1) => {
      maleria.forEach((element) => {
        if (e1 === element) {
          cnt2++;
        }
      });
    });
  }

  if (cnt2 === maleria.length) diagnosis.innerHTML = "You have maleria";
  else {
    myArr.forEach((e1) => {
      chickenpox.forEach((element) => {
        if (e1 === element) {
          cnt3++;
        }
      });
    });
  }

  if (cnt4 === chickenpox.length) diagnosis.innerHTML = "You have chikenpox";
  else {
    myArr.forEach((e1) => {
      common_cold.forEach((element) => {
        if (e1 === element) {
          cnt4++;
        }
      });
    });
  }

  if (cnt5 === common_cold.length) diagnosis.innerHTML = "You have common cold";
  else {
    myArr.forEach((e1) => {
      dengue.forEach((element) => {
        if (e1 === element) {
          cnt5++;
        }
      });
    });
  }

  if (cnt5 === dengue.length) diagnosis.innerHTML = "You have Dengue";

  my_speech.innerHTML = transcript;
};
