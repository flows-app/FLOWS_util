const AWS = require("aws-sdk");

exports.handler = (event, context,callback) => {
  console.log("event");
  console.log(JSON.stringify(event,null,2));
  console.log("context");
  console.log(JSON.stringify(context,null,2));
  let date = new Date().toISOString();
  let result={"today":date.substring(0,10)};
  console.log(JSON.stringify(result,null,2));
  callback(null,result);
}
