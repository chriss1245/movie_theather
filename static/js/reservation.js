const OPEN_HOUR = 9; // hour at which the movie theather opens
const HOUR_SIZE = 40; // size in pixeles of each hour

let g_extra_weeks = 0; // how many weeks on the future the customer wants to see projections
let g_src_url = window.location.href + '/projections'; // data url for requesting the data

// html elements
let next_week_btn = document.getElementById("next_week");
let prev_week_btn = document.getElementById("previous_week");
let projection_details = document.getElementById("reservation_details")
let reservation_form = {
    projection_id: document.getElementById("movie_projection_id"),
    button: document.getElementById("reserve_button")
}

// Main buttons behavior
reservation_form.button.disabled = true;
next_week_btn.onclick = function ()
{
    g_extra_weeks += 1;
    request_movie_projections();
    if (g_extra_weeks > 0)
        prev_week_btn.disabled = false;
}
prev_week_btn.onclick = function ()
{
    g_extra_weeks -= 1;
    request_movie_projections();
    if (g_extra_weeks < 1)
        prev_week_btn.disabled = true;
}


let request_movie_projections = function()
{
    /*
        Makes a request to the server for movie projections for the current week
        plus the number of extra weeks specified.
    */
    let initial_date = new Date();
    let params = "?";
    let xmlhttp = new XMLHttpRequest()

    params += "date=" + initial_date.getDate();
    params += "&month=" + (initial_date.getMonth() + 1);
    params += "&year=" + initial_date.getFullYear();
    params += "&hour=" + initial_date.getHours();
    params += "&minute=" + initial_date.getMinutes();
    params += "&extra_weeks=" + g_extra_weeks;
    
    // Http request
    xmlhttp.onload = function ()
    {
        days = JSON.parse(this.responseText);
        set_projections(days);
    }
    xmlhttp.open("GET", g_src_url + params , true)
    xmlhttp.send(params);
}
request_movie_projections(); // fetch the data from the server


// Called when click in a movie projection cell. Displays information about the movie projection
let show_reservation = function (ev)
{   
    cell = ev.target
    reservation_form.button.disabled = false;
    reservation_form.projection_id.value = cell.projection.id;

    while(projection_details.lastChild)
        projection_details.removeChild(projection_details.lastChild);
    var p = document.createElement("p");
    p.innerHTML = '<b>Date:</b> <br>' + cell.projection.month + " " +  cell.projection.day + ', ' + cell.projection.year;
    projection_details.append(p);
    p = document.createElement("p");
    if (cell.projection.min == 0)
    p.innerHTML = "<b>Hour:</b> " + cell.projection.hour + ":00"
    else
        p.innerHTML = "<b>Hour:</b> " + cell.projection.hour + ":" + cell.projection.min;
    projection_details.append(p);
    p = document.createElement("p");
    p.innerHTML = "<b>Screen:</b> " + cell.projection.screen;
    projection_details.append(p);

}

let set_projections = function (days)
{
    /*
        Allocates the movie projections on the schedule
    */
    /*
    Expected response
    days={  0:[{hour:11, min:3, duration:2, duration_min:23, title:"joker", id:2, day:23, month:"October", year:2021}, {hour:12, min:30, duration:2, duration_min:0,title:"joker", id:1}],
            1:[{hour:12, min:23, duration:2, duration_min:12 ,title:"joker", id:2}],
            2:[{hour:12, min:25, duration:2, duration_min:10,title:"joker", id:1}],
            3:[{hour:16, min:50, duration:2, duration_min:5,title:"joker", id:1}],
            4:[{hour:12, min:23, duration:2, duration_min:50,title:"joker", id:1}],
            5:[{hour:18, min:23, duration:2, duration_min:50,title:"joker", id:1}],
            6:[{hour:12, min:0, duration:2, duration_min:12,title:"joker", id:1}]
        }
    */
    for (d in days)
    {
        var day = days[d];
        
        var offset_row = 0
        var column = document.getElementById(d + '');

        // removes all the elements that were before at the column of the day
        while(column.childElementCount > 1)
                column.removeChild(column.lastChild);
        for (p in day) // for each projection
        {
            projection = day[p]
            var row = (projection.hour - OPEN_HOUR) % 24; // defines a row for the hour, the hour of each projection is greater than OPEN_HOUR

            // Fills all the not needed rows before of the projection row
            for (var r=offset_row; r<row; r++)
            {
                cell = document.createElement('div');
                cell.className = "projection"
                cell.style.height = "40px"
                cell.innerHTML = ""
                column.appendChild(cell)
            }
            // if row is greater than offset_row the movie projections do not overlap
            if (row >= offset_row)
            {
                // Creates a new cell with a height proportional to the minute of beggining of the movie
                cell = document.createElement('div');
                cell.className = "projection"
                cell.style.height = Math.round(projection.min*40/60,0) + "px"
                cell.innerHTML = ""
                column.appendChild(cell)
                
                // Computes how many 40px rows is going to use the movie projection
                var rows_used = projection.duration + Math.ceil((projection.duration_min+projection.min)/60, 0)

                // Adds the movie projection
                cell = document.createElement('div');
                cell.className = "projection"
                cell.style.backgroundColor = "red";
                cell.style.height =  projection.duration * 40 + Math.round(projection.duration_min * 40 / 60, 0) + "px";
                cell.style.backgroundClip= "content-box"

                // Makes that minutes apper in format 00 if needed
                if (projection.min == 0)
                    var minutes = '00';
                else
                    var minutes = projection.min + '';

                cell.innerHTML = "Screen: " + projection.screen + "<br>At: " + projection.hour + ":" + minutes;
                cell.id="d" + d + "p" + p;
                cell.day = column.firstChild.innerHTML;
                cell.projection = projection;
                cell.onclick = function(ev){show_reservation(ev)}
                column.appendChild(cell)

                // Creates a cell with heigqht proportional to the minutes left for completing an hour at the last used cell
                cell = document.createElement('div');
                cell.className = "projection"
                cell.style.height = 40 - (Math.round(projection.duration_min*40/60, 0) + Math.round(projection.min*40/60,0)) % 41 + "px" 
                column.appendChild(cell)

                offset_row = row + rows_used;
            }
            else // the projections overlap
            {
                // rows used for the movie projection (diferent hours)
                var rows_used = projection.duration + Math.round((projection.duration_min+projection.min)/60, 0)

                // data regarding with last cell (the one that fills the reamining minutes for completing an hour)
                last_cell = column.lastChild;
                var last_height = parseInt(last_cell.style.height.replace("px", ""));
                // recalculates the height of the last cell
                var new_height  = (last_height - Math.round(projection.min*40/60,0) )+ 'px'; 
                var extra = 0;
                // removes the cell if the new height is smaller than 1
                if (new_height > 0)
                    last_cell.style.height = new_height;
                else
                    last_cell.remove()

                //projection cell
                cell = document.createElement("div")
                cell.className = "projection"
                cell.style.backgroundColor = "blue";
            
                cell.style.height =  (row - offset_row  + rows_used)*40 + Math.round((projection.duration_min)*40/60 , 0) + "px";
                cell.style.backgroundClip= "content-box"
                cell.innerHTML = "Screen: " + projection.screen + "<br>At: lolito" + projection.hour + ":" + projection.min;
                cell.day = column.firstChild.innerHTML;
                cell.projection = projection;
                cell.onclick = function(ev){show_reservation(ev)}
                column.appendChild(cell)

                // cell for completing the row
                cell = document.createElement('div');
                cell.className = "projection"
                cell.style.height = 40 - (Math.round(projection.duration_min*40/60, 0) + Math.round(projection.min*40/60,0)) % 41 + rows_used + "px" 
                column.appendChild(cell)

                offset_row = row + rows_used;
            }
        }

        // After setting all the movie projections, fill the rest of the hours with cells
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