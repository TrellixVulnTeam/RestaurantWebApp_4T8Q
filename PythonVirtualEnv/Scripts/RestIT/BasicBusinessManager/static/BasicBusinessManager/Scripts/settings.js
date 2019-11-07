function buildUserEnhancedObjectFromJSON(typeData="", userID=0)
{
  //builds object from json to Client/Employee/CO
  var requestObject ="";
  var requestURL="";
  switch(typeData)
  {
    case "Client":
      requestObject = "client/";
      break;
    case "CompanyOwner":
      requestObject = "company_owner/";
      break;
    case "Employee":
        requestObject = "employee/";
      break;
    default:
        requestObject = "rest";
  }
  if(requestObject === "rest")
  {
    alert("bug appeared");
  }
  else
  {
    requestURL = 'http://127.0.0.1:8000/rest/'+requestObject+userID+'.json';
    getUserObjectFromJSON(requestURL);
  }
}
function chuj(){
  alert("chuj");
}
function getUserObjectFromJSON(fullURLForJSON)
{
  var request = new XMLHttpRequest();
  request.open('GET', fullURLForJSON);
  request.responseType = 'json';
  request.send();
  request.onload = function() {
    var user = request.response;
    loadSettingsFormGettingDataFromObject(user);
  }
function loadSettingsFormGettingDataFromObject(userObject)
  {
    document.getElementById("street").value = userObject.address;
    //document.getElementById("settings").innerHTML = chuj['username'];
    
  }
}
