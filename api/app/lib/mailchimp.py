import logging
import mailchimp_marketing as MailchimpMarketing
from app import app as flask_app

LOG = logging.getLogger(__name__)

class MailChimpClient:
    """Mailchimp client API."""

    def __init__(self):
        """Initialize mailchimp client."""

        self.client = MailchimpMarketing.Client()
        client.set_config({"api_key": flask_app.config["MAILCHIMP_API_KEY"]})
