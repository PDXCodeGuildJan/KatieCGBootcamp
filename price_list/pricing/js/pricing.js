// Establish the event listener for when thet click an item
// Add the click event handler in the "add-item button"

var addItemButton = document.getElementById("add-item");
addItemButton.onclick = addItem;

var addStockButton = document.getElementById("add-stock");
addStockButton.onclick = addStock;

var removeStockButton = document.getElementById("remove-stock");
removeStockButton.onclick = removeStock;

var products = [];

/**
 * Add the item in the text fields to the inventory
 * list, which is stored inside the table body (id="inventory")
 **/
function addItem() {
	var materialName = document.getElementById("name").value;
	var price = document.getElementById("price").value;
	// Get whether or not the checkbox has been checked
	var inStock = document.getElementById("in-stock").checked;


	// Create a new instance of the Product
	// object with the new Item's info

	var newProd = new Product(materialName, price, inStock);
	products.push(newProd);

};

/** 
 * Adds all the items in the products array to
 * the HTML.
 **/ 
function displayInventory() {

// Loop through the products array, adding each Products
// to the inventory table in the HTML
	for (var i = 0; i < products.length; i++) {
		// Make a new row for product i
		var rewRow = document.createElement("TR");

		// Make a TD for the checkbox
		var checkbow = document.createElement("TD");

		// Make a TD for the material name
		var matName = document.createElement("TD");
		matName.textContent = products[i].prodName;

		// Make a TD for the price
		var price = document.createElement("TD");
		price.textContent = products[i].price;

		// Make a TD for the stock toggle
		var inStock = document.createElement("TD");
		inStock.textContent = (function(inStock) {
			if (inStock) {
				return "Yes";
			}
			return "No";
		}(products[i].inStock]));

	};

}


/**
 * Toggles the inStock status on the selected
 * rows inside of the inventory to "No"
 * Use querySelectorAll()
 **/
function removeStock() {
	// Get all checked stock boxes 
	var getRemoveBoxes = document.querySelectorAll("tbody > tr >td > input:checked");


	for (var i = 0; i < getRemoveBoxes.length; i++) {
		var status = getRemoveBoxes[i].parentNode.parentNode.children[3];

		status.textContent = "No";

		status.className = "false";
	};
};

/**
 * Toggles the inStock status on the selected 
 * rows inside of inventory to "Yes"
 **/
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


/**
 * Constructor for the Product object 
 **/
 function Product(name, price, inStock) {
 	this.prodName = name;
 	this.price = price;
 	this.inStock = inStock

 	this.setStock = function(stock){
 		this.inStock = stock;
 	} 

 }



