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
function getEmployeeJsonUrl(userId)
{
  var url = "http://127.0.0.1:8000/rest/employee/";
  url+=userId+".json";
  return url;
}
function getCompanyID(userId)
{
  var url=getEmployeeJsonUrl(userId);
  var jsonFile;
  //get employee json
  $.getJSON(url,function(data)
  {
    jsonFile=JSON.stringify(data);
    $.ajax({
      type: "GET",
      url: url,
      CSRF: csrftoken,
      data: jsonFile,
      contentType: "application/json",
      success: function(data){
        jsonFile = JSON.stringify(data);
      },
    });
  });
  console.log(jsonFile);
}
function chooseRestItFunction(fun,userId)
{
  if(fun==="sender")
  {
    hideMenu();
    runRecieverUI(getCompanyID(userID));
  }
  else
  {
    if(fun==="receiver")
    {
      hideMenu();
      getCompanyID(userId);
      var reciever = new Reciever();
      reciever.runSenderUI();
    }
  }
}
function hideMenu(){
  $(".card").hide();
}
/////////////////////this part will be done with React.js///////////////////////////
function getOrdersFromDatabase()
{

}
class Reciever
{
  constructor()
  {

  }
  runRecieverUI()
  {
    //TODO - odebrać jsona i przekształcic w obiekt, spróbować zacząć reacta
    getUndoneOrders()
    {
      var csrftoken = getCookie('csrftoken');
      var user = new Object; 
      var jsonFile;
      $.getJSON(url,function(data)
      {
        jsonFile=JSON.stringify(data);
        jsonFile = getJsonObjectWithDataFromHTML(idVariablesArray,jsonFile);
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
    class Box extends React.Component{
      render()
      {
        return
        (
          //here box will be rendered
          <div class="order_box">

          </div>
        );
      }
    }
    class OrderManager extends React.Component
    {
      constructor(props)
      {
        super(props);
        this.state = 
        {
          history:[
            {

            }
          ],
          
        }
      }
      render()
      {
        
        return(
          <div class="order_box_container">
            
          </div>
        );
      }
    }

    ReactDOM.render(<Game />, document.getElementById("root"));
  }
}
/////////////////////////////////////SENDER REACT/////////////////////////////////////////////////
function runSenderUI()
{
  class Box extends React.Component{
    render()
    {
      return
      (
        //here box will be rendered
        <div class="order_box">

        </div>
      );
    }
  }
  class OrderManager extends React.Component
  {
    constructor(props)
    {
      super(props);
      this.state = 
      {
        history:[
          {

          }
        ],
        
      }
    }
    render()
    {
      
      return(
        <div class="order_box_container">
          
        </div>
      );
    }
  }

  ReactDOM.render(<Game />, document.getElementById("root"));
}

