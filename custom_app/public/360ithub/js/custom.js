//Hero Area
$('.hero-slider').slick({
  infinite: true,
  arrows: false,
  dots: true,
  autoplay: true,
  speed: 500,
  slidesToShow: 1,
  slidesToScroll: 1
});

//People Love Slider
$('.people-slider').slick({
  infinite: true,
  arrows: false,
  dots: true,
  autoplay: true,
  speed: 500,
  slidesToShow: 1,
  slidesToScroll: 1
});

//People Love Slider
$('.software-slider').slick({
  infinite: true,
  arrows: false,
  dots: false,
  autoplay: true,
  speed: 7500,
  slidesToShow: 7,
  slidesToScroll: 1,
  responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 3.5,
        slidesToScroll: 1,
        infinite: true,
        dots: false
      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 1
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 1
      }
    }
  ]
});

//People Love Slider
$('.slider-industries').slick({
  infinite: true,
  arrows: false,
  dots: true,
  autoplay: true,
  speed: 1000,
  slidesToShow: 1,
  slidesToScroll: 1
});

//Blog Slider
$('.slider-blog').slick({
  dots: true,
  infinite: true,
  arrows: true,
  autoplay: false,
  speed: 500,
  slidesToShow: 3,
  slidesToScroll: 1,
  responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 1,
        infinite: true,
        dots: true
      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }
  ]
});

//Life Gallery
$('.lifegallery').slick({
  infinite: true,
  arrows: false,
  dots: false,
  autoplay: true,
  speed: 1000,
  slidesToShow: 3,
  slidesToScroll: 1
});


//Counter 
$('.count').each(function () {
  $(this).prop('Counter', 0).animate({
    Counter: $(this).text()
  }, {
    duration: 3000,
    easing: 'swing',
    step: function (now) {
      $(this).text(Math.ceil(now));
    }
  });
});


//var mainDiv = document.getElementById('main-button');
//mainDiv.addEventListener('click', function(){
  //this.children.item(0).classList.toggle('fa-times');
  //this.classList.toggle('open');
//});s
 

new WOW().init();


//count:
//let counts = setInterval(updated);
//let upto = 0;
//function updated() {
  //let count = document.getElementById("counter");
  //count.innerHTML = ++upto;
  //if (upto === 1000) {
    //clearInterval(counts);
  //}
//}