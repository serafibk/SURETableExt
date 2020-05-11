var fs = require('fs');
var http = require('http');
var express = require('express')
var app = express();
app.use(express.urlencoded());
app.post('/',function(req,res){
  var json = req.body.JSON;
  fs.writeFile('coords.json', json, 'utf8', function(err){
    if(err) return console.log(err);
  });
  res.send("recieved");
})
app.listen(8080);
console.log('server running at local:8080');
