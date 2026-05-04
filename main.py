from fastmcp import FastMCP
import httpx
import os

mcp = FastMCP("369Management - Systeme.io")

API_KEY = os.environ.get("SYSTEMEIO_API_KEY", "7lxs70h8xs23wnumucqls0sedbdxn40cjbqclxs67myr91obvmik5iye1bma179e")
BASE_URL = "https://api.systeme.io/api"
HEADERS  = {"X-API-Key": API_KEY, "Content-Type": "application/json"}

@mcp.tool()
async def lister_produits():
    """Liste tous les produits digitaux"""
    async with httpx.AsyncClient() as c:
        r = await c.get(f"{BASE_URL}/products", headers=HEADERS)
        return r.json()

@mcp.tool()
async def creer_produit(nom: str, prix: float, description: str = ""):
    """Crée un nouveau produit digital"""
    payload = {"name": nom, "price": prix, "description": description}
    async with httpx.AsyncClient() as c:
        r = await c.post(f"{BASE_URL}/products", json=payload, headers=HEADERS)
        return r.json()

@mcp.tool()
async def lister_commandes():
    """Liste les commandes et ventes"""
    async with httpx.AsyncClient() as c:
        r = await c.get(f"{BASE_URL}/orders", headers=HEADERS)
        return r.json()

@mcp.tool()
async def lister_contacts():
    """Liste les contacts et leads"""
    async with httpx.AsyncClient() as c:
        r = await c.get(f"{BASE_URL}/contacts", headers=HEADERS)
        return r.json()

if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=8000)