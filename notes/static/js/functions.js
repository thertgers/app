async function getFile(id, url) {
  let myPromise = new Promise(function(myResolve, myReject) {
    let req = new XMLHttpRequest();
    req.open('GET', url);
    req.onload = function() {
      if (req.status == 200) {myResolve(req.response);}
      else {myResolve("File not Found");}
    };
    req.send();
  });
  document.getElementById(id).innerHTML = await myPromise;
  document.getElementById(id).classList.remove('invisible');
  //window.history.pushState(url, url, url);
}
async function postFile(url) {
  let myPromise = new Promise(function(myResolve, myReject) {
    formData = new FormData(document.getElementsByTagName('form')[0]);
    let req = new XMLHttpRequest();
    req.addEventListener(' error', function( event ) {
        alert( 'Error sending form data.' );
    } );
    req.onreadystatechange = function() {
      if (req.readyState == 4 && req.status == 200) {
      document.getElementById('col2').innerHTML = req.response;34
      myResolve(req.response);}
      else {myResolve("File not Found");}
    };
    req.open('POST', url);
    req.send(formData);
  });
  return await myPromise;
}
var scrollSpy = new bootstrap.ScrollSpy(document.body, {
  target: '#navbar'
})
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})
var tooltipEL = document.getElementsByClassName('tooltip')
var tooltip = new bootstrap.Tooltip(tooltipEL, options)
