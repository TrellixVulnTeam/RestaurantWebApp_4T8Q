//import {} from '../../scripts/csrf.js';
//import {Receiver} from '../receiver/receiver.js';
// Importing combination 
//import React, {Component} from 'react'; 
// Importing Module 
//import ReactDOM from 'react-dom'; 
//import ChangeColor from './change-color.js'; 
// Importing CSS 
//import './index.css'; 
define([
  'dad'
], function() {
  console.log("123123");
});
/*
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
}/*
/////////////////////////////////////SENDER REACT/////////////////////////////////////////////////
define(function runSenderUI()
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
});*/