# Permissions and Groups Setup

## Custom Permissions
The `Article` model has the following custom permissions:
- `can_view`: Allows users to view articles.
- `can_create`: Allows users to create new articles.
- `can_edit`: Allows users to edit existing articles.
- `can_delete`: Allows users to delete articles.

## Groups and Permissions
We have set up three user groups with varying permissions:
- `Viewers`: Can only view articles (`can_view`).
- `Editors`: Can view, create, and edit articles (`can_view`, `can_create`, `can_edit`).
- `Admins`: Full access to articles, including view, create, edit, and delete (`can_view`, `can_create`, `can_edit`, `can_delete`).

## Enforcing Permissions in Views
Permissions are enforced in the views using the `@permission_required` decorator.
Example: 
```python
@permission_required('app_name.can_edit', raise_exception=True)
def article_edit(request, pk):
    # Edit logic


# Django Application Security Measures

## Secure Settings
- `DEBUG = False`: Ensures that the application doesn't expose sensitive information in production.
- `SECURE_BROWSER_XSS_FILTER = True`: Enables XSS filtering in browsers.
- `X_FRAME_OPTIONS = 'DENY'`: Prevents clickjacking attacks by disallowing the embedding of pages in iframes.
- `SECURE_CONTENT_TYPE_NOSNIFF = True`: Stops browsers from MIME-sniffing a response from the server.
- `CSRF_COOKIE_SECURE` and `SESSION_COOKIE_SECURE`: Ensure cookies are sent over HTTPS.
- `SECURE_HSTS_SECONDS`: Enforces the use of HTTPS by browsers for a set period.

## CSRF Protection
All forms are secured with CSRF tokens using Django's built-in `{% csrf_token %}` tag.

## SQL Injection Protection
We use Django’s ORM to interact with the database and avoid raw SQL queries. Input validation is done using Django forms, and `get_object_or_404()` is used for fetching individual objects securely.

## Content Security Policy (CSP)
The application enforces a Content Security Policy (CSP) to limit the sources from which scripts, styles, and other resources can be loaded. This helps mitigate XSS attacks.
