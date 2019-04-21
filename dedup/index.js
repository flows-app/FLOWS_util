exports.handler = (event, context,callback) => {
  event.dedupid=JSON.stringify(event);
  if(context.clientContext && context.clientContext.custom
    && context.clientContext.custom.lastvalue
    && context.clientContext.custom.lastvalue == event.dedupid){
    callback(null, {});
  }else{
    callback(null, event);
  }
}
