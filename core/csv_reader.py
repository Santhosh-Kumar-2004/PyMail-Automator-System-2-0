import pandas as pd
import re
import os
from core.logger_config import logger

# Regex pattern for email validation
EMAIL_PATTERN = r"^[\w\.-]+@[\w\.-]+\.\w+$"

def load_recipients(csv_path="data/recipients.csv"):
    """Read and validate recipient emails from CSV."""
    if not os.path.exists(csv_path):
        logger.error(f"❌ Recipients file not found at: {csv_path}")
        return []

    try:
        df = pd.read_csv(csv_path)
        valid_recipients = []

        for _, row in df.iterrows():
            name = str(row.get("name", "")).strip()
            email = str(row.get("email", "")).strip()

            if re.match(EMAIL_PATTERN, email):
                valid_recipients.append({"name": name, "email": email})
            else:
                logger.warning(f"⚠️ Invalid email skipped: {email}")

        logger.info(f"✅ Loaded {len(valid_recipients)} valid recipients.")
        return valid_recipients

    except Exception as e:
        logger.error(f"Error reading recipients: {e}")
        return []
