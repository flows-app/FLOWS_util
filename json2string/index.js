var AWS = require("aws-sdk");

exports.handler = (event, context,callback) => {
  console.log("event");
  console.log(JSON.stringify(event,null,2));

  let str = JSON.stringify(event);
  let output = {"output":str}
  callback(null, output);
}
