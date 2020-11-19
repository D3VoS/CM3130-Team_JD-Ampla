$(document).ready(function(){
    const calendar = document.querySelector("#app-calendar");

    var d = new Date();
    var m = d.getMonth(); // Actual Month
    var y = d.getFullYear(); // Actual Year
    var day = d.getDay();

    function getNoOfDaysInMonth(month, year){ // Gets the number of days in the month
        return new Date(year, month, 0).getDate();
    }

    function getFirstDayOfMonth(month, year){
        return new Date(year, month, 1).getDay();
    }

    var n = 0; //Extra Months
    var z = 0; //Extra Years
    var yz = y + z //Current Year Selected
    var mn = m + n //Current Month Selected

    noOfDays = getNoOfDaysInMonth(mn, yz);
    weekday = getFirstDayOfMonth(mn, yz)
    
    for (let day = 1; day <= noOfDays; day++){

        

        $(".calendarDates").append( `<div class = "day">${day}</div>`)
        console.log(weekday)
    }
    
    $("#next").click(function(){
        if (mn == 12){ // If the person goes over 12 months, it adds 1 to the year and resets the month
            n = -(m - 1);
            z++;
            mn = m + n;
            yz = y + z
        }
        else{
            n++;
            mn = m + n;
        }
    });
    $("#previous").click(function(){
        if (mn == 1){ //Reverse of #next function
            n = (12 - m);
            z--;
            mn = m + n;
            yz = y + z;
        }
        else{
            n--;
            mn = m + n
        }
    });
    
});
