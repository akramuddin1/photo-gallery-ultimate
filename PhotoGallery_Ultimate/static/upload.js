document.getElementById("uploadForm")?.addEventListener("submit",e=>{
e.preventDefault();
const f=e.target,p=document.getElementById("progress");
const d=new FormData(f),x=new XMLHttpRequest();
x.open("POST","/upload");p.style.display="block";
x.upload.onprogress=e=>{if(e.lengthComputable)p.value=e.loaded/e.total*100};
x.onload=()=>location.reload();x.send(d);
});