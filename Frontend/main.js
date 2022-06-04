var visitorCounterContainer = document.getElementById("counter");

/**
 * Retrieving visitor count -- use this variable in the future to get count from the database 
 * For now lets use this variable for local storage 
**/

var visitCount = localStorage.getItem("page_view");

//use if to check if page_view entry is present 
if(visitCount){
    visitCount = Number(visitCount) + 1;
    localStorage.setItem("page_view", visitCount);
}
else{ 
    visitCount = 1;
    localStorage.setItem("page_view",1);
}
visitorCounterContainer.innerHTML = visitCount;

