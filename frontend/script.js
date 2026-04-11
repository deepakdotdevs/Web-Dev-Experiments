function updateChar() {
    const val = document.getElementById('newsInput').value;
    document.getElementById('charCount').textContent = val.length + ' characters';
}

function clearInput() {
    document.getElementById('newsInput').value = '';
    document.getElementById('charCount').textContent = '0 characters';
    const box = document.getElementById('resultBox');
    box.style.display = 'none';
}

async function checkNews() {
    const text = document.getElementById('newsInput').value.trim();
    const btn  = document.getElementById('analyzeBtn');

    const box      = document.getElementById('resultBox');
    const iconWrap = document.getElementById('resultIconWrap');
    const icon     = document.getElementById('resultIcon');
    const verdict  = document.getElementById('resultVerdict');
    const conf     = document.getElementById('resultConf');
    const confBar  = document.getElementById('confBar');
    const confPct  = document.getElementById('confPct');
    const statsRow = document.getElementById('statsRow');
    const scan     = document.getElementById('scanLine');

    // Empty input guard
    if (!text) {
        showResult('warn', '⚠️', 'No input provided',
            'Please paste some news text above before analyzing.', null, null);
        return;
    }

    // Loading state
    btn.disabled = true;
    btn.innerHTML = '<div class="spinner"></div><span class="btn-text">Analyzing...</span>';
    scan.style.display = 'block';
    box.style.display  = 'none';

    try {
        const response = await fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text })
        });

        if (!response.ok) throw new Error('Server error: ' + response.status);

        const data       = await response.json();
        const isReal     = data.prediction.toLowerCase().includes('real');
        const confidence = parseFloat(data.confidence) || 0;
        const words      = text.split(/\s+/).filter(Boolean).length;
        const readTime   = Math.ceil(words / 200);

        const type    = isReal ? 'real' : 'fake';
        const emoji   = isReal ? '✅' : '🚫';
        const label   = isReal ? 'Likely Real News' : 'Likely Fake News';
        const subtext = `Confidence score: ${confidence.toFixed(1)}%`;

        showResult(type, emoji, label, subtext, confidence, {
            words, confidence, readTime
        });

    } catch (err) {
        showResult('error', '🔌', 'Server not reachable',
            'Make sure your Flask backend is running on localhost:5000', null, null);
        console.error('Fetch error:', err);
    } finally {
        btn.disabled = false;
        btn.innerHTML = `
            <svg class="btn-icon" width="18" height="18" viewBox="0 0 24 24" fill="none"
                 stroke="currentColor" stroke-width="2.5" stroke-linecap="round">
                <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
            </svg>
            <span class="btn-text">Analyze News</span>
            <div class="btn-shimmer"></div>
        `;
        scan.style.display = 'none';
    }
}

function showResult(type, emoji, label, subtext, confidence, stats) {
    const box      = document.getElementById('resultBox');
    const icon     = document.getElementById('resultIcon');
    const verdict  = document.getElementById('resultVerdict');
    const conf     = document.getElementById('resultConf');
    const confBar  = document.getElementById('confBar');
    const confPct  = document.getElementById('confPct');
    const confSec  = document.getElementById('confBarSection');
    const statsRow = document.getElementById('statsRow');

    // Set type class
    box.className = 'result-box ' + type;
    box.style.display = 'block';

    icon.textContent    = emoji;
    verdict.textContent = label;
    conf.textContent    = subtext;

    if (confidence !== null && (type === 'real' || type === 'fake')) {
        confSec.style.display = 'block';
        confBar.style.width   = '0%';
        confPct.textContent   = confidence.toFixed(0) + '%';
        setTimeout(() => { confBar.style.width = confidence + '%'; }, 60);
    } else {
        confSec.style.display = 'none';
    }

    if (stats) {
        statsRow.style.display = 'flex';
        statsRow.innerHTML = `
            <div class="stat-chip">
                <div class="stat-chip-val">${stats.confidence.toFixed(0)}%</div>
                <div class="stat-chip-lbl">Confidence</div>
            </div>
            <div class="stat-chip">
                <div class="stat-chip-val">${stats.words}</div>
                <div class="stat-chip-lbl">Word Count</div>
            </div>
            <div class="stat-chip">
                <div class="stat-chip-val">${stats.readTime} min</div>
                <div class="stat-chip-lbl">Read Time</div>
            </div>
        `;
    } else {
        statsRow.style.display = 'none';
    }
}