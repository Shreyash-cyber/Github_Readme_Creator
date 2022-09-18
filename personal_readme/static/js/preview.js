function copyToClipboard(text) {
  var dummy = document.createElement("textarea");
  document.body.appendChild(dummy);
  dummy.value = text;
  dummy.select();
  document.execCommand("copy");
  document.body.removeChild(dummy);
}
function copyEvent() {
  var elem = document.getElementById("copy").innerHTML;
  
  elem = elem.replace(/\n/g, "")
  .replace(/[\t ]+\</g, "<")
  .replace(/\>[\t ]+$/g, ">")
  
  copyToClipboard(elem);
}
