/* 
 * Objectives:
 * PAGE 247 IN BOOK HAS A TON OF FORM EVENTS
 * PAGE 249 IN BOOK HAS A GREAT FORM EXAMPLE
 * 1. Add form validation that works in all major browsers (you'll need to deactivate browser validate to check this)
 * 2. Form validation should have all fields marked "required" required, and all email fields should 
 *    require and check for proper email syntax.
 * 3. Any validation errors should be presented clearly to the user so that they may correct them
 * 4. On completion of the form, navigate the user to the gallery, passing their name to the page
 * 
 */

 /* 
  * ID's, Classes, etc.:
  *
  * 1. <section class="signup">
  * 2. <form id= "signup">
  * 3. <input id= submit>
  *
  */


function removeFormVal() {

	var validation = document.getElementById("signup");
	ValidatorEnable(validation, false);
}
