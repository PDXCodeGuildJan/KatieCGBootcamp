/* 
* Objectives:
*
* 1. Update the slogan to add a ", user_name", with the user's name
* X 2. Loop through the image folder and display each image in the folder
* 3. Add the functionality so that if a user clicks on an image, the lightbox appears with that image loaded in
* 4. When the lightbox is up, is the user clicks anywhere not on the image, the lightbox closes
*
*/

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


function addName () {
	var userName = document.getElementsByClassName("tagline");

	var newTagline = userName + "your FACE";

	console.log("Your FACE");



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
			// imageIndex ++
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

window.addEventListener("load", galleryDisplay);











