var csrftoken = Cookies.get('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function ajaxr() {
	$.ajax({
		beforeSend: function(xhr, settings) {
	        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
	            xhr.setRequestHeader("X-CSRFToken", csrftoken);
	        }
    	},
        url: '/monitor_update/',
        data: { 'id': dev_id },
        dataType: 'application/json',
        type:"POST",
        complete: function(data){
        	j = data["responseText"];
        	j = JSON.parse(j)
        	document.getElementById("desired_window").innerHTML = JSON.stringify(j["desired"]["windowOpen"]);
        	document.getElementById("reported_temp").innerHTML = JSON.stringify(j["reported"]["temperature"]);
        	document.getElementById("reported_window").innerHTML = JSON.stringify(j["reported"]["windowOpen"]);
            //document.getElementById("reported_latitude").innerHTML = parseFloat(JSON.stringify(j["reported"]["latitude"]));
            //document.getElementById("reported_longitude").innerHTML = parseFloat(JSON.stringify(j["reported"]["longitude"]));
            dev_lat = parseFloat(JSON.stringify(j["reported"]["latitude"]));
            dev_lon = parseFloat(JSON.stringify(j["reported"]["longitude"]));
        },
        success: function(data){
            // Do something??
        }
    })
}

setInterval(ajaxr, 1000);