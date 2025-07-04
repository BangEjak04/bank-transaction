from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from models import db, Cheque
from config import *
from datetime import datetime

app = Flask(
    __name__,
    static_url_path="/",
    static_folder="public",
    template_folder="resources/views"
)
app.config.from_object('config')

with app.app_context():
    db.init_app(app)
    db.create_all()

@app.route("/cheque")
def index():
    cheques = Cheque.query.order_by(Cheque.created_at.desc()).all()
    return render_template("index.html", cheques=cheques)

@app.route("/cheque/create", methods=["POST"])
def create():
    try:
        # Ambil data terakhir berdasarkan end_number
        last_cheque = Cheque.query.order_by(Cheque.end_number.desc()).first()
        if last_cheque and last_cheque.end_number.isdigit():
            last_end_number = int(last_cheque.end_number)
        else:
            last_end_number = 0

        # Hitung start_number otomatis jika kosong
        form_start = request.form.get("start_number", "").strip()
        if form_start:
            start_number = form_start.zfill(6)
        else:
            start_number = str(last_end_number + 1).zfill(6)

        # Hitung end_number otomatis jika kosong
        form_end = request.form.get("end_number", "").strip()
        if form_end:
            end_number = form_end.zfill(6)
        else:
            end_number = str(int(start_number) + 499).zfill(6)

        # Buat objek cheque baru
        cheque = Cheque(
            cheque_type=request.form["cheque_type"],
            cheque_code=request.form["cheque_code"],
            date=datetime.strptime(request.form["date"], "%Y-%m-%d"),
            start_number=start_number,
            end_number=end_number,
            status=request.form.get("status", "Belum Dikeluarkan"),
        )
        db.session.add(cheque)
        db.session.commit()
        flash("Data cheque berhasil ditambahkan!", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Terjadi kesalahan: {e}", "error")
    return redirect(url_for("index"))

@app.route("/cheque/bulk-release", methods=["POST"])
def bulk_release():
    cheque_ids = request.form.get("cheque_ids", "")
    giro_number = request.form.get("giro_number")
    giro_name = request.form.get("giro_name")

    if not cheque_ids:
        flash("Tidak ada data yang dipilih", "error")
        return redirect(url_for("index"))

    ids = [int(cid) for cid in cheque_ids.split(",") if cid.isdigit()]
    
    for cheque in Cheque.query.filter(Cheque.id.in_(ids)).all():
        cheque.status = "Sudah Dikeluarkan"
        cheque.giro_number = giro_number
        cheque.giro_name = giro_name

    db.session.commit()
    flash("Berhasil mengeluarkan cek.", "success")
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)