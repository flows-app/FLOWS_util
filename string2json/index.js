var AWS = require("aws-sdk");

exports.handler = (event, context,callback) => {
  console.log("event");
  console.log(event);

  let obj = JSON.parse(event.input);
  callback(null, obj);
}
