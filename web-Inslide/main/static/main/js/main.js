$('.slider').slick({
    autoplay:true,
    autoplaySpeed:20000,
    speed: 1500,
    fade: true,
    infinite: true,
    pauseOnHover: false,
    arrows:false,
    mobileFirst:true,
    pauseOnFocus: false,
    lazyLoad: 'ondemand'
});

function foo(x) { return (x < 10) ? '0' + x : x; }
function clock() {
  var now = new Date();
  var h = now.getHours();
  var m = now.getMinutes();
  var s = now.getSeconds();
  var t = foo(h) + ':' + foo(m) + ':' + foo(s);
  document.getElementById('clock').textContent = t; // 例2
}
setInterval(clock, 1000);
window.onload = clock;