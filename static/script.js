document.addEventListener('DOMContentLoaded', () => {
    const textInput = document.getElementById('text-input');
    const analyzeBtn = document.getElementById('analyze-btn');
    const resultSection = document.getElementById('result-section');
    const polarityBar = document.getElementById('polarity-bar');
    const subjectivityBar = document.getElementById('subjectivity-bar');
    const polarityVal = document.getElementById('polarity-val');
    const subjectivityVal = document.getElementById('subjectivity-val');
    const sentimentBadge = document.getElementById('sentiment-badge');

    analyzeBtn.addEventListener('click', async () => {
        const text = textInput.value.trim();
        if (!text) return;

        analyzeBtn.disabled = true;
        analyzeBtn.textContent = 'Analyzing...';

        try {
            const response = await fetch('/analyze', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text })
            });

            const data = await response.json();

            // Show results
            resultSection.classList.remove('hidden');

            // Animate values
            updateMetric(polarityVal, polarityBar, data.polarity, true);
            updateMetric(subjectivityVal, subjectivityBar, data.subjectivity, false);

            // Update badge
            sentimentBadge.textContent = data.label;
            sentimentBadge.className = 'badge ' + data.label.toLowerCase();

        } catch (error) {
            console.error('Error:', error);
            alert('Something went wrong during analysis.');
        } finally {
            analyzeBtn.disabled = false;
            analyzeBtn.textContent = 'Analyze Sentiment';
        }
    });

    function updateMetric(labelEl, barEl, value, isPolarity) {
        // Simple decimal to percentage
        let percent = isPolarity ? ((value + 1) / 2) * 100 : value * 100;

        labelEl.textContent = value.toFixed(2);
        barEl.style.width = `${percent}%`;

        // Qualitative colors for polarity
        if (isPolarity) {
            if (value > 0.1) barEl.style.background = 'var(--positive)';
            else if (value < -0.1) barEl.style.background = 'var(--negative)';
            else barEl.style.background = 'var(--neutral)';
        }
    }
});
