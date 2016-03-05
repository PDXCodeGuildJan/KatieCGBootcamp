/** 
* Objectives:
*
* 1. Update the slogan to add a ", user_name", with the user's name
* X 2. Loop through the image folder and display each image in the folder
* X 3. Add the functionality so that if a user clicks on an image, the lightbox appears with that image loaded in
* X 4. When the lightbox is up, is the user clicks anywhere not on the image, the lightbox closes
*
**/

// page 391 for loading name???

/* ----------------------------------------- */

// function addName () {
// 	var userName = document.getElementsByClassName("tagline");

// 	var newTagline = userName + "your FACE";

// 	console.log("Your FACE");

// }

/**
 * Loop through a file of pictures to display photos in a grid form
 **/
function galleryDisplay() {
 	// Create var imageGrid to grab and store the Id "gallery"
	var imageGrid = document.getElementById("gallery");

	// Init var imageIndex to loop through to display each 
	var imageIndex = 1
	// var imageList begins the <ul> to eventually store each <li>, or each photo
	var imageList = "<ul>"
	// Init var imageGallery to an empty string. We will use this for each photo we loop through
	var imageGallery = "";
	// While there are still photos to loop through...
	while (imageIndex <= 60) {

		if (imageIndex <= 9) {
			// Add a "0" to each image index
			imageGallery = "<li><img src='images/pdxcg_0" + imageIndex + ".jpg' /></li>"
		// If/When the imageIndex is 42
		} else if (imageIndex === 42) {
			// Skip that photo entirely (because it does not exist.)
			imageGallery = ""
		
		} else {
			// Concatinate the image index to the img src tag
			imageGallery = "<li><img src='images/pdxcg_" + imageIndex + ".jpg' /></li>"			
		};

	imageList += imageGallery;
	imageIndex ++
	};
	// Append a closing </ul> after each photo has been looped through to finish the <ul>
	imageList += "</ul>"
	imageGrid.innerHTML = imageList


};

/*----------------------- 
EVENT LISTENERS*/
// Create an event listener for the gallery Id. Every time it is clicked, call imageEnlarge
document.getElementById("gallery").addEventListener("click", imageEnlarge);
// Create an event listener for the image_show Id. Every time it is clicked, call imageRevert
document.getElementById("image_show").addEventListener("click", imageRevert);
/*-----------------------*/

/**
 * Enlarge a photo when it has been clicked
 **/
function imageEnlarge(event) {
	// If the IMG has been clicked
	if (event.target.nodeName === "IMG") {
		// init var enlargePhoto to grab and store Id "image_show"
		var enlargePhoto = document.getElementById("image_show");
		// The id image_show's className will be switched to "display_img"
		// to display the enlarged photo
		enlargePhoto.className = "display_img";

		// Target the img src inside of the div
		enlargePhoto.firstChild.src = event.target.src;
	};

};

/**
 * Make the enlarged photo disappear, reverting back to the gallery display
 **/
function imageRevert() {
	// If the anywhere but the IMG has been clicked
	if (event.target.nodeName != "IMG") {
		// init var revert to grab and store Id "image_show"
		var revert = document.getElementById("image_show");
		// The id image_show's className will be switched to "display_none"
		// Only if the background has been clicked
		revert.className = "display_none";
	};

};
// Load the gallery page
window.addEventListener("load", galleryDisplay);











