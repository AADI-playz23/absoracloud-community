# AbsoraCloud Storage - Official Documentation

## 1. System Architecture
AbsoraCloud Storage is a high-speed, standalone file hosting service. User accounts, passwords, and active storage plans are managed via a central database, while the actual files are stored securely across multiple global nodes to ensure redundancy.

## 2. Storage Plans & Quotas
Users are assigned a strict capacity limit based on their active plan:
* **Free Plan:** 3.75 GB Storage Space
* **Plus Plan:** 8 GB Storage Space (Price: ₹99)
* **Pro Plan:** 12 GB Storage Space (Price: ₹199)
* **Max Plan:** 15 GB Storage Space (Price: ₹299)

## 3. Account Registration & Limits
* If a user logs in with an unregistered username, the system automatically creates a new account for them on the Free Plan.
* **Password Requirement:** Passwords must be at least 6 characters long.
* **Username Requirement:** Usernames must be between 3 and 50 characters, containing only letters, numbers, and underscores (no spaces or special characters).

## 4. The Payment & Upgrade Workflow
Upgrading storage plans is handled via an automated UPI system:
1. The user selects a premium plan and scans the generated UPI QR code.
2. The user must upload a screenshot of the successful transaction.
3. The system securely archives the payment proof and instantly upgrades the user's database entry, unlocking the new storage capacity immediately.
