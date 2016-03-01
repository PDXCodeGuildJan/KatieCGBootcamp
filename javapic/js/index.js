/* 
 * Objectives:
 * 
 * X 1. Have the background image of the jumbotron change to another image in the folder every 10 seconds
 *  2. Make sure the toe photo does not show up anymore
 */

 /* 
  * ID's, classes, etc:
  *
  * 1. <span class= "tagline">
  * 2. <div id= "jumbotron" class= "jumbotron">
  * 3. <div class= "bottom_jumbo">
  *
  */


var imageIndex = 1;

function jumboTron() {
	var jumbo = document.getElementById("jumbotron");
  	console.log(jumbo);

  	if (imageIndex <= 9) {
  		jumbo.style.backgroundImage = "url('images/pdxcg_0" + imageIndex + ".jpg')";
  		imageIndex += 1;

  	} else if (imageIndex >= 10 && imageIndex != 42) {
  		jumbo.style.backgroundImage = "url('images/pdxcg_" + imageIndex + ".jpg')";
  		imageIndex += 1;

  	} else {
  		jumbo.style.backgroundImage = "";
  		
  		imageIndex += 1;
  	}

  	if (imageIndex >= 61) {

  		imageIndex = 1;
  	}


 };


// var imageIndex = 1
window.setInterval(jumboTron, 10000);
// window.addEventListener("load", jumboTron);	