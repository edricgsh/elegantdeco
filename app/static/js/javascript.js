// Side navigation
function w3_open() {
    var x = document.getElementById("mySidebar");
    x.style.width = "100%";
    x.style.fontSize = "40px";
    x.style.paddingTop = "10%";
    x.style.display = "block";
}
function w3_close() {
    document.getElementById("mySidebar").style.display = "none";
}

// Tabs
function openCity(evt, cityName) {
  var i;
  var x = document.getElementsByClassName("city");
  for (i = 0; i < x.length; i++) {
     x[i].style.display = "none";
  }
  var activebtn = document.getElementsByClassName("testbtn");
  for (i = 0; i < x.length; i++) {
      activebtn[i].className = activebtn[i].className.replace(" w3-dark-grey", "");
  }
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " w3-dark-grey";
}

var mybtn = document.getElementsByClassName("testbtn")[0];
mybtn.click();

// Accordions
function myAccFunc(id) {
    var x = document.getElementById(id);
    if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-show";
    } else {
        x.className = x.className.replace(" w3-show", "");
    }
}

// Slideshows
var slideIndex = 1;

function plusDivs(n) {
slideIndex = slideIndex + n;
showDivs(slideIndex);
}

function showDivs(n) {
  var x = document.getElementsByClassName("mySlides");
  if (n > x.length) {slideIndex = 1}
  if (n < 1) {slideIndex = x.length} ;
  for (i = 0; i < x.length; i++) {
     x[i].style.display = "none";
  }
  x[slideIndex-1].style.display = "block";
}

showDivs(1);

// Progress Bars
function move() {
  var elem = document.getElementById("myBar");
  var width = 5;
  var id = setInterval(frame, 10);
  function frame() {
    if (width == 100) {
      clearInterval(id);
    } else {
      width++;
      elem.style.width = width + '%';
      elem.innerHTML = width * 1  + '%';
    }
  }
}
// Automatic Slideshow - change image every 4 seconds
var myIndex = 0;
carousel();

function carousel() {
    var i;
    var x = document.getElementsByClassName("mySlides");
    for (i = 0; i < x.length; i++) {
       x[i].style.display = "none";
    }
    myIndex++;
    if (myIndex > x.length) {myIndex = 1}
    x[myIndex-1].style.display = "block";
    setTimeout(carousel, 4000);
}

// Used to toggle the menu on small screens when clicking on the menu button
function myFunction() {
    var x = document.getElementById("navDemo");
    if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-show";
    } else {
        x.className = x.className.replace(" w3-show", "");
    }
}

// When the user clicks anywhere outside of the modal, close it
var modal = document.getElementById('ticketModal');
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
//Map
function myMap() {
  myCenter=new google.maps.LatLng(41.878114, -87.629798);
  var mapOptions= {
    center:myCenter,
    zoom:12, scrollwheel: false, draggable: false,
    mapTypeId:google.maps.MapTypeId.ROADMAP
  };
  var map=new google.maps.Map(document.getElementById("googleMap"),mapOptions);

  var marker = new google.maps.Marker({
    position: myCenter,
  });
  marker.setMap(map);
}

//Modal

//Modal with next
var data = [
    { src: "https://placehold.it/150x150?text=Image1", title: "Image 1", description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean a est mauris. Sed non sollicitudin lacus. Sed maximus facilisis purus, et blandit lectus vehicula in." },
    { src: "https://placehold.it/150x150?text=Image2", title: "Image 2", description: "Aenean accumsan metus ipsum, id vehicula felis semper sed. Sed hendrerit pulvinar porttitor. Etiam id tortor leo. Integer ex dui, vulputate vel iaculis sit amet, laoreet eu sem." },
    { src: "https://placehold.it/150x150?text=Image3", title: "Image 3", description: "Vivamus luctus est at sapien sollicitudin, nec mattis arcu condimentum. Vivamus sed varius diam. Nulla varius, tortor vel tempus feugiat, libero felis pellentesque mi, sit amet sagittis lacus massa et erat. " },
    { src: "https://placehold.it/150x150?text=Image4", title: "Image 4", description: "Vestibulum eu ex ac nunc pretium hendrerit vel in quam. Morbi imperdiet imperdiet pharetra." }
  ];

var currentItem = 0;

function prevImg() {
  if (currentItem > 0) {
    currentItem--;
  }
  loadData();
}

function nextImg() {
  if (currentItem < data.length - 1) {
    currentItem++;
  }
  loadData();
}

function loadData() {
  $("#modalTitle").html(data[currentItem].title);
  $("#modalImg").attr("src", data[currentItem].src).attr("alt", data[currentItem].title);
  $("#modalText").html(data[currentItem].description);

  // enable/disable nav buttons
  $("#navPrev").removeAttr("disabled");
  $("#navNext").removeAttr("disabled");

  if (currentItem == 0) {
    $("#navPrev").attr("disabled", "disabled");
  }
  else if (currentItem == data.length - 1) {
    $("#navNext").attr("disabled", "disabled");
  }
}

function openModal(idx) {
  currentItem = idx;
  loadData();
  $("#modal").modal();
}

$(document).ready(function () {
  var $thumbs = $(".thumbnails");

  // dynamically add thumbnails to page
  for (var i = 0; i < data.length; i++) {
    $thumbs.append('<a href="#" onclick="openModal(' + i + ')" class="thumbnail" data-toggle="modal" alt="' + data[i].title + '"><img src="' + data[i].src + '" class="img-responsive center-block" /></a>');
  }
});
