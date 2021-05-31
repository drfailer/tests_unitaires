var path = "http://127.0.0.1/";
var user_id=-1;
// code:
let cd = document.querySelector('#code-input');
// test id
let id_exercice = document.querySelector('#exercise-id');

async function recupCode() {
    if(document.getElementById('exercise-id').value != "")
    {
        await getId(); 
        await getCode();
        setTimeout(getTest,2000);     
    }
}

function displayTestsDetails() {
    var urlInfo = path+"php/get_info.php?id_exercise=" + id_exercice.value;
    fetch(urlInfo).then(response => response.text()).then(data => {
        console.log(data);
        document.querySelector('#test-details').innerText = data;
    }).catch(error => {
        console.log(error);
        document.querySelector('#test-details').innerText = error;
    })
}


// get a user id:
async function  getId()
{    
    return fetch(path+"php/get_id.php")
        .then((response) => response.json())
        .then(response => {
            user_id = response;
            console.log("GET ::: " + response);
        })
        .catch(error => {
            console.log("getIDError:" + error);
        })
}

// post the code inside the design text area
async function getCode()
{
    return fetch(path+"php/get_code.php", {
        method: 'post',
	
	body: JSON.stringify({"user_id": user_id, "id_exercise": id_exercice.value, "code": cd.value}),
        headers: {
            'Content-Type': 'application/json'}
    })
        .then(function (resp) {
            console.log("REPONSE ::: ", resp)
        })
        .catch(function (err) {
            console.log("ERROR ::: ", err)
        })
}

// get the result of our code
async function getTest()
{
    var urlResult = path+"php/get_result.php?user_id=" + user_id;
    await fetch(urlResult).then(data => {
        console.log("GET ::: ", data);
        data.text().then(function (text) {
            
            document.querySelector('#result-output').innerText = text;
        });
    }).catch(error => {
        console.log(error);
        document.querySelector('#result-output').innerText = error;
    })
}
