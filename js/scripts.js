// # GET: fetch an existing resource.The URL contains all the necessary information the server needs to locate and return the resource.
// # POST: create a new resource.POST requests usually carry a payload that specifies the data for the new resource.
// # PUT: update an existing resource.The payload may contain the updated data for the resource.
// # DELETE: delete an existing resource.

url = "http://0.0.0.0:8080/"


function form_submission(event) {
    event.preventDefault();
    new_city = $("#new-city-name")[0];
    form = $("#new-city")[0];
    data = {
        "name": new_city.value
    }
    $.ajax({
        url: url+"add_city",
        type: "POST",
        data: data,
        dataType: 'jsonp',
        success: function(data) {
            alert("success");
        }
    })
}
function get_all_cities() {
    $.ajax({
        url: url + "cities",
        type: "GET",
        dataType: 'application/json',
        success: function (data) {
            console.log(data);
        }
    });
}

$(document).ready(function(){
    get_all_cities();
})