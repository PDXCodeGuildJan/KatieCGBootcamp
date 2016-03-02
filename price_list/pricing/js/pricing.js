// Establish the event listener for when thet click an item
// Add the click event handler in the "add-item button"

var addItemButton = document.getElementById("add-item");
addItemButton.onclick = addItem;

var addDelItem = document.getElementById("del-item");
addDelItem.onclick = deleteItem;

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

	displayInventory();
};

/** 
 * Adds all the items in the products array to
 * the HTML.
 **/ 
function displayInventory() {
	var inventory = document.getElementById("inventory");
	inventory.innerHTML = "";
// Loop through the products array, adding each Products
// to the inventory table in the HTML
	for (var i = 0; i < products.length; i++) {
		// Make a new row for product i
		var newRow = document.createElement("TR");
		newRow.id = i;

		// Make a TD for the checkbox
		var checkbox = document.createElement("TD");
			// Make the actual checkbox
			var innerCheckBox = document.createElement("INPUT");
			// Set the input type to checkbox
			innerCheckBox.type = "checkbox";
			innerCheckBox.className = "selector";
			// Add the checkbox into the TD
			checkbox.appendChild(innerCheckBox);

		// Make a TD for the material name
		var matName = document.createElement("TD");
		matName.textContent = products[i].prodName;

		// Make a TD for the price
		var price = document.createElement("TD");
		price.textContent = products[i].price;

		// Make a TD for the stock toggle
		var inStock = document.createElement("TD");
		// Set the TD's text content to either yes or now,
		// based on the product at index i's inStock property.
		inStock.textContent = (function(inStock) {
			if (inStock) {
				return "Yes";
			}
			return "No";
		}(products[i].inStock));
		// Set the classs on the TD to the correct class
		inStock.setAttribute("class", products[i].inStock);
	
		// Add all TDs to the TR
		newRow.appendChild(checkbox);
		newRow.appendChild(matName);
		newRow.appendChild(price);
		newRow.appendChild(inStock);

		// Add the row to the table body
		inventory.appendChild(newRow);
	};

};

/**
 * Toggles the inStock status on the selected
 * rows inside of the inventory to "No"
 * Use querySelectorAll()
 **/
function removeStock() {
	// Get all checked stock boxes 
	var getRemoveBoxes = getSelectedRowBoxes();

	// For every index of the length of the array
	for (var i = 0; i < getRemoveBoxes.length; i++) {
		// Using DOM manipulation get a selected checked box in the array 
		var status = getRemoveBoxes[i].parentNode.parentNode.children[3];
		// Change the status to "No"
		status.textContent = "No";
		// Change the class to "false"
		status.className = "false";

		// Update the Product in the products array that 
		// corresponds to the checked checkbox we're updating.
		var prodId = getRemoveBoxes[i].parentNode.parentNode.id;
		products[prodId].inStock = false;

	};
};

/**
 * Toggles the inStock status on the selected 
 * rows inside of inventory to "Yes"
 **/
function addStock() {
	// Get array of selected checkboxes from helper function
	var boxesChecked = getSelectedRowBoxes();
	// for every index of the length of the array
	for (var i = 0; i < boxesChecked.length; i++) {
		// Using DOM manipulation get a selected checkbox in the array
		var status = boxesChecked[i].parentNode.parentNode.lastChild;
		// Change status to "Yes"
		status.textContent = "Yes";
		// And the class is now "true"
		status.className = "true";

		// Update the Product in the products array that 
		// corresponds to the checked checkbox we're updating.
		var prodId = boxesChecked[i].parentNode.parentNode.id;
		products[prodId].inStock = true;

	};

};

/**
 * Delete the selected rows from the inventory.
 **/
function deleteItem() {

	// First, determine all the selected rows
	var selected = getSelectedRowBoxes();


	// Delete the Product objects that correspond
	// to those rows from the products arrays
	for (var i = selected.length -1; i>= 0; i--) {
		// Get the Id on the row the checkbox is in
		var prodId = selected[i].parentNode.parentNode.id;
		// Delete the product at that index (id= index)
		delete products[prodId];
		products.splice(prodId, 1);
	};


	// Render the HTML list, using displayInventory
	displayInventory();

};

/** 
 * Helper function to get all the checked checkboxes in
 * the HTML's inventory
 * Returns: array of selected checkboxes
 **/
function getSelectedRowBoxes () {
	var selected = document.querySelectorAll("tbody > tr >td > input:checked");
	return selected;

};

/**
 * Constructor for the Product object 
 **/
function Product(name, price, inStock) {
	this.prodName = name;
	this.price = price;
	this.inStock = inStock;

	this.setStock = function(stock){
		this.inStock = stock;
 	

	};
};



