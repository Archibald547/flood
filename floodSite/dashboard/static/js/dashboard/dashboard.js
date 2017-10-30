var opened = "no"
var minutes = 5;
var seconds = 0;
var interval;

function change() {
    var exp = {{user.myprofile.exp}};
    if (exp==1){
        includeLinkStyle("{% static 'css/growing1.css' %}");
    }
    if (exp==2){
        includeLinkStyle("{% static 'css/growing2.css' %}");
    }
    if(exp>=3){
        includeLinkStyle("{% static 'css/growing3.css' %}");
    }
}
      
function includeLinkStyle(url) {
    var link = document.createElement("link");
    link.rel = "stylesheet";
    link.type = "text/css";
    link.href = url;
    document.getElementsByTagName("head")[0].appendChild(link);
}
change();

function startTimer(duration, display, mode) {
    var timer = duration;

    interval = setInterval(function () {
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.text(minutes + ":" + seconds);

        if (--timer < 0) {
            var sound = document.getElementById("audio");
            sound.play();
            clearInterval(interval);
        }

    }, 1000);
}

jQuery(function ($) {
    var time = seconds + minutes * 60,
        display = $('#value');

    $("#startTimer").click(function() {
        clearInterval(interval);
        startTimer(seconds + minutes * 60, display);
    });

    $("#stopTimer").click(function() {
        clearInterval(interval);
        if (time != seconds + minutes * 60) {
            display.text(minutes + ":" + seconds);
        }
    });

    $("#resetTimer").click(function() {
        clearInterval(interval);
        startTimer(time, display);
    });

    $("#value").click(function() {
       var min = prompt("How many minutes? (must be a whole number and less than or equal to 60)", "5");
        if (Number.isInteger(Number(min)) && Number(min) <= 60) {
            minutes = min;
            seconds = 0;
            time = seconds + minutes * 60,
            clearInterval(interval);
            startTimer(seconds + minutes * 60, display);
        }
    });
});

$(document).ready(function() {
    window.location.href;
    if (((window.location.href).indexOf("todo/task") !== -1) || 
    ((window.location.href).indexOf("todo/complete") !== -1) || 
    ((window.location.href).indexOf("todo/delete") !== -1) || 
    ((window.location.href).indexOf("todo/list") !== -1)) {
    	document.getElementById("dropup").className = "dropup open"    
    }

    if ((window.location.href).indexOf("dashboard/") !== -1) {
        console.log("");
        var url = window.location.toString();
        window.location = url.replace(/dashboard/, 'todo');
    }
});

function displayModal() {
    if (opened == "no") {
        document.getElementById("dropup").className = "dropup open"
        opened = "yes"
    } else {
        document.getElementById("dropup").className = "dropup"
        opened = "no"
    }
}

function showTimer() {
    var x = document.getElementById("timer");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}