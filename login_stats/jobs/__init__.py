import csv
import frappe
from frappe.utils import getdate,get_datetime,add_days
from frappe.utils.file_manager import save_file
from frappe.utils import get_site_path

def generate_user_login_report():
    """Fetch user login data, create a CSV file, and send it via email."""
    
    # Fetch user login data from Activity logs
    users = frappe.get_all(
        "Activity Log",
        filters={"communication_date": ["between",[get_datetime(add_days(getdate(),-1)),get_datetime("{} 23:59:59".format(add_days(getdate(),-1)))]]},
        fields=["full_name", "user", "count(*) as login_attempts"],
        group_by="user"
    )


    if not users:
        frappe.log_error("No users found", "Login Statistics")
        return

    # Define CSV file path
    file_path = get_site_path("private", "files", "user_login_stats.csv")
    
    # Write data to CSV file
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Full Name", "User Email", "Login Attempts"])  # Header
        
        for user in users:
            writer.writerow([user["full_name"], user["user"], user["login_attempts"]])
    
    # Attach and send email
    send_email_with_csv(file_path)

def send_email_with_csv(file_path):
    """Send an email with the generated CSV file."""
    
    recipients = ["shahzadnaser1122@gmail.com"]  # Replace with the actual recipient email
    
    try:
        # Attach file to Frappe
        with open(file_path, "rb") as file:
            file_content = file.read()

        file_doc = save_file("user_login_stats.csv", file_content, "", "", is_private=1)
        # Send email
        frappe.sendmail(
            recipients=recipients,
            subject="Daily User Login Report",
            message="Attached is the daily user login report.",
            attachments=[{
                "file_url": file_doc.file_url
            }]
        )
    
    except Exception as e:
        frappe.log_error(f"Failed to send email: {str(e)}", "Login Statistics")

