# Oracle Terminal (Hardened & Private)

A dedicated, hardened terminal application for your Oracle server.
This project is now configured for **Private-Only Access** via Tailscale.

## Features

- **Tailscale Only:** The terminal is bound EXCLUSIVELY to your Tailscale IP (`100.75.79.110`), making it invisible to the public internet.
- **Layered Security:** Includes Basic Authentication (`admin:oracle-root-access`) as a second layer of defense.
- **Session Persistence:** Automatically uses `tmux` with a default session (`root-session`), ensuring your work stays alive even if you disconnect.
- **Session Manager:** Includes a custom `menu` tool for managing sessions, windows, and system status.
- **Root-Level Access:** Runs as a privileged container with `chroot` to the host filesystem.

---

## Accessing the Terminal

1.  **Connect to Tailscale:** Ensure your device (phone, laptop) is connected to your Tailnet.
2.  **Open URL:** Visit: `http://100.75.79.110:7681`
3.  **Login:**
    - **User:** `admin`
    - **Password:** `oracle-root-access`

---

## Session Management (The "menu" tool)

Once logged in, type:
```bash
menu
```
This interactive manager allows you to:
1.  **List All Sessions:** View active tmux sessions.
2.  **Kill Current Session:** Force a reset if the session becomes unresponsive.
3.  **New Window:** Open a new window within the same session.
4.  **System Status:** Quick view of server health via `htop`.

---

## Server Setup & Maintenance

The active configuration is located on the Oracle server at `/opt/oracle-terminal/`.

### Configuration Files
- `server/docker-compose.yml`: Defines the `ttyd` service with Tailscale IP binding and host filesystem access.
- `server/term-menu.sh`: The source for the interactive session manager (installed at `/usr/local/bin/term-menu`).

### Manual Installation
To re-install the session manager on the server:
```bash
sudo cp server/term-menu.sh /usr/local/bin/term-menu
sudo chmod +x /usr/local/bin/term-menu
sudo bash -c 'echo "alias menu=/usr/local/bin/term-menu" > /etc/profile.d/terminal-menu.sh'
```

### Restarting the Service
```bash
cd /opt/oracle-terminal
docker-compose down
docker-compose up -d
```

---

## Development & Backup

- **Sync from Server:** Use `scp` to pull the active `docker-compose.yml` and `term-menu.sh` back to this repository.
- **GitHub:** This repository serves as the definitive backup for the hardened terminal state.
