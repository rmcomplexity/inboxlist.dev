import os
import tempfile

import pytest

from app import app


@pytest.fixture
def client():
    """Creates a Flask test client."""

    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    with app.test_client() as client:
        # with app.app_context():
        #    app.init_db()
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])


@pytest.fixture
def mail_chimp_client():
    """Creates a mock mailchipm client."""

    class MailChimpLists:
        """Mock lists endpoint."""
        def add_list_member(self, list_id, body, **kwargs):
            """Mock add_list_member:
            https://mailchimp.com/developer/api/marketing/list-members/add-member-to-list/
            """
            return {
                "id": "test_id",
                "email_address": "test_address"
            }

    class MailChimpClient:
        """Mock mailchimp class."""

        def lists(self):
            """Lists endpoint."""
            return MailChimpLists()            
