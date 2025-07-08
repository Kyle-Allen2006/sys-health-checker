# System Health Checker

A simple Python tool to monitor system health and resource usage.

## Features

- Monitors CPU, RAM, and Disk usage
- Pings specified network hosts (e.g., Google, local router)
- Logs output to `logs/system_log.txt`
- Alerts when thresholds are exceeded

## Technologies Used

- Python 3
- `psutil` – for system resource monitoring
- `ping3` – for host reachability
- Logging via local text file

---

## About the Project

This script is a lightweight **Automated System Health Checker**, designed to assist with real-time monitoring of a system’s key performance indicators. It checks disk space, memory usage, CPU load, and basic network connectivity. 

Originally built as part of my portfolio to show proficiency in Python scripting and troubleshooting automation.

---

## Future Improvements

- Add cross-platform support for Linux/Mac
- Implement a GUI for easier user interaction
- Schedule automated checks using `cron` or Task Scheduler
- Include email alert functionality when thresholds are exceeded


## Getting Started

1. Clone this repo:
   ```bash
   git clone https://github.com/kyle-allen2006/sys-health-checker.git
   cd sys-health-checker
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   ```

3. Install dependencies:
   ```bash
   pip install psutil ping3
   ```

4. Run the script:
   ```bash
   python health_check.py
   ```

   About the Developer:

Hello and welcome, I’m Kyle Allen I am a passionate developer transitioning into software engineering after 16 years of experience in robotics and automation. I’m currently pursuing my Software Engineering degree at WGU while building real-world projects to strengthen my skills in modern web development.

Background in robotics, controls, industrial automation, and maintenance.

Current student at Western Governors University (WGU).

Strong foundation in programming logic and problem solving.

Actively building a full-stack portfolio using Node.js, Angular, MongoDB, and more.

This project is part of my personal growth journey as I transition into full-time software development. I'm eager to bring my technical experience and dedication to a forward-thinking development team.