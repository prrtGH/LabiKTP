console.log(document.querySelector("*.fold-button")) 

var foldBtns = document.getElementsByClassName("fold-button"); 

console.log(foldBtns) 

for (var i = 0; i<foldBtns.length; i++){ 
	foldBtns[i].addEventListener("click", function(event) { 
		if( this.innerHTML == "Cвернуть"){ 
			this.parentElement.className+=' folded'; 
			this.innerHTML = "Развернуть"; 
		}
		else
		{ 
			this.parentElement.className=this.parentElement.className.replace(' folded','') 
			this.innerHTML = "Cвернуть"; 
		}; 
	}); 
}

