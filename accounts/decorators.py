from django.shortcuts import redirect

def allowed_roles(roles=[]):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):

            # 🚨 SAFE CHECK (prevents AnonymousUser crash)
            if not request.user.is_authenticated:
                return redirect("/login/")

            # 🚨 FIX: prevent "AnonymousUser has no role" error
            user_role = getattr(request.user, "role", None)

            if user_role not in roles:
                return redirect("/login/")  # or show "not allowed page"

            return view_func(request, *args, **kwargs)

        return wrapper
    return decorator