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
