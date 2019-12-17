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
require(["https://unpkg.com/babel-standalone@6/babel.min.js"]);
require(["es6!csrf"]);
require(["es6!../components/main/order_manager_home"]);
console.log("readed");
