
from reportlab.pdfgen import canvas
from datetime import datetime

def generate_pue_report(daily_stats, filename="pue_report.pdf"):
    c = canvas.Canvas(filename)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 800, "RackMind - Weekly PUE & Cost Report")
    c.setFont("Helvetica", 10)
    c.drawString(50, 780, f"Generated: {datetime.now()}")
    y = 750
    for day in daily_stats:
        c.drawString(50, y, f"{day['date']}: Avg PUE {day['avg_pue']} | Wasted ${day['wasted_cost']:.2f} | Max Temp {day['max_temp']}C")
        y -= 20
    c.drawString(50, y-20, "Recommendation: Increase setpoint to 77F to save ~$280/month")
    c.save()
    print(f"Report saved to {filename}")
