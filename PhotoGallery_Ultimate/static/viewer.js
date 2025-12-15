let viewer, viewerImg, images=[], idx=0, scale=1, startX=0;
document.addEventListener("DOMContentLoaded",()=>{
viewer=document.getElementById("viewer");
viewerImg=document.getElementById("viewer-img");
images=[...document.querySelectorAll(".card img")].map(i=>i.src);
document.addEventListener("keydown",e=>{
if(viewer.style.display!=="flex")return;
if(e.key==="Escape")closeViewer();
if(e.key==="ArrowRight")next();
if(e.key==="ArrowLeft")prev();
});
viewerImg.addEventListener("wheel",e=>{
e.preventDefault();scale+=e.deltaY*-0.001;scale=Math.min(Math.max(1,scale),3);
viewerImg.style.transform=`scale(${scale})`;
});
viewer.addEventListener("touchstart",e=>startX=e.touches[0].clientX);
viewer.addEventListener("touchend",e=>{
let endX=e.changedTouches[0].clientX;
if(startX-endX>50)next();
if(endX-startX>50)prev();
});
});
function openViewer(src){viewer.style.display="flex";idx=images.indexOf(src);scale=1;viewerImg.style.transform="scale(1)";viewerImg.src=src;}
function closeViewer(){viewer.style.display="none";}
function next(){idx=(idx+1)%images.length;viewerImg.src=images[idx];reset();}
function prev(){idx=(idx-1+images.length)%images.length;viewerImg.src=images[idx];reset();}
function reset(){scale=1;viewerImg.style.transform="scale(1)";}