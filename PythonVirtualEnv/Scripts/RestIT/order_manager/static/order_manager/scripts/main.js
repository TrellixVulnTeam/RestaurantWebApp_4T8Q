require.config({
  config: {
    es6: {
      resolveModuleSource: function(source) {
        return 'es6!'+source;
      }
    }
  },
  paths: {
    es6: "./es6",
    babel: "./babel-5.8.34.min"
  },
});
console.log("reading ...");
require(["https://unpkg.com/babel-standalone@6/babel.min.js"],()=>{console.log("1");});
require(["es6!csrf"],()=>{console.log("2");});
require(["es6!../components/main/order_manager_home"],()=>{
  var dupa = require("../components/main/order_manager_home");
  console.log("3");
  console.log(dupa);
});
