var opened = "no"

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