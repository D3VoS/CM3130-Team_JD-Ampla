$(document).ready(function(){
    const calendar = document.querySelector("#app-calendar");

    var d = new Date();
    var currentMonth = d.getMonth(); // Actual Month
    var currentYear = d.getFullYear(); // Actual Year
    var currentDate = d.getDate();

    let days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
    let months = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"];

    function getNoOfDaysInMonth(month, year){ // Gets the number of days in the month
        return new Date(year, month + 1, 0).getDate(); 
    }

    function getFirstDayOfMonth(month, year){
        return new Date(year, month, 1).getDay();
    }

    var calculatedMonth = currentMonth; //Extra Months
    var calculatedYear = currentYear; //Extra Years
    
    function getHeading(){
        $("#heading").html(`${months[calculatedMonth] + " " + calculatedYear}`) // Creates the title
    }
    
    function getCalendar(){
        $(".calendarDates").empty();

        for (let weekday = 1; weekday <= getFirstDayOfMonth(calculatedMonth, calculatedYear); weekday++){
            $(".calendarDates").append(`<div class = "spacer"></div>`);
        }

        $('div.spacer:last').css({
            'border-right': '3px solid #001e57'
        })
        
        for (let day = 1; day <= getNoOfDaysInMonth(calculatedMonth, calculatedYear); day++){

            if (currentDate == day && currentMonth == calculatedMonth && currentYear == calculatedYear){
                $(".calendarDates").append(`<div class = "day" id = "today" >${day}</div>`); //Marked for today for separate css 
            }
            else{
                $(".calendarDates").append(`<div class = "day">${day}</div>`);
            }
            
        }
    }
    
    getHeading();
    getCalendar();

    var deviation = 0;
    
    $("#next").click(function(){
        
        if (calculatedMonth >= 11 && deviation < 12){ // If the person goes over 12 months, it adds 1 to the year and resets the month
            calculatedMonth = 0;
            calculatedYear++;
            getHeading();
            getCalendar();
            deviation++;
        }
        else if (deviation < 12){
            calculatedMonth++;
            getHeading();
            getCalendar();
            deviation++;
        }
    });
    $("#previous").click(function(){
        if (calculatedMonth <= 0 && deviation > -12 ){ //Reverse of #next function
            calculatedMonth = 11;
            calculatedYear--;
            getHeading();
            getCalendar();
            deviation--;
        }
        else if (deviation > -12){
            calculatedMonth--;
            getHeading();
            getCalendar();
            deviation--;
        }
    });
    
});
