import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Reset Me ❤️",
    page_icon="🧸",
    layout="centered"
)

html = r"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
*{
 box-sizing:border-box;
}

body{
 margin:0;
 min-height:100vh;
 background:linear-gradient(135deg,#ffd6e8,#fff5fa);
 display:flex;
 justify-content:center;
 align-items:center;
 overflow:hidden;
 font-family:'Comic Sans MS',cursive;
}

.card{
 width:95%;
 max-width:450px;
 background:white;
 border-radius:30px;
 padding:30px 20px;
 text-align:center;
 box-shadow:0 10px 30px rgba(255,80,140,.25);
}

.teddy{
 font-size:90px;
 animation:bounce 1s infinite;
}

@keyframes bounce{
50%{transform:translateY(-15px);}
}

h1{
 color:#ff4d88;
 font-size:32px;
}

p{
 font-size:20px;
 color:#555;
}

button{
 width:45%;
 padding:15px;
 margin:10px;
 border:none;
 border-radius:30px;
 font-size:20px;
 color:white;
}

#yes{
 background:#ff4d88;
}

#no{
 background:#888;
 position:absolute;
}

.heart{
 position:absolute;
 animation:fall linear forwards;
 font-size:25px;
}

@keyframes fall{
from{top:-10%;}
to{top:110%;}
}

@media(max-width:600px){
 h1{font-size:27px;}
 p{font-size:18px;}
 .teddy{font-size:75px;}
 button{
  width:80%;
  font-size:22px;
 }
}
</style>
</head>

<body>

<div class="card">

<div class="teddy">🧸❤️</div>

<h1>Will you reset me? 🥺</h1>

<p>
From now I will ask for bacchami again 💕
</p>

<button id="yes">YES ❤️</button>
<button id="no">NO 😒</button>

<h2 id="msg"></h2>

</div>


<script>

let no=document.getElementById("no");

function moveNo(){
 no.style.left=Math.random()*70+"vw";
 no.style.top=Math.random()*70+"vh";
}

no.addEventListener("mouseover",moveNo);
no.addEventListener("touchstart",moveNo);


document.getElementById("yes").onclick=function(){

document.getElementById("msg").innerHTML=
"Yayyy 🥰❤️ I promise I will be your baccha again 🧸💕";

for(let i=0;i<50;i++){
 let h=document.createElement("div");
 h.innerHTML="❤️";
 h.className="heart";
 h.style.left=Math.random()*100+"%";
 h.style.animationDuration=(2+Math.random()*3)+"s";
 document.body.appendChild(h);
}

}

</script>

</body>
</html>
"""

components.html(html,height=750,scrolling=False)
