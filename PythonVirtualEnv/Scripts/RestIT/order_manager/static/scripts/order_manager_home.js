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


class Switcher{

  static hideMenu(){
    $(".card").hide();
  }

  static getCompanyID(userId)
  {
    var base = "http://127.0.0.1:8000/";
    var url = base + "rest/employee/"+userId+".json";
    var companyID;
    return $.getJSON(url,function(data){
    });
  }

  static chooseRestItFunction(foo,userId){
    if(foo==="sender"){
      hideMenu();
      runRecieverUI(getCompanyID(userId));
    }
    else{
      if(foo==="receiver"){
        this.hideMenu();
        var companyID;
        $.when(this.getCompanyID(userId)).done(function(data){
          var employee = data;
          companyID = employee.workplace;
          var receiver = new Receiver(companyID);
        });
      }
    }
  }
}
/////////////////////this part will be done with React.js///////////////////////////  //////////////////////////////////REACT part of reciever//////////////////////////////////////////////////////

function OrderFieldTitle(props){
  return(
    <h4>{props.id} {props.time.slice(11,19)}</h4>
  );
}
function OrderFieldContent(props){//dokonczyc jutro
  var content="";
  for(var i = 0; i<props.products.length; i++){
    content+=(<p> - {props.products.pop()}</p>);
  }
  console.log(content);
  return(
    <div className="order_box_content">
      {content}
    </div>
  );
}
class OrderBox extends React.Component{

  render()
  {
    console.log(this.props);
    return(
      <button className="order_box" id = {this.props.order.id} onClick={this.props.onOrderClick}>
        <OrderFieldTitle id={this.props.order.id} time = {this.props.order.order_date}/>
        <OrderFieldContent products ={this.props.order.products}/>
      </button>
    );
  }
}
class OrdersBoard extends React.Component{//3x3 board for the start
  renderBox(i){
    //console.log(this.props.orders.orders[i]);
    return(
      <OrderBox
        key = {i}
        order = {this.props.orders.orders[i]}
        onOrderClick = {()=>this.props.onOrderClick(i)}
      />
    );
  }
  render()
  {
    var order_boxes = [];
    for(var i=0; i<9;i++){
      if(i<this.props.orders.orders.length){
        order_boxes.push(this.renderBox(i));
      }
      else{
        break;
      }
    }
    console.log(order_boxes);
    return(
      <div className="order_board">
        {order_boxes}
      </div>
    );
  }
}
class OrdersReceiver extends React.Component{//waiting for extensions(? no idea what kind of yet)
  constructor(props){
    //console.log("props:");
    //console.log(props);
    super(props);
    const orders = this.props.orders.results;
    this.state = {
      currentOrders:{orders},
    }
  }
  render()
  {
    return(
      <div className="order_board_container">
        <OrdersBoard 
          orders={this.state.currentOrders}
          onOrderClick={id=>this.onOrderClick(id)}
        />
      </div>
    );
  }
  onOrderClick(id){
    alert(id);

  }

}
///////////////////////END OF REACT ORDER RECEIVER///////////////////////////////////////////////////////
class Receiver{

  constructor(companyID){
    this.companyID = companyID;
    this.companyID = this.companyID[0];///decision for workplace - todo
    this.orders="";
    var me = this;
    $.when(this.getUndoneOrders()).done(function(data){
      me.orders=data;
      me.runReceiverUI();
    });
  }

  runReceiverUI(){
    //console.log(this.orders);
    //var reactReceiver = new OrdersReciever(this.orders);
    ReactDOM.render(<OrdersReceiver orders = { this.orders }/>, document.getElementById("order_board"));
  }

   getUndoneOrdersJsonUrl(){
    var base = "http://127.0.0.1:8000/";
    var url = base + "rest/order/?delivered=false&deliverant="+ this.companyID;
    return url;
  }

  getUndoneOrders(){
    var url = this.getUndoneOrdersJsonUrl();
    //console.log(url);
    return $.getJSON(url,function(data){
    });
  }
}  



/////////////////////////////////////SENDER REACT/////////////////////////////////////////////////
function runSenderUI()
{
  class Box extends React.Component{
    render()
    {
      return(
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

