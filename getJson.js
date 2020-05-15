var fs = require('fs');
var http = require('http');
var express = require('express')
var app = express();
var i=0;
app.use(express.urlencoded());
app.post('/',function(req,res){
  var json = req.body.JSON;
  var filename = 'coords'+i+'.json';
  fs.writeFile(filename, json, 'utf8', function(err){
    if(err) return console.log(err);
  });
  i+=1;
  res.send("recieved");
})
app.listen(8080);
console.log('server running at local:8080');
