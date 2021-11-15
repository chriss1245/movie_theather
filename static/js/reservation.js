src = "data/reservation"

const OPEN_HOUR = 9;
const HOUR_SIZE = 41;
var xmlhttp = new XMLHttpRequest();
var begin_filled = false

xmlhttp.onload = function ()
{
    days = JSON.parse(this.responseText);
    set_projections(days);
}
xmlhttp.open("GET", src)
xmlhttp.setRequestHeader("Content-type", src);
xmlhttp.send();


// Projections manager
let set_projections = function (days)
{
    /*
    var projection;
    var cell;
    var offset = 0;
    var last_col = 0;
    var last_row = -1;
    for (p in projections)
    {
        projection = projections[p];
        col = projection.date.weekday
        row = ((projection.date.hour - OPEN_HOUR) % 24)// Format 24 hours and added 1 at all the hours so they concide with the table indexes
        row_ = projection.date.minute/40
        
        if (!begin_filled)
        {
            for (var c=0; c<col; c++)
            {
                column = document.getElementById(c+'');
                for (var r=0; r<16; r++)
                {
                    cell = document.createElement('div');
                    cell.className = "projection"
                    cell.style.height = "40px"
                    cell.innerHTML = ""
                    column.appendChild(cell) 
                }
            }
            begin_filled = true;
        }
        else if (last_col < col)
        {
            column = document.getElementById(last_col+'');
            alert(last_col)
            for (var r=last_row; r<16; r++)
            {
                cell = document.createElement('div');
                cell.className = "projection"
                cell.style.height = "40px"
                cell.innerHTML = ""
                column.appendChild(cell) 
            }
        }

        

        idx = 'r' + row + 'c' + col;
        console.log(projection)
        last_col = projection.date.weekday;
        last_row = row+1;
        column = document.getElementById(projection.date.weekday+'')
        for(var r=0; r < row; r++)
        {
            cell = document.createElement('div');
            cell.className = "projection"
            cell.style.height = "40px"
            cell.innerHTML = ""
            column.appendChild(cell)
        }


        
        cell = document.createElement('div');
        cell.className = "projection"
        cell.style.backgroundColor = "red";
        cell.style.height = "80px"
        cell.style.backgroundClip= "content-box"
        cell.innerHTML = "testing";

         // the row is 40 px, 60 min -> 40px, then row_ min -> x px

        cell.onclick=function () {alert('lol')}


        item = document.createElement('input')
        item.setAttribute("type", "button")
        item.style.marginTop = '0px';
        item.style.background = 'red';
        item.style.width = '100%';
        item.style.height = '220%'
        item.style.border = '0px solid black'
        
        cell.appendChild(item)
        console.log(cell, item)

        column.appendChild(cell);
    }


    for (var c=last_col+1; c<7; c++)
    {
        column = document.getElementById(c+'');
        for (var r=0; r<16; r++)
        {
            cell = document.createElement('div');
            cell.className = "projection"
            cell.style.height = "40px"
            cell.innerHTML = ""
            column.appendChild(cell) 
        }
    }
    */
}