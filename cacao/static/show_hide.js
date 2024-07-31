/* SHOW & HIDE QUESTIONS */

const START = document.getElementById('the_start');
const WHY = document.getElementById('result_why');
const QUANTITY = document.getElementById('result_quantity');
const PRICE = document.getElementById('result_price');
const BUDGET = document.getElementById('result_budget');
const CONTENT = document.getElementById('result_content');
const RESULT = document.getElementById('the_result');
const POPULAR = document.getElementById('popular');


function show_why(event){
	
	START.classList.add('hide');
	WHY.classList.remove('hide');
}
function show_quantity(event){
	WHY.classList.add('hide');
	QUANTITY.classList.remove('hide');
}
function show_price(event){
	QUANTITY.classList.add('hide');
	PRICE.classList.remove('hide');
}
function show_budget(event){
	PRICE.classList.add('hide');
	BUDGET.classList.remove('hide');
}
function show_content(event){
	BUDGET.classList.add('hide');
	CONTENT.classList.remove('hide');
}
function show_result(event){
	CONTENT.classList.add('hide');
	RESULT.classList.remove('hide');
}

function show_popular(event){
	POPULAR.classList.remove('hide');
}
