var opened = "no"
var minutes = 5;
var seconds = 0;
var mode = "stop";
var interval;

function startTimer(duration, display, mode) {
    var timer = duration;

    interval = setInterval(function () {
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.text(minutes + ":" + seconds);

        if (--timer < 0) {
            timer = duration;
        }
        console.log(minutes)
        console.log(seconds)

    }, 1000);
}

jQuery(function ($) {
    var time = seconds + minutes * 60,
        display = $('#value');

    $("#startTimer").click(function() {
        startTimer(seconds + minutes * 60, display);
    });

    $("#stopTimer").click(function() {
        clearInterval(interval);
        display.text(minutes + ":" + seconds);
    });

    $("#resetTimer").click(function() {
        clearInterval(interval);
        startTimer(time, display);
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
});

function displayModal() {
    if (opened == "no") {
        document.getElementById("dropup").className = "dropup"
        opened = "yes"
        console.log("opened")
    } else {
        document.getElementById("dropup").className = "dropup open"
        opened = "no"
        console.log("closed")
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

        // document.getElementById('timer').innerHTML = 03 + ":" + 00;
        // startTimer();

        // function startTimer() {
        //   var presentTime = document.getElementById('timer').innerHTML;
        //   var timeArray = presentTime.split(/[:]+/);
        //   var m = timeArray[0];
        //   var s = checkSecond((timeArray[1] - 1));
        //   if(s==59){m=m-1}
        //   //if(m<0){alert('timer completed')}
          
        //   document.getElementById('timer').innerHTML = m + ":" + s;
        //   setTimeout(startTimer, 1000);
        // }

        // function checkSecond(sec) {
        //   if (sec < 10 && sec >= 0) {sec = "0" + sec}; // add zero in front of numbers < 10
        //   if (sec < 0) {sec = "59"};
        //   return sec;
        // }