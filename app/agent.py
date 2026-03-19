import os

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.tools import tool

from dotenv import load_dotenv

from langgraph.prebuilt import create_react_agent


load_dotenv()


llm = ChatGoogleGenerativeAI(

    model="gemini-2.0-flash",

    google_api_key=os.environ.get("GOOGLE_API_KEY")

)


@tool

def get_trending_topics(platform: str) -> str:

    """Get trending topics for a given social media platform.

    Use this when the user asks about what content is currently popular."""

    # Your actual implementation here

    return f"Trending topics for {platform}: AI art, productivity tips, behind-the-scenes content"


system_prompt = """You are AlgoRhythm, a content creator assistant.

You help creators plan posts, choose hashtags, and identify trending topics.

Use your tools when the user asks about trends or platform-specific content."""


@tool
def get_content_ideas(niche: str) -> str:
    """Get content format ideas for a given niche or topic.
    Use this when the user asks for content ideas, formats, or creative suggestions."""
    return (
        f"Content ideas for {niche}: "
        "1) Carousel post — break down a common myth in your niche into 5 slides. "
        "2) Reel — show a before and after transformation in 30 seconds. "
        "3) Story series — share 3 quick tips over 3 consecutive days. "
        "4) Long-form video — do a full tutorial or deep dive on a topic your audience keeps asking about."
    )



agent = create_react_agent(

    model=llm,

    tools=[get_trending_topics, get_content_ideas],

    prompt=system_prompt

)

