var curentImageId = document.querySelector('.choosenid').innerHTML;
var allImagesId = [... document.querySelectorAll('.allid')].map((e) => e.innerHTML);
var curentImage = document.getElementsByClassName('curentImage');
curentImage[0].style.display = "none"
var curentIm = document.getElementsByClassName('choosenid');
curentIm[0].style.display = "none";
console.log(curentIm);
var curentIms = document.getElementsByClassName('allid');
for (p = 0; p < curentIms.length; p++) {
  curentIms.item(p).style.display = "none";
}
console.log(curentIms);

for(var u = 0; u < allImagesId.length; u++) {
  if (curentImageId == allImagesId[u]) {
    var currentSlide = u;
  }
  
}
console.log(currentSlide);

function showSlide(slideIndex) {
  const slides = document.getElementsByClassName('carouselImgs')
  if (slideIndex >= slides.length) { currentSlide = 0 }
  if (slideIndex < 0) { currentSlide = slides.length -1 }
  for (var i = 0; i < slides.length; i++) {
    slides[i].style.display = 'none'
  }
  slides[currentSlide].style.display = 'flex'
} 


function nextSlide() {
  showSlide(currentSlide += 1);
}

function previousSlide() {
  showSlide(currentSlide -= 1);
}

window.onload = function () {
  showSlide(currentSlide);
  document.getElementById('prev').addEventListener('click', function () {
    previousSlide();
  })
  document.getElementById('next').addEventListener('click', function () {
    nextSlide();
  })
}