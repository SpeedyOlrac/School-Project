/*
	Author: Carlo Gonzalez
	Class: CS 366
	Secion: 1
	Description: CSS Page for Rancid Tomatoes.
		With centered contect box and HTML/CSS checkers. 
-*/

"use strict";

$(document).ready(() => {
	const xyPos = setXY();
	const x = 0;
	const y = 1;
	var xPos = 0;
	var yPos = 0;

	//Sets up the Puzzle area.
	$('#puzzlearea > div').each(function(idx){
		idx++; 
		$(this).css({
    		left: xyPos[idx][x], 
			top: xyPos[idx][y],
			position: 'absolute'
		});

		$(this).attr('id', idx);
		var bgpos = xPos + "px " + yPos + "px";
		$(this).css('backgroundPosition', bgpos );
		xPos -= 100;
		if (xPos == -400){
			xPos = 0;
			yPos -= 100;
		}
	});

	//setup the local Variables
	var emptySq = moveUpate(16);
	const puzzle = $('#puzzlearea').children();
	var curr = [];
	for (var i = 1; i <= 16; i++)
		curr[i] = i;

/* 	-----     Events Handlers	 -----					*/
	/*
		Decs: Adds the Highlighted class to div when mouse over.
			For some reason it doesn't change the border color.
			had to add that manualy
	*/
	puzzle.hover(function() {
			var id = parseInt($(this).attr('id'));
			if (emptySq.includes(id) )
			{
				$(this).addClass("highlighted");
				//not sure why it is not changing the highlighted border color
	  			$(this).css('borderColor', 'red');
	  		}
  		}, function(){
			$(this).removeClass("highlighted");  		
	  		$(this).css('borderColor', 'black');
  		}
  	);

	/*
		Decs: On Mouse Click, if the square in next to the empty
		spot move it
	*/
	puzzle.click(function() { 

		moveBlock($(this));
		if (isCorrect(curr))
			alert("Congratulations! You solved the puzzle!");
	});

	/*
		Decs: When the Shuffle Button is press, 
		shift the board around
	*/

	$("#shufflebutton").on('click', () => {

		print("button");
		var i =0;
		while (i<300){
			var rand = emptySq[parseInt(Math.random() * 4) + 1];
			if (rand <= 16 )
			{
				var name = "#" + rand; 
				moveBlock($(name));
				i++;
			}
		}
	});

	/*
		Desc:   Moves the div that was selected
		Pre: 	A div that is Adjected to the empty square
		Post: 	The Div is move to the new location. Curr, emptysq
				and this.id are updated
	*/
	function moveBlock(_this){

		var id = parseInt(_this.attr('id'));		
		// print(id + ", " + emptySq);
		if (emptySq.includes(id)){
			_this.css({top: xyPos[emptySq[0]][y] + "px" ,
						 left: xyPos[emptySq[0]][x] + "px", 
						   });

			_this.attr('id', emptySq[0]);
			emptySq = moveUpate(id);
			curr[_this.attr('id')] = curr[emptySq[0]];
			curr[emptySq[0]] = 16;
		}
	}	

});

/*
	Desc:   Maintains the empty location and it's neighbor
	Pre: 	The location of the Empty location
	Post: 	Returns the updated array with theh new empty location
*/

function moveUpate(n){
	var a= [5];
	a[0] = n;
	if (n >= 5 )
		a[1] = n - 4;
	else null;

	if (n <= 12)
		a[2] = n + 4;
	else null;
	
	if (n%4 != 1)
		a[3] = n - 1;
	else null;

	if (n%4 != 0)
		a[4] = n+1;
	else null;
	//print(a);
	return a;
}

/*
	Desc:   Make and array of x and y off
	Pre: 	None
	Post: 	The Div is move to the new location. Curr, emptysq
			and this.id are updated
*/
function setXY(){
	var temp = [];
	var x = 0;
	var y = 0;

	for (var i = 1; i <= 16; i++) {
		temp[i] = [ x, y];
		x += 100;
		if (x == 400){
			x = 0;
			y += 100;
		}
	}
	return  temp;
}

/*
	Desc:   Check to see if curr is in order.
	Pre: 	the array curr 
	Post: 	If Curr is in order, then the box is order return true.
			If Curr is not in order, return false
*/
function isCorrect(curr){
	for(var i = 1; i <= 16; i++){
		if (curr[i] != i)
			return false;
	}
		return true;
}

function print(str){
	console.log(str);
}