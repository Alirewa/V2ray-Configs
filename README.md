<div align="center">

# 🔒 Free V2Ray / Xray Configs

> Free, fresh, and ready-to-use V2Ray & Xray subscription links — auto-updated every 30 minutes from 180+ Telegram channels and verified GitHub sources. No login. No ads. Just copy and use.

[![Auto-Updated](https://img.shields.io/badge/Auto--Updated-Every_30_min-4ade80?style=for-the-badge)](https://raw.githubusercontent.com/Alirewa/v2ray-configs/main/config.txt)
[![Sources](https://img.shields.io/badge/Sources-180%2B_Channels-2CA5E0?style=for-the-badge)](https://github.com/Alirewa/v2ray-configs)
[![Configs](https://img.shields.io/badge/Configs-2000%2B-orange?style=for-the-badge)](https://raw.githubusercontent.com/Alirewa/v2ray-configs/main/config.txt)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

</div>

---

## ⚡ Subscription Links

### Main — 2000 configs (full pool)

```
https://raw.githubusercontent.com/Alirewa/v2ray-configs/main/config.txt
```

### Sub 1 — Top 100 (highest quality, TLS/REALITY priority)

```
https://raw.githubusercontent.com/Alirewa/v2ray-configs/main/sub1.txt
```

### Sub 2 — Next 100 (high quality)

```
https://raw.githubusercontent.com/Alirewa/v2ray-configs/main/sub2.txt
```

### Sub 3 — Next 100 (good quality)

```
https://raw.githubusercontent.com/Alirewa/v2ray-configs/main/sub3.txt
```

> One config per line — raw format, directly usable in any V2Ray / Xray client or Telegram bot.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Stats](#-stats)
- [Supported Protocols](#-supported-protocols)
- [Compatible Clients](#-compatible-clients)
- [How to Use](#-how-to-use)
- [How It Works](#-how-it-works)
- [License](#-license)

---

## 📖 Overview

This repository provides a **free, automatically maintained** collection of V2Ray and Xray proxy configurations. The configs are scraped from 180+ public Telegram channels and top GitHub aggregators, deduplicated, and refreshed every 30 minutes via a GitHub Actions workflow — so you always get fresh, working configs.

---

## 📊 Stats

| Item | Value |
|---|---|
| 🔄 Update interval | Every 30 minutes |
| 📡 Sources | 180+ Telegram channels + 20 GitHub repos |
| 🔢 Main pool | 2,000 configs (after full deduplication) |
| ⭐ Sub files | sub1/sub2/sub3 — 100 quality-ranked configs each |
| 🧹 Dedup method | Exact string + UUID/identifier matching |
| 📄 Output format | Raw — one config per line (bot/client ready) |
| 🆓 Cost | Free forever |

### Quality Score (for sub files)

| Signal | Points |
|--------|--------|
| `security=reality` | +4 |
| `security=tls` or `trojan://` | +3 |
| Port 443 or 8443 | +2 |
| Domain name (not raw IP) | +2 |
| SNI / Host header set | +1 |
| WebSocket / path set | +1 |

---

## 🌐 Supported Protocols

| Protocol | Included |
|---|---|
| VLESS | ✅ |
| VMess | ✅ |
| Trojan | ✅ |
| Shadowsocks | ✅ |
| WireGuard | ✅ |
| Hysteria2 | ✅ |

---

## 📱 Compatible Clients

| Platform | Recommended Client |
|---|---|
| Android | v2rayNG, Hiddify |
| iOS | Streisand, Shadowrocket |
| Windows | v2rayN, Hiddify |
| macOS | V2Box, Hiddify |
| Linux | v2ray-core, Xray-core |

---

## 🚀 How to Use

1. Copy the subscription link above
2. Open your V2Ray / Xray client
3. Add a new **subscription** and paste the link
4. Click **Update** — done!

---

## ⚙️ How It Works

1. A scheduled GitHub Actions workflow runs every 30 minutes
2. It scrapes configured Telegram channels and GitHub sources
3. Configs are deduplicated by exact string and UUID
4. The cleaned list is written to `config.txt` and committed
5. The raw file URL is always up-to-date and ready to use

---

## 📄 License

Distributed under the **MIT License** — free to use, modify, and distribute.

---

<div align="center">

Made with ❤️ by [Alirewa](https://github.com/Alirewa)

</div>
