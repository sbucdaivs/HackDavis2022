// onclick handler for the yes checkbox
$(".yes").click(function() {
  $(".phone-number").show();
});

function submit_data() {
  const patientData = {
    // name: document.getElementById("name").value,
    age: document.getElementById("age").valueAsNumber,
    heart_rate: document.getElementById("heart-rate").valueAsNumber,
    bp_systolic: document.getElementById("blood-pressure-systolic").valueAsNumber,
    bp_diastolic: document.getElementById("blood-pressure-diastolic").valueAsNumber,
    blood_sugar: document.getElementById("blood-sugar").valueAsNumber,
    body_temp: document.getElementById("btemp").valueAsNumber
  }
  console.log(patientData)
  postData("http://35.197.88.17/api/get_risk", patientData).then(data => {
    // showing the correct response
    if(data.risk_level == "low") {
      $(".low-risk").show();
    } else if (data.risk_level == "medium") {
      $(".med-risk").show();
    } else if (data.risk_level == "high") {
      $(".high-risk").show();
    }
  console.log(data)})
}

async function postData(url = '', data = {}) {
  // Default options are marked with *
  const response = await fetch(url, {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'same-origin', // include, *same-origin, omit
    headers: {
      'Content-Type': 'application/json'
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    redirect: 'follow', // manual, *follow, error
    referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
    body: JSON.stringify(data) // body data type must match "Content-Type" header
  });
  return response.json(); // parses JSON response into native JavaScript objects
}