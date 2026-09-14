# pocai

Serveur MCP (Model Context Protocol) construit avec [FastMCP](https://gofastmcp.com).

## Structure

- `server.py` — définit le serveur MCP (`mcp = FastMCP("pocai")`) et ses tools.
- `requirements.txt` — dépendances Python (`fastmcp`).

## Tools MCP disponibles

### `getTemperature`

- **Paramètre** : `city` (string)
- **Retour** : objet JSON `{ "temperature": number, "humidity": number }`
- Les valeurs sont actuellement simulées aléatoirement (pas d'appel à une API météo externe).

## Lancer le serveur

```bash
.venv/Scripts/python.exe server.py
```

Le serveur est lancé en transport HTTP sur le port 8080, exposé sur le path `/mcp-weather` (`http://127.0.0.1:8080/mcp-weather`).

## Conventions

- Les tools sont déclarés avec le décorateur `@mcp.tool` sur des fonctions Python.
- Le schéma de sortie d'un tool est dérivé du type de retour annoté (ici un modèle Pydantic `WeatherReading`) afin que les clients MCP reçoivent un schéma JSON explicite plutôt qu'un simple `dict`.

## Divers
Si tu crées de nouveaux fichiers et qu'ils doivent être sur le repo, exécute git add sur ces fichiers
