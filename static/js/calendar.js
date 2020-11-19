$(document).ready(function(){
    const calendar = document.querySelector("#app-calendar");

    var d = new Date();
    var m = d.getMonth();
    var y = d.getFullYear();

    function getNoOfDaysInMonth(month, year){
        return new Date(year, month, 0).getDate();
    }

    
    
});
