# Free V2Ray Configs — Auto-Updated Every 30 Minutes

> Free, fresh v2ray subscription links updated automatically every 30 minutes
> from 180+ Telegram channels and GitHub aggregators.
> Pure raw output — works with any V2Ray client or Telegram bot.

---

## Subscription Links

### Main (2000 configs — full pool)

```
https://raw.githubusercontent.com/Alirewa/v2ray-configs/main/config.txt
```

### Sub 1 — Top 100 (highest quality)

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

> Sub files rank configs by health signals: TLS/REALITY security, port 443,
> domain names, SNI, and WebSocket — higher score = top of the list.

---

## Supported Protocols

| Protocol | Description |
|----------|-------------|
| `vless://` | VLESS — lightweight, modern |
| `vmess://` | VMess — original V2Ray protocol |
| `trojan://` | Trojan — disguised as HTTPS |
| `ss://` | Shadowsocks — fast and portable |

---

## How to Use

### Android — V2RayNG
1. Open V2RayNG → menu → **Subscription group settings**
2. Tap **+** → paste one of the URLs above → Save
3. Menu → **Update subscription** → connect

### iOS — Shadowrocket / Streisand
1. Tap **+** → Type: Subscribe → paste URL → Save
2. Tap Update to fetch configs

### Windows / macOS — V2RayN / Hiddify
1. Servers → Add subscription → paste URL → OK
2. Right-click subscription → Update

### Telegram Bot / Script

```bash
curl -s https://raw.githubusercontent.com/Alirewa/v2ray-configs/main/sub1.txt
```

---

## How It Works

```
Telegram (180+ channels)  ─┐
                            ├─► fetch_configs.py ─► dedup ─► config.txt (2000)
GitHub (20 repos)          ─┘                           └─► sub1/2/3.txt (100 each)
```

- GitHub Actions cron runs every 30 minutes (`:00` and `:30`)
- Scrapes Telegram public channel pages and GitHub raw sub files
- Deduplicates by exact string and by UUID
- Caps at 2000 unique configs for `config.txt`
- Scores all configs by quality → top 300 split into `sub1`, `sub2`, `sub3`

---

## Quality Score Signals

| Signal | Points |
|--------|--------|
| `security=reality` | +4 |
| `security=tls` or `trojan://` | +3 |
| Port 443 or 8443 | +2 |
| Domain name (not raw IP) | +2 |
| SNI or Host header set | +1 |
| WebSocket / path set | +1 |

---

## Stats

- **2000** configs in main sub — updated every 30 min
- **300** quality-ranked configs in sub1/sub2/sub3
- **180+** Telegram sources + **20** GitHub sources
- UUID-level deduplication (no duplicate servers)

---

## Keywords

`v2ray config free` · `free vless config` · `vmess config free` · `trojan config`
`v2ray subscription link` · `v2rayNG sub` · `free proxy 2025` · `xray config`
`shadowsocks free` · `v2ray sub url` · `free vpn config` · `v2ray free server`
`vless subscription` · `reality config` · `کانفیگ رایگان` · `سابسکریپشن v2ray`

---

## Disclaimer

Configs are collected from publicly available Telegram channels and GitHub repos.
Use responsibly and in accordance with your local laws.
