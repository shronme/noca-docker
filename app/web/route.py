from app.web.views import views


def init_views(app):
    app.add_url_rule('/api/user', view_func=views.TempView.as_view('temp_view'))

