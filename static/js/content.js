 var choice = document.getElementById('choice').getElementsByTagName('li');
		 var content = document.getElementById('content').getElementsByTagName('li');
		 for (let i = choice.length - 1; i >= 0; i--) {
		 	choice[i].addEventListener("click",function(){
		 		for (let j = content.length - 1; j >= 0; j--) {
		 	 	content[j].style.display="none";
		 	 	choice[j].style.backgroundColor="#99CCFF";
		 	 }
		 	 content[i].style.display="block";
		 	 choice[i].style.backgroundColor="white";
		 })
		 	 
	   };


	   var searchInput = document.querySelector(".search-text");
	   searchInput.addEventListener("focus",function(){
	   	   this.value="";
	   	   this.style.borderColor="#99CCFF";
	   });
	   searchInput.addEventListener("blur",function(){
	   	   this.value="请输入你想要搜索的内容";
	   	   this.style.borderColor="#CCCCCC";
	   });

	   var Image=['F://图片/a3.jpg','F://图片/a1.jpg','F://图片/a2.jpg'];
		var timer=null;
		var i=0
		// document.body.style.backgroundImage="url(../image/study.jpg)";
		timer=setInterval(function(){             
            document.body.style.backgroundImage="url("+Image[i]+")";
            i++;
            if(i>2){
               i=0;
            }
		},5000);
