var cold = document.getElementById("cold");
var hot = document.getElementById("hot");
var btnCold = document.getElementById("btn-cold");
var btnHot = document.getElementById("btn-hot");
var result = document.getElementById("result");
var score = 23;

function up(){if(score < 30 ){score ++;}
  result.innerHTML = score;}

function down(){if(score > 18 ){score --;}
  result.innerHTML = score;}


cold.addEventListener('mouseover',function(){
	btnCold.classList.add('cold-active');
});

cold.addEventListener('mouseout',function(){
	btnCold.classList.remove('cold-active');
});
hot.addEventListener('mouseover',function(){
	btnHot.classList.add('hot-active');
});
hot.addEventListener('mouseout',function(){
	btnHot.classList.remove('hot-active');
});