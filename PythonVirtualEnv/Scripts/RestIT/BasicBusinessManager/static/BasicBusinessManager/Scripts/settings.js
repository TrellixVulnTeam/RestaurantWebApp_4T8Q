//////////////////////////////////////CSRF code/////////////////////////////
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

function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
//  $ajaxSetup - Sets the default values for future AJAX requests, beforeSend: runs function before sending reequest
$.ajaxSetup({
  beforeSend: function(xhr, settings) 
  {     
      var csrftoken = getCookie('csrftoken');
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
  }
});
//////////////////////////END OF CSRF CODE///////////////////////////////////////////
function buildUserEnhancedObjectFromJSON(typeData="", userID=0,operationType="GET",username="")
{
  //first function 
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
    switch(operationType)
    {
      case "PUT":
        putUserObject(requestURL,username);
        //putClientObject(requestURL);
        break;
      case "GET":
        fillTextboxesWithGetUserObjectFromJSON(requestURL);
        break;
      default:
        break;
    }
  }
}
function fillTextboxesWithGetUserObjectFromJSON(fullURLForJSON)
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
function putClientObject(url)
{
  var csrftoken = getCookie('csrftoken');
  /*var xhttp = new XMLHttpRequest()
  xhttp.open("POST", url, true);
  xhttp.setRequestHeader("X-CSRFToken", csrftoken);
  xhttp.send();*/
  var user = new Object; 
  var jsonFile;
  $.getJSON(url,function(data)
  {
    jsonFile=JSON.stringify(data);
    tempObj = JSON.parse(jsonFile);
    tempObj.address = $("#street").val();
    tempObj.birthday = $("#birthday").val();
    jsonFile = JSON.stringify(tempObj);
    console.log(jsonFile);
    $.ajax({
      type: "PUT",
      url: url,
      CSRF: csrftoken,
      data: jsonFile,
      contentType: "application/json",
    });
  });
}
function createURLForUserObject(url,username)
{
  var temp = url.split("/");
  temp[4]="user";
  temp[temp.length-1]=username+".json";
  var finalUrl = "";
  for(i = 0;i < temp.length; i++)
  {
    finalUrl+=temp[i] +"/";
  }
  return finalUrl;
}
//todo - ogarnąć pozostałe typy kont
function putUserObject(url,username)
{
  var csrftoken = getCookie('csrftoken');
  var user = new Object; 
  var jsonFile;
  url = createURLForUserObject(url,username);
  console.log(url);
  $.getJSON(url,function(data)
  {
    jsonFile=JSON.stringify(data);
    tempObj = JSON.parse(jsonFile);
    tempObj.first_name = $("#firstname").val();
    tempObj.last_name = $("#lastname").val();
    jsonFile = JSON.stringify(tempObj);
    console.log(jsonFile);
    $.ajax({
      type: "PUT",
      url: url,
      CSRF: csrftoken,
      data: jsonFile,
      contentType: "application/json",
    });
  });
}
