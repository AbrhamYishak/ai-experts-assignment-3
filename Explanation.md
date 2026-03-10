# Bug Analysis and Fix Explanation

## What were the bugs

1. When the token was of type `dict`, there was no way to retrieve the `access_token`. As a result, the function returned `None`, causing **Test 5** to fail.
2. When the token was of type `dict`, stale tokens could not be refreshed. This also caused **Test 5** to fail.
3. Not a bug but the if statement is extended to check if the access_token is present not just the full token.

---

## Why did this happen

1. The first bug happened because in the `if api` statements, we only checked if the token was an instance of `OAuth2Token` or if it was not `None`. The case where the token was of type `dict` was skipped, which caused the `Authorization` header to be `None`.
2. The second bug happened because the refresh logic only triggered when the token was `None` or when it was an expired `OAuth2Token`. Tokens of type `dict` that were expired did not trigger a refresh.
3. The third bug happend when the OAuth2Token is not None but when the access_token inside is None

---

## Why the fix solves the problem

1. The first solution works because it handles the case when the token is of type `dict` and sets `header["Authorization"]` to `"Bearer " + access_token`.
2. The second solution works because it extends the existing condition to support tokens of type `dict`. It checks whether the token has expired and triggers a refresh when necessary.
3. The third solution works because it check the existence of the access token in the token of type `dict` and `OAuth2Token`

---

## Realistic edge cases not yet covered by tests

1. Tokens that are `dict` but **missing required field** like `expires_at`. Current tests assume these fields exist, so malformed token dictionaries are not tested.
2. Tokens that are `dict` but have an **invalid `expires_at` format** (for example, a string that cannot be parsed into a valid date or timestamp).
3. Tokens of an **unexpected type** (neither `dict`, `OAuth2Token`, nor `None`).
