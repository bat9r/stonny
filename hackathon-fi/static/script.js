particlesJS('particles-js', {
    particles: {
        number: { value: 60, density: { enable: true, value_area: 800 } },
        color: { value: '#ffffff' },
        opacity: { value: 0.2, random: true },
        size: { value: 1.5 },
        move: { enable: true, speed: 0.6 }
    },
    interactivity: {
        events: { onhover: { enable: true, mode: "repulse" }, resize: true },
        modes: { repulse: { distance: 100, duration: 0.4 } }
    }
});

const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');

marked.setOptions({
    highlight: null
});

function appendMessage(sender, text, raw = false) {
    const row = document.createElement('div');
    row.className = `message-row ${sender}-row`;
    
    if (sender === 'bot') {
        const avatar = document.createElement('div');
        avatar.className = 'avatar';
        avatar.textContent = '🐘';
        row.appendChild(avatar);
    }

    const msg = document.createElement('div');
    msg.className = 'message';
    
    if (sender === 'bot' && raw) {
        const clean = text.replace(/^<final>\n?/, '').replace(/\n?<\/final>$/, '').trim();
        msg.innerHTML = `<pre style="white-space:pre-wrap;font-size:12px;color:#7FFFD4;margin:0;">${clean}</pre>`;
    } else {
        msg.innerHTML = sender === 'bot' ? marked.parse(text) : text;
    }

    row.appendChild(msg);
    chatBox.appendChild(row);
    chatBox.scrollTo({ top: chatBox.scrollHeight, behavior: 'smooth' });
    return row;
}

async function generateGeminiFile() {
    const botMessages = document.querySelectorAll('.bot-row .message');
    if (botMessages.length === 0) return;

    const promptForAgent = `Based on this idea generate the content of GEMINI.md to build whole app. Use ONLY Markdown raw`;
    userInput.value = promptForAgent;

    // sendMessage але відповідь рендеримо як raw
    const text = userInput.value.trim();
    userInput.value = '';
    userInput.disabled = true;
    sendBtn.disabled = true;

    const loadingRow = appendMessage('bot', 'thinking...');
    loadingRow.id = 'loading-msg';

    try {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: text })
        });
        const data = await response.json();
        document.getElementById('loading-msg')?.remove();
        appendMessage('bot', data.status === 'success' ? data.reply : 'Error: ' + data.reply, true);
    } catch {
        document.getElementById('loading-msg')?.remove();
        appendMessage('bot', 'Connection failed.');
    }

    userInput.disabled = false;
    sendBtn.disabled = false;
    userInput.focus();
}

async function sendMessage(isSilent = false) {
    const text = userInput.value.trim();
    if (!text) return;
    
    if (!isSilent) {
        appendMessage('user', text);
    }
    
    userInput.value = '';
    userInput.disabled = true;
    sendBtn.disabled = true;
    
    const loadingRow = appendMessage('bot', 'thinking...');
    loadingRow.id = 'loading-msg';
    
    try {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: text })
        });
        
        const data = await response.json();
        const loadingMsg = document.getElementById('loading-msg');
        if (loadingMsg) loadingMsg.remove();
        
        if (data.status === 'success') {
            appendMessage('bot', data.reply);
        } else {
            appendMessage('bot', 'Error: ' + data.reply);
        }
    } catch (err) {
        const loadingMsg = document.getElementById('loading-msg');
        if (loadingMsg) loadingMsg.remove();
        appendMessage('bot', 'Connection failed.');
    }
    
    userInput.disabled = false;
    sendBtn.disabled = false;
    userInput.focus();
}

async function generateGeminiFile() {
    const botMessages = document.querySelectorAll('.bot-row .message');
    if (botMessages.length === 0) return;

    const promptForAgent = `Based on this idea generate the content of GEMINI.md to build whole app. Use ONLY Markdown raw`;
    userInput.value = promptForAgent;

    // sendMessage але відповідь рендеримо як raw
    const text = userInput.value.trim();
    userInput.value = '';
    userInput.disabled = true;
    sendBtn.disabled = true;

    const loadingRow = appendMessage('bot', 'thinking...');
    loadingRow.id = 'loading-msg';

    try {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: text })
        });
        const data = await response.json();
        document.getElementById('loading-msg')?.remove();
        appendMessage('bot', data.status === 'success' ? data.reply : 'Error: ' + data.reply, true);
    } catch {
        document.getElementById('loading-msg')?.remove();
        appendMessage('bot', 'Connection failed.');
    }

    userInput.disabled = false;
    sendBtn.disabled = false;
    userInput.focus();
}

function handleKeyPress(e) {
    if (e.key === 'Enter') sendMessage();
}

window.addEventListener('DOMContentLoaded', () => {
    const params = new URLSearchParams(window.location.search);
    const idea = params.get('idea');

    if (idea) {
        appendMessage('bot', idea);
    } else {
        appendMessage('bot', "Hello there! I'm Stonny🐘. What great dream are we building today on STON.fi?");
    }
});