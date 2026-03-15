# Oracle Terminal (Standalone)

A dedicated, standalone terminal application for your Oracle server.
This project consists of two parts:
1.  **Server:** A Docker container running `ttyd` (web terminal) + `cloudflared` (tunnel).
2.  **Client:** A lightweight Windows application (Python) that connects to the terminal.

## Prerequisites

- **Server:** Docker & Docker Compose installed on your Oracle Server.
- **Client:** Python 3.10+ installed on your Windows laptop.
- **Cloudflare:** A Cloudflare account for creating the tunnel.

---

## Part 1: Server Setup

1.  **Create a Cloudflare Tunnel:**
    Run this on your local machine (or server) if you have `cloudflared` installed:
    ```bash
    cloudflared tunnel login
    cloudflared tunnel create oracle-term
    ```
    This will generate a UUID and a credentials JSON file (e.g., `~/.cloudflared/<UUID>.json`).

2.  **Prepare Server Files:**
    Copy the `server/` directory from this project to your Oracle server (e.g., to `~/oracle-terminal`).

3.  **Configure Tunnel:**
    - Copy your tunnel credentials JSON file to `server/credentials.json`.
    - Edit `server/config.yml`:
        - Replace `<TUNNEL_UUID>` with your tunnel's UUID.
        - Update `hostname` (e.g., `terminal-app.suras.org`) to your desired domain.

4.  **Route DNS:**
    In your Cloudflare Dashboard (DNS), create a **CNAME** record:
    - Name: `terminal-app` (or whatever hostname you chose)
    - Target: `<UUID>.cfargotunnel.com`

5.  **Start the Service:**
    SSH into your server and run:
    ```bash
    cd ~/oracle-terminal
    docker-compose up -d
    ```
    
    *Security Note:* This exposes your root shell to the internet via the tunnel. Ensure you configure **Cloudflare Access (Zero Trust)** for this hostname to add an authentication layer (e.g., limit to your email only).

---

## Part 2: Client Setup (Windows)

1.  **Install Python:**
    Ensure Python is installed. Download from python.org if needed.

2.  **Install Dependencies:**
    Open PowerShell in the `client/` folder and run:
    ```powershell
    pip install -r requirements.txt
    ```

3.  **Configure App:**
    Edit `client/app.py`:
    - Update `TERMINAL_URL` to match the hostname you configured in Part 1.

4.  **Run the App:**
    Double-click `client/app.py` or run:
    ```powershell
    python client/app.py
    ```

## Notes
- **Full Access:** The terminal runs as `root` inside the container but is `chroot`ed to the host filesystem. You have full control over the server.
- **Independence:** This setup is completely separate from InfraGem or other services. It runs in its own network stack.
