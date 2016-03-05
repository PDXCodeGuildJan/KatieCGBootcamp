// * 
//  * Objectives:
//  * PAGE 247 IN BOOK HAS A TON OF FORM EVENTS
//  * PAGE 249 IN BOOK HAS A GREAT FORM EXAMPLE
//  * 1. Add form validation that works in all major browsers (you'll need to deactivate browser validate to check this)
//  * 2. Form validation should have all fields marked "required" required, and all email fields should 
//  *    require and check for proper email syntax.
//  * 3. Any validation errors should be presented clearly to the user so that they may correct them
//  * 4. On completion of the form, navigate the user to the gallery, passing their name to the page
//  *



function removeFormVal() {
// Remove the automatic form validation
var signUp = document.getElementById("signup").noValidate = true;
}

function formSubmit(event) {
	// Prevent the form from reverting back to the default setting
	event.preventDefault()


	if (addName() == true && addUsername() == true && addEmail() == true) {
		window.location="gallery.html";
	}

};

function addName() {
	
	// Retrieve information from user when name has been added to the correct form field
	var name = document.forms["signup"]["name"].value
	// console.log("name")

	
	
	if (name == null || name == "") {
		// Notify user of missing field
		alert("Please ensure you have added your name before resubmitting form.");
		// return false
		return false;

	}
	// If name has been added,
	// return true
	return true;

};

function addUsername() {
	
	// Retrieve information from user when the username has been added to the correct form field
	var userName = document.forms["signup"]["username"].value
	// Check form to make sure the field isn't empty
	// If it is:
	if (userName == null || userName == "") {
		// Notify user of missing field
		alert("Please ensure you have added a username before resubmitting form.")
		// return false
		return false;
	}
	
	// If username has been added,
	// return true
	return true;

};

function addEmail() {
	
	// Retrieve information from user when the e-mail has been added to the correct form field
	var email = document.forms["signup"]["email"].value

	// Using regex, affirm that the e-mail given is a valid one 
	// var inputEval = /^[^@\s]+e+$/.test(email);
	// If the input is a valid email
	if (/^[^\s@]+@[^\s\.@]+\.[^\s\.@]+$/.test(email)) {
		return true;
	} else {
	// If the input is not a valid email
	alert("Please ensure you have added a correct e-mail before resubmitting form.");
	return false;
	};
};

/*----------------------- 
EVENT LISTENERS*/
document.getElementById("signup").addEventListener("submit", formSubmit, true);
removeFormVal()
/*-----------------------*/
