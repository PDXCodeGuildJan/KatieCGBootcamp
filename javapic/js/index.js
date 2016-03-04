/* 
 * Objectives:
 * 
 * X 1. Have the background image of the jumbotron change to another image in the folder every 10 seconds
 *  2. Make sure the toe photo does not show up anymore
 */

// Init the var imageIndex to start at one so the jumbotron loops through each photo
var imageIndex = 1;

/**
 * Create a jumbotron to loop through each photo every ten seconds
 **/
function jumboTron() {
  // Init var jumbo to grab and store Id "jumbotron"
	var jumbo = document.getElementById("jumbotron");
    // If the photo index is <= 9
  	if (imageIndex <= 9) {
  		// The background image of the id "jumbotron" will display each photo
      jumbo.style.backgroundImage = "url('images/pdxcg_0" + imageIndex + ".jpg')";
  		// Increment by one to continute looping through
      imageIndex += 1;
    // If the photo index is >= 10 and the imageIndex is not 42
  	} else if (imageIndex >= 10 && imageIndex != 42) {
  		// The background image of the id "jumbotron" will dispaly each photo
      jumbo.style.backgroundImage = "url('images/pdxcg_" + imageIndex + ".jpg')";
  		// Increment by one to continue looping through
      imageIndex += 1;

  	} else {
      // This is so the jumbotron skips over the missing #42 photo
      // It replaces the black screen with the default photo
      // Not perfect, but it fails gracefully!
  		jumbo.style.backgroundImage = "";
  		// Increment by one to continue looping through
  		imageIndex += 1;
  	};
    // To stop the "loop", if the imageIndex is >= 61
  	if (imageIndex >= 61) {
      // Start the "loop" over!
  		imageIndex = 1;
  	};

 };
// Sets the jumbotron to display & change photo every 10 seconds!
window.setInterval(jumboTron, 10000);
