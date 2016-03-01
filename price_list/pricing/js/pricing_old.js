// Establish the event listener for when thet click an item
// Add the click event handler in the "add-item button"

var addItemButton = document.getElementById("add-item");
addItemButton.onclick = addItem;

var addStockButton = document.getElementById("add-stock");
addStockButton.onclick = addStock;

var removeStockButton = document.getElementById("remove-stock");
removeStockButton.onclick = removeStock;

var products = [];

/* Add the item in the text fields to the inventory
 * list, which is stored inside the table body (id="inventory")
 */
function addItem() {
	var materialName = document.getElementById("name").value;
	// console.log(materialName);
	var price = document.getElementById("price").value;
	// console.log(price);

	// Get whether or not the checkbox has been checked
	var inStock = document.getElementById("in-stock").checked;
	// console.log(inStock);



	// var invetory is assigned to the id "inventory"
	var inventory = document.getElementById("inventory");
	// var tableEmpty is set to nothing so we can add to the row later
	var tableEmpty = "<td> <input type='checkbox' class='stock' /></td>";
	var tableMarName = "<td>" + materialName + "</td>";
	var tablePrice = "<td>" + price + "</td>";
	// this row will have data from inStock to be displayed as the class
	var tableStock = "<td class='" + inStock + "'>"
	

	// if var inStock is true (In other words, if the box is checked):
	if (inStock == true) {
		// var tableStock will display "yes"
		tableStock += "Yes </td>"
	
	// if var tableStock is anything but true
	} else {
		// var tableStock will display "no"
		tableStock += "No </td>"
	};
	

	// NewTableRow will create a table with the data from the vars above!
	var newTableRow = "<tr>" + tableEmpty + tableMarName + tablePrice + tableStock + "</tr>";

	// displays all data in each row, += allowing to add more than one row!
	inventory.innerHTML += newTableRow;

	// Create a new instance of the Product
	// object with the new Item's info

	var newProd = new Product(materialName, price, inStock);
	products.push(newProd);

};  

/* Toggles the inStock status on the selected
 * rows inside of the inventory to "No"
 * Use querySelectorAll()
 */
function removeStock() {
	// Get all checked stock boxes 
	var getRemoveBoxes = document.querySelectorAll("tbody > tr >td > input:checked");


	for (var i = 0; i < getRemoveBoxes.length; i++) {
		var status = getRemoveBoxes[i].parentNode.parentNode.children[3];

		status.textContent = "No";

		status.className = "false";
	};
};

/* Toggles the inStock status on the selected 
 * rows inside of inventory to "Yes"
 */
function addStock() {

	// Find all selected boxes 
	var getBoxes = document.getElementsByClassName("stock");
	// console.log("this is a list of all boxes: ", getBoxes);
	// Create an empty array to put the checked boxes in
	var boxesChecked = [];
	// for each index in getBoxes...
	for (var i = 0; i < getBoxes.length; i++) {

		if (getBoxes[i].checked) {
			boxesChecked.push(getBoxes[i]);
		}
	}

	for (var i = 0; i < boxesChecked.length; i++) {

		var status = boxesChecked[i].parentNode.parentNode.lastChild;

		status.textContent = "Yes";

		status.className = "true";
	}


};


/* Constructor for the Product object */
 function Product(name, price, inStock) {
 	this.prodName = name;
 	this.price = price;
 	this.inStock = inStock

 	this.setStock = function(stock){
 		this.inStock = stock;
 	} 

 }



