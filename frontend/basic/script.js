//bound to button onclick

function userLoggedIn(){
    //get the value in the input element
    let userInput = document.getElementById('adjective-input').value
    //change the inner HTML of the adjective (span) element
    document.getElementById('text-box').innerHTML = userInput + " is in the system"
}


