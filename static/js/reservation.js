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



let reserve_now = function()
{
    if (confirm("Reserve?"))
    {
        xmlhttp.open("POST", "reservation");
        // still needs to implement the post
    }
}
// Projections manager
let set_projections = function (days)
{
    
    days={  0:[{hour:11, min:3, duration:2, duration_min:23, title:"joker", id:1}, {hour:12, min:30, duration:2, duration_min:0,title:"joker", id:1}],
            1:[{hour:12, min:23, duration:2, duration_min:12 ,title:"joker", id:1}],
            2:[{hour:12, min:25, duration:2, duration_min:10,title:"joker", id:1}],
            3:[{hour:16, min:50, duration:2, duration_min:5,title:"joker", id:1}],
            4:[{hour:12, min:23, duration:2, duration_min:50,title:"joker", id:1}],
            5:[{hour:18, min:23, duration:2, duration_min:50,title:"joker", id:1}],
            6:[{hour:12, min:0, duration:2, duration_min:12,title:"joker", id:1}]
        }
    
    for (d in days)
    {
        var day = days[d];
        var offset_row = 0

        for (p in day)
        {
            projection = day[p]

            var row = (projection.hour - OPEN_HOUR) % 24;

            column = document.getElementById(d+'');
            for (var r=offset_row; r<row; r++)
            {
                cell = document.createElement('div');
                cell.className = "projection"
                cell.style.height = "40px"
                cell.innerHTML = ""
                column.appendChild(cell)
            }
            if (row >= offset_row)
            {
                // fix minutes
                cell = document.createElement('div');
                cell.className = "projection"
                cell.style.height = Math.round(projection.min*40/60,0) + "px"
                cell.innerHTML = ""
                column.appendChild(cell)
                
                var rows_used = projection.duration + Math.ceil((projection.duration_min+projection.min)/60, 0)
                cell = document.createElement('div');
                cell.className = "projection"
                cell.style.backgroundColor = "red";
                cell.style.height =  projection.duration*40 + Math.round(projection.duration_min*40/60, 0) + "px";
                cell.style.backgroundClip= "content-box"
                cell.innerHTML = "testing";
                cell.onclick=function () {alert('lol')}
                column.appendChild(cell)

                cell = document.createElement('div');
                cell.className = "projection"
                cell.style.height = 40 - (Math.round(projection.duration_min*40/60, 0) + Math.round(projection.min*40/60,0)) % 41 + "px" 
                column.appendChild(cell)
                
                
                console.log(rows_used)
                offset_row = row + rows_used;
            }
            else
            {
                var rows_used = projection.duration + Math.ceil((projection.duration_min+projection.min)/60, 0)
                last_cell = column.lastChild;
                var last_height = parseInt(last_cell.style.height.replace("px", ""));
                var new_height  = (last_height - Math.round(projection.min*40/60,0) )+ 'px';
                var extra = 0;
                if (new_height > 0)
                {
                    last_cell.style.height = new_height;
                }
                else
                {
                    last_cell.remove()
                    extra = rows_used
                }
                cell = document.createElement("div")
                cell.className = "projection"
                cell.style.backgroundColor = "blue";
                cell.style.height =  (row - offset_row  + rows_used)*40 + Math.round((projection.duration_min)*40/60, 0) + "px";
                cell.style.backgroundClip= "content-box"
                cell.innerHTML = "testing";
                cell.onclick=function () {alert('lol')}
                column.appendChild(cell)

                cell = document.createElement('div');
                cell.className = "projection"
                cell.style.height = 40 - (Math.round(projection.duration_min*40/60, 0) + Math.round(projection.min*40/60,0)) % 41 + rows_used + "px" 
                column.appendChild(cell)
                offset_row = row + rows_used;
            }
        }
        for (var r=offset_row; r<16; r++)
        {
            cell = document.createElement('div');
            cell.className = "projection"
            cell.style.height = "40px"
            cell.innerHTML = ""
            column.appendChild(cell)
        }
    }
}