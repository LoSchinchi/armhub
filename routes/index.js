var express = require('express');
var router = express.Router();

// GET home page
router.get('/', function(req, res, next) {
  res.render('index');
});

router.get('/project', function(req, res, next) {
  res.render('project');
});

router.get('/code', function(req, res, next) {
  res.render('code');
});

module.exports = router;
