// frappe.ready(function() {
// 	// Example: Set the session user to the user field when the page is ready
// 	var sessionUser = "{{ user }}";
// 	$('input[data-fieldname="user"]').val(sessionUser);

// 	var project_name = "{{ project_name }}";
// 	alert(project_name);
// 	$('input[data-fieldname="project"]').val(project_name);
// 	// $('select[data-fieldname="project"]').val(project_name);
// 	// $('select[data-fieldname="project"]').trigger('change');


// 	// Example: Alert the session user when the page is ready
// 	// alert("Hello, " + sessionUser + "! The page is ready.");

// 	// You can bind events, manipulate the DOM, or perform other actions here
// });


frappe.ready(function() {
    
    // Example: Set the session user to the user field when the page is ready
    var sessionUser = "{{ user }}";
    $('input[data-fieldname="user"]').val(sessionUser);

    var customerName = "{{ customer_name }}"; // Use a single variable for customer name

    // Set the customer name in the input field
    $('input[data-fieldname="customer"]').val(customerName);

    var projectNames = "{{ project_name }}".split(','); // Split the project names by comma
    var projectDropdown = $('select[data-fieldname="project"]');

    // Clear existing options in the dropdown
    projectDropdown.empty();

    // Add each project name as an option to the dropdown
    for (var i = 0; i < projectNames.length; i++) {
        var projectName = projectNames[i].trim(); // Remove leading/trailing whitespaces
        projectDropdown.append('<option value="' + projectName + '">' + projectName + '</option>');
    }
    // You can bind events, manipulate the DOM, or perform other actions here
});
