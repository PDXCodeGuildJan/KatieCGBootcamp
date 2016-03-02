/* 
* Objectives:
*
* 1. Update the slogan to add a ", user_name", with the user's name
* X 2. Loop through the image folder and display each image in the folder
* X 3. Add the functionality so that if a user clicks on an image, the lightbox appears with that image loaded in
* X 4. When the lightbox is up, is the user clicks anywhere not on the image, the lightbox closes
*
*/

// page 391 for loading name???

/* 
 * ID's, classes, etc:
 *
 * 1. <main class= "gallery_page">
 * 2. <span class="tagline">
 * 3. <section id= "gallery" class= "gallery">
 * 4. <div id= "image_show" class= "display_none">
 * 
 */

 /* ----------------------------------------- */


// function addName () {
// 	var userName = document.getElementsByClassName("tagline");

// 	var newTagline = userName + "your FACE";

// 	console.log("Your FACE");

// }
document.addEventListener("click", test)

function test(event) {
	console.log(event.target.nodeName)

}


function galleryDisplay() {
 
	var imageGrid = document.getElementById("gallery");

	
	var imageIndex = 1
	var imageList = "<ul>"
	var imageGallery = "";

	while (imageIndex <= 60) {
		if (imageIndex <= 9) {

			imageGallery = "<li><img src='images/pdxcg_0" + imageIndex + ".jpg' /></li>"
		} else if (imageIndex === 42) {
			imageGallery = ""
		
		} else {

			imageGallery = "<li><img src='images/pdxcg_" + imageIndex + ".jpg' /></li>"			
		};


	imageList += imageGallery;
	imageIndex ++
	// console.log(imageList)
	// console.log(imageGallery) 
	};

	imageList += "</ul>"
	imageGrid.innerHTML = imageList


};

// document.addEventListener("gallery" onclick)
document.getElementById("gallery").addEventListener("click", imageEnlarge);
document.getElementById("image_show").addEventListener("click", imageRevert);

function imageEnlarge(event) {
	console.log(event.target.src);
	console.log("The imageEnlarge is now reporting to the console for duty, ma'am!");
	// get imageEnlarge to display the class "display_img" when a photo is clicked
	// something like (but not syntactically) onlick class = "display_img"?
	if (event.target.nodeName === "IMG") {
		var enlargePhoto = document.getElementById("image_show");
		console.log("Enlarged Photo??: ", enlargePhoto);
		enlargePhoto.className = "display_img";

		// Target the img src inside of the div
		enlargePhoto.firstChild.src = event.target.src;
	};

}

function imageRevert() {
	console.log("The imageRevert is now reporting to the console for duty, your highness!");
	if (event.target.nodeName != "IMG") {

		var revert = document.getElementById("image_show");
		// Only if the background has been clicked...
		revert.className = "display_none";
	};

};

window.addEventListener("load", galleryDisplay);











