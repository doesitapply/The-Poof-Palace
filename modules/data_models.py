from dataclasses import dataclass
from typing import Optional

@dataclass
class SocialPost:
    """Represents a piece of content ready to be published."""
    image_path: str
    caption: str
    alt_text: str
    source_idea: Optional[str] = None

@dataclass
class CommunityTrend:
    """Represents a trend or popular idea from the community."""
    platform: str
    content: str
    engagement_score: int
