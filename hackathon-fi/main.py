import os
import json
import uuid
import time
import secrets
import base64
import hashlib
import asyncio
import logging
from typing import Any, Optional

import websockets
from nacl.signing import SigningKey
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi import Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("face-web")

app = FastAPI()

# --- Style ---
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# --- Auth ---
BASIC_USER = os.getenv("APP_USERNAME")
BASIC_PASS = os.getenv("APP_PASSWORD")
security = HTTPBasic()

OPENCLAW_WS_URL = os.getenv("OPENCLAW_WS_URL", "ws://openclaw-gateway:18789")
OPENCLAW_GATEWAY_TOKEN = os.getenv("OPENCLAW_GATEWAY_TOKEN", "")
OPENCLAW_SESSION_KEY = os.getenv("OPENCLAW_SESSION_KEY", "agent:stonny:main")
OPENCLAW_TIMEOUT_SECONDS = float(os.getenv("OPENCLAW_TIMEOUT_SECONDS", "120"))
OPENCLAW_DEVICE_KEY_FILE = os.getenv(
    "OPENCLAW_DEVICE_KEY_FILE",
    "/data/face-web-device-ed25519.key",
)
OPENCLAW_AGENT_ID = os.getenv("OPENCLAW_AGENT_ID", "stonny")

WIDGET = """
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap" rel="stylesheet">
<style>
    #oc-widget { 
        position: fixed; 
        bottom: 32px; 
        right: 32px; 
        width: 340px; 
        z-index: 2147483647; 
        font-family: 'Montserrat', sans-serif; 
    }

    #oc-btn { 
        width: 100%; 
        background: linear-gradient(135deg, #0D47A1, #1976D2); 
        color: white; 
        border: 1px solid rgba(127, 255, 212, 0.4); 
        border-radius: 12px; 
        padding: 14px 20px; 
        font-size: 15px; 
        font-weight: 700; 
        cursor: pointer; 
        box-shadow: 0 4px 20px rgba(13, 71, 161, 0.4); 
        transition: all 0.4s ease;
    }

    #oc-btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 0 25px rgba(127, 255, 212, 0.4);
        background: linear-gradient(135deg, #1976D2, #7FFFD4);
        color: #010206;
    }

    #oc-result { 
        background: rgba(1, 2, 6, 0.8) !important; 
        backdrop-filter: blur(25px) saturate(180%) !important;
        border: 1px solid rgba(127, 255, 212, 0.15) !important; 
        border-radius: 12px !important; 
        padding: 16px !important; 
        margin-top: 8px !important; 
        box-shadow: 0 30px 60px rgba(0,0,0,0.7), 0 0 20px rgba(127, 255, 212, 0.2) !important; 
        display: none; 
        max-height: 400px !important; 
        overflow-y: auto !important; 
        animation: ocFadeIn 0.4s ease-out;
    }

    #oc-text { 
        all: unset !important; 
        display: block !important; 
        margin-bottom: 16px !important; 
        font-size: 14px !important; 
        line-height: 1.5 !important; 
        color: #ffffff !important; 
        white-space: pre-wrap !important; 
        word-break: break-word !important; 
        font-weight: 400;
    }

    .oc-actions { display: flex; gap: 8px; }

    #oc-discuss, #oc-retry { 
        flex: 1;
        border: none; 
        border-radius: 8px; 
        padding: 10px; 
        font-size: 14px; 
        font-weight: 700; 
        cursor: pointer; 
        transition: all 0.3s ease;
    }

    #oc-discuss { 
        background: #7FFFD4; 
        color: #010206; 
    }

    #oc-discuss:hover { 
        box-shadow: 0 0 15px #7FFFD4;
        transform: translateY(-2px);
    }

    #oc-retry {
        background: rgba(255, 255, 255, 0.05);
        color: #ffffff;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    #oc-retry:hover {
        background: rgba(255, 255, 255, 0.15);
    }

    @keyframes ocFadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
</style>

<div id="oc-widget">
    <button id="oc-btn" onclick="ocGenerate()">✨ Generate an idea</button>
    <div id="oc-result">
        <div id="oc-text"></div>
        <div class="oc-actions">
            <button id="oc-retry" onclick="ocReset()">🔄 New idea</button>
            <button id="oc-discuss" onclick="window.location.href='/chat?idea=' + encodeURIComponent(document.getElementById('oc-text').innerText)">💬 Discuss</button>
        </div>
    </div>
</div>

<script>
function ocReset() {
    const text = document.getElementById('oc-text');
    const retryBtn = document.getElementById('oc-retry');
    text.style.opacity = "0.5";
    retryBtn.disabled = true;
    retryBtn.innerText = "⏳...";
    ocGenerate();
}

async function ocGenerate() {
    const btn = document.getElementById('oc-btn');
    const result = document.getElementById('oc-result');
    const text = document.getElementById('oc-text');
    const retryBtn = document.getElementById('oc-retry');
    
    if (btn.style.display !== 'none') {
        btn.disabled = true;
        btn.innerHTML = '⏳ working on...';
    }
    
    try {
        const res = await fetch('/api/chat', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ message: 'Come up with an interesting and fresh idea for using STON.fi. Your answer should be brief but interesting. Use plain text without Markdown.Ideas MUST be cool, I mean some application with fancy UI that will be interesting for users. We are creating application for demo, so it MUST be exiting.' })
        });
        const data = await res.json();
        text.innerText = data.reply || 'No response';
        text.style.opacity = "1";
        btn.style.display = 'none';
        result.style.display = 'block';
        retryBtn.disabled = false;
        retryBtn.innerText = "🔄 New idea";
    } catch(e) {
        btn.style.display = 'block';
        btn.disabled = false;
        btn.innerHTML = '✨ Generate an idea';
        result.style.display = 'none';
    }
}
</script>
"""


def require_auth(credentials: HTTPBasicCredentials = Depends(security)):
    if not BASIC_USER or not BASIC_PASS:
        raise HTTPException(
            status_code=500,
            detail="Authentication not configured on server"
        )
    ok_user = secrets.compare_digest(credentials.username, BASIC_USER)
    ok_pass = secrets.compare_digest(credentials.password, BASIC_PASS)
    if not (ok_user and ok_pass):
        raise HTTPException(
            status_code=401,
            detail="Unauthorized",
            headers={"WWW-Authenticate": "Basic"},
        )

def load_or_create_device_identity() -> dict[str, Any]:
    os.makedirs(os.path.dirname(OPENCLAW_DEVICE_KEY_FILE), exist_ok=True)

    if os.path.exists(OPENCLAW_DEVICE_KEY_FILE):
        with open(OPENCLAW_DEVICE_KEY_FILE, "rb") as f:
            seed = f.read()
    else:
        seed = os.urandom(32)
        with open(OPENCLAW_DEVICE_KEY_FILE, "wb") as f:
            f.write(seed)

    sk = SigningKey(seed)
    vk = sk.verify_key

    public_key_b64 = base64.b64encode(bytes(vk)).decode("ascii")
    device_id = hashlib.sha256(bytes(vk)).hexdigest()

    return {
        "signing_key": sk,
        "public_key": public_key_b64,
        "device_id": device_id,
    }


def build_device_auth_payload(
    *,
    device_id: str,
    client_id: str,
    client_mode: str,
    role: str,
    scopes: list[str],
    signed_at_ms: int,
    token: str,
    nonce: str,
) -> bytes:
    scopes_part = ",".join(scopes)
    payload = (
        f"v2|{device_id}|{client_id}|{client_mode}|{role}|"
        f"{scopes_part}|{signed_at_ms}|{token}|{nonce}"
    )
    return payload.encode("utf-8")


def sign_device_payload(signing_key: SigningKey, payload_bytes: bytes) -> str:
    signature = signing_key.sign(payload_bytes).signature
    return base64.b64encode(signature).decode("ascii")


class ChatRequest(BaseModel):
    message: str


class OpenClawWsClient:
    def __init__(self, ws_url: str, token: str, session_key: str, agent_id: str):
        self.ws_url = ws_url
        self.token = token
        self.session_key = session_key
        self.agent_id = agent_id
        self.ws = None

    async def __aenter__(self):
        self.ws = await websockets.connect(
            self.ws_url,
            open_timeout=20,
            ping_interval=20,
            ping_timeout=20,
            max_size=10 * 1024 * 1024,
        )
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if self.ws:
            await self.ws.close()

    async def send_json(self, payload: dict[str, Any]):
        raw = json.dumps(payload, ensure_ascii=False)
        logger.info("WS >>> %s", raw)
        await self.ws.send(raw)

    async def recv_json(self) -> dict[str, Any]:
        raw = await self.ws.recv()
        logger.info("WS <<< %s", raw)
        return json.loads(raw)

    async def rpc(self, method: str, params: dict[str, Any]) -> dict[str, Any]:
        req_id = str(uuid.uuid4())

        await self.send_json({
            "type": "req",
            "id": req_id,
            "method": method,
            "params": params,
        })

        while True:
            msg = await self.recv_json()
            if msg.get("type") == "res" and msg.get("id") == req_id:
                return msg

    async def connect(self) -> dict[str, Any]:
        challenge = await self.recv_json()

        if challenge.get("type") != "event" or challenge.get("event") != "connect.challenge":
            raise RuntimeError(f"Expected connect.challenge, got: {challenge}")

        payload = challenge.get("payload") or {}
        nonce = payload.get("nonce")
        if not nonce:
            raise RuntimeError(f"connect.challenge without nonce: {challenge}")

        ident = load_or_create_device_identity()

        client_id = "gateway-client"
        client_mode = "backend"
        role = "operator"
        scopes = [
            "operator.admin",
            "operator.read",
            "operator.write",
            "operator.approvals",
            "operator.pairing",
        ]
        signed_at_ms = int(time.time() * 1000)

        to_sign = build_device_auth_payload(
            device_id=ident["device_id"],
            client_id=client_id,
            client_mode=client_mode,
            role=role,
            scopes=scopes,
            signed_at_ms=signed_at_ms,
            token=self.token,
            nonce=nonce,
        )

        signature = sign_device_payload(ident["signing_key"], to_sign)

        req_id = str(uuid.uuid4())

        await self.send_json({
            "type": "req",
            "id": req_id,
            "method": "connect",
            "params": {
                "minProtocol": 3,
                "maxProtocol": 3,
                "client": {
                    "id": client_id,
                    "version": "face-web",
                    "platform": "linux",
                    "mode": client_mode,
                },
                "role": role,
                "scopes": scopes,
                "caps": ["tool-events"],
                "auth": {
                    "token": self.token,
                },
                "userAgent": "face-web/1.0",
                "locale": "en-US",
                "device": {
                    "id": ident["device_id"],
                    "publicKey": ident["public_key"],
                    "signature": signature,
                    "signedAt": signed_at_ms,
                    "nonce": nonce,
                },
            },
        })

        while True:
            msg = await self.recv_json()
            if msg.get("type") == "res" and msg.get("id") == req_id:
                if msg.get("ok") is False:
                    raise RuntimeError(f"connect failed: {msg}")
                return msg

    async def load_history(self) -> dict[str, Any]:
        return await self.rpc("chat.history", {
            "sessionKey": self.session_key
        })

    async def ensure_session_exists(self) -> None:
        sessions_res = await self.rpc("sessions.list", {})
        payload = sessions_res.get("payload") or sessions_res.get("result") or {}
        sessions = payload.get("sessions", []) if isinstance(payload, dict) else []

        for item in sessions:
            if isinstance(item, dict) and item.get("key") == self.session_key:
                return

        create_res = await self.rpc("sessions.create", {
            "key": self.session_key,
            "agentId": self.agent_id,
        })

        if create_res.get("ok") is False:
            raise RuntimeError(f"sessions.create failed: {create_res}")

    async def sessions_preview(self) -> dict[str, Any]:
        return await self.rpc("sessions.preview", {
            "keys": [self.session_key]
        })

    def _extract_text_from_content(self, content: Any) -> str:
        if isinstance(content, str):
            return content.strip()

        if isinstance(content, list):
            parts = []
            for item in content:
                if isinstance(item, dict) and item.get("type") == "text":
                    text = item.get("text")
                    if isinstance(text, str):
                        parts.append(text)
            return "".join(parts).strip()

        return ""

    def _extract_last_assistant_from_preview(self, payload: dict[str, Any]) -> str:
        previews = payload.get("previews", [])
        if not isinstance(previews, list):
            return ""

        for preview in previews:
            if not isinstance(preview, dict):
                continue
            if preview.get("key") != self.session_key:
                continue

            items = preview.get("items", [])
            if not isinstance(items, list):
                continue

            for item in reversed(items):
                if not isinstance(item, dict):
                    continue

                if item.get("role") == "assistant":
                    text = self._extract_text_from_content(item.get("content"))
                    if text:
                        return text

                message = item.get("message")
                if isinstance(message, dict) and message.get("role") == "assistant":
                    text = self._extract_text_from_content(message.get("content"))
                    if text:
                        return text

                text = item.get("text")
                if isinstance(text, str) and text.strip():
                    return text.strip()

        return ""

    async def send_chat(self, text: str) -> tuple[Optional[str], str]:
        await self.ensure_session_exists()
 
        req_id = str(uuid.uuid4())
        run_id: Optional[str] = None
        collected_parts: list[str] = []
 
        await self.send_json({
            "type": "req",
            "id": req_id,
            "method": "sessions.send",
            "params": {
                "key": self.session_key,
                "message": text,
            },
        })
 
        deadline = asyncio.get_running_loop().time() + OPENCLAW_TIMEOUT_SECONDS
 
        while True:
            remaining = deadline - asyncio.get_running_loop().time()
            if remaining <= 0:
                break
 
            try:
                msg = await asyncio.wait_for(self.recv_json(), timeout=remaining)
            except asyncio.TimeoutError:
                break
 
            if msg.get("type") == "res" and msg.get("id") == req_id:
                if msg.get("ok") is False:
                    raise RuntimeError(f"sessions.send failed: {msg}")
 
                payload = msg.get("payload") or msg.get("result") or {}
                if isinstance(payload, dict):
                    run_id = payload.get("runId") or run_id
 
                    # OpenClaw finished synchronously — previews in res, no runId, no events coming.
                    # Pull full text from chat.history instead of waiting for events.
                    if "previews" in payload and not run_id:
                        logger.info("sessions.send returned synchronous result, fetching full history")
                        history_res = await self.load_history()
                        history_payload = history_res.get("payload") or history_res.get("result") or {}
                        messages = history_payload.get("messages", [])
                        for m in reversed(messages):
                            if isinstance(m, dict) and m.get("role") == "assistant":
                                full_text = self._extract_text_from_content(m.get("content"))
                                if full_text:
                                    collected_parts.append(full_text)
                                    break
                        break  # No events expected, we're done
 
                continue
 
            if msg.get("type") != "event":
                continue
 
            payload = msg.get("payload", {})
            if not isinstance(payload, dict):
                continue
 
            if msg.get("event") == "session.message":
                if payload.get("sessionKey") != self.session_key:
                    continue
 
                message = payload.get("message", {})
                if isinstance(message, dict) and message.get("role") == "assistant":
                    text_part = self._extract_text_from_content(message.get("content"))
                    if text_part:
                        collected_parts.append(text_part)
 
                state = payload.get("state")
                if state == "final":
                    break
 
            if msg.get("event") == "agent":
                if run_id and payload.get("runId") != run_id:
                    continue
 
                if payload.get("stream") == "assistant":
                    data = payload.get("data", {})
                    if isinstance(data, dict):
                        delta = data.get("delta")
                        if isinstance(delta, str) and delta:
                            collected_parts.append(delta)
                            continue
 
                        full_text = data.get("text")
                        if isinstance(full_text, str) and full_text:
                            collected_parts.append(full_text)
                            continue
 
                if payload.get("stream") == "lifecycle":
                    data = payload.get("data", {})
                    if isinstance(data, dict) and data.get("phase") == "end":
                        break
 
            if msg.get("event") == "chat":
                if run_id and payload.get("runId") != run_id:
                    continue
 
                message = payload.get("message", {})
                if isinstance(message, dict):
                    text_part = self._extract_text_from_content(message.get("content"))
                    if text_part:
                        collected_parts.append(text_part)
 
                if payload.get("state") == "final":
                    break
 
        final_text = self._dedupe_and_join(collected_parts).strip()
 
        if not final_text:
            preview_res = await self.sessions_preview()
            logger.info("PREVIEW >>> %s", json.dumps(preview_res, ensure_ascii=False))
            preview_payload = preview_res.get("payload") or preview_res.get("result") or {}
            if isinstance(preview_payload, dict):
                final_text = self._extract_last_assistant_from_preview(preview_payload)
 
        if not final_text and collected_parts:
            final_text = collected_parts[-1].strip()
 
        if not final_text:
            final_text = "[empty reply from OpenClaw stream]"
 
        return run_id, final_text

    def _dedupe_and_join(self, parts: list[str]) -> str:
        if not parts:
            return ""

        out = ""
        for part in parts:
            if not part:
                continue

            if part.startswith(out):
                out = part
            elif out.startswith(part):
                continue
            else:
                out += part

        return out.strip()


# @app.get("/", response_class=HTMLResponse)
# async def read_root(request: Request, _=Depends(require_auth)):
#     return templates.TemplateResponse(request=request, name="index.html")


@app.get("/chat", response_class=HTMLResponse)
async def chat_page(request: Request, _=Depends(require_auth)):
    return templates.TemplateResponse(request=request, name="chat.html")


@app.get("/api/health")
async def api_health(_=Depends(require_auth)):
    return {
        "ok": True,
        "ws_url": OPENCLAW_WS_URL,
        "session_key": OPENCLAW_SESSION_KEY,
        "agent_id": OPENCLAW_AGENT_ID,
        "token_set": bool(OPENCLAW_GATEWAY_TOKEN),
        "device_key_file": OPENCLAW_DEVICE_KEY_FILE,
    }


@app.get("/api/debug/ws-connect")
async def debug_ws_connect(_=Depends(require_auth)):
    try:
        async with OpenClawWsClient(
            ws_url=OPENCLAW_WS_URL,
            token=OPENCLAW_GATEWAY_TOKEN,
            session_key=OPENCLAW_SESSION_KEY,
            agent_id=OPENCLAW_AGENT_ID,
        ) as client:
            result = await client.connect()
            return {"ok": True, "connect_result": result}
    except Exception as e:
        logger.exception("debug_ws_connect failed")
        return JSONResponse(
            status_code=500,
            content={"ok": False, "error": f"{type(e).__name__}: {repr(e)}"},
        )


@app.get("/api/debug/ws-history")
async def debug_ws_history( _=Depends(require_auth)):
    try:
        async with OpenClawWsClient(
            ws_url=OPENCLAW_WS_URL,
            token=OPENCLAW_GATEWAY_TOKEN,
            session_key=OPENCLAW_SESSION_KEY,
            agent_id=OPENCLAW_AGENT_ID,
        ) as client:
            await client.connect()
            history = await client.load_history()
            preview = await client.sessions_preview()
            return {
                "ok": True,
                "history": history,
                "preview": preview,
            }
    except Exception as e:
        logger.exception("debug_ws_history failed")
        return JSONResponse(
            status_code=500,
            content={"ok": False, "error": f"{type(e).__name__}: {repr(e)}"},
        )


@app.post("/api/chat")
async def api_chat(req: ChatRequest, _=Depends(require_auth)):
    text = req.message.strip()
    if not text:
        return {"status": "error", "reply": "Empty message"}

    try:
        async with OpenClawWsClient(
            ws_url=OPENCLAW_WS_URL,
            token=OPENCLAW_GATEWAY_TOKEN,
            session_key=OPENCLAW_SESSION_KEY,
            agent_id=OPENCLAW_AGENT_ID,
        ) as client:
            await client.connect()
            run_id, reply = await client.send_chat(text)

        return {
            "status": "success",
            "reply": reply,
            "runId": run_id,
        }

    except Exception as e:
        logger.exception("OpenClaw WS chat failed")
        return {
            "status": "error",
            "reply": f"OpenClaw WS error: {type(e).__name__}: {repr(e)}"
        }

@app.get("/ston.fi", response_class=HTMLResponse)
async def proxy_docs( _=Depends(require_auth)):
    with open("templates/docs.html", "r") as f:
        html = f.read()
    
    html = html.replace('</body>', WIDGET + '\n</body>')
    return HTMLResponse(content=html)