from .api_clients import OllamaClient, ComfyUIClient, InstagramClient, TikTokClient, TwitterClient
from .data_models import SocialPost
import os
import datetime

class Orchestrator:
    def __init__(self, config):
        self.config = config
        self.ollama = OllamaClient(config)
        self.comfy = ComfyUIClient(config)
        self.instagram = InstagramClient(config)
        self.tiktok = TikTokClient(config)
        self.twitter = TwitterClient(config)
        # self.shopify = ShopifyClient(config)

    def run_daily_content_cycle(self):
        """Generates and posts one piece of standard content."""
        print("--- Running Daily Content Cycle ---")
        
        # 1. Get a content idea
        idea_prompt = "Give me a simple, one-sentence idea for an illustration of Lil Poof. Focus on a classic cat behavior like napping, playing, or being mischievous."
        system_prompt_idea = "You are a creative director for The Poof Palace brand."
        idea = self.ollama.generate_text(system_prompt_idea, idea_prompt)
        print(f"Generated Idea: {idea}")

        # 2. Generate the image
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        image_filename = f"pp_{timestamp}.png"
        image_path = os.path.join(self.config['IMAGE_OUTPUT_DIR'], image_filename)
        
        image_success = self.comfy.generate_image(subject_prompt=idea, output_path=image_path)
        
        if not image_success:
            print("Failed to generate image. Aborting cycle.")
            return

        # 3. Generate the caption and alt text
        caption_prompt = f"Write a witty, regal caption from the perspective of Lil Poof for an image depicting: '{idea}'. Include 3-5 relevant hashtags."
        alt_text_prompt = f"Write a descriptive alt text for an image of: '{idea}' in a whimsical storybook style."
        system_prompt_caption = "You are Lil Poof, the cat queen of The Poof Palace. You are witty, regal, and slightly dramatic."
        
        caption = self.ollama.generate_text(system_prompt_caption, caption_prompt)
        alt_text = self.ollama.generate_text(system_prompt_caption, alt_text_prompt)
        print(f"Generated Caption: {caption}")

        # 4. Create the social post object
        post = SocialPost(image_path=image_path, caption=caption, alt_text=alt_text, source_idea=idea)
        
        # 5. Publish to all platforms
        print("📱 Publishing to social media platforms...")
        
        # Instagram
        instagram_success = self.instagram.post_image(post.image_path, post.caption)
        
        # Twitter (shorter caption)
        twitter_caption = self._create_twitter_caption(caption)
        twitter_success = self.twitter.post_tweet(twitter_caption, post.image_path)
        
        # TikTok (video content - using placeholder for now)
        tiktok_success = self.tiktok.post_video("output/videos/placeholder.mp4", caption)
        
        print("--- Content Cycle Complete ---")
        print(f"📊 Platform Results:")
        print(f"   Instagram: {'✅' if instagram_success else '❌'}")
        print(f"   Twitter: {'✅' if twitter_success else '❌'}")
        print(f"   TikTok: {'✅' if tiktok_success else '❌'}")

    def _create_twitter_caption(self, instagram_caption: str) -> str:
        """Create a Twitter-appropriate caption (shorter, under 280 chars)."""
        twitter_prompt = f"Create a Twitter version of this Instagram caption (under 280 characters, keep the royal personality): '{instagram_caption}'"
        system_prompt = "You are Lil Poof, the cat queen. Create witty, royal Twitter posts."
        
        twitter_caption = self.ollama.generate_text(system_prompt, twitter_prompt)
        
        # Ensure it's under 280 characters
        if len(twitter_caption) > 280:
            twitter_caption = twitter_caption[:277] + "..."
            
        return twitter_caption

    def run_community_analysis_cycle(self):
        """Placeholder for analyzing community trends."""
        print("--- Analyzing Community Trends (Not Implemented) ---")
        # In the future, this would scrape Reddit/X, find top comments,
        # and return a CommunityTrend object.
        pass

    def run_product_poll_cycle(self):
        """Placeholder for creating and posting a product poll."""
        print("--- Running Product Poll Cycle (Not Implemented) ---")
        # 1. Generate 3 image variations on a theme.
        # 2. Create a carousel post with a poll.
        # 3. Post to Instagram.
        pass
