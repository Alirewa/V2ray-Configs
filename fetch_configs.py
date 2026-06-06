import requests
from bs4 import BeautifulSoup
import pytz
import jdatetime

SOURCES = [
    "https://t.me/s/Awlix_ir",
    "https://t.me/s/beiten",
    "https://t.me/s/beta_v2ray",
    "https://t.me/s/CloudCityy",
    "https://t.me/s/config_v2ray",
    "https://t.me/s/Configforvpn01",
    "https://t.me/s/ConfigsHubPlus",
    "https://t.me/s/configV2rayForFree",
    "https://t.me/s/configV2rayNG",
    "https://t.me/s/DailyV2RY",
    "https://t.me/s/DigiV2ray",
    "https://t.me/s/DirectVPN",
    "https://t.me/s/Easy_Free_VPN",
    "https://t.me/s/EliV2ray",
    "https://t.me/s/FalconPolV2rayNG",
    "https://t.me/s/forwardv2ray",
    "https://t.me/s/FOX_VPN66",
    "https://t.me/s/foxrayiran",
    "https://t.me/s/free4allVPN",
    "https://t.me/s/freeland8",
    "https://t.me/s/FreeNet1500",
    "https://t.me/s/FreeV2rays",
    "https://t.me/s/freev2rayssr",
    "https://t.me/s/FreeVlessVpn",
    "https://t.me/s/frev2ray",
    "https://t.me/s/frev2rayng",
    "https://t.me/s/God_CONFIG",
    "https://t.me/s/inikotesla",
    "https://t.me/s/iranvpnet",
    "https://t.me/s/iSeqaro",
    "https://t.me/s/mahsaamoon1",
    "https://t.me/s/MsV2ray",
    "https://t.me/s/napsternetv_config",
    "https://t.me/s/Network_442",
    "https://t.me/s/OutlineVpnOfficial",
    "https://t.me/s/ParsRoute",
    "https://t.me/s/PrivateVPNs",
    "https://t.me/s/proxystore11",
    "https://t.me/s/ServerNett",
    "https://t.me/s/Shadowlinkserverr",
    "https://t.me/s/ShadowSocks_s",
    "https://t.me/s/ShadowsocksM",
    "https://t.me/s/shadowsocksshop",
    "https://t.me/s/v2_team",
    "https://t.me/s/v2_vmess",
    "https://t.me/s/v2line",
    "https://t.me/s/V2pedia",
    "https://t.me/s/v2ray_ar",
    "https://t.me/s/v2ray_custom",
    "https://t.me/s/v2ray_for_free",
    "https://t.me/s/V2Ray_FreedomIran",
    "https://t.me/s/V2RAY_NEW",
    "https://t.me/s/v2ray_outlineir",
    "https://t.me/s/v2rayan",
    "https://t.me/s/v2RayChannel",
    "https://t.me/s/V2rayN_Free",
    "https://t.me/s/v2rayn_server",
    "https://t.me/s/v2rayng_org",
    "https://t.me/s/v2rayng_v",
    "https://t.me/s/v2rayNG_VPN",
    "https://t.me/s/V2RayOxygen",
    "https://t.me/s/ViPVpn_v2ray",
    "https://t.me/s/vmess_iran",
    "https://t.me/s/vmess_vless_v2rayng",
    "https://t.me/s/vmessiran",
    "https://t.me/s/VmessProtocol",
    "https://t.me/s/vmessq",
    "https://t.me/s/VorTexIRN",
    "https://t.me/s/VPN_443",
    "https://t.me/s/vpn_ocean",
    "https://t.me/s/vpn_proxy_custom",
    "https://t.me/s/vpn_tehran",
    "https://t.me/s/vpnmasi",
    "https://t.me/s/WeePeeN",
    "https://t.me/s/yaney_01",
    "https://t.me/s/YtTe3la",
    "https://t.me/s/vpn_xw",
    "https://t.me/s/azadi_az_inja_migzare",
    "https://t.me/s/reality_daily",
    "https://t.me/s/zen_cloud",
    "https://t.me/s/V2rayCollectorDonate",
    "https://t.me/s/iP_CF",
    "https://t.me/s/TLS_v2ray",
    "https://t.me/s/v2raycollector",
    "https://t.me/s/Cov2ray",
    "https://t.me/s/v2ray_cartel",
    "https://t.me/s/speedconfig00",
    "https://t.me/s/FOXNT",
    "https://t.me/s/EspinasVPN",
    "https://t.me/s/vpnsshocean",
    "https://t.me/s/filterkoshi",
    "https://t.me/s/ARv2ray",
    "https://t.me/s/Eleven_vpn",
    "https://t.me/s/freeownvpn",
    "https://t.me/s/msv2raynp",
    "https://t.me/s/Injastvpn",
    "https://t.me/s/Joker_v2ray_configs",
    "https://t.me/s/JOKERRVPN",
    "https://t.me/s/kvetch_matin",
    "https://t.me/s/mrsoulb",
    "https://t.me/s/Netifyvpn",
    "https://t.me/s/NETMelliAnti",
    "https://t.me/s/networld_vpn",
    "https://t.me/s/Prime_Verse",
    "https://t.me/s/SAVTEAM",
    "https://t.me/s/Shadownet021",
    "https://t.me/s/V2ray_Collector",
    "https://t.me/s/v2ray_hubb",
    "https://t.me/s/v2rayconfigsNN",
    "https://t.me/s/v2rayng_021",
    "https://t.me/s/V2RayNG_CaFe",
    "https://t.me/s/V2rayNG3",
    "https://t.me/s/v2rayserverfreenet",
    "https://t.me/s/v2xay",
    "https://t.me/s/vemssprotocol",
    "https://t.me/s/vpnaloo",
    "https://t.me/s/zeshtobad",
    "https://t.me/s/ProxyFn",
    "https://t.me/s/prrofile_purple",
    "https://t.me/s/shadowproxy66",
    "https://t.me/s/sinavm",
    "https://t.me/s/VPNCUSTOMIZE",
    "https://t.me/s/Outline_ir",
    "https://t.me/s/Pruoxyi",
    "https://t.me/s/v2ray_configs_pool",
    "https://t.me/s/v2ray_configs_pools",
    "https://t.me/s/ultrasurf_12",
    "https://t.me/s/V2RAY_VMESS_free",
    "https://t.me/s/FreakConfig",
    "https://t.me/s/v2rayNG_Matsuri",
    "https://t.me/s/meli_proxyy",
    "https://t.me/s/oneclickvpnkeys",
    "https://t.me/s/Outline_Vpn",
    "https://t.me/s/proxy_kafee",
    "https://t.me/s/v2ray_sub",
    "https://t.me/s/SaghiVpnX",
    "https://t.me/s/Daily_Configs",
    "https://t.me/s/customv2ray",
    "https://t.me/s/UnlimitedDev",
    "https://t.me/s/vmessorg",
    "https://t.me/s/v2rayngvpn",
    "https://t.me/s/SafeNet_Server",
    "https://t.me/s/vmesskhodam",
    "https://t.me/s/singbox1",
    "https://t.me/s/Viturey",
    "https://t.me/s/pPal03",
    "https://t.me/s/Rayan_Config",
    "https://t.me/s/info_2it_channel",
    "https://t.me/s/lexernet",
    "https://t.me/s/AblNet7",
    "https://t.me/s/manzariyeh_rasht",
]

SCHEMES = ("vmess://", "vless://", "ss://", "trojan://")

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}


def fetch_page(url: str) -> str:
    try:
        r = requests.get(url.strip(), headers=HEADERS, timeout=15)
        r.raise_for_status()
        return r.text
    except Exception as e:
        print(f"[SKIP] {url} — {e}")
        return ""


def extract_configs(html: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    results = []
    for tag in soup.find_all("code"):
        text = tag.get_text(separator="\n").strip()
        for line in text.splitlines():
            line = line.strip()
            if any(line.startswith(s) for s in SCHEMES):
                # Strip the comment/label fragment (#...) at the end
                clean = line.split("#")[0].rstrip()
                if clean:
                    results.append(clean)
    return results


def main():
    all_configs: list[str] = []

    for url in SOURCES:
        html = fetch_page(url)
        if html:
            found = extract_configs(html)
            print(f"[OK] {url.split('/')[-1]:30s} → {len(found)} configs")
            all_configs.extend(found)

    # Deduplicate while preserving first-seen order
    seen: set[str] = set()
    unique: list[str] = []
    for c in all_configs:
        if c not in seen:
            seen.add(c)
            unique.append(c)

    now = jdatetime.datetime.now(pytz.timezone("Asia/Tehran"))
    date_str = now.strftime("%Y/%m/%d")
    time_str = now.strftime("%H:%M")
    header = f"# به‌روزرسانی: {date_str} ساعت {time_str} | {len(unique)} کانفیگ"

    with open("config.txt", "w", encoding="utf-8") as f:
        f.write(header + "\n")
        for i, cfg in enumerate(unique, start=1):
            label = f"#{i} | {date_str}"
            f.write(f"{cfg}{label}\n")

    print(f"\n✅ {len(unique)} unique configs saved to config.txt")


if __name__ == "__main__":
    main()
