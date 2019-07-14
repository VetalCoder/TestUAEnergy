from django.views.generic.base import View
from django.utils import translation
from django.shortcuts import redirect


class SetLangView(View):
    def dispatch(self, request, *args, **kwargs):
        if translation.LANGUAGE_SESSION_KEY in request.session:
            request.session[translation.LANGUAGE_SESSION_KEY] = kwargs["lang"]
        else:
            request.session.update({translation.LANGUAGE_SESSION_KEY: kwargs["lang"]})
        translation.activate(translation.LANGUAGE_SESSION_KEY)
        return redirect(request.META["HTTP_REFERER"])
