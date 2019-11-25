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

  //this part will be done with React.js
function getOrdersFromDatabase()
{

}

function runRestItUI(typeData="", userID=0,operationType="GET",username="")
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
