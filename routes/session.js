let express = require('express');
let router = express.Router();
let multipart = require('connect-multiparty');
let fs = require('fs');
let path = require('path');
let { exec } = require('child_process');

let multipartMiddleware = multipart({ uploadDir: 'uploads' });

const USERNAME = 'armhub', PASSWORD = 'zetaupi';
let loginUnaVolta = false, datiSbagliati = false;
exec('python3 python/lcdIP.py');
//exec('python3 python/main.py');

router.get('/', function(req, res, next) {
    if(req.body.logout !== undefined) {
        loginUnaVolta = false;
        //exec('python3 python/lcdIP.py');
        return;
    }
    res.render('login', { accPossibile: !loginUnaVolta, datiSbagliati: datiSbagliati });
});

// POST session listing
router.post('/editor', multipartMiddleware, function(req, res, next) {
    fs.writeFile('dati/isRunning.txt', '', {encoding: 'utf8'}, function(err) { });
    
    act = req.body.action;
    if(act == 'DOWNLOAD') {
        let content = req.body.content.split('\\n').join('\n');
        fs.writeFile('downloads/file.py', content, {encoding: 'utf8'}, function(err) {
            if(err)
                console.log('error');
            else
                res.download('downloads/file.py');
        });
    } else if(act == 'UPLOAD') {
        fs.readdir('uploads', {withFileTypes: true}, function(err, data) {
            if(err)
                console.log(err);
            else {
                let path = 'uploads/' + data[0].name;
                fs.readFile(path, { encoding: 'utf8' }, function (err, data) {
                    if(err)
                        res.render('editor', { arr: [''], exc: undefined });
                    else {
                        let d = data.split('\n');
                        console.log('d: ', d);
                        let td = [];
                        for(let _d of d)
                            td.push(_d.trim());
                        console.log('_td: ', td);

                        exec('rm -r uploads/*')

                        res.render('editor', { arr: td, exc: undefined });
                    }
                });
            }
        });
    } else if(act == 'RUN') {
        fs.writeFile('python/run.py', req.body.content.split('\\n').join('\n'), {encoding: 'utf8'}, function(err) {
            if(!err)
                exec('python3 python/setFileRun.py', function(error, stdout, stderr) {
                    if(error)
                        throw error;
                    else {
                        fs.readFile('dati/editorException.txt', 'utf-8', function(err, data) {
                            if(err)
                                throw err;
                            else {
                                const CONTENT = data;
                                fs.readFile('dati/tempEditorLines.txt', 'utf-8', function(err, data) {
                                    if(err)
                                        throw err;
                                    else if(CONTENT != '')
                                        res.render('editor', { arr: data.split('\n'), exc: CONTENT.split('\n') });
                                    else
                                        res.render('editor', { arr: data.split('\n'), exc: undefined });
                                });
                            }
                        });
                    }
                });
        });
    } else
        res.render('editor', { arr: [''], exc: undefined });
});

// solo per entrare, sarà da concellare
router.get('/editor', function(req, res, next) {
    res.render('editor', { arr: [''], exc: undefined });
});

router.post('/interface', function(req, res, next) {
    if(req.body.username !== undefined) {
        if(req.body.username !== USERNAME || req.body.password !== PASSWORD) {
            datiSbagliati = true;
            res.redirect('/session');
            return;
        } else if(loginUnaVolta) {
            res.redirect('/session');
            return;
        } else {
            exec('python3 python/main2.py', function(error, stdout, stderr) {
                if(error)
                    console.log(error)
                else
                    console.log(stdout)
            });
        }
    } else if(req.body.dati !== undefined) {
        let s = req.body.dati;
        let datiDef = [];
        let t = s.split(',');
        for(let dato of t) 
            datiDef.push(parseInt(dato.split(': ')[1]))
        let content = 'motore ' + (datiDef[0] + 1) + ': ' + datiDef[1] + '\n';

        fs.writeFile('dati/datiMotori.txt', content, {encoding: 'utf8'}, function(err) { });
    }
    console.log('here')
    //loginUnaVolta = true;
    datiSbagliati = false;
    res.render('controlsInterface');
});

module.exports = router;
