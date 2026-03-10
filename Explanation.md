What were the bugs:
    1, When the token was of type dict, there was no way to retrieve the access_token. As a result, the function       returned None, causing Test 5 to fail.
    2, When the token was of type dict, stale tokens could not be refreshed. This also caused Test 5 to fail.
Why did this happend:
    1, The first bug happend because in the if api statements we were checking if token is instance of OAuth2Token or if token is not None. we jumped over the case when token is type dict which made the Authorization in the header None
    2, The second bug happend because we requested for refresh token only when the token is None or when the token is type of OAuth2Token and is expired but we did not request when the token is type dict and expired.
Why does your fix actually solve it:
    1, The first solution work because it handle the case when token is type of dict and set header["Authorization"] to "Bearer + access_token"
    2, The second solution work because it extends the existing if condition to support tokens of type dict. It verifies whether the expiration time has passed and triggers a token refresh when necessary.
What’s one realistic case / edge case your tests still don’t cover:
    1, When the token is a dict but does not contain required fields such as access_token or expires_at. The current tests assume these fields exist, so malformed token dictionaries are not tested.
    2, When the token is a dict but the expires_at value has an invalid format (for example a string that cannot be parsed into a valid date or timestamp).
    3, When the token is unexpected type instead of a dict or token object or None.

