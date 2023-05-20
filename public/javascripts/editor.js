let nRighe, editor, lineSelected, nTab, nBackSpacePremuti

nRighe = 1
nTab = 0
editor = document.getElementById("editor")
lineSelected = 1
nBackSpacePremuti = 0

for(let k = 0; k < editor.childElementCount; k ++) {
    setLineOnUpload(k + 1)
    setCodeLine(k + 1)
}

editor.addEventListener("keyup", () => {
    if (event.keyCode === 13 && lineSelected != null) {
        let inp = document.getElementById("inp_code_" + lineSelected.toString()).value
        if (inp.indexOf(':') !== -1)
            nTab++
        setCodeLine(lineSelected)
        newLine()

        let divNext = document.getElementById('code_line_' + lineSelected.toString())
        let pTab = document.createElement("p")
        pTab.innerHTML = ''
        for (let k = 0; k < 4 * nTab; k++)
            pTab.innerHTML += '&nbsp;'
        divNext.appendChild(pTab)

        selectLine(lineSelected)
        if (nBackSpacePremuti > 0)
            nBackSpacePremuti--
    } else if (event.keyCode === 8 && lineSelected != null) {
        //removeLine(lineSelected)
        nBackSpacePremuti++
        if (nBackSpacePremuti % 4 === 0 && nTab > 0)
            nTab--
    } else if (event.keyCode === 38 && lineSelected > 1) {
        setCodeLine(lineSelected)
        lineSelected--
        selectLine(lineSelected)
        if (nBackSpacePremuti > 0)
            nBackSpacePremuti--
    } else if (event.keyCode === 40 && lineSelected < editor.childElementCount) {
        setCodeLine(lineSelected)
        lineSelected++
        selectLine(lineSelected)
        if (nBackSpacePremuti > 0)
            nBackSpacePremuti--
    }
});

document.getElementById("line_1").addEventListener("click", () => {
    if (lineSelected !== 1) {
        lineSelected = 1
        selectLine(1)
    }
});
selectLine(1);

window.addEventListener('beforeunload', function() {
    $.ajax({
        method:"POST",
        url: "/session",
        data: "logout=''",
        success: function() {},
        error: function() {}
    });
});

function newLine() {
    let linesToShift = []
    while(editor.childElementCount > lineSelected) {
        linesToShift.push(editor.lastChild)
        editor.removeChild(editor.lastChild)
    }

    lineSelected ++
    let n = lineSelected
    let newLine = document.createElement("div")
    newLine.className = "line"
    newLine.id = "line_" + lineSelected.toString()
    newLine.addEventListener("click", () => {
        if(n !== lineSelected) {
            setCodeLine(lineSelected)
            lineSelected = n;
            selectLine(n);
        }
    })

    let nLine = document.createElement("p")
    nLine.className = "nLine"
    nLine.innerHTML = lineSelected.toString()
    nLine.addEventListener("dblclick", () => {
        nLine.style.cursor = "auto"
        removeLine(lineSelected)
    })
    newLine.appendChild(nLine)

    let divCodeLine = document.createElement("div")
    divCodeLine.className = "codeLine"
    divCodeLine.name = "ciao"
    divCodeLine.id = "code_line_" + lineSelected.toString()
    newLine.appendChild(divCodeLine)

    let inpLine = document.createElement("input")
    inpLine.type = "text"
    inpLine.className = "code"
    inpLine.id = "inp_code_" + lineSelected.toString()
    inpLine.value = ""
    newLine.appendChild(inpLine)

    editor.appendChild(newLine)
    for(let k = 0; k < linesToShift.length; k ++) {
        let e = linesToShift[linesToShift.length - 1 - k]
        let n = parseInt(e.firstChild.innerHTML)
        e.firstChild.innerHTML = (n + 1).toString()
        e.id = "line_" + (n + 1).toString()
        editor.appendChild(e)
    }
    setCodeLine(lineSelected - 1)
    selectLine(lineSelected)
}
function setCodeLine(line) {
    const keyWords = [ "for", "in", "while",
                       "and", "or", "not",
                       "if", "elif", "else",
                       "from", "import", "as",
                       "raise", "try", "except",
                       "finally", "with", "assert",
                       "global", "nonlocal", "def",
                       "return", "lambda", "yield",
                       "class", "del", "break",
                       "continue", "pass", "True",
                       "False", "is", "None"
    ]
    let id = "inp_code_" + line.toString()
    let str = document.getElementById(id).value

    document.getElementById(id).style.width = "0"
    document.getElementById(id).value = ""
    id = "code_line_" + line.toString()
    let div = document.getElementById(id)
    div.style.width = "100%"

    let arrStr = str.split(" ")
    for(let k = 0; k < arrStr.length; k ++) {
        if(arrStr[k] !== "") {
            let t
            if (keyWords.indexOf(arrStr[k]) !== -1) {
                t = document.createElement("b")
                t.className = "keyWord"
            } else {
                t = document.createElement("p")
                t.className = ""
            }
            t.innerHTML = arrStr[k]
            div.appendChild(t)
        }
        let t1 = document.createElement("p")
        t1.innerHTML = "&nbsp"
        div.appendChild(t1)
    }

}
function selectLine(n) {
    let line = document.getElementById("inp_code_" + n.toString())

    let str = "", div = document.getElementById("code_line_" + n.toString())
    while(div.childElementCount > 0) {
        str += div.firstChild.innerHTML;
        div.removeChild(div.firstChild)
    }

    line.style.width = "100%"
    line.style.padding = "5px"
    div.style.width = "0"

    str = str.split("&nbsp;")
    str = str.join(" ")
    line.value = str

    line.focus()
}
function removeLine(n) {
    let len = editor.childElementCount
    editor.removeChild(document.getElementById("line_" + n.toString()))
    for(let k = n + 1; k <= len; k++) {
        let line = document.getElementById("line_" + k.toString())
        line.id = "line_" + (k - 1).toString()

        let nLine = document.getElementsByClassName("nLine")[k - 2]
        nLine.innerHTML = (k - 1).toString()

        let inp = document.getElementById("inp_code_" + k.toString())
        inp.id = "inp_code_" + (k - 1).toString()

        let code = document.getElementById("code_line_" + k.toString())
        code.id = "code_line_" + (k - 1).toString()
    }

    setCodeLine(editor.childElementCount)
    selectLine(lineSelected -1)
    lineSelected --
}
function uploadFile() {
    let file = document.getElementById("fileDaCaricare")
    file.click()
}
function fileUploaded() {
    let but = document.getElementsByClassName("butt")[2]
    but.type = "submit"
    but.value = "UPLOAD"
    but.onclick = "resetSubmitUploadFile()"
}
function resetSubmitUploadFile() {
    let but = document.getElementsByClassName("butt")[2]
    but.type = "button"
    but.value ="CARICA UN FILE"
    but.onclick="uploadFile()"

    let file = document.getElementById("fileDaCaricare")
    file.value = ""
}
function setLineOnUpload(n) {
    let div_1 = document.getElementsByClassName('line')[n - 1]
    div_1.id = 'line_' + n.toString()
    div_1.addEventListener("click", () => {
        if(n !== lineSelected) {
            setCodeLine(lineSelected)
            lineSelected = n;
            selectLine(n);
        }
    })

    let p = document.getElementsByClassName('nLine')[n - 1]
    p.innerHTML = n.toString()

    let div_2 = document.getElementsByClassName('codeLine')[n - 1]
    div_2.id = 'code_line_' + n.toString()
    let str = div_2.innerHTML
    div_2.innerHTML = ''

    let inp = document.getElementsByClassName('code')[n - 1]
    inp.id = 'inp_code_' + n.toString()
    inp.value = str
}

function load() {
    let s = '';
    for(let k = 0; k < editor.childElementCount; k ++) {
        let t = document.getElementsByClassName('codeLine')[k];
        let arrTemp = [];
        while(t.childElementCount > 0) {
            arrTemp.push(t.firstChild);
            s += ((t.firstChild.innerHTML == '&nbsp;')? ' ' : t.firstChild.innerHTML);
            t.removeChild(t.firstChild);
        }
        arrTemp.forEach(e => t.appendChild(e));
        s = s + '\\n';
    }
    s = s.trim();

    let inp = document.createElement('input');
    inp.style.height = '0';
    inp.style.visibility = 'hidden';
    inp.type = 'text';
    inp.name = 'content';
    inp.value = s;
    document.getElementsByName('perEditor')[0].appendChild(inp);
    document.getElementsByName('perEditor')[0].submit();
}

/*
function delDblLine() {
    removeLine(lineSelected)
    if(lineSelected > editor.childElementCount)
        lineSelected = editor.childElementCount
    selectLine(lineSelected)
}*/
/*
function checkDeleteLine() {
    if(lineSelected === 1)
        return
    let str_t_1 = document.getElementById("inp_code_" + (lineSelected - 1).toString())
    let lastChar = str_t_1[str_t_1.length - 1]
    if(lastChar === undefined)
        lastChar = ""

    let inp_t = document.getElementById("inp_code_" + lineSelected.toString())
    if(inp_t.value === "") {
        inp_t.value += lastChar
        delDblLine()
    }
}*/