var AWS = require("aws-sdk");

exports.handler = (event, context,callback) => {
  callback(null, {"now":new Date().toISOString()});
}
