# AbsoraCloud Web Hosting - Official Documentation

## 1. Plans, Storage, and Slot Limits
AbsoraCloud offers four distinct web hosting tiers. Users are restricted to a specific number of active instances (slots) and storage quotas based on their plan:

* **Starter Plan:** 1 Slot Maximum | 500MB Storage Limit
* **Developer Plan:** 2 Slots Maximum | 50GB Storage Limit
* **Professional Plan:** 5 Slots Maximum | 200GB Storage Limit
* **Studio Plan:** 10 Slots Maximum | 1TB Storage Limit

## 2. Uptime and Node Lifecycles
The Absora Engine handles server uptime differently depending on the user's active tier:
* **Starter Plan (Ephemeral Nodes):** Starter instances are designed for temporary testing. They have a strict 6-hour lifecycle. After 6 hours of uptime, the engine will automatically shut down the instance and mark the slot as offline. Users must manually reactivate it.
* **Premium Plans (Developer, Professional, Studio):** These plans feature 24/7 continuous uptime. The backend engine utilizes a Smart Keep-Alive system that seamlessly relays the server state before standard timeout limits are reached, ensuring zero downtime.

## 3. Network Routing and Domains
* **Subdomains:** All active slots automatically receive a secure, proxied subdomain routed through the AbsoraCloud DNS network.
* **Custom Domains:** Dedicated custom domain linking is exclusively available and automatically enforced for users on the **Studio Plan**.

## 4. File Management and Security Protocols
Every active web hosting slot comes with a secure, built-in PHP file manager accessed via `/upload.php`. 
* **Storage Quotas:** The system actively calculates directory size upon every upload. If a file exceeds the user's plan limit, the upload is blocked.
* **Executable Blocking (Anti-Malware):** For security purposes, users are strictly prohibited from uploading server-side executables. The system will automatically block and reject files with the following extensions: `.php`, `.sh`, `.py`, `.cgi`, and `.htaccess`. Only static web files are permitted.
