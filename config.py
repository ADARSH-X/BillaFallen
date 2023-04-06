from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("17704723"))
API_HASH = getenv("3976907b2e519cae8e7bae986ebaf0b1")

BOT_TOKEN = getenv("6161598035:AAF2AnlPr6NtfEe8qTa2ZdtRZ8ao1t9tD3Y", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("5747046335"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/cde4dc3ccfef4ef74f63f.jpg")

SESSION = getenv("BQAWa9PiF4RFENdFQB87lAcjtecriHocBRldo45ulVMYafqxOVofw8-ZOXU0Zn5YlTS_YKb-CLalLRW6Wk7uzvB2hCIs5BbRCebJR4J6n-4gu5Hdo9f1jgCaR02sGKhmU97lay9SRq9eI-DDXSuAcl8YD2c39cFZ5HdGy-ffIeseOF8NGm6LevcRkLQKaydpZGZfrZCVbgV0V65y8wXgvDqxRvArD_VYrctZ1mCyRAviPV-SmrVoJPB-doa356tJGhI-fgd4AZUyq4qK0gb3AWpZl-lBb2ZokSBZGW3WgkCvMMlaSh6Q-g6jrHBOpD94RXBkfiMXnwJknLHU_3rBA0_tAAAAAXYYYxcA", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DramaticClubb")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/dramaticsticker")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
