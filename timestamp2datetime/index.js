const AWS = require("aws-sdk");
const SNS = new AWS.SNS();

const AccountPrefix = "arn:aws:sns:"+process.env.AWS_REGION+":"+process.env.ACCOUNTID+":";

exports.handler = (event, context,callback) => {
  console.log("event");
  console.log(JSON.stringify(event,null,2));
  console.log("context");
  console.log(JSON.stringify(context,null,2));
  let ts = Number(event.ts);
  //check if timestamp is seconds or milliseconds
  if( ts < 1000000000000){
    ts *= 1000;
  }
  let date = new Date(ts).toISOString();
  let result={"datetime":date};
  console.log(JSON.stringify(result,null,2));
  callback(null,result);
}
