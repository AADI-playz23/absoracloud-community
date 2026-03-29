import json
import os
import sys
import time

# Note: In production, this file path will be passed dynamically by the GitHub Action
POST_FILE_PATH = os.environ.get("POST_FILE", "dummy.json")

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def save_comment(post_id, author, body):
    timestamp = int(time.time())
    safe_name = author.replace(" ", "")
    filename = f"db/comments/{post_id}/{timestamp}_{safe_name}.json"
    
    os.makedirs(f"db/comments/{post_id}", exist_ok=True)
    
    comment_data = {
        "id": timestamp,
        "author": author,
        "body": body,
        "upvotes": 0
    }
    
    with open(filename, 'w') as f:
        json.dump(comment_data, f, indent=2)
    print(f"Comment saved to {filename}")

def main():
    try:
        user_post = load_json(POST_FILE_PATH)
    except Exception as e:
        print(f"Error loading post: {e}")
        sys.exit(1)

    category = user_post.get("category", "").lower()
    body_text = user_post.get("body", "").lower()

    # Only trigger if the user actually requested the bot
    if "#absoraai" not in body_text:
        print("Bot not mentioned. Exiting.")
        sys.exit(0)

    # 1. THE STAFF INTERCEPT: Block AI from answering VPS/MC configs
    if category in ["vps", "mchost", "minecraft"]:
        reply_body = f"Hello {user_post['author']}! VPS and Minecraft Server configurations require manual staff assistance to ensure accuracy. Please edit your post and tag #absoracloud so a human technician can help you directly."
        save_comment(user_post['id'], "AbsoraBot", reply_body)
        print("Intercepted: Sent staff redirect message.")
        sys.exit(0) 

    # 2. NORMAL AI ROUTING: Web Hosting & Storage
    print("Routing to Gemini API...")
    
    doc_path = ""
    if category == "webdisk" or category == "webhosting":
        doc_path = "docs/web_hosting.md"
    elif category == "storage" or category == "cloudstorage":
        doc_path = "docs/cloud_storage.md"
    
    # Check if we have docs for this category
    if doc_path and os.path.exists(doc_path):
        with open(doc_path, 'r') as f:
            system_context = f.read()
        
        # --- GEMINI API CALL WOULD GO HERE ---
        # Example:
        # response = gemini.generate_content(
        #     f"System Context: {system_context}\n\nUser Question: {user_post['body']}"
        # )
        # save_comment(user_post['id'], "AbsoraBot", response.text)
        
        print(f"Successfully processed query for {category} using {doc_path}")
    else:
        # Fallback if category is weird or docs are missing
        save_comment(user_post['id'], "AbsoraBot", f"I'm sorry {user_post['author']}, I don't have enough information to answer that right now. Please tag #absoracloud for human assistance!")

if __name__ == "__main__":
    main()
