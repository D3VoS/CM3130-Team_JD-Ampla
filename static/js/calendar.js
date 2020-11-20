$(document).ready(function(){
    const calendar = document.querySelector("#app-calendar");

    var d = new Date();
    var currentMonth = d.getMonth(); // Actual Month
    var currentYear = d.getFullYear(); // Actual Year
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
        
        for (let day = 1; day <= getNoOfDaysInMonth(calculatedMonth, calculatedYear); day++){
            $(".calendarDates").append(`<div class = "day">${day}</div>`);
        }
    }
    
    getHeading();
    getCalendar();
    
    $("#next").click(function(){
        
        if (calculatedMonth >= 11){ // If the person goes over 12 months, it adds 1 to the year and resets the month
            calculatedMonth = 0;
            calculatedYear++;
            getHeading();
            getCalendar();
        }
        else{
            calculatedMonth++;
            getHeading();
            getCalendar();
        }
    });
    $("#previous").click(function(){
        if (calculatedMonth <= 0){ //Reverse of #next function
            calculatedMonth = 11;
            calculatedYear--;
            getHeading();
            getCalendar();
        }
        else{
            calculatedMonth--;
            getHeading();
            getCalendar();
        }
    });
    
});
