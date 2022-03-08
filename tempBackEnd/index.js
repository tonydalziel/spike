const express = require('express');
const app = express();
var cors = require('cors');

app.use(cors());

reportsInfo = [
  {
    "id":"ChIJH0RBxIp9fkgRuV5LKoN4PAM",
    "name":"Loft Durham",
    "reports": 2,
    "lastReport": "02:27:26",
    "severity": 0.11,
    "location":"15-17, North Rd, Durham"
 },
 {
    "id":"ChIJkSBUwol9fkgRSCue7fUuujI",
    "name":"Klute",
    "photoID":"Aap_uECOgT4ArfSorF2crgUNQpTfvO_wr_95J-OdBIx3MkXwHCCM2svuE5ym4gja7qfbAdVsNAXUsaDJkmmhXIPjZfqOtmN7aMJYFsVFWbqflTTrgIl1CRmHLwVgR5Kd_39QJUMw6EwUoSMeLWVCX6wm6A6Fcr293LKbyPJOT3beBIyWepeF",
    "reports": 24,
    "lastReport": "05:53:20",
    "severity": 0.38,
    "location":"Elvet Bridge, Durham"
 },
 {
    "id":"ChIJhUa_THx9fkgRY_M770E3xAc",
    "reports": 43,
    "lastReport": "01:20:12",
    "severity": 0.69,
    "name":"New Durham & District Workmens Club",
    "location":"Belles Ville, Durham"
 },
 {
    "id":"ChIJjd2knGGHfkgRCPJzLTwXyRY",
    "name":"24 North Bailey Club",
    "reports": 43,
    "lastReport": "06:00:33",
    "severity": 0.59,
    "location":"24 N Bailey, Durham"
 },
 {
    "id":"ChIJhejgs2KHfkgRL9r36YUntNw",
    "name":"Dunelm Club Ltd",
    "reports": 29,
    "lastReport": "02:20:11",
    "severity": 0.63,
    "location":"55 Old Elvet, Durham"
 },
 {
    "id":"ChIJKx3ZM8-AfkgR-s54-bewGL0",
    "name":"Browney Social Club",
    "reports": 17,
    "lastReport": "07:37:38",
    "severity": 0.87,
    "location":"30 Browney La, Durham"
 }
]


//Could additionally store the name of each user to return
startTime = new Date(Date.now() - 2*24*60*60*1000);
startTimeString = startTime.valueOf();

loginDetails = [
    {username:"admin",password:"pass",lastReport: startTimeString}
]


//Request for names / reports etc. -> Develop more advanced pages later on
app.get('/basicReports', function(req, resp) {
    resp.json(reportsInfo)
} );

app.get('/login',function(req,resp){
  if(loginDetails.some(login => (login.username === req.query.username) && (login.password === req.query.password) )){
    index = loginDetails.findIndex(user => user.username === req.query.username);
    resp.json({valid:true,username:req.query.username,lastReport: loginDetails[index].lastReport})
  }else{
    resp.json({valid:false})
  }
});

app.get('/locations',function(req,resp){
  resp.json(reportsInfo.map(report => {
    return report.name;
  }));
});

app.get('/makeReport',function(req,resp){
  indexUser = loginDetails.findIndex(user => user.username === req.query.username);
  indexLocation = reportsInfo.findIndex(location => location.name === req.query.name);
  loginDetails[indexUser].lastReport = Date.now();
  reportsInfo[indexLocation].reports += 1;
  resp.status(200).end();
});

app.get('/newUser',function(req,resp){
  if(loginDetails.some(login => (login.username === req.query.username))){
    resp.json({valid:false,message:"The username is already taken"});
  }else{
    loginDetails.push({username:req.query.username,password:req.query.password,lastReport: 0});
    resp.json({valid:true,message:"Successfully registered"});
  }
});

app.use(express.json());
app.listen(8090);