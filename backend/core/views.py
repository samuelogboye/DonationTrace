from django.shortcuts import redirect


def return_home_to_docs(request):
    return redirect("swagger-schema")
