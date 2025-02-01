# Login Statistics App for ERPNext

## Overview
This custom ERPNext app automatically generates and emails a daily CSV report containing user login statistics. The report includes the first name, last name, and the number of login attempts for each user.

## Features
- Automatically collects user login statistics.
- Generates a CSV report with user details.
- Sends the report via email to a predefined recipient.
- Runs daily using ERPNext's built-in scheduler.

## Installation
### Prerequisites
Ensure you have a working ERPNext instance installed.

### Steps to Install
1. Navigate to your ERPNext bench directory:
   ```sh
   cd ~/frappe-bench
   ```
2. Get the app from the GitHub repository:
   ```sh
   bench get-app login_stats https://github.com/yourusername/login_stats.git
   ```
3. Install the app on your site:
   ```sh
   bench --site yoursite install-app login_stats
   ```
4. Restart the bench to apply changes:
   ```sh
   bench restart
   ```

## Configuration
1. Set the recipient email address in the app settings.
2. Ensure your ERPNext email settings are correctly configured.
3. The app will automatically schedule the daily report generation and email.

## Usage
- The app runs in the background and requires no manual intervention.
- You can check the logs to verify email delivery and CSV file generation.
- The generated CSV file will be attached to the email and sent to the configured recipient.
- There is also a Report called *Login Attempts Report* which preview the login attempts during selected period.

## Uninstallation
If you wish to remove the app, run:
```sh
bench --site yoursite uninstall-app login_stats
bench remove-app login_stats
```

## Contribution
Feel free to fork the repository and submit pull requests to improve the app.

## License
This project is licensed under the MIT License.

## Contact
For any issues or inquiries, please open an issue on the GitHub repository.

