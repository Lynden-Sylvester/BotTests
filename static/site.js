document.getElementById("home").style.display = "inline";

function new_user() {
    document.getElementById("home").innerHTML = "Hello";
}

document.getElementById('submitButton').onclick = function () {

  // Get the current string in the text box
  var input = document.getElementById('inputBox').value;
  var input2 = document.getElementById('inputBox2').value;


  function responseListener() {
                document.getElementById('responseDiv').innerHTML = this.responseText;
            }

}

setTimeout(function () {
    location.reload();
}, 1000);