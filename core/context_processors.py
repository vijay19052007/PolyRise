# core/context_processors.py
def global_data(request):
    return {
        'site_name': 'PolyRise',
        # Add more here like notifications count, user data, etc.
    }
