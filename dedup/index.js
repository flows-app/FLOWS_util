exports.handler = (event, context,callback) => {
  event.dedupid=JSON.stringify(event);
  if(context.clientContext.custom.lastvalue == event.dedupid){
    callback(null, {});
  }else{
    callback(null, event);
  }
}
