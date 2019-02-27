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
        dataType: 'json',
        success: function (msg) {
            if (msg) {
                // alert("Somebody" + name + " was added in list !");
                location.reload(true);
            } else {
                alert("Cannot add to list !");
            }
            // get_all_cities();

        }
        // success: function(data) {
        //     alert("success");
        //     console.log(data);
        // }
    })
}

function insert_into_page(cities_list) {
    let cities_var = document.getElementById("allCities");
    cities_list.forEach(element => {
        var elem = document.createElement("li");
        elem.textContent = element;
        cities_var.appendChild(elem)
    });
}

function get_all_cities() {
    $.getJSON(url + "cities", function (data) {
        // console.log(data);
        insert_into_page(data['Cities'])
    });
}

$(document).ready(function(){
    get_all_cities();
})