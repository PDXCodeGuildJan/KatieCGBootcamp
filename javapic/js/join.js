/**
 * Remove the automatic validation built-in on some browsers
 **/
function removeFormVal() {
// Remove the automatic form validation
var signUp = document.getElementById("signup").noValidate = true;
}

/**
 * Submit form once every field has been correct filled in
 **/
function formSubmit(event) {
	// Prevent the form from reverting back to the default setting
	event.preventDefault()

	// If all fields have been filled in correctly
	if (addName() == true && addUsername() == true && addEmail() == true) {
		// Call the gallery.html page! Success!
		window.location="gallery.html";
	};

};

/**
 * Add name to name field of the login page
 **/
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

/**
 * Add username to username field of the login page
 **/
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

/**
 * Add e-mail to username field of the login page. Check e-mail validity using RegEx
 **/
function addEmail() {
	
	// Retrieve information from user when the e-mail has been added to the correct form field
	var email = document.forms["signup"]["email"].value

	// Using regex, affirm that the e-mail given is a valid one 
	if (/^[^\s@]+@[^\s\.@]+\.[^\s\.@]+$/.test(email)) {
		return true;
	} else {
	// If the input is not a valid email
	alert("Please ensure you have added a correct e-mail before resubmitting form.");
	return false;
	};
};

/*----------------------- 
EVENT LISTENERS AND CALLS*/
document.getElementById("signup").addEventListener("submit", formSubmit, true);
removeFormVal()
/*-----------------------*/
