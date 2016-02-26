/* 
 * Objectives:
 * 
 * 1. Have the background image of the jumbotron change to another image in the folder every 10 seconds
 *
 */

 /* 
  * ID's, classes, etc:
  *
  * 1. <span class= "tagline">
  * 2. <div id= "jumbotron" class= "jumbotron">
  * 3. <div class= "bottom_jumbo">
  *
  */


  function jumboTron() {

  	var jumbo = document.getElementById("jumbotron");

  	var photoTest = "<img src='images/pdxcg_03.jpg' />"

  	jumbo.innerHTML = photoTest

  };

  window.addEventListener("load", jumboTron)