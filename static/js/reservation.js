src = "data/reservation"

var xmlhttp = new XMLHttpRequest();

xmlhttp.onload = function ()
{
    myObj = JSON.parse(this.responseText);
    console.log(myObj)
}
xmlhttp.open("GET", src)
xmlhttp.setRequestHeader("Content-type", src);
xmlhttp.send();
