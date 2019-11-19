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
  baseURL = 'http://127.0.0.1:8000/rest/';
  switch(typeData)
  {
    case "Client":
      requestObject = "client/";
      requestURL = createURLForEnhancedUserObject(baseURL,requestObject,userID)
      switch(operationType)
      {
        case "PUT":
          putClientObject(requestURL);
          break;
        case "GET":
          fillTextboxesWithGetUserObjectFromJSON(requestURL);
          break;
        default:
          break;
      }
      break;
    case "CompanyOwner":
      requestObject = "company_owner/";
      requestURL = createURLForEnhancedUserObject(baseURL,requestObject,userID)
      switch(operationType)
      {
        case "PUT":
          putClientObject(requestURL);
          break;
        case "GET":
          fillTextboxesWithGetUserObjectFromJSON(requestURL);
          break;
        default:
          break;
      }
      break;
    case "Employee":
        requestObject = "employee/";
        requestURL = createURLForEnhancedUserObject(baseURL,requestObject,userID)
        switch(operationType)
        {
          case "PUT":
            putClientObject(requestURL);
            break;
          case "GET":
            fillTextboxesWithGetUserObjectFromJSON(requestURL);
            break;
          default:
            break;
        }
      break;
    default:
        requestObject = "rest";
  }
  if(requestObject === "rest")
  {
    alert("unknown accout type");
  }
  else
  {
    switch(operationType)
    {
      case "PUT":
        requestObjectForBasicUser = createURLForEnhancedUserObject(baseURL,"user",username);
        putUserObject(requestObjectForBasicUser);
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
  //todo <---------ogarnięty backend - przesyłanie funkcji. Zrobić żeby działał PUT dla wszystkich (client chyba działa)
  var csrftoken = getCookie('csrftoken');
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
function putEmployeeObject(url)
{
  var csrftoken = getCookie('csrftoken');
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
function putCompanyOwnerObject(url)
{
  var csrftoken = getCookie('csrftoken');
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
function putUserObject(url)
{
  var csrftoken = getCookie('csrftoken');
  var user = new Object; 
  var jsonFile;
  url = createURLForEnhancedUserObject(url,username,"user");
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
function createURLForEnhancedUserObject(base_domain_rest_url="",account_type="",username="")
{
  var temp = "";
  temp = base_domain_rest_url+account_type+username+".json";
  return temp;
}
