import re

file_path = 'aero-compare.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add new Tab
tabs_html_old = '''<div class="tabs">
  <div class="tab active" onclick="switchTab('regimes')">📐 Régimes de vitesse</div>
  <div class="tab" onclick="switchTab('polaire')">📉 Polaires de vol</div>
  <div class="tab" onclick="switchTab('finesse')">🏆 Finesse &amp; Taux de chute</div>
  <div class="tab" onclick="switchTab('physique')">⚗️ Physique du vol</div>
  <div class="tab" onclick="switchTab('table')">📋 Tableau complet</div>
  <div class="tab" onclick="switchTab('refs')">📚 Références</div>
</div>'''
tabs_html_new = '''<div class="tabs">
  <div class="tab active" onclick="switchTab('regimes')">📐 Régimes de vitesse</div>
  <div class="tab" onclick="switchTab('polaire')">📉 Polaires de vol</div>
  <div class="tab" onclick="switchTab('finesse')">🏆 Finesse &amp; Taux de chute</div>
  <div class="tab" onclick="switchTab('physique')">⚗️ Physique du vol</div>
  <div class="tab" onclick="switchTab('parametric')">🌌 Espace Paramétrique</div>
  <div class="tab" onclick="switchTab('table')">📋 Tableau complet</div>
  <div class="tab" onclick="switchTab('refs')">📚 Références</div>
</div>'''
content = content.replace(tabs_html_old, tabs_html_new)

# 2. Add Parametric Space Tab HTML
param_html = '''<!-- ═══════════════ TAB 7: PARAMETRIC ═══════════════ -->
<div id="tab-parametric" class="tab-content fi">
  <div class="stitle">Espace Paramétrique Global <span class="note">— Masse, Vitesse, Finesse et Taux de chute</span></div>
  
  <div class="insight" style="margin-bottom:1.5rem">
    Visualisation de l'<strong>espace paramétrique complet</strong> (25 entités). 
    <br>• <strong>Graphique 1 (Bulles) :</strong> Axe X = Vitesse de croisière, Axe Y = Finesse, Taille de bulle = Masse (échelle log), Couleur = Type.
    <br>• <strong>Graphique 2 :</strong> Masse vs Plage de vitesse (Vmax - Vmin).
    <br>• <strong>Graphique 3 :</strong> Vitesse de croisière vs Taux de chute.
  </div>

  <div class="card" style="margin-bottom:1.5rem">
    <h3>Vitesse vs Finesse (Taille des bulles = Masse proportionnelle)</h3>
    <div class="chart-wrap" style="height:450px"><canvas id="bubbleChart"></canvas></div>
  </div>

  <div class="grid2">
    <div class="card">
      <h3>Masse (kg) vs Plage de Vitesse exploitable (km/h)</h3>
      <div class="chart-wrap" style="height:350px"><canvas id="massSpeedRangeChart"></canvas></div>
    </div>
    <div class="card">
      <h3>Vitesse Croisière vs Taux de chute (m/s)</h3>
      <div class="chart-wrap" style="height:350px"><canvas id="speedSinkChart"></canvas></div>
    </div>
  </div>
</div>

<!-- ═══════════════ TAB 5: TABLE ═══════════════ -->'''
content = content.replace('<!-- ═══════════════ TAB 5: TABLE ═══════════════ -->', param_html)

# 3. Inject masses into JS objects
masses = {
    'albatross': 8.5, 'condor': 11, 'swift': 0.04, 'falcon': 1.0, 'eagle': 4.5,
    'goose': 2.5, 'frigate': 1.5, 'crane': 5.0, 'hummingbird': 0.003, 'butterfly': 0.0005,
    'dragonfly': 0.001, 'bat': 0.05,
    'asw22': 600, 'ls8': 400, 'hangglider': 120, 'paraglider': 100, 'ultralight': 450,
    'solar': 2300, 'evtol': 2177, 'a320': 73500, 'b787': 254000, 'helicopter': 3800,
    'f22': 38000, 'concorde': 185000, 'x43': 1300, 'wingsuit': 90
}
for key, mass in masses.items():
    content = re.sub(rf"(id:'{key}',.*?)vMin:", rf"\g<1>mass:{mass},vMin:", content, flags=re.DOTALL)

# 4. Add table column for mass
content = content.replace('<th style="background:rgba(26,46,69,0.5);font-size:0.7rem">Hover</th>', '<th style="background:rgba(26,46,69,0.5);font-size:0.7rem">Masse (kg)</th>\n    <th style="background:rgba(26,46,69,0.5);font-size:0.7rem">Hover</th>')
content = content.replace('<td style="text-align:center"></td>', '<td style="font-weight:700"></td>\n      <td style="text-align:center"></td>')

# 5. Inject JS logic for new charts
js_code = '''
// ═══════════════════════════════════════════════════
// TAB PARAMETRIC
// ═══════════════════════════════════════════════════
function buildParametric() {
  const common = { responsive:true, maintainAspectRatio:false, plugins:{ legend:{labels:{color:'#6a8daa'}} } };

  // 1. Bubble Chart (Vcruise vs LD, bubble=Mass)
  const bData = E.filter(e=>e.mass).map(e => ({
    x: e.vCruise,
    y: e.LD,
    r: Math.max(3, Math.log10(e.mass * 10000) * 3), // scale visually
    raw: e
  }));
  new Chart(document.getElementById('bubbleChart').getContext('2d'), {
    type: 'bubble',
    data: {
      datasets: [
        {
          label: 'Animaux',
          data: bData.filter(d=>d.raw.type==='animal'),
          backgroundColor: 'rgba(255,143,0,0.6)', borderColor: '#FF8F00'
        },
        {
          label: 'Machines',
          data: bData.filter(d=>d.raw.type==='machine'),
          backgroundColor: 'rgba(0,188,212,0.6)', borderColor: '#00BCD4'
        }
      ]
    },
    options: {
      ...common,
      scales: {
        x: { type:'logarithmic', title:{display:true,text:'Vitesse de Croisière (km/h) - Log',color:'#6a8daa'}, ticks:{color:'#6a8daa'} },
        y: { title:{display:true,text:'Finesse (L/D)',color:'#6a8daa'}, ticks:{color:'#6a8daa'} }
      },
      plugins: {
        tooltip: { callbacks: { label: c => ${c.raw.raw.name}: kg, V=km/h, L/D= } }
      }
    }
  });

  // 2. Mass vs Speed Range (Vmax - Vmin)
  new Chart(document.getElementById('massSpeedRangeChart').getContext('2d'), {
    type: 'scatter',
    data: {
      datasets: [
        { label: 'Animaux', data: E.filter(e=>e.type==='animal'&&e.mass).map(e=>({x:e.mass, y:e.vMax-e.vMin, raw:e})), backgroundColor: '#FF8F00' },
        { label: 'Machines', data: E.filter(e=>e.type==='machine'&&e.mass).map(e=>({x:e.mass, y:e.vMax-e.vMin, raw:e})), backgroundColor: '#00BCD4' }
      ]
    },
    options: {
      ...common,
      scales: {
        x: { type:'logarithmic', title:{display:true,text:'Masse (kg) - Log',color:'#6a8daa'}, ticks:{color:'#6a8daa'} },
        y: { type:'logarithmic', title:{display:true,text:'Plage de vitesse (Vmax - Vmin)',color:'#6a8daa'}, ticks:{color:'#6a8daa'} }
      },
      plugins: { tooltip: { callbacks: { label: c => ${c.raw.raw.name}: Range=km/h } } }
    }
  });

  // 3. Vcruise vs Sink Rate
  new Chart(document.getElementById('speedSinkChart').getContext('2d'), {
    type: 'scatter',
    data: {
      datasets: [
        { label: 'Animaux', data: E.filter(e=>e.type==='animal'&&e.wMin).map(e=>({x:e.vCruise, y:e.wMin, raw:e})), backgroundColor: '#FF8F00' },
        { label: 'Machines', data: E.filter(e=>e.type==='machine'&&e.wMin).map(e=>({x:e.vCruise, y:e.wMin, raw:e})), backgroundColor: '#00BCD4' }
      ]
    },
    options: {
      ...common,
      scales: {
        x: { type:'logarithmic', title:{display:true,text:'Vitesse Croisière (km/h)',color:'#6a8daa'}, ticks:{color:'#6a8daa'} },
        y: { type:'logarithmic', title:{display:true,text:'Taux de chute (m/s)',color:'#6a8daa'}, ticks:{color:'#6a8daa'} }
      },
      plugins: { tooltip: { callbacks: { label: c => ${c.raw.raw.name}: Vz=m/s } } }
    }
  });
}

function switchTab(t){
  document.querySelectorAll('.tab').forEach(el=>el.classList.remove('active'));
  document.querySelector('.tab[onclick="switchTab(\\''+t+'\\')"]').classList.add('active');
  document.querySelectorAll('.tab-content').forEach(el=>el.classList.remove('active'));
  document.getElementById('tab-'+t).classList.add('active');
  
  if(t==='parametric' && !window.parametricBuilt){
    buildParametric();
    window.parametricBuilt=true;
  }
}
'''

content = content.replace('function switchTab(t){', js_code + '\n/* ')
content = content.replace('  document.getElementById(\'tab-\'+t).classList.add(\'active\');\n}', '*/\n')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Modification complete")
