/* Fruit Search filtering logic */

const input = document.querySelector('#fruit');
const suggestions = document.querySelector('.suggestions ul');

const fruit = ['Apple', 'Apricot', 'Avocado 🥑', 'Banana', 'Bilberry', 'Blackberry', 'Blackcurrant', 'Blueberry', 'Boysenberry', 'Currant', 'Cherry', 'Coconut', 'Cranberry', 'Cucumber', 'Custard apple', 'Damson', 'Date', 'Dragonfruit', 'Durian', 'Elderberry', 'Feijoa', 'Fig', 'Gooseberry', 'Grape', 'Raisin', 'Grapefruit', 'Guava', 'Honeyberry', 'Huckleberry', 'Jabuticaba', 'Jackfruit', 'Jambul', 'Juniper berry', 'Kiwifruit', 'Kumquat', 'Lemon', 'Lime', 'Loquat', 'Longan', 'Lychee', 'Mango', 'Mangosteen', 'Marionberry', 'Melon', 'Cantaloupe', 'Honeydew', 'Watermelon', 'Miracle fruit', 'Mulberry', 'Nectarine', 'Nance', 'Olive', 'Orange', 'Clementine', 'Mandarine', 'Tangerine', 'Papaya', 'Passionfruit', 'Peach', 'Pear', 'Persimmon', 'Plantain', 'Plum', 'Pineapple', 'Pomegranate', 'Pomelo', 'Quince', 'Raspberry', 'Salmonberry', 'Rambutan', 'Redcurrant', 'Salak', 'Satsuma', 'Soursop', 'Star fruit', 'Strawberry', 'Tamarillo', 'Tamarind', 'Yuzu'];

input.addEventListener("input", search);
window.addEventListener("DOMContentLoaded", loadlist);

function loadlist(){
	let temp = `<ul class="list-item">`
	fruit.forEach((item) => {
		temp += `<li class="list-item"> ${item} </li>`; 
	});
	temp += '</ul>';

	suggestions.innerHTML = temp;
};

function search(str) {
	let temp = '';
	const val = fruit.filter((fruits)=> 
	fruits.toLowerCase().includes(str.target.value.toLowerCase()))
	
	if(val.length>0){
		temp = `<ul class="list-items">`
	val.forEach((item) => {
		temp += `<li class="list-item"> ${item} </li>`; 
	});
	temp += '</ul>';
}else{
	temp = `<div class="no-item"> No Item Found </div>`;
}
suggestions.innerHTML = temp;
}
 


document.addEventListener("click", Usesuggestion);

function Usesuggestion(){
	input.value = this.innerHTML;
	
}



/*function loadlist(){
	let temp = '<ul class="list-item">'
	fruit.forEach((item) => {
		temp += '<li class="list-item"> ${item} </li>'; 
	});
	temp += '</ul>';

	output.innerHTML = temp
}*/

/*
function searchHandler(e) {
	// TODO
}

/*function showSuggestions(results, inputVal) {
	return results.filter((el)=>
	el.toLowerCase().includes(inputVal));
}


input.addEventListener('keyup', searchHandler);
suggestions.addEventListener('click', useSuggestion)*/