//<!--lightbox-form js-->


//<!--gallery js-->
var img = document.querySelectorAll('.gallery img'),
	lightbox= document.querySelector('#lightbox-overlay'),
	lightboxImg= lightbox.querySelector('img');

	console.log(img);

for(var i = 0; i < img.length ; i++){
    img[i].addEventListener('click',function(){
        var imgNewSrc = this.getAttribute('data-lightbox');
        console.log(imgNewSrc);

        //lightboxImg의 src의 값을 이미지의 경로로 지정
        lightboxImg.setAttribute('src',imgNewSrc);
        //lightbox보이도록
        lightbox.classList.add('visible');

    });
}

//lightbox 를 클릭하면 다시 사라지도록
lightbox.addEventListener('click',function(){
    this.classList.remove('visible');
});

