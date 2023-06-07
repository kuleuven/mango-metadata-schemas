from flask import (
    Flask,
    g,
    redirect,
    request,
    url_for,
    render_template,
    Blueprint,
    session,
    current_app,
)

import bleach

import schema_manager
from schema_manager.editor import metadata_schema_editor_bp
from schema_manager.form import metadata_schema_form_bp
from schema_manager.view import metadata_schema_view_bp

app = Flask(__name__)
app.secret_key = "HV44H6oH-eKMqJDU0W6Xw6ch_c4wpmDWf5tgD0p-0Gc"
app.config.from_pyfile("config.py")

with app.app_context():
    app.register_blueprint(metadata_schema_form_bp)
    app.register_blueprint(metadata_schema_editor_bp)
    app.register_blueprint(metadata_schema_view_bp)


# html and js escape dangerous content
@app.template_filter("bleach_clean")
def bleach_clean(suspect, **kwargs):
    return bleach.clean(suspect, **kwargs)


@app.route("/")
def index():
    return redirect(url_for("metadata_schema_editor_bp.metadata_schemas"))
