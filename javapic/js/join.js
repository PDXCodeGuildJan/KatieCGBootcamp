/** 
 * Objectives:
 * PAGE 247 IN BOOK HAS A TON OF FORM EVENTS
 * PAGE 249 IN BOOK HAS A GREAT FORM EXAMPLE
 * 1. Add form validation that works in all major browsers (you'll need to deactivate browser validate to check this)
 * 2. Form validation should have all fields marked "required" required, and all email fields should 
 *    require and check for proper email syntax.
 * 3. Any validation errors should be presented clearly to the user so that they may correct them
 * 4. On completion of the form, navigate the user to the gallery, passing their name to the page
 **/

 /** 
  * ID's, Classes, etc.:
  *
  * 1. <section class="signup">
  * 2. <form id= "signup">
  * 3. <input id= submit>
  **/


  // Form Element 572

  // List of Form Controls 573


function removeFormVal() {
	// alert("I have been added!")
	document.getElementById("signup").noValidate = true;

};

function formSubmit() {

	// Ensure that all three fields of the form (name, username, and e-mail) have been 
	// correctly added and formatted

	// If they have been, submit form & move on to the gallery page!

};

function addName() {
	
	// Retrieve information from user when name has been added to the correct form field
	var name = document.forms["signup"]["name"].value
	console.log("name")

	
	
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
	// If username field is empty
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
	
	/*
	^ outside of brackets = start at very beginning of the string
	^ inside of brackets = everything we DONT want
	\s = space 
	+ = one or more of these characters
	$ = end at the dollar sign
	regex: /^[^@\s]+@[^@\s]+\.[^@\s]+$/

	*/

	// If so, 
	// return true

	// If not, 
	// Notify user of incorrect e-mail input
	// return false

};



removeFormVal()
addName()
addUsername()