import os
from mastodon import Mastodon
from config import MASTODON_BASE_URL, MASTODON_ACCESS_TOKEN
from openrouter import SocialMediaPost

# ------------------------
# Initialize Mastodon client
# ------------------------
if not MASTODON_ACCESS_TOKEN or not MASTODON_BASE_URL:
    raise RuntimeError("Mastodon API credentials not set in .env")

mastodon = Mastodon(
    access_token=MASTODON_ACCESS_TOKEN,
    api_base_url=MASTODON_BASE_URL,
)

# ------------------------
# Function to post content
# ------------------------
def post_to_mastodon(post: SocialMediaPost, image_path: str | None = None, dry_run: bool = True):
    """
    Posts a SocialMediaPost to Mastodon.
    If dry_run=True, just prints what would be posted.
    """
    # Combine caption + hashtags
    MAX_STATUS_LENGTH = 500
    content = f"{post.caption}\n\n{post.hashtags}"
    content = content[:MAX_STATUS_LENGTH]  # truncate to Mastodon limit

    if dry_run:
        print("=== DRY RUN ===")
        print("Caption + Hashtags:")
        print(content)

        if image_path:
            print("Image path:", image_path)
            print("Image prompt (optional, not posted):", post.image_prompt)
        else:
            print("No image provided")
        
        print("================")
        return

    try:
        media_ids = None

        # Upload image if provided
        if image_path:
            media = mastodon.media_post(
                image_path,
                # description=post.image_prompt  # alt-text (good practice)
            )
            media_ids = [media["id"]]

        # Create status
        mastodon.status_post(
            status=content,
            media_ids=media_ids
        )

        # FIX: Fixed emoji encoding
        print("✅ Successfully posted to Mastodon!")

    except Exception as e:
        # FIX: Fixed emoji encoding
        print("❌ Failed to post to Mastodon:", e)