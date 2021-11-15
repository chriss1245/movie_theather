src = "data/reservation"

const OPEN_HOUR = 8;
var xmlhttp = new XMLHttpRequest();

xmlhttp.onload = function ()
{
    projections = JSON.parse(this.responseText);
    set_projections(projections);
}
xmlhttp.open("GET", src)
xmlhttp.setRequestHeader("Content-type", src);
xmlhttp.send();


// Projections manager
let set_projections = function (projections)
{
    var projection;
    var cell;
    for (p in projections)
    {
        projection = projections[p];
        col = projection.date.weekday
        row = ((projection.date.hour - OPEN_HOUR) % 24) + 1 // Format 24 hours and added 1 at all the hours so they concide with the table indexes
        row_ = projection.date.minute

        idx = 'r' + row + 'c' + col;
        
        column = document.getElementById('1')
        cell = document.createElement('div');
        cell.style.borderBottom = "0px solid black"
        cell.style.backgroundColor = "red";
        cell.style.height = "40px"
        cell.style.backgroundClip= "content-box"
        cell.innerHTML = "testing";

         // the row is 40 px, 60 min -> 40px, then row_ min -> x px

        cell.onclick=function () {alert('lol')}


        /*item = document.createElement('input')
        item.setAttribute("type", "button")
        item.style.marginTop = '0px';
        item.style.background = 'red';
        item.style.width = '100%';
        item.style.height = '220%'
        item.style.border = '0px solid black'
        
        cell.appendChild(item)
        console.log(cell, item)*/
        column.appendChild(cell);
        console.log(column)
        
    }
}