////////////////////////////
///
///		Only the check box table
///

/// toggle all check box
function toggle_check_box_all(source) {
	var remember = document.getElementById('checkBoxAll');
    checkboxes = document.getElementsByName('select_ref');
    for(var i=0, n=checkboxes.length;i<n;i++) {
		checkboxes[i].checked = remember.checked;
	}
    
    // disable/enable the check submit
    if (remember.checked){
		$("#id_submit_checked").removeAttr("disabled");
	}
	else{
		$("#id_submit_checked").attr("disabled", "disabled");
	}
    
	$.ajax({
		url: $('#table_with_check_id').attr("set-check-box-values-url"),
		data : { check_box_all : remember.checked }, // data sent with the post request
		success: function (data) { },
	});
};

/// add function to toggle the checkbox in tables
/// set the Listener and get the checked in the server, and set the box check in the client
$(document).ready(function(){
	var element = document.getElementById("checkBoxAll");
	if (element === null) return;
	
	element.addEventListener ("click", toggle_check_box_all, false);
	var elements = document.getElementsByName("select_ref");
	for(var i = 0, n = elements.length; i < n; i++){
		elements[i].addEventListener('click', toggle_check_box, false);
	}
	
	/// set the 'check_box_all' true or false
	var check_box_all_session = $('#table_with_check_id').attr("check_box_all");
	if (check_box_all_session == "True" ){
		element.checked = true;
		checkboxes = document.getElementsByName('select_ref');
    	for(var i=0, n=checkboxes.length;i<n;i++) {
    		checkboxes[i].checked = element.checked;
		}
	}
	else element.checked = false;

	// get all checked in the server
	$.ajax({
		url: $('#table_with_check_id').attr("set-check-box-values-url"),
		data : { get_check_box_single : '1' }, // data sent with the post request
		success: function (data) {
			var count = 0;
			for (key in data){
				if (key === 'is_ok'){ continue; }
				var remember = document.getElementById(key);
				if (remember != null){
					remember.checked = data[key];
				}
				
				if (data[key]){
					count += 1;
				}
			}
			// disable/enable the check submit
			if (count > 0) $("#id_submit_checked").removeAttr("disabled");
			else $("#id_submit_checked").attr("disabled", "disabled");
		},
	});
	 
});


/// set the master checked box in the server
function toggle_check_box(source) {
	var element = document.getElementById("checkBoxAll");
	if (element === null) return;
	element.checked = false;

	$.ajax({
		url: $('#table_with_check_id').attr("set-check-box-values-url"),
		data : { check_box : source.srcElement.checked,
				 value : source.srcElement.value }, // data sent with the post request
		success: function (data) { },
	});
};


// if the user pressed the 
//$('#id_add_all_checked').on('submit', function (e) {
//    $.ajax({
//		url: $('#table_with_check_id').attr("set-check-box-values-url"),
//        data : { count_check_boxes : '1' }, // data sent with the post request
//		success: function (data) {
//			if (data['count_check_boxes'] < 1){
//				alert('There is no samples selected.\nPlease, for this option select some samples.');
//				e.preventDefault();
//			}
//		},
//		// handle a non-successful response
//        error : function(xhr,errmsg,err) {
//            alert(errmsg);
//        },
//	});
//	return false;
//});


///
///		END Only the check box table
///
////////////////////////////