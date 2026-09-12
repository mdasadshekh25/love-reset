
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Reset Me ❤️", page_icon="🧸")

html = """
<!DOCTYPE html>
<html>
<head>
<style>
body{
background:linear-gradient(#ffe6f2,#ffffff);
text-align:center;
font-family:Comic Sans MS, cursive;
overflow:hidden;
}
h1{color:#ff4d88;font-size:42px;}
.teddy{font-size:100px;animation:bounce 1s infinite;}
@keyframes bounce{50%{transform:translateY(-20px);}}

button{
padding:15px 35px;
border:none;
border-radius:30px;
font-size:22px;
cursor:pointer;
margin:20px;
}
#yes{background:#ff4d88;color:white;}
#no{
background:#777;color:white;
position:absolute;
}

.heart{
position:absolute;
font-size:25px;
animation:fall 4s linear infinite;
}
@keyframes fall{
from{top:-10%;}
to{top:100%;}
}
</style>
</head>

<body>

<div class="teddy">🧸❤️</div>

<h1>Will you reset me? 🥺</h1>

<p style="font-size:25px">
From now I will ask for bacchami again 💕
</p>

<button id="yes" onclick="yesClick()">YES ❤️</button>
<button id="no">NO 😒</button>

<h2 id="msg"></h2>

<script>

let no=document.getElementById("no");

no.onmouseover=function(){
    no.style.left=Math.random()*70+"%";
    no.style.top=Math.random()*70+"%";
}

function yesClick(){

document.getElementById("msg").innerHTML=
"Yayyy 🥰❤️ I promise I will be your baccha again 🧸💕";

for(let i=0;i<40;i++){
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

components.html(html, height=700)
