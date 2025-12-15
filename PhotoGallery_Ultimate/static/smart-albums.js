function classifyImage(img){
const n=img.src.toLowerCase();
if(n.includes("screenshot"))return"Screenshots";
if(n.includes("download")||n.includes("whatsapp")||n.includes("telegram"))return"Downloads";
return"Camera";
}
function buildSmartAlbums(){
const imgs=document.querySelectorAll(".card img");
const g={Camera:[],Screenshots:[],Downloads:[]};
imgs.forEach(i=>g[classifyImage(i)].push(i.closest(".card")));
const c=document.querySelector(".grid");c.innerHTML="";
Object.entries(g).forEach(([k,v])=>{
if(!v.length)return;
const t=document.createElement("h4");t.className="album-title";t.innerText=k;c.appendChild(t);
v.forEach(x=>c.appendChild(x));
});
}