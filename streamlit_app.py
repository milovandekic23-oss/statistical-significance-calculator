import streamlit as st

# Use triple quotes """ to tell Python: "Everything inside here is just text"
calculator_html = <!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Stats Checker</title>
<style>
body{font-family:sans-serif;padding:40px;background:#f0f2f5;display:flex;justify-content:center}
.card{background:#fff;padding:30px;border-radius:12px;box-shadow:0 4px 20px rgba(0,0,0,0.1);width:350px}
input{width:100%;padding:10px;margin:10px 0 20px 0;border:1px solid #ccc;border-radius:6px;box-sizing:border-box}
button{width:100%;padding:12px;background:#007aff;color:#fff;border:none;border-radius:6px;font-size:16px;font-weight:600;cursor:pointer}
#result{margin-top:20px;padding:15px;border-radius:8px;display:none;text-align:center;font-weight:bold}
.sig{background:#d1e7dd;color:#0f5132}.trend{background:#fff3cd;color:#664d03}.none{background:#f8d7da;color:#842029}
</style>
</head>
<body>
<div class="card">
<h3>Stats Significance</h3>
<label>N1 Size</label><input type="number" id="n1" value="97">
<label>Group 1 %</label><input type="number" id="p1" value="24">
<label>N2 Size</label><input type="number" id="n2" value="873">
<label>Group 2 %</label><input type="number" id="p2" value="16">
<button onclick="calc()">Check Result</button>
<div id="result"></div>
</div>
<script>
function calc(){
const n1=parseInt(document.getElementById('n1').value),p1=document.getElementById('p1').value/100,n2=parseInt(document.getElementById('n2').value),p2=document.getElementById('p2').value/100;
const pp=(n1*p1+n2*p2)/(n1+n2),se=Math.sqrt(pp*(1-pp)*(1/n1+1/n2)),z=Math.abs(p1-p2)/se;
const pv=2*(1-erf(z/Math.sqrt(2)));
const r=document.getElementById('result');r.style.display="block";
let t=`P-value: ${pv.toFixed(4)}<br>`;
if(pv<0.05){r.className="sig";t+="✅ SIGNIFICANT (95%)"}
else if(pv<0.10){r.className="trend";t+="⚠️ TREND (90%)"}
else{r.className="none";t+="❌ NOT SIGNIFICANT"}
r.innerHTML=t}
function erf(x){const a1=0.254829592,a2=-0.284496736,a3=1.421413741,a4=-1.453152027,a5=1.061405429,p=0.3275911,s=(x<0)?-1:1;x=Math.abs(x);const t=1/(1+p*x),y=1-(((((a5*t+a4)*t)+a3)*t+a2)*t+a1)*t*Math.exp(-x*x);return s*y}
</script>
</body>
</html>"""
<style>
    body {
        font-family: sans-serif;
        padding: 40px;
        background: #f0f2f5;
        display: flex;
        justify-content: center;
    }
    /* ... the rest of your CSS ... */
</style>

<div class="container">
    <h1>Statistical Significance Calculator</h1>
    <!-- ... the rest of your HTML ... -->
</div>

<script>
    // ... any JavaScript you have ...
</script>
"""

# This command actually renders the code onto the screen
st.html(calculator_html)
