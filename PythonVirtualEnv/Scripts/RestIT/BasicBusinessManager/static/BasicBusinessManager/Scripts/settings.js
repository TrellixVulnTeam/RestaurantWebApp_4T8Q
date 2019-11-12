/*$.ajax({
  type: "POST",
  url: "file",
  data: { CSRF: getCSRFTokenValue()}
})
.done(function( msg ) {
  alert( "Data: " + msg );
});
$("body").bind("ajaxSend", function(elm, xhr, s){
  if (s.type == "POST") {
     xhr.setRequestHeader('X-CSRF-Token', getCSRFTokenValue());
  }
});*/

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
  beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
  }
});

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
    baseURL = 'http://127.0.0.1:8000/rest/';
    requestURL = baseURL+requestObject+userID+'.json';
    getUserObjectFromJSON(requestURL);
  }
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
